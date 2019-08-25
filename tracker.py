import socket, sys, threading, json,time,optparse,os

def validate_ip(s):
    """
    Check if an input string is a valid IP address dot decimal format
    Inputs:
    - a: a string

    Output:
    - True or False
    """
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def validate_port(x):
    """
    Check if the port number is within range
    Inputs:
    - x: port number

    Output:
    - True or False
    """
    if not x.isdigit():
        return False
    i = int(x)
    if i < 0 or i > 65535:
            return False
    return True


class Tracker(threading.Thread):
    def __init__(self, port, host='0.0.0.0'):
        threading.Thread.__init__(self)
        self.port = port #port used by tracker
        self.host = host #tracker's IP address
        self.BUFFER_SIZE = 8192
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket to accept connections from peers

         # Track (ip, port, exp time) for each peer using a dictionary
         # You can optionally use (ip,port) as key
        self.users = {}

        # Track (ip, port, modified time) for each file
        # Only the most recent modified time and the respective peer are store
        # {'ip':,'port':,'mtime':}
        
        self.files = {}

        self.lock = threading.Lock()
        try:
            #Bind to address and port
            self.server.bind((self.host, self.port))
            
        except socket.error:
            print(('Bind failed %s' % (socket.error)))
            sys.exit()
            
        #YOUR CODE
        self.server.listen(3) #listen for up to 3 connections

    def check_user(self):
        #Check if the peers are alive or not
        """Steps:
            1. check if a peer has expired or not
            2. if expired, remove items self.users and self.files ()
            [Pay attention to race conditions (Hint: use self.lock)]
        """
        
        tmp_files = self.files.copy() # Create a copy of the files as you cannot iterate and modify dictionary at the                                       # same time
        tmp_users = self.users.copy()
        
        self.lock.acquire() # This locks the resource
        for user, exp_time in tmp_users.items():
            if time.time() > exp_time: # if current time is greater than expiry time for the user
                del self.users[user]
                for file, info in tmp_files.items():
                    if info["port"] == user[1]:
                        del self.files[file]         # deletes the files associated with that specific port

        self.lock.release() # This unlocks the resources
        
        #schedule the method to be called periodically
        t = threading.Timer(20, self.check_user)
        t.start()

   #Ensure sockets are closed on disconnect (This function is Not used)
    def exit(self):
        self.server.close()

    def run(self):
        # start the timer to check if peers are alive or not
        t = threading.Timer(20, self.check_user)
        t.start()

        print(('Waiting for connections on port %s' % (self.port)))
        while True:
            #accept incoming connection
            conn, addr = self.server.accept() # accept socket connections

            #process the message from a peer
            threading.Thread(target=self.process_messages, args=(conn, addr)).start()


    def process_messages(self, conn, addr):
        conn.settimeout(180.0)
        print(('Client connected with ' + addr[0] + ':' + str(addr[1])))

        while True:
            #receiving data from a peer
            data = ''
            while True:
                part = conn.recv(self.BUFFER_SIZE).decode()
                data =data+ part
                if len(part) < self.BUFFER_SIZE:
                    break

            # Check if the received data is a json string of the anticipated format. If not, ignore.
            # NOTE: THERE IS MORE DATA STRUCTURE CHECKS DOWN BELOW, it causes an error with json.loads(data) so was
            # moved to occur after json.loads(data) in order to prevent this error
            
            try:
                json.loads(data) 
            except ValueError:
                data = ''        # ignoring the data if it is not in JSON format.
                return
            
            #deserialize
            data_dic = json.loads(data)
            
            """
            1) Update self.users and self.files if nessesary
            2) Send directory response message
            Steps:1. Check message type (initial or keepalive). See Table I in description.
                  2. If this is an initial message from a peer and the peer is in self.users, create the corresponding entry in self.users
                  DONE 2. If this is a  keepalive message, update the expire time with the respective peer
                  3. For an intial message, check the list of files. Create a new entry in user.files if one does not exist,
                  or, update the last modifed time to the most recent one
                  4. Pay attention to race conditions (Hint: use self.lock)
            """

            if isinstance(data_dic, dict):      # check to see if data_dic is of type dictionary (successful)
                initial_key = ("port","files")  # initialize the keys for initial message and keep alive message
                keepalive_key = ("port")
                if (len(data_dic) == 2) and (set(initial_key) <= data_dic.keys()): # using sets to compare multi key dict
                    messagetype = 'initial'
                elif (len(data_dic) == 1) and (keepalive_key in data_dic.keys()):
                    messagetype = 'keepalive'
                else:
                    messagetype = 'invalid'                                        # if message type is invalid, the server will
            else:                                                                  # wont process the messages to prevent crashing
                messagetype = 'invalid' # if message recieved is not dictionary, reject it
                
            if messagetype == 'keepalive': # if keep alive message, update the timer and send back self.files
                conn_ip = addr[0]
                conn_port = data_dic["port"]
                self.lock.acquire() # This locks the resource
                self.users[(conn_ip,conn_port)] = (time.time() + 10) # update the expiry timer for the user
                json_files = json.dumps(self.files)
                conn.send(json_files.encode())
                self.lock.release() # This unlocks the resources
                
            elif messagetype == 'initial':
                conn_ip = addr[0]
                conn_port = data_dic["port"]
                mykey1 = (conn_ip,conn_port) # this is the key used to store self.files enteries
                # NOTE: Assumption (2) states that the initial message is only sent once, this is why implementation is this way
                if (set(mykey1) <= self.users.keys()): # if the initial message is being sent again and user exists, dump
                    json_files = json.dumps(self.files)
                    conn.send(json_files.encode())
                    # NOTE: it is also assumed that files are never modified, so if initial message sent twice, ignore.
                    
                else:
                    self.lock.acquire() # This locks the resource
                    self.users[(conn_ip,conn_port)] = (time.time() + 10) #Added to the list of alive users
                    # This is the first instance of the initial message from this client.
                    for file in data_dic["files"]:
                        file_name = file["name"]
                        mtime = int(file["mtime"])
                        if file_name not in self.files.keys(): # if the file is not in the list of stored files in tracker:
                            self.files[file_name] = {"ip":conn_ip, "mtime":mtime, "port":conn_port} # add that file
                        else:
                            if mtime > int(self.files[file_name]["mtime"]): # if modified file time is > stored file
                                self.files[file_name] = {"ip":conn_ip, "mtime":mtime, "port":conn_port}
                    
                    self.lock.release() # This unlocks the resources
                    
                    json_files = json.dumps(self.files)
                    conn.send(json_files.encode())
                    
        conn.close() # Close
    
if __name__ == '__main__':
    parser = optparse.OptionParser(usage="%prog ServerIP ServerPort")
    options, args = parser.parse_args()
    if len(args) < 1:
        parser.error("No ServerIP and ServerPort")
    elif len(args) < 2:
        parser.error("No  ServerIP or ServerPort")
    else:
        if validate_ip(args[0]) and validate_port(args[1]):
            server_ip = args[0]
            server_port = int(args[1])
        else:
            parser.error("Invalid ServerIP or ServerPort")
    tracker = Tracker(server_port,server_ip)
    tracker.start()

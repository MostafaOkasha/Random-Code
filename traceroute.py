#!/usr/bin/python

import optparse
import socket
import sys
import time
import math

icmp = socket.getprotobyname('icmp')
udp = socket.getprotobyname('udp')

def create_sockets(ttl, timeout):
    """
    Sets up a sending and receiving socket necessary for traceroute.
    """
    # Opens a new UDP socket
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)

    # Opens a new socket for ICMP messages
    recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    # Set ttl value for the sending socket
    send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
    
    #recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)
    recv_socket.settimeout(timeout)
    
    return recv_socket, send_socket


def avg(rtt_List):
    """ 
    Returns the average of the round trip times
    """

    return sum(rtt_List)/len(rtt_List)

def std_dev(rtt_List):
    """
    Returns the general population standard deviation 
    of the round trip times
    """

    avg = sum(rtt_List)/len(rtt_List)
    stddev = 0
    for i in rtt_List:
        stddev += math.pow((i - avg), 2)
    return math.sqrt(stddev/len(rtt_List))

def main(dest_name, port, max_hops, timeout):

    # IP address from command line argument domain name
    dest_addr = socket.gethostbyname(dest_name)

    ttl = 1
    print "traceroute to %s (%s), %d hops max, %d byte packets" % (dest_name, dest_addr, max_hops, sys.getsizeof(""))
    
    while True:
        
        # Initialize empty round trip time list
        rtt_values = []

        # Send 3 packets for traceroute
        for i in range(0, 3):

            # Create sockets and send a single empty packet to destination
            recv_socket, send_socket = create_sockets(ttl, timeout)
            recv_socket.bind(("", port))
            send_socket.sendto("", (dest_name, port))

            # Record the start time of data send
            start_time = time.time()

            curr_addr = None
            curr_name = None

            # Receive an ICMP message indicating succesful message
            try:

                # Obtain data and address of network device which returned ICMP message
                _, curr_addr = recv_socket.recvfrom(512)
                curr_addr = curr_addr[0]

                try:
                    # Retrieve domain name of network device
                    curr_name = socket.gethostbyaddr(curr_addr)[0]
                except:
                    # Use ip address if domain name wasnt retrievable
                    curr_name = curr_addr

            # Resend packet in case of timeout
            except socket.timeout:
                send_socket.sendto("", (dest_name, port))

            except socket.error:
                pass

            finally:
                send_socket.close()
                recv_socket.close()

            # Record round trip time and store in list
            duration = (time.time() - start_time) * 1000 # Multiplied by 1000 for ms
            rtt_values.append(duration)


        # If network device responded to packet send
        if curr_addr is not None:
            """
            Print format is as follows:
            5 xe-2-2-0.tor10.ip4.gtt.net (77.67.69.237) 12.321 ms 12.321 ms 12.321 ms avg: 12.321 ms stddev: 0 ms
            """

            print "%d %s (%s) %.3f ms %.3f ms %.3f ms avg = %.3fms stddev = %.3fms" % \
            (ttl, curr_name, curr_addr, rtt_values[0], rtt_values[1], rtt_values[2], avg(rtt_values), std_dev(rtt_values))

        # If network device did not respond
        else:
            print "%d %s\n" % (ttl, "* * *"),

        # Increment TTL 
        ttl += 1

        # If packet has reached destination or ttl has reached max hops, break the while loop
        if curr_addr == dest_addr or ttl > max_hops:
            break

    return 0

if __name__ == "__main__":
    parser = optparse.OptionParser(usage="%prog [options] hostname")
    parser.add_option("-p", "--port", dest="port",
                      help="Port to use for socket connection [default: %default]",
                      default=33434, metavar="PORT")
    parser.add_option("-m", "--max-hops", dest="max_hops",
                      help="Max hops before giving up [default: %default]",
                      default=30, metavar="MAXHOPS")
    """
 	Add an option of timeout value; default value is 5 second
    """
    parser.add_option("-t", "--timeout", dest="timeout",
                      help="Set the timeout value before sending timeout error [default: %default]",
                      default=5, metavar="TIMEOUT")

    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error("No destination host")
    else:
        dest_name = args[0]

    """
	Modify the following to include an argument to store the timeout value
    """
	#Change the following line (DONE)
    sys.exit(main(dest_name=dest_name,
                  port=int(options.port),
                  max_hops=int(options.max_hops),
                  timeout=int(options.timeout)))

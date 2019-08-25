import socket, sys, threading, json,time,optparse,os

import time
##this is an initial message:
filerecieve1 = {"port": 8001,"files": [{"mtime":1548878750.8774116, "name":"fileA.txt"}]}
filerecieve2 = {"port": 8002,"files": [{"mtime":1548878750.8776329, "name":"fileB.txt"}]}
ip1 = "127.0.0.1"
ip2 = "127.0.0.1"

listoffiles = {"fileB.txt": {"ip":"127.0.0.1","mtime":1548878750.8776329, \
                             "port": 8002},"fileA.txt": {"ip":"127.0.0.1","mtime":1548878750.8774116, "port": 8001}}

keepalive = {"port": 8001}

files = {}
users = {} #{"ip":"", "port": ''}

mykey1 = ("port","files")
mykey2 = ("port")
mykey3 = ("fileB.txt")

if set(mykey1) <= filerecieve1.keys():
    print("yes")
else:
    print("no")

if mykey2 in keepalive.keys():
    print("yes")
else:
    print("no")

if mykey3 in listoffiles.keys():
    print("yes")
else:
    print("no")


#First we recieve an initial message: this is a file recieve message.
users[(ip1,filerecieve1["port"])] = (time.time() + 180)
#user_info = {("port": filerecieve1["port"], "ip": ip1): "exp_time": time.time()}
#users.update(user_info)
print(users.keys())
print(users)

time.sleep(2)
##fake keepalive signal
users[(ip1,filerecieve1["port"])] = (time.time() + 180)
print(users)
##fake timeout signal
del users[(ip1,filerecieve1["port"])]
print(users)

#Add the first initial message to the list of files. 
#myfiles = filerecieve1.get("files")

#print(myfiles)
#print(type(myfiles))

#print(myfiles[0])
for file in filerecieve1["files"]:
    name = file["name"]
    port = filerecieve1["port"]
    print(type(name))
    mtime = file["mtime"]
    print(type(mtime))
    files[name] = {"ip":ip1, "mtime":mtime, "port":port}
    print(files)
    #files.update(file_name: {"ip":conn_ip, "mtime":mtime, "port":conn_port})



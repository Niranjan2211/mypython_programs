#!/usr/bin/bash
import os
import socket
def set_hostname():
    file = open("/QHOSTNAME")
    hostname = file.read()
    cmd = ("hostnamectl set-hostname %s" % hostname)
    os.system(cmd)

#set_hostname()
myhostname = socket.gethostname()
myIP = socket.gethostbyname(socket.gethostname())

#First Method
#print("Hostname is: {}!#$%^&*(){}".format(myhostname,myIP))
#print("IP Address: {}".format(myIP))

#Second Method
print("Hostname is: %s" % myhostname)
print("IP Address is: %s" % myIP)



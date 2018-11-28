#!/usr/bin/python
import os
import socket
#ipv4 = os.popen('ip addr show ens33').read().split("inet ")[1].split("/")[0]
#ipv4 = os.popen('ip addr show ens33')

#print(ipv4)
#gethostname() -- return the current hostname
#gethostbyname() -- map a hostname to its IP number
#gethostbyaddr() -- map an IP number or hostname to DNS info
#getservbyname() -- map a service name and a protocol name to a port number

hname = socket.gethostname()
ipaddr = socket.gethostbyname(hname)
a = socket.gethostbyaddr("192.168.9.20")
print hname
print ipaddr
print a

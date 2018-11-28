#!/usr/bin/python
import socket
def host_IP():
   try:
      hname = socket.gethostname()
      hip = socket.gethostbyname(hname)
      print("Hostname:  ",hname)
      print("IP Address: ",hip)
   except:
      print("Unable to get Hostname and IP")
<<<<<<< HEAD
host_IP()
=======
# Driver code
host_IP() #Function call
>>>>>>> 8058f070af105fff7940debfb8f7d2dae71590e1

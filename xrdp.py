#!/usr/bin/env python
import os, pwd
import os.path
# Below is the function to print an empty Line, for more verbose
def E_line():
    print ""
    return;
############End of E_line Function
#####################################################################
E_line()
#print "Checking if XRDP installed..?"

def RPM_CHK():
    status=os.system("rpm -qa | grep -w ^xrdp > /dev/null")
    if status == 0:
      return "\033[1;32;40m\tXRDP Installed successfully..\033[0m"
    else:
      return "\033[1;31;40m\tXRDP Package not Installed.\033[0m"
E_line()
#####################################################################
#print "Checking if XRDP installed..?"
def SER_CHK():
    status=os.system("systemctl status xrdp  > /dev/null")
    if status == 0:
      return "\033[1;32;40m\tXRDP service is running..\033[0m"
    else:
      return "\033[1;31;40m\tXRDP service is not running.\033[0m"
#####################################################################
#print "Checking if XRDP installed..?", RPM_CHK()
#print "Checking if XRDP Service Running..?", SER_CHK()
#print "Checking if XRDP Service Enabled..?", SER_ENB()
#print "Checking if Mate-Desktop RPM Installed..?", SER_ENB()
#print "Checking if Mate-Session-Manager RPM Installed..?", MATE_SES() 
#print "Checking if Tigervnc RPM Installed..?", TIG_VNC() 

####################################################################
def SER_ENB():
    status=os.system("systemctl is-enabled xrdp > /dev/null")
    if status == 0:
      return "\033[1;32;40m\tXRDP service enabled..\033[0m"
    else:
      return "\033[1;31;40m\tXRDP service not running.\033[0m"
######################################################################
def MATE_CHK():
    status=os.system("rpm -qa | grep -w mate-desktop > /dev/null")
    if status == 0:
      return "\033[1;32;40m\tMate-Desktop RPM Installed..\033[0m"
    else:
      return "\033[1;31;40m\tMate-Desktop RPM Not Installed..\033[0m"
######################################################################
def MATE_SES():
    status=os.system("rpm -qa | grep -w mate-session-manager > /dev/null")
    if status == 0:
      return "\033[1;32;40m\tMate-Session-Manager RPM Installed..\033[0m"
    else:
      return "\033[1;31;40m\tMate-Session-Manager RPM Not Installed..\033[0m"
#####################################################################
def TIG_VNC():
    status=os.system("rpm -qa | grep -w mate-session-manager > /dev/null")
    if status == 0:
      return "\033[1;32;40mTigervnc RPM Installed..\033[0m"
    else:
      return "\033[1;31;40m\tTigervnc RPM Not Installed..\033[0m"
############################################################################
def USER():
    from getpass import getuser
    print(getuser())
    return ("hello")
#USER()######################################










print "Checking if XRDP installed..?", RPM_CHK()
print "Checking if XRDP Service Running..?", SER_CHK()
print "Checking if XRDP Service Enabled..?", SER_ENB()
print "Checking if Mate-Desktop RPM Installed..?", SER_ENB()
print "Checking if Mate-Session-Manager RPM Installed..?", MATE_SES() 
print "Checking if Tigervnc RPM Installed..?", TIG_VNC() 






        



















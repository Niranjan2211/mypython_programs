#!/usr/bin/env python
import platform
import sys
import fileinput

for line in fileinput.input("/etc/sysconfig/selinux", inplace=True):
    print line.replace("SELINUX=enabled", "SELINUX=disabled"),

def osversion():
    release = ''.join(platform.linux_distribution())
    OS = release.split()
    OStype = OS[0]
    if OStype == "Red":
       print "This is RedHat OS"
    elif OStype == "CentOS":
       print "This is CentOS"

#osversion()
release = ''.join(platform.linux_distribution())
OS = release.split()
OStype = OS[0]
if OStype == "CentOS":
   		      lines = [ '[rabbitmq_erlang-source]',
                                'name=rabbitmq_erlang-source',
                                'baseurl=https://packagecloud.io/rabbitmq/erlang/el/7/SRPMS',
                                'gpgcheck=1',
                                'enabled=1',
                                'gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rabbitmq',
                              ]
                      with open("/etc/yum.repos.d/test.repo", "w+") as f:
                           for i in lines:
                               f.write(i + "\n")
                               #print done

       #print "This is RedHat OS"
elif OStype == "Red":
                      print "This is RedHat"
'''
lines = [ '[rabbitmq_erlang-source]',
          'name=rabbitmq_erlang-source',
          'baseurl=https://packagecloud.io/rabbitmq/erlang/el/7/SRPMS',
          'gpgcheck=1',
          'enabled=1',
          'gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rabbitmq',
        ]

done = "Operation successfully completed"
with open("/var/repos.d/test.repo", "w") as f:
     for i in lines:
         f.write(i + "\n")
     print done
'''

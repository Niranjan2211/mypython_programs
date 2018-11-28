#!/usr/bin/env python
import platform
import sys


release = ''.join(platform.linux_distribution())
if "CentOS" in release:
    print "This is CentOS"
    if "Red" in release:
       print "This is Redhat"
else:
    print "This is Ubuntu"





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

#!/usr/bin/env python
import platform
import sys
#release = platform.linux_distribution()
#print release

"""
#THis is one Method
if "CentOS Linux" in platform.linux_distribution():
    print "This is CentOS"
else:
    print "This is Redhat"
"""

#THis is another method 

release = ''.join(platform.linux_distribution())
if "CentOS" in release:
    print "This is CentOS"
    if "Red" in release:
       print "This is Redhat"
else:
    print "This is Ubuntu"


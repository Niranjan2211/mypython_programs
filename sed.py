#!/usr/bin/env python
import subprocess
#subprocess.call("sed s'/SELINUX=disabled/SELINUX=enabled/g' /tmp/selinux", shell=True)
file =  subprocess.call(['sed', 's/SELINUX=enabled/SELINUX=disabled/g', '/tmp/selinux'])
print file



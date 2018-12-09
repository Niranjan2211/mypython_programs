#! /usr/bin/python
import fileinput
for line in fileinput.input("/tmp/selinux", inplace=True):
    print line.replace("SELINUX=enabled", "SELINUX=disabled"),

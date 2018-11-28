#!/opt/anaconda/envs/myenv/bin/python

f = open("/etc/resolv.conf")
print "Name of the file: ", f.name
print "Closed or not: ", f.closed
print "Opening Mode: ", f.mode
print "Softspace flag: ", f.softspace

#!/opt/anaconda/envs/myenv/bin/python

for line in  open("/etc/resolv.conf"):
    if "nameserver" in line:
        print line,

with  open("resolv.conf") as f:
      print(f.read())



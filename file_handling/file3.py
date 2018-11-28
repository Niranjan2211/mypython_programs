#!/opt/anaconda/envs/myenv/bin/python
import os

#os.remove("test001")

if os.path.exists("test001"):
   os.remove("test001")
else:
   print("File Doesn't exist")



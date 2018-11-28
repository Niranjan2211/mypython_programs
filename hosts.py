##!/usr/bin/python
#!/opt/anaconda/envs/myenv/bin/python
import json
import socket
node_name = socket.gethostname()
with open('data.json','r+') as f:
     data = json.load(f)
data['name'] = node_name
f.seek(0)
json.dump(data, f, indent=4)
f.truncate()

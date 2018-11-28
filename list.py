#!/usr/bin/python
#nodes = list()
#print "Enter 10 Node names: "

instance = raw_input("Enter the server: ")
if instance.startswith('dev'):
   print("This is %s "% instance)
else:
    print("This is not %s"%  instance)





'''
for i in range(3):
    instance = raw_input("Enter the server: ")
    nodes.append(instance)
    print(nodes) 
    for i in nodes:
        env = i[:3]
        if i.startswith('dev'):
           length = len(i)
           i = i.capitalize()
           print "%s is %s environment and length is %d" %s (i,env,length)
        elif i.startswith('uat'):
             length = len(i)
             i = i.capitalize()
             print "%s is %s environment and length is %d" %s (i,env,length)
        elif i.startswith('prod'):
             length = len(i)
             i = i.capitalize()
             print "%s is %s environment and length is %d" %s (i,env,length)


'''

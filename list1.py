#!/opt/anaconda/envs/myenv/bin/python
alist = [123, 456, 'abc', 'def']
blist = ['ghi', 'lkj', 789, 987]

alist.extend(blist)
print alist

alist.append(blist)
print alist

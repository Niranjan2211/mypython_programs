#!/usr/bin/env python
list = ['ansible', 
        'baseurl=https://releases.ansible.com/ansible/rpm/release/epel-7-x86_64/',
        'enabled=1',
        'gpgcheck=1',
        'gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ansible-release'
        ]

print list[0]

for i in list:
    print i
    repofile = open("/var/yum.repos.d/test1.repo", "w")
    i.write(repofile)
    


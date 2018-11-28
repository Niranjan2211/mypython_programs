#!/usr/bin/env python

str0 = "om Sri Ganesha"
str1 = "Sri"
str2 = "Rama"

str_len = len(str1)+3
str_rev = str1.rjust(str_len)

str2_len = len(str2)+7
str2_rev = str2.rjust(str2_len)

print str0[0:3]
print str_rev
print str2_rev
print ""
print str0

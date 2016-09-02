#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Tu-tu-tu'
import os
import re
cwd = os.getcwd()
print 'Every time the program is started to record clear last time'
try:
    garbage = os.listdir(os.getcwd() + "\\BBScan\\report\\")
    for i in garbage:
        os.remove(os.getcwd() + "\\BBScan\\report\\" + str(i))
except Exception,e:
    pass
domain = raw_input('Please enter the domain name (No HTTP://):\n')
os.chdir(os.getcwd() + '\\subDomainsBrute\\')
os.system(os.getcwd() + '/subDomainsBrute.py '+str(domain) + " -o output.txt")
zz = "([\d]+?\.[\d]+?\.[\d]+?\.[\d]+?)"
by = re.compile(zz)
f = open(os.getcwd() + "/output.txt",'r')
list = by.findall(f.read())
f.close()
set = set(list)
os.chdir(cwd)
for i in set:
    os.system(os.getcwd() + '/BBScan/BBScan.py --host ' + str(i) + " --network 24 --browser")
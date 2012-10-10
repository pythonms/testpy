# -*- coding: utf-8 -*-

'''
Created on 08-10-2012

@author: mszot
'''


import os
import sys
import time

print dir(sys.stdout)
print sys.stdout.encoding 

def bar(x):
    return x + 1 

print os.name
print bar(1)

class M(object):
    def __init__(self):
        self.x = 1
        self.y = 2
    def poka(self):
        print self.x, self.y
    def mline(self):
        f=open('fout.txt','w+')
        for i in range(20):
            time.sleep(0.5)
            print 'line',i
            f.write('line'+str(i)+'\n')
        f.close()

x = M()
x.poka()
print x
print u'ąśżź'
x.mline()
print os.getpid()

if __name__ == '__main__':
    print 'main'
    
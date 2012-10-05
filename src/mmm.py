# -*- coding: utf-8 -*-

import os

def bar(x=3):
    return x * 10 

def foo():
    print 'foo' * 3
    print 'line' * 2 * 3
    
# koment
# koment 2
x = 123
y = 'abc'

print x,y
print 'end'
foo()
#dodalem komentarz ąśżźę ół
print os.name
#print os.__doc__
print os.environ 
print bar()
print 'ąśż'

class A(object):
    def __init__(self):
        self.x = 'ax'
    def poka(self):
        print self.x
        
class B(A):
    def __init__(self):
        self.x = 'bx'
        self.y = 'by'
    def poka(self):
        print self.x,self.y
        
class C(B):
    def __init__(self):
        super(C,self).__init__()
        self.z = 'cz'


d = C()
print d.z,d.x,d.y


class A2(object):
    def __init__(self):
        super(A2,self).__init__()
        self.x = 'ax'
    def poka(self):
        print self.x
        
class B2(object):
    def __init__(self):
        super(B2,self).__init__()
        self.x = 'bx'
        self.y = 'by'
    def poka(self):
        print self.x,self.y
        
class C2(A2,B2):
    def __init__(self):
        super(C2,self).__init__()
        self.z = 'cz'


d = C2()
print d.z,d.x,d.y
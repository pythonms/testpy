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
#dodalem komentarz ąśżźńółÓŁąśę
print os.name
print os.__doc__
print os.environ 
print bar()
print 'ąśę'

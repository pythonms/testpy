# -*- coding: utf-8 -*-

'''
Created on 08-10-2012

@author: mszot
'''
import os

def foo(x):
    print x
    
    
import __main__

foo(os.name)
print dir(__main__)
for i in dir(__main__):
    print '__main__.'+i
    exec 'print __main__.'+i
    
#f_exec = open('shell_test.py')
f_exec = open('run.py')
code = f_exec.readlines()
exec f_exec



import sys
import StringIO
# create file-like string to capture output
codeOut = StringIO.StringIO()
codeErr = StringIO.StringIO()
code = """
def f(x):
    x = x + 1
    return x
print 'This is my output.'
"""
# capture output and errors
sys.stdout = codeOut
sys.stderr = codeErr
#exec code
exec f_exec
# restore stdout and stderr
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
#print f(4)
s = codeErr.getvalue()
print "error:\n%s\n" % s
s = codeOut.getvalue()
print "output:\n%s" % s
codeOut.close()
codeErr.close()
print 'PID:',os.getpid()
execfile('shell_test.py')

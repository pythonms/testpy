# -*- coding: utf-8 -*-

import subprocess
import os
import time

print os.getpid()
try:
    proc = subprocess.Popen(['C:\Python27\python.exe'] +
                            ['C:\mmm\_repo\\testpy\src\shell.py'],shell=False)
    print 'PID z try',proc.pid
    
except:
    print 'PRINT Exception:'
finally:
    print 'END'

for i in range(15):
    time.sleep(1)
    print proc
    print proc.pid

try:
    proc.kill()
except WindowsError,e:
    print e
    print 'Brak procesu'

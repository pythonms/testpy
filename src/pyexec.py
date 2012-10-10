# -*- coding: utf-8 -*-

import subprocess
import os
import time
import ConfigParser
import machine
import __main__

#===============================================================================
# Config: set your system variables
#===============================================================================
mid = machine.get_machine_info()

config = ConfigParser.ConfigParser()
config.read('main.cfg')
python_path = config.get(mid, 'python_path')
work_dir = config.get(mid, 'work_dir')
exec_file = config.get(mid, 'exec_file')

#===============================================================================
# Set configuration (before commit comment this)
#===============================================================================
config = ConfigParser.RawConfigParser()
config.add_section(mid)
config.set(mid, 'python_path', 'C:/Python27/python.exe')
config.set(mid, 'work_dir', os.getcwdu().replace('\\','/'))
config.set(mid, 'exec_file', '/shell.py')
# Writing our configuration file to 'main.cfg'
with open('main.cfg', 'w+b') as configfile:
    config.write(configfile)

pid = os.getpid()
try:
    print __main__.__file__, 'PID:', pid 
    proc = subprocess.Popen([python_path] + \
                            [work_dir + exec_file],shell=False)
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

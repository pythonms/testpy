# -*- coding: utf-8 -*-

'''
Created on 09-10-2012

@author: mszot
'''

import subprocess

print subprocess.call(["ls", "-l","-a","-s"], shell = True)
print subprocess.call("exit 1", shell = True)
#Run command with arguments. Wait for command to complete. and 
#If the return code was zero then return, otherwise raise CalledProcessError. 
print subprocess.check_call(["ls", "-l"])
print subprocess.check_call("exit 0", shell=True)
print subprocess.check_output(["echo", "Hello World!"], shell=True)
print subprocess.check_output("dir",stderr=subprocess.STDOUT,shell=True)

import shlex
print 'podaj komende:',
command_line = 'ls'
#command_line = raw_input()
args = shlex.split(command_line)
print args
p = subprocess.Popen(args)

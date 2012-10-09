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

# output=`mycmd myarg`
# becomes
output = subprocess.check_output(["ls", "mmm*"])
print('`mycmd myarg`:' + output)

# output=`dmesg | grep hda`
# becomes
p1 = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "shell"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]
print 'grep:',output

# Alternatively, for trusted input, the shell’s own pipeline support may still be used directly:
#output=`dmesg | grep hda`
# becomes
output=subprocess.check_output("ls | grep mmm*", shell=True)
print('ls | grep mmm*:' + output)

# sts = os.system("mycmd" + " myarg")
# becomes
sts = subprocess.call("ls" + " -al", shell=True)
print 'sts:',sts

import sys
try:
    retcode = subprocess.call("ls" + " -al", shell=True)
    if retcode < 0:
        print >>sys.stderr, "Child was terminated by signal", -retcode
    else:
        print >>sys.stderr, "Child returned", retcode
except OSError, e:
    print >>sys.stderr, "Execution failed:", e
    
    
# P_NOWAIT example:
# pid = os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg")
# ==>
print 'dir:'
##pid = subprocess.Popen(["cmd", "dir"]).pid
##print pid
# P_WAIT example:
# 3retcode = os.spawnlp(os.P_WAIT, "/bin/mycmd", "mycmd", "myarg")
# ==>
##retcode = subprocess.call(["cmd", "ls"])
##print retcode
#Vector example:
#os.spawnvp(os.P_NOWAIT, path, args)
#==>
print subprocess.Popen(['c:\Python27\python.exe'] + ['D:\dysk_c\python_cpp\\testpy\src\shell.py'])
#Environment example:
#os.spawnlpe(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg", env)
#==>
## subprocess.Popen(["cmd", "ls -al"], env={"PATH": "/usr/bin"})

bufsize = 4092
# pipe = os.popen("cmd", 'r', bufsize)
# ==>
##pipe = subprocess.Popen("cmd", shell=True, bufsize=bufsize, stdout=subprocess.PIPE).stdout

# pipe = os.popen("cmd", 'w', bufsize)
# ==>
##pipe = subprocess.Popen("cmd", shell=True, bufsize=bufsize, stdin=subprocess.PIPE).stdin

# (child_stdin, child_stdout) = os.popen2("cmd", mode, bufsize)
# ==>
##p = subprocess.Popen("cmd", shell=True, bufsize=bufsize,stdin=subprocess.PIPE,
##                      stdout=subprocess.PIPE)
##(child_stdin, child_stdout) = (p.stdin, p.stdout)

##p = subprocess.Popen(["c:\Python27\python.exe", "D:\dysk_c\python_cpp\\testpy\src\shell_test.py"], bufsize=bufsize, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
##(child_stdin, child_stdout) = (p.stdin, p.stdout)
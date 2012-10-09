# -*- coding: utf-8 -*-

'''
Created on 09-10-2012

@author: mszot
'''

import subprocess

print subprocess.call(["ls", "-l"], shell = False)
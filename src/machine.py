# -*- coding: utf-8 -*-

'''
Created on 10-10-2012

@author: mszot
'''

import platform


def get_machine_info():
    machine_id = platform.system() +"_"+ platform.release() +'_' \
            + platform.machine() +'_'+platform.node()+ '_pyVer:' + platform.python_version()
    return machine_id


if __name__ == '__main__':
    print get_machine_info()
# -*- coding: utf-8 -*-

'''
Created on 10-10-2012

@author: mszot
'''

import platform


def get_machine_info():
    """Get machine info system_ver_32/64bit_hostname_pyVer"""
    machine_id = platform.system() +"_"+ platform.release() +'_' \
            + platform.machine() +'_'+platform.node()+ '_pyVer:' \
            + platform.python_version()
    return machine_id


if __name__ == '__main__':
    print get_machine_info()
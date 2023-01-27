#!/usr/bin/python3

import subprocess
import os
import sys
import fileinput
import re

def install():
    """run sudo ./installstartup.py to install startupscripts"""
    # find path of current service 
    dir_path = os.path.realpath("startupscript.py")

    #create service
    createservice = subprocess.run(["sudo","cp","startup.service","/etc/systemd/system/startupscript.service"])
    if createservice.returncode == 0:
        print("startupservice is created")
    else:
        print("startupservice failed")
        sys.exit(1)

    #modify path of ExecStart=
    searchexp = "ExecStart="
    newpath="ExecStart="+dir_path
    sedterm = "/"+searchexp+"/c"+newpath
    print(sedterm)
    # python method to replace
    #for line in fileinput.input("/etc/systemd/system/startupscript.service"):
    #    if searchexp in line:
    #        line = line.replace("ExecStart=",newpath)
    #        sys.stdout.write(line)
    #        print("replaced")
    #        break
    
    # modify with sh
    modifyservice = subprocess.run(["sudo","sed","-i",sedterm,"/etc/systemd/system/startupscript.service"])
    if modifyservice.returncode == 0:
        print("modifyservice is successful")
    else:
        print("startupservice failed")
        sys.exit(1)
    
    #enable service
    enableservice = subprocess.run(["sudo","systemctl","enable","startupscript.service"])
    if enableservice.returncode == 0:
        print("startupservice is enabled")
    else:
        print("startupservice failed")
        sys.exit(1)
    sys.exit(0)

install()
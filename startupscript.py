#!/usr/bin/python3

import subprocess
import os
import sys

ListofStartProcesses = []
#(name, sh,[command,arg1,arg2,...])

# add sudo apt upgrade
ListofStartProcesses.append(("apt update",["sudo","apt","update"]))

# add sudo apt upgrade
ListofStartProcesses.append(("apt upgrade",["sudo","apt","upgrade","-y"]))

# add a sampele python code
ListofStartProcesses.append(("end of startup process",["python3","printendofstartup.py"]))

# run all processes
for name, cmd in ListofStartProcesses:
    runprocess = subprocess.run(cmd)
    if runprocess.returncode == 0:
        print(name+" startupservice started")
    else:
        print(name+" startupservice failed")
        sys.exit(1)

sys.exit(0)
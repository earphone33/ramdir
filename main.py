#!/usr/bin/python3

import subprocess
import os

files = subprocess.getoutput("/usr/bin/ls -A")
files.split()

if "makerampart.bash" in files:
    print ("makerampart.bash found")

else:
    print ("!No makerampart.bash found!")
    exit()

dirToRam = input("enter a directory to save to ram (be careful!): ")

if os.path.isdir(dirToRam):
    print("Directory is real")
else:
    print("!Directory not found!")
    exit()

sizeToCopy=str(subprocess.getoutput("du -sh "+dirToRam).split()[0])
print("requiered RAM to proceed:", sizeToCopy)
os.system("./makerampart.bash "+sizeToCopy)
print("creating RAM partition")

print("==> Copying contents of "+dirToRam+" to /tmp/ramdir")
os.system("sudo cp -r "+dirToRam+" /tmp/ramdir")
print("Done!")

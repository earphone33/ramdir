#!/usr/bin/python3

import subprocess
import os

def askYesNo(text):
    putt = input(text, "[y/n]")
    if putt.upper() == "y":
        return True
    return False

files = subprocess.getoutput("/usr/bin/ls -A")
files.split()

if "makerampart.bash" in files:
    print ("makerampart.bash found")

else:
    print ("!No makerampart.bash found!")
    exit()

dirToRam = input("enter a directory to save to ram (be careful!): ")
mountpoint = input("enter a mountpoint to mount to ramdir to: ")

try:
    os.scandir(mountpoint) != "":
        if askYesNo("directory "+mountpoint+" not empty! Remove contents?") :
            print("==> removing "+mountpoint)
            os.system("rm -r "+mountpoint)
        else:
            print("!Not possible to proseed! esiting!")
except FileNotFoundError:
    if askYesNo("Directory "+mountpoint+" not found, create it?")
        print("==> Creating directory "+mountpoint)
        os.system("mkdir -p "+mountpoint)

if os.path.isdir(dirToRam):
    print("Directory "+dirToRam+" is real")
else:
    print("!Directory "+dirToRam+" not found!")
    exit()

sizeToCopy=str(subprocess.getoutput("du -sh "+dirToRam).split()[0])

print("requiered RAM to proceed:", sizeToCopy)
os.system("./makerampart.bash "+sizeToCopy+" "+mountpoint)
print("creating RAM partition")

print("==> Copying contents of "+dirToRam+" to /tmp/ramdir")
os.system("sudo cp -r "+dirToRam+" /tmp/ramdir")
print("Done!")

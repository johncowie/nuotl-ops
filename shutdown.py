#!/usr/bin/env python
import subprocess, sys

PROCESS_NAME = sys.argv[1]

pidFileName = "%s.pid" %(PROCESS_NAME)
pidFile = open(pidFileName)

pid = pidFile.readline()
pidFile.close()

print "Killing process ", pid
subprocess.Popen('rm %s && kill %s' %(pidFileName, pid), shell=True)


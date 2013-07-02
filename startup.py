#!/usr/bin/env python
import subprocess, sys

JAR_FILE = sys.argv[1]
CONFIG_FILE = sys.argv[2]
LOG_FILE = sys.argv[3]

command = 'nohup java -jar -server %s %s' %(JAR_FILE, CONFIG_FILE)

logFile = open(LOG_FILE, 'w+')
pidFile = open("process.pid", 'w+')

p = subprocess.Popen(command, shell=True, stdout=logFile, stderr=logFile)

print "Started ", p.pid

pidFile.write(str(p.pid))
pidFile.close()
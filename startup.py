#!/usr/bin/env python
import subprocess, sys

PROCESS_NAME = sys.argv[1]
JAR_FILE = sys.argv[2]
CONFIG_FILE = sys.argv[3]
LOG_FILE = sys.argv[4]

command = 'nohup java -jar -server %s %s' %(JAR_FILE, CONFIG_FILE)

logFile = open(LOG_FILE, 'w+')
pidFile = open("%s.pid" %(PROCESS_NAME), 'w+')

# TODO add logic to only run startup command if pid doesn't exist?
p = subprocess.Popen(command, shell=True, stdout=logFile, stderr=logFile)

print "Started ", p.pid

pidFile.write(str(p.pid))
pidFile.close()
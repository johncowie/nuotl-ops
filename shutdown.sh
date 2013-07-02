#!/bin/bash

if [ -f "process.pid" ]
then
  PID=$(cat process.pid)
  rm process.pid    
  kill $PID
else
  echo "no process.pid file exists"
fi
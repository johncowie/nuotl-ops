#!/bin/bash

if [ -f "process.pid" ]
then
  echo "Please stop existing process (kill the PID in process.pid)"
else
  nohup $* > /dev/null 2> /dev/null < /dev/null &
  PID=$!
  echo $PID > process.pid
  echo "Started process $PID"
fi
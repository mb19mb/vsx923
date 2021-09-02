#!/bin/bash

source /home/pi/habridge/skripte/config.sh

#echo $0
echo $1
(echo open $HOST $PORT
    sleep $SLEEP
    echo $1
    echo -e "\r"
    sleep $SLEEP
    echo exit) | telnet 


#!/bin/bash

source /home/pi/habridge/skripte/config.sh

echo "ausschalten.sh" >> $VSX_LOG

(echo open $HOST $PORT
    sleep $SLEEP
    echo "MO"
    echo -e "\r"
    sleep $SLEEP
    echo "060VL"
    echo -e "\r"
    sleep $SLEEP
    echo "PF"
    echo -e "\r"
    sleep $SLEEP
    echo exit) | telnet


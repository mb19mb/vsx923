#!/bin/bash

source /home/pi/habridge/skripte/config.sh

echo "einschalten.sh" >> $VSX_LOG

(echo open $HOST $PORT
    sleep $SLEEP
    echo "PO"
    echo -e "\r"
    sleep 4
    echo "01FN"
    echo -e "\r"
    sleep $SLEEP
    echo $VOL_INIT"VL"
    echo -e "\r"
    sleep $SLEEP
    echo "MF"
    echo -e "\r"
    echo exit) | telnet


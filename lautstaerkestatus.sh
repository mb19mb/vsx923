#!/bin/bash

source /home/pi/habridge/skripte/config.sh

echo "lautstaerkestatus.sh" >> $VSX_LOG

# vorher tmp file leeren!!!
echo "">$VSX_VOL_TMP_FILE

(echo open $HOST $PORT
    sleep $SLEEP
    echo "?V"
    echo -e "\r"
    sleep $SLEEP
    echo exit) | telnet | tee -a -i $VSX_VOL_TMP_FILE


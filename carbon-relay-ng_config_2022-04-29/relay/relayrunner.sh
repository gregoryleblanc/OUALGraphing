#!/bin/bash
sleep 15
/home/pi/go/bin/carbon-relay-ng /home/pi/go/etc/carbon-relay-ng.conf 2>&1 >> carbon-relay-ng.log & 
sleep 1h; kill $(cat /home/pi/go/var/carbon-relay-ng.pid) && rm /home/pi/go/var/carbon-relay-ng.pid

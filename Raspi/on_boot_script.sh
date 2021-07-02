#!/bin/sh -e
sleep 20
sudo pon gprs
sleep 20

. /home/pi/Raspi/export_nam_pass_host.sh

python3 /home/pi/Raspi/main.py
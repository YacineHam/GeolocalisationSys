#!/bin/sh -e

python3 /home/pi/Raspi/gprs_power_up.py

sleep 30

. /home/pi/Raspi/export_nam_pass_host.sh

python3 /home/pi/Raspi/main.py
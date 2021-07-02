#!/bin/sh -e
sleep 10
python3 /home/pi/Raspi/gprs_power_up.py
sleep 10
sudo pon gprs
sleep 20

. /home/pi/Raspi/export_nam_pass_host.sh

python3 /home/pi/Raspi/main.py
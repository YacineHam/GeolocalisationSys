#!/bin/sh -e
read -p "Please enter the car username: " username
read -p "Please enter the car password: " passwd
read -p "Please enter the server's Hostname: " host
echo '#!/bin/sh -e' > /home/pi/Raspi/export_nam_pass_host.sh
echo 'export CAR_NAME='"$username" >> /home/pi/Raspi/export_nam_pass_host.sh
echo 'export CAR_PASSWD='"$passwd" >> /home/pi/Raspi/export_nam_pass_host.sh
echo 'export GPS_HOST='"$host" >> /home/pi/Raspi/export_nam_pass_host.sh

. /home/pi/Raspi/export_nam_pass_host.sh

#!/bin/sh -e

enable_swap_uart(){

# UART auf ttyAMA0
    echo >> /boot/config.txt
    echo "#enable and swap uart" >> /boot/config.txt
    echo dtoverlay=disable-bt >> /boot/config.txt
    echo enable_uart=1 >> /boot/config.txt
    echo core_freq=250 >> /boot/config.txt
    echo force_turbo=1 >> /boot/config.txt

    echo -e "successfully configured file /boot/config.txt\n"
}

install_required(){
    sudo apt_get install minicom ppp screen elinks
}

create_file_gprs_in_peers(){
    # create file gprs in /etc/ppp/peers/
    echo > /etc/ppp/peers/gprs
    # echo user \"internet\" >> /etc/ppp/peers/gprs
    echo connect \"/usr/sbin/chat -v -t15 -f /etc/chatscripts/gprs -T internet\" >> /etc/ppp/peers/gprs
    echo /dev/serial0 \\n9600 >> /etc/ppp/peers/gprs

    echo noipdefault \\nusepeerdns \\ndefaultroute \\npersist \\nnoauth  >> /etc/ppp/peers/gprs

    echo nocrtscts\\nlocal >> /etc/ppp/peers/gprs

    echo nlock \\nmodem \\npassive \\nnovj \\nhide-password  \\nholdoff 10 \\nmaxfail 0 \\ndebug >> /etc/ppp/peers/gprs

    echo replacedefaultroute >> /etc/ppp/peers/gprs

echo -e "successfully configured file /etc/ppp/peers/gprs\n"
}

set_interface_ppp(){
#ppp0 in /etc/network/interfaces
    if grep -q 'auto gprs' /etc/network/interfaces;
    then
        echo -e "provider gprs already set in /etc/network/interfaces\n"
    else
        echo "  " >> /etc/network/interfaces
        echo "#set up ppp0 interface" >> /etc/network/interfaces
        echo auto gprs >> /etc/network/interfaces
        echo iface gprs inet ppp >> /etc/network/interfaces
        echo provider gprs >> /etc/network/interfaces
    fi

    echo -e "successfully configured file /etc/network/interfaces\n"
}



echo -e "\nConfiguration starts \n"

sudo enable_swap_uart
sudo install_required

sudo create_file_gprs_in_peers
sudo set_interface_ppp

. /home/pi/Raspi/set_username_passwd.sh

sudo pip3 install /home/pi/Raspi/requirements.txt
pip3 install /home/pi/Raspi/requirements.txt

sudo echo '#!/bin/sh -e\n\n. /home/pi/Raspi/on_boot_script.sh & \nexit 0'>  /etc/rc.local

echo -e "configuration finished \n"

echo "reboot starts in 5 seconds" 
sleep 5
sudo reboot
#!/bin/bash
#
#script to reset usb bus1 when broadcom bluetooth goes incommunicado
#Written by Nate Lannan

isActive=$(lsusb | grep Broadcom)
if [ -z "$isActive" ];
then
	echo "Unbinding USB bus 1"	
	echo -n "usb1" > /sys/bus/usb/drivers/usb/unbind
	echo "Binding USB bus 1"
	echo -n "usb1" > /sys/bus/usb/drivers/usb/bind
	echo "Waiting 15 seconds for Broadcom BT to start"
	sleep 15 
else
	echo "Broadcom BT is active"
fi

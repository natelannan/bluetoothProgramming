#!/bin/bash
#
#

isActive=$(lsusb | grep Broadcom)
if [ -z "$isActive" ];
then
  echo "Unbinding USB bus 1"
  echo -n "usb1" > /sys/bus/usb/drivers/usb/unbind
  echo "Binding USB bus 1"
  echo -n "usb1" > /sys/bus/usb/drivers/usb/bind
  echo "Waiting 15 seconds to allow Broadcom BT to start"
  sleep 15
else
  echo "Broadcom BT is active"
fi

import sys
import bluetooth
import time

LMm_addr = "38:C0:96:41:0E:A2"
uuid = "00001101-0000-1000-8000-00805f9b34fb"
sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#sock=bluetooth.BluetoothSocket(bluetooth.SERIAL_PORT_PROFILE)
#port=bluetooth.get_available_port(bluetooth.RFCOMM)
port=1
sock.connect((LMm_addr,port))
#sock.bind((LMm_addr,port))
#sock.listen(1)
#print "listening on port %d" % port
#lmm_sock,address = sock.accept()
#print "accepted connection from ",address

#data = sock.recv(1024)
#print "received [%s]" % data
print "device connected"
time.sleep(3)

sock.close()

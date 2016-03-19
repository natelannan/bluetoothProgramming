import sys
import bluetooth

LMm_addr = "38:C0:96:41:0E:A2"
uuid = "00001101-0000-1000-8000-00805f9b34fb"
serviceMatch=bluetooth.find_service(uuid=uuid)
if len(serviceMatch)==0:
    print "Could not locate LMm-G serial port service"
    sys.exit(0)

firstMatch=serviceMatch[0]
port=firstMatch["port"]
name=firstMatch["name"]
host=firstMatch["host"]

print "Connecting to \"%s\" on %s" % (name, host)

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#port=bluetooth.get_available_port(bluetooth.RFCOMM)
sock.connect((host,port))
#sock.bind((LMm_addr,port))
#sock.listen(1)
#print "listening on port %d" % port
#lmm_sock,address = sock.accept()
#print "accepted connection from ",address

data = sock.recv(1024)
print "received [%s]" % data

sock.close()

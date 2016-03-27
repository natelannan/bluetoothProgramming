import sys
import bluetooth

LMm_addr = "38:C0:96:41:0E:A2"
uuid = "00001101-0000-1000-8000-00805f9b34fb"
serviceMatch=bluetooth.find_service(uuid=uuid, address=LMm_addr)
if len(serviceMatch)==0:
    print "Could not locate LMm-G serial port service"
    sys.exit(0)

firstMatch=serviceMatch[0]
port=firstMatch["port"]
name=firstMatch["name"]
host=firstMatch["host"]

print "Connecting to \"%s\" on %s on port %s" % (name, host, port)

#sock=bluetooth.BluetoothSocket(bluetooth.SCO)
sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#port=bluetooth.get_available_port(bluetooth.RFCOMM)
sock.connect((host,port))
#sock.connect((host))
#sock.bind((LMm_addr,port))
#sock.listen(1)
#print "listening on port %d" % port
#lmm_sock,address = sock.accept()
#print "accepted connection from ",address
enq="\002ETC:VER ?;\003\016"
dump="\002CMN:ALL ?;\003\034"
getData="\002ETC:FWD ?;\003\032"


sock.send(getData)
i=0
data = []
while "\003" not in data:
    data.append(sock.recv(1))
    print "received [%r]" % data[i]
    i=i+1

chksum=sock.recv(1)
print "checksum [%r]" % chksum
    
sock.close()

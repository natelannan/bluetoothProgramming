import sys
import re
import bluetooth
import select
import time
#from socket import *

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
sock.settimeout(0.5)
#sock.connect((host))
#sock.bind((LMm_addr,port))
#sock.listen(1)
#print "listening on port %d" % port
#lmm_sock,address = sock.accept()
#print "accepted connection from ",address
enq="\002ETC:VER ?;\003\016"
dump="\002CMN:ALL ?;\003\034"
getData="\002ETC:FWD ?;\003\032"
ack="\006"

while 1:
    #time.sleep(.5)
    
    sock.send(getData)
    
    field=0
    data = ''
    meas = ''
    intensity = ''
    error = 1
    
    while '\003' not in data:
        #ready=select.select([sock],[],[],2)
        
        #if ready[0]:
        try:
            character=sock.recv(1)
            #print character
            data=data+character
            if data == '\006\002ETC:FWD ':
                #print 'foo'
                field=1
                #print "received [%r]" % data[i]
            if character == ";":
                field=field+1
            elif field==5:
                #print 'bar'
                meas=meas+character
            elif field==1:
                #print 'baz'
                intensity=intensity+character
            elif field==4:
                error =int(character)
        except bluetooth.btcommon.BluetoothError as error:
            if str(error)=="timed out":
                print error," Resending"
                sock.send(getData)
            else:
                sys.exit(error)
                
        #else:
            #print "Resending"
            #sock.send(getData)

    chksum=sock.recv(1)
        #print "checksum [%r]" % chksum

    if error == 1:
        print "Intensity = %s \t Methane (ppm-m) = %s" % (float(intensity),int(meas))
    else:
        print "Error = %d" % int(error)

    sock.send(ack)    
sock.close()

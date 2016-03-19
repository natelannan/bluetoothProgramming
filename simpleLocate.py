import bluetooth

#target_name = "LMm-G"
target_name = "Pocket Rocket"
target_address = None
nearby_devices = bluetooth.discover_devices()

#bluetooth detection and name lookup are probablilistic
#if this fails try a couple more times
for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name(bdaddr):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
else:
    print "could not find target bluetooth device nearby"

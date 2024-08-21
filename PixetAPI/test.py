
import sys

# Add the current directory to sys.path
sys.path.append('.')
import pypixet

print("pixet core init...") 
pypixet.start() 
pixet=pypixet.pixet 
devices = pixet.devicesByType(pixet.PX_DEVTYPE_TPX3) 
dev = devices[0] 
dev.setOperationMode(pixet.PX_TPX3_OPM_EVENT_ITOT) 
print("dev.doSimpleAcquisition (3 frames @ 1 sec) - start") 
rc = dev.doSimpleAcquisition(3, 1, pixet.PX_FTYPE_AUTODETECT, "example.png") 
print("dev.doSimpleAcquisition - end:", rc, "(0 is OK)") 
pixet.exitPixet()
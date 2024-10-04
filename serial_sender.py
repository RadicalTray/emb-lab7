import serial
import hashlib
from random import randbytes
# Change N to be smaller for experiment
N = 1000000

datagen = randbytes(N)
h = hashlib.new('md5')
h.update(datagen)
print('MD5 is :', h.hexdigest())
# Change the device here for Windows, it would be COM....  for Mac, I have no idea
# The second argument is baudrate
ser = serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0', 1000000) 

ser.write(datagen)




import serial
import time
import hashlib
# Change N to be smaller for experiment
N = 1000000

h = hashlib.new('md5')
# Change the device here for Windows, it would be COM....  for Mac, I have no idea
# The second argument is baudrate
ser = serial.Serial('/dev/serial/by-id/usb-FTDI_Dual_RS232-HS-if01-port0', 1000000) 
ser.flush()
data = ser.read(1)
starttime = time.time()
while len(data) < N:
    newdat = ser.read(N-len(data))
    data = data + newdat
stoptime =time.time()
h.update(data)
print(f'Data length is {len(data)}\nMD5 is : {h.hexdigest()}')
print('Total time is :', stoptime - starttime)


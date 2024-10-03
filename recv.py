import serial
import time
import hashlib

# N = 1_000_000
N = 1_000

h = hashlib.new('md5')
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.flush()
data = ser.read(1)
starttime = time.time()
data = data + ser.read(N - len(data))
stoptime = time.time()
h.update(data)
print(f'Data length is {len(data)}\nMD5 is : {h.hexdigest()}')
print('Total time is :', stoptime - starttime)

hash_dump = open('recv.md5', 'w')
print(h.hexdigest(), file=hash_dump)

data_dump = open('recv_data', 'wb')
data_dump.write(data)

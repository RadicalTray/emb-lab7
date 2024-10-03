import serial
import hashlib
from random import randbytes
import time

# N = 1_000_000
N = 100_000

datagen = randbytes(N)

h = hashlib.new('md5')
h.update(datagen)
print('MD5 is :', h.hexdigest())

ser = serial.Serial('/dev/ttyUSB1', 9600)

i = 0;
while i < N:
    batchSize = 1024
    batch = datagen[i : i + batchSize]
    print(batch)
    ser.write(batch)
    i += len(batch)
    time.sleep(0.5)

file = open('send_data', 'w')
print(h.hexdigest(), file=file)
print()
print(datagen, file=file)

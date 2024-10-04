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

ser = serial.Serial('/dev/ttyUSB1', 115200)

batchSize = 1024
i = 0

batch = datagen[i : i + batchSize]
ser.write(batch)
i += len(batch)

while i < N:
    time.sleep(0.1)
    batch = datagen[i : i + batchSize]
    ser.write(batch)
    i += len(batch)

hash_dump = open('send.md5', 'w')
print(h.hexdigest(), file=hash_dump)

data_dump = open('send_data', 'wb')
data_dump.write(datagen)

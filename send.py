import serial
import hashlib
from random import randbytes

# N = 1_000_000
N = 10_000

datagen = randbytes(N)

h = hashlib.new('md5')
h.update(datagen)
print('MD5 is :', h.hexdigest())

ser = serial.Serial('/dev/ttyUSB1', 9600)
ser.write(datagen)

file = open('output', 'w')
print(datagen, file=file)

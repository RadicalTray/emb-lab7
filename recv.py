import serial
import time
import hashlib

# N = 1_000_000
N = 10_000

h = hashlib.new('md5')
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.flush()
data = ser.read(1)
starttime = time.time()
while len(data) < N:
    newdat = ser.read(1)
    # newdat = ser.read(N - len(data))
    data = data + newdat
    print(f'{len(data)}:', newdat)
stoptime = time.time()
h.update(data)
print(f'Data length is {len(data)}\nMD5 is : {h.hexdigest()}')
print('Total time is :', stoptime - starttime)

file = open('output', 'w')
print(data, file=file)

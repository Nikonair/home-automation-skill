import serial
import time
 
s = serial.Serial('/dev/ttyUSB0', 9600) 
s.open()
time.sleep(5) # wait for Arduino Reset
s.write(2)
time.sleep(1)
s.close()
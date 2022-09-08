# type: ignore
import board
import time
import digitalio
g=digitalio.DigitalInOut(board.GP16)
r=digitalio.DigitalInOut(board.GP15)
x=10
print(x)
time.sleep(1)
for i in range(10):
    if x>0:
        x-=1
        print(x)
        time.sleep(1)
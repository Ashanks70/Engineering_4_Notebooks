# type: ignore
import board
import time
import digitalio
g=digitalio.DigitalInOut(board.GP16)
r=digitalio.DigitalInOut(board.GP15)
r.direction = digitalio.Direction.OUTPUT
g.direction = digitalio.Direction.OUTPUT
x=10
print(x)
time.sleep(1)
for i in range(10):
    if x>0:
        x-=1
        print(x)

        if x==0:
            r.value=True
            time.sleep(1)
            r.value=False
        else:
            g.value=True
            time.sleep(.5)
            g.value=False
            time.sleep(.5)
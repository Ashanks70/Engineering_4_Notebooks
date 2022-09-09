# type: ignore
import board
import time
import digitalio
g=digitalio.DigitalInOut(board.GP16)#green LED
r=digitalio.DigitalInOut(board.GP15)#Red LED
button=digitalio.DigitalInOut(board.GP3)#button
button.direction = digitalio.Direction.INPUT
r.direction = digitalio.Direction.OUTPUT
g.direction = digitalio.Direction.OUTPUT
x=10
while True:
    if button.value==False:
        break
for i in range(10):#run 10 times
    if x>0:#run through all numbers
        print(x)
        x-=1
        if x==0:
            time.sleep(1)
            print(x)
            r.value=True
            time.sleep(1)
            r.value=False
        else:
            g.value=True
            time.sleep(.5)
            g.value=False
            time.sleep(.5)
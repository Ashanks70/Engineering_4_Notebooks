# type: ignore
import board
import time
import digitalio
g=digitalio.DigitalInOut(board.GP15)#green LED
r=digitalio.DigitalInOut(board.GP16)#Red LED
button=digitalio.DigitalInOut(board.GP3)#button
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN
r.direction = digitalio.Direction.OUTPUT
g.direction = digitalio.Direction.OUTPUT
state=False
x=10
while True:
    if button.value==False:
        state=True
    if state==True and button.value==True:
        state=False
        for i in range(10):#run 10 times
            if button.value==False:
                state=True
            if (button.value==True) and (state==True) and (x != 10):
                print("ABORT")
                state=False
                x=10
                break
            if x>0:#run through all numbers
                print(x)
                x-=1
                if x==0:
                    time.sleep(1)
                    print(x)
                    print("liftoff")
                    r.value=True
                    time.sleep(1)
                    r.value=False
                else:
                    g.value=True
                    time.sleep(.5)
                    g.value=False
                    time.sleep(.5)
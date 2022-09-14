# type: ignore
import board
import time
import pwmio
from adafruit_motor import servo
import digitalio
pwm_servo = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)#bring servo
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)#name servo
g=digitalio.DigitalInOut(board.GP15)#green LED
r=digitalio.DigitalInOut(board.GP16)#Red LED
button=digitalio.DigitalInOut(board.GP3)#button
button.direction = digitalio.Direction.INPUT#button backend
button.pull = digitalio.Pull.DOWN#button backend
r.direction = digitalio.Direction.OUTPUT#LED backend
g.direction = digitalio.Direction.OUTPUT#LED backend
state=False
x=10
servo1.angle=0
while True:
    if button.value==False:
        state=True
    
    if state==True and button.value==True:
        state=False
        for i in range(180):#run 180 times
            if servo1.angle!=180:# only go to max angle

                servo1.angle+=1
            if i/10-i//10==.5:#run every x.5 seconds
                r.value=False
                g.value=False
            if button.value==False:#prevent the button from being pressed twice
                state=True
            if (button.value==True) and (state==True):
                print("ABORT")
                servo1.angle=0
                state=False#toggle anti double-trigger
                x=10
                break
            if x>0 and i//10==i/10:#run through all numbers
                print(x)
                x-=1
                if x==0:
                    print(x)
                    print("liftoff")
                    servo.angle=180#make sure it reaches the final angle
                    r.value=True
                else:
                    g.value=True
            time.sleep(.09)#sleep for roughly 10/180(1/18) seconds
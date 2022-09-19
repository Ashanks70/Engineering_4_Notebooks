# type:ignore
import board
import time
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import digitalio
import terminalio
import displayio
import busio
import adafruit_mpu6050
displayio.release_displays()
led=digitalio.DigitalInOut(board.GP12)
led.direction=digitalio.Direction.OUTPUT
sda_pin = board.GP10#other is 0x3d
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, 0x68)#0x68
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP6)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
splash= displayio.Group()
title = "ANGULAR VELOCITY"
xvalue = "X rotation = "
yvalue = "Y rotation = "
zvalue = "Z rotation = "


while True:
    print("Acceleration: ","x =" , round(mpu.acceleration[0],3), "," ,"y =",round(mpu.acceleration[1],3),",","z = ",round(mpu.acceleration[2],3))
    if abs(mpu.acceleration[0])>=8.8  or abs(mpu.acceleration[1])>=8.8:
        led.value=True
    else:
        led.value=False
    splash=displayio.Group()
    x=str(round(mpu.gyro[0],3))
    y=str(round(mpu.gyro[1],3))
    z=str(round(mpu.gyro[2],3))
    xtext = label.Label(terminalio.FONT, text=xvalue, color = 0xFFFF00, x=5, y=20)
    ytext = label.Label(terminalio.FONT, text=yvalue, color = 0xFFFF00, x=5, y=30)
    ztext = label.Label(terminalio.FONT, text=zvalue, color = 0xFFFF00, x=5, y=40)
    text_area = label.Label(terminalio.FONT, text=title, color = 0xFFFF00, x=5, y=5)
    splash.append(text_area)
    splash.append(xtext)
    splash.append(ytext)
    splash.append(ztext)
    xset = label.Label(terminalio.FONT, text=x, color = 0xFFFF00, x=80, y=20)
    yset = label.Label(terminalio.FONT, text=y, color = 0xFFFF00, x=80, y=30)
    zset = label.Label(terminalio.FONT, text=z, color = 0xFFFF00, x=80, y=40)
    splash.append(xset)
    splash.append(yset)
    splash.append(zset)
    display.show(splash)
    time.sleep(.5)
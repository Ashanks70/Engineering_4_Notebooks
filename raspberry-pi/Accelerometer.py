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
sda_pin = board.GP14#other is 0x3d
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu =adafruit_mpu6050.MPU6050(i2c)#0x68
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=GP6)

while True:
    print("Acceleration: ","x =" , mpu.acceleration[0], "," ,"y =",mpu.acceleration[1],",","z = ",mpu.acceleration[2])
    if abs(mpu.acceleration[0])>=8.8  or abs(mpu.acceleration[1])>=8.8:
        led.value=True
    else:
        led.value=False
    time.sleep(.5)
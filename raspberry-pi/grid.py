#type:ignore
import board
import busio
import terminalio
import time
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
sda_pin = board.GP10
scl_pin = board.GP11
i2c = busio.I2C(scl_pin, sda_pin)
displayio.release_displays()#0x3d
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP22)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
splash=displayio.Group()
hline = Line(0,32,128,32, color=0xFFFF00)
splash.append(hline)
display.show(splash)
bline = Line(64,0,64,64,color=0xFFFF00)
splash.append(bline)
display.show(splash)
while True:
    time.sleep(.5)
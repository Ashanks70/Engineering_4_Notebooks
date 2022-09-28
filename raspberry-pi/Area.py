#type:ignore
import board
import busio
import terminalio
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
counter=0
area=0
a1=0
a2=0
b1=0
b2=0
c1=0
c2=0
error=0
time=0
def calculate(a,b,c,d,e,f):
    s1=a*(d-f)/2
    s2=c*(f-b)/2
    s3=e*(b-d)/2
    area = abs(s1+s2+s3)
    print(f"the triangle with the points {a},{b} , {c},{d} , {e},{f} has an area of {area}.")
def test(point):
    try:
        float(point)
        return 0
    except:
        print("Error, try again")
        return 1

while True:
    splash=displayio.Group()
    hline = Line(0,32,128,32, color=0xFFFF00)
    splash.append(hline)
    bline = Line(64,0,64,64,color=0xFFFF00)
    splash.append(bline)
    aput=input("input first point")
    a=aput.split(",")
    aa = test((a[0]))
    ab = test(a[1])
    if aa==1 or ab==1:
        error=1
        pass
    else:
        acircle = Circle(64+int(a[0]), 32-int(a[1]), 1, outline=0xFFFF00)
        splash.append(acircle)
        display.show(splash)
    if error == 1:
        pass
    else:
        bput=input("input second point")
        b=bput.split(",")
        ba=test(b[0])
        bb=test(b[1])
        if ba==1 or bb==1:
            error=1
            pass
        else:

            bcircle = Circle(64+int(b[0]), 32-int(b[1]), 1, outline=0xFFFF00)
            splash.append(bcircle)
            display.show(splash)

    if error==1:
        error=0
        pass
    else:
        cput=input("input third point")
        c=cput.split(",")
        ca=test(c[0])
        cb=test(c[1])
        if ca==1 or cb==1:
            pass
        else:

            ccircle = Circle(64+int(c[0]), 32-int(c[1]), 1, outline=0xFFFF00)
            triangle = Triangle(64+int(a[0]), 32-int(a[1]), 64+int(b[0]), 32-int(b[1]), 64+int(c[0]), 32-int(c[1]), outline=0xFFFF00)
            splash.append(triangle)
            splash.append(ccircle)
            display.show(splash)
            a1=float(a[0])
            a2=float(a[1])
            b1=float(b[0])
            b2=float(b[1])
            c1=float(c[0])
            c2=float(c[1])
            calculate(a1,a2,b1,b2,c1,c2)
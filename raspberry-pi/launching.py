#type:ignore
import board
import busio
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
triangles=[[-50,-17,-57,12,-22,-7],[28,-14,60,-7,54,18],[45,30,51,-1,18,6],[5,5,19,15,22,10]]
counter=[]
area=0
y=[]
z=0
position=[]
def centroid(a,b,c,d,e,f):
    set1=((a+c+e)/3)
    set2=((b+d+f)/3)
    print(set1,",",set2)
    distance=(set1**2+set2**2)**(1/2)
    print(distance)
    return(distance)
def calculate(a,b,c,d,e,f):
    s1=a*(d-f)/2
    s2=c*(f-b)/2
    s3=e*(b-d)/2
    area = abs(s1+s2+s3)
    return area
while True:
    splash=displayio.Group()
    hline = Line(0,32,128,32, color=0xFFFF00)
    splash.append(hline)
    bline = Line(64,0,64,64,color=0xFFFF00)
    splash.append(bline)
    display.show(splash)
    print (len(triangles))
    for r in range(len(triangles)):
        i=triangles[r-1]
        print(i)
        tri = Triangle(i[0],i[1],i[2],i[3],i[4],i[5], outline=0xFFFF00)
        x=calculate(i[0],i[1],i[2],i[3],i[4],i[5])
        if x>100:
            counter.append(x)
            position.append(centroid(i[0],i[1],i[2],i[3],i[4],i[5]))
            if min(position)==centroid(i[0],i[1],i[2],i[3],i[4],i[5]):
                y=[i[0],i[1],i[2],i[3],i[4],i[5]]
                z=centroid(i[0],i[1],i[2],i[3],i[4],i[5])
        splash.append(tri)
        display.show(splash)
    print(f"the closest triangle with an area of {x} has the vertices {y} with a distance of {z} ")
    time.sleep(5)
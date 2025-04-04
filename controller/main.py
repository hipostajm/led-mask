import threading
from controller.pins import Pins
from controller.pixels import Pixels
from controller.matrix import Matrix
import time

width, hight = 64, 32

pins = Pins(red0=19, red1=26, green0=11, green1=5, blue0=6, blue1=13, a=25, b=8, c=7, d=1, clk=16, latch=20, oe=21) # your gpio connection with matrix https://learn.lushaylabs.com/content/images/size/w1000/2023/11/hub75-pinout.png
pixels = Pixels(width=width, hight=hight)
matrix = Matrix(pixels, pins)

a = True

threading.Thread(target=matrix.run, args=a).start()

for i in width:
    time.sleep(0.25)
    pixels.set_pixel(i, 1, 7)
    pixels.set_pixel(i, 3, 7)

time.sleep(5)
a = False
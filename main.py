import threading
from pins import Pins
from pixels import Pixels
from matrix import Matrix
import time

width, hight = 64, 32

pins = Pins(red0=19, red1=26, green0=11, green1=5, blue0=6, blue1=13, a=25, b=8, c=7, d=1, clk=16, latch=20, oe=21)
pixels = Pixels(width=width, hight=hight, initial_value=0)
matrix = Matrix(pixels, pins)


def matrix_run():
    while True:
        matrix.refresh()
    
threading.Thread(target=matrix_run).start()

for i in width:
    time.sleep(1)
    pixels.set_pixel(i, 23, 7)
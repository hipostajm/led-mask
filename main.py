from pins import Pins
from pixels import Pixels
from matrix import Matrix

# red0 = 19
# green0 = 11
# blue0 = 6
# red1 = 26
# green1 = 5
# blue1 = 13
# clk = 16
# a_pin = 25
# b_pin = 8
# c_pin = 7
# d_pin = 1
# latch_pin = 20
# oe_pin = 21


pins = Pins(red0=19, red1=26, green0=11, green1=5, blue0=6, blue1=13, a=25, b=8, c=7, d=1, clk=16, latch=20, oe=21)
pixels = Pixels(64, 32)
matrix = Matrix(pixels, pins)

while True:
    matrix.refresh()
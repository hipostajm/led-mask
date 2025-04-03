from PIL import Image
import math
im = Image.open('./test.png').convert("RGB")

pixels = list(im.getdata())
width, height = im.size

# print(pixels)

pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

colors = ((0,0,0), (2, 0, 253), (255, 2, 1,), (255, 2, 253), (0, 255, 28), (2, 255, 255), (255, 255, 29), (225,255,255))

def flatter(pixels, width, height):

    new_pixels = []

    for y in range(height):
        new_pixels.append([])
        for x in range(width):
            new_pixels[y].append(0)
    

    for y in range(len(pixels)):
        for x in range(y):
            minimal = math.inf
            picked_color = 0
            for i, color in enumerate(colors):
                dif_sum = abs(sum(color) - sum(pixels[y][x]))
                if dif_sum < minimal:
                    minimal = dif_sum
                    picked_color = i

            new_pixels[y][x] = picked_color

    return new_pixels

pixels = flatter(pixels, width, height)


import RPi.GPIO as GPIO
import time

delay = 0.000001

GPIO.setmode(GPIO.BCM)
red0 = 19
green0 = 11
blue0 = 6
red1 = 26
green1 = 5
blue1 = 13
clk = 16
a_pin = 25
b_pin = 8
c_pin = 7
d_pin = 1
latch_pin = 20
oe_pin = 21

GPIO.setup(red0, GPIO.OUT)
GPIO.setup(green0, GPIO.OUT)
GPIO.setup(blue0, GPIO.OUT)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(green1, GPIO.OUT)
GPIO.setup(blue1, GPIO.OUT)
GPIO.setup(clk, GPIO.OUT)
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)
GPIO.setup(d_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(oe_pin, GPIO.OUT)

width = 64
hight = 32

# screen = [[0 for x in range(width)] for x in range(hight)]
screen = pixels

def clock():
    GPIO.output(clk, 1)
    GPIO.output(clk, 0)

def latch():
    GPIO.output(latch_pin, 1)
    GPIO.output(latch_pin, 0)

def bits_from_int(x):
    a_bit = x & 2**0
    b_bit = x & 2**1
    c_bit = x & 2**2
    d_bit = x & 2**3
    return (a_bit, b_bit, c_bit, d_bit)

def set_row(row):
    #time.sleep(delay)
    a_bit, b_bit, c_bit, d_bit = bits_from_int(row)
    GPIO.output(a_pin, a_bit)
    GPIO.output(b_pin, b_bit)
    GPIO.output(c_pin, c_bit)
    GPIO.output(d_pin, d_bit)
    #time.sleep(delay)

def set_color_top(color):
    #time.sleep(delay)
    red, green, blue, x = bits_from_int(color)
    GPIO.output(red0, red)
    GPIO.output(green0, green)
    GPIO.output(blue0, blue)
    #time.sleep(delay)

def set_color_bottom(color):
    #time.sleep(delay)
    red, green, blue, x = bits_from_int(color)
    GPIO.output(red1, red)
    GPIO.output(green1, green)
    GPIO.output(blue1, blue)
    #time.sleep(delay)

def refresh():
    for row in range(hight//2):
        GPIO.output(oe_pin, 1)
        set_color_top(0)
        set_row(row)
        #time.sleep(delay)
        for col in range(width):
            set_color_top(screen[row][col])
            set_color_bottom(screen[row+hight//2][col])
            clock()
        #GPIO.output(oe_pin, 0)
        latch()
        GPIO.output(oe_pin, 0)
        time.sleep(delay)

def fill_rectangle(x1, y1, x2, y2, color):
    for x in range(x1, x2):
        for y in range(y1, y2):
            screen[y][x] = color


def set_pixel(x, y, color):
    screen[y][x] = color

while True:
    refresh()

from pixels import Pixels
from pins import Pins
import RPi.GPIO as GPIO
import time

class Matrix:
    def __init__(self, pixels: Pixels, pins: Pins, delay: int = 0.000001):
        self.pixels = pixels
        self.pins = pins
        self.delay = delay

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(tuple(pins.__dict__.values()), GPIO.OUT)

    def _clock(self):
        GPIO.output(self.pins.clk, 1)
        GPIO.output(self.pins.clk, 0)
    
    def _latch(self):
        GPIO.output(self.pins.latch, 1)
        GPIO.output(self.pins.latch, 0)

    def _bits_from_int(self, x: int):
        a_bit = x & 2**0
        b_bit = x & 2**1
        c_bit = x & 2**2
        d_bit = x & 2**3
        return (a_bit, b_bit, c_bit, d_bit)
    
    def _set_row(self, row):
        a_bit, b_bit, c_bit, d_bit = self._bits_from_int(row)
        GPIO.output(self.pins.a, a_bit)
        GPIO.output(self.pins.b, b_bit)
        GPIO.output(self.pins.c, c_bit)
        GPIO.output(self.pins.d, d_bit)
    
    def _set_color_top(self, color): #the top leyer of matrix
        red, green, blue, x = self._bits_from_int(color) # x is not used
        GPIO.output(self.pins.red0, red)
        GPIO.output(self.pins.green0, green)
        GPIO.output(self.pins.blue0, blue)

    def _set_color_bottom(self, color): #the bottom leyer of matrix
        red, green, blue, x = self._bits_from_int(color) # x is not used
        GPIO.output(self.pins.red1, red)
        GPIO.output(self.pins.green1, green)
        GPIO.output(self.pins.blue1, blue)

    def refresh(self):
        for row in range(self.pixels.hight//2):
            GPIO.output(self.pins.oe, 1)
            self._set_color_top(0)
            self._set_row(row)
            #time.sleep(delay)
            for col in range(self.pixels.width):
                self._set_color_top(self.pixels.get_pixel(col,row))
                self._set_color_bottom(self.pixels.get_pixel(col,row+self.pixels.hight//2))
                self._clock()
            #GPIO.output(oe_pin, 0)
            self._latch()
            GPIO.output(self.pins.oe, 0)
            time.sleep(self.delay)
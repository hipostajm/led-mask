from pydantic.dataclasses import dataclass

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

@dataclass
class Pins():
    #collors
    red0: int
    red1: int
    green0: int
    green1: int
    blue0: int
    blue1: int

    #addresing
    a: int
    b: int
    c: int
    d: int

    #idk how to discrbie those
    clk: int
    latch: int
    oe: int

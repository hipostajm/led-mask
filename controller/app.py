from flask import Flask
from flask import request
import time
import threading
from pins import Pins
from pixels import Pixels
from matrix import Matrix

width, hight = 64, 32

pins = Pins(red0=19, red1=26, green0=11, green1=5, blue0=6, blue1=13, a=25, b=8, c=7, d=1, clk=16, latch=20, oe=21) # your gpio connection with matrix https://learn.lushaylabs.com/content/images/size/w1000/2023/11/hub75-pinout.png
pixels = Pixels(width=width, hight=hight)
matrix = Matrix(pixels, pins)

a = True

threading.Thread(target=matrix.run, args=(a,)).start()

app = Flask(__name__)

@app.get("/test")
def test():
    def thread():
        for w in range(width):
            time.sleep(0.25)
            for h in range(hight):
                pixels.set_pixel(w, h, w%8)
    threading.Thread(target=thread).start()
    return {"succes": True}

@app.post("/set")
def test():
    data = request.get_json()
    def thread():
        pixels.set_pixel(data["x"], data["y"], data["color"])
    threading.Thread(target=thread).start()
    return {"succes": True}
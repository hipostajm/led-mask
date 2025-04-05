from flask import Flask
from flask import request
import time
import threading
from pins import Pins
from pixels import Pixels
from matrix import Matrix
from condictional import Condictional
from animated_image import AnimatedImage

width, height = 64, 32

pins = Pins(red0=19, red1=26, green0=11, green1=5, blue0=6, blue1=13, a=25, b=8, c=7, d=1, clk=16, latch=20, oe=21) # your gpio connection with matrix https://learn.lushaylabs.com/content/images/size/w1000/2023/11/hub75-pinout.png
pixels = Pixels(width=width, height=height)
matrix = Matrix(pixels, pins)

condictional = Condictional()
animation_condictional = Condictional()

main_thread = threading.Thread(target=matrix.run, args=(condictional,))
main_thread.start()


app = Flask(__name__)

@app.get("/test/")
def test():
    def thread():
        for w in range(width):
            time.sleep(0.25)
            for h in range(height):
                pixels.set_pixel(w, h, w%8)
    threading.Thread(target=thread).start()
    return {"succes": True}, 200

@app.patch("/set/")
def set():    
    data = request.get_json()
    pixels.set_pixel(int(data["x"]), int(data["y"]), int(data["color"]))
    return {"succes": True}, 200

@app.delete("/clear/")
def clear():
    pixels.clear()
    return {"sucess": True}, 200

@app.put("/set-all/")
def set_all():
    animation_condictional.condiction = False

    data = request.get_json()
    pixels.set_all(data["pixels"])
    return {"succes": True}, 200

@app.get("/get-pixel")
def get_pixel():
    data = request.get_json()
    return pixels.get_pixel(int(data["x"]), int(data["y"])), 200

@app.get("/get-pixels")
def get_pixels():
    return pixels.get_pixels, 200

@app.get("/kill/")
def kill():
    condictional.condiction = False
    return {"succes": True}, 200

@app.get("/start/")
def start():
    kill()
    condictional.condiction = True
    main_thread = threading.Thread(target=matrix.run, args=(condictional,))
    main_thread.start()
    return {"sucess": True}, 200

@app.put("/animate/")
def animate():
    animation_condictional.condiction = False
    

    data = request.get_json()
    animated_image = AnimatedImage(data["delay"], data["frames"])
    animation_condictional.condiction = True
    animation_thread = threading.Thread(target=animated_image.animate, args=(pixels, animation_condictional))
    
    animation_thread.start()
    return {"sucess": True}, 200

@app.get("/size/")
def size():
    return {"height": height, "width": width}
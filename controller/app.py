from main import pixels, width
from flask import Flask
import time

app = Flask(__name__)

@app.get("/")
def get():
    for i in range(width):
        time.sleep(0.05)
        pixels.set_pixel(i, 10, 7)
        pixels.set_pixel(i, 30, 7)
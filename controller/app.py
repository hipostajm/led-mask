from main import pixels, width
from flask import Flask
import time

app = Flask(__name__)

@app.get("/<int: id>")
def get(id: int):
    for i in range(width):
        time.sleep(0.05)
        pixels.set_pixel(i, i, 7)
    return {"succes": True}

if __name__ == "__main__":
    app.run(host='0.0.0.0')
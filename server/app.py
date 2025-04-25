from flask import Flask
from flask import request
from flask import redirect
import requests
from sys import path
from werkzeug.utils import secure_filename
from PIL import Image
from io import BytesIO
from resize_image import resize_image
from flat_image import flat_image
from send_image import send_image

path.append("")


IP = "https://192.168.1.41:5000"
height, width = 32, 64 #requests.get(url=IP+"/size/", verify=False).json().values()

app = Flask(__name__)

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {"jpg", "png", "webp"}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowd_file(filename: str, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.get("/image/")
def get_image():
    with open("./forms/image-form.html") as form:
        return form.read() 

@app.post("/image/")
def post_image():

    if "image" not in request.files:
        return "No image was sended ;("
    
    file = request.files["image"]

    if file and allowd_file(file.filename, ALLOWED_EXTENSIONS):
        filename = secure_filename(file.filename)
        image = Image.open(BytesIO(file.stream.read())).convert("RGBA")
        image = resize_image(image, width, height)
        image = flat_image(image, width, height)

        requests.post(json={"image": image}, url=IP+"/set-all/")

        return redirect("/image/"), 200
    
    elif file and allowd_file(file.filename, ("gif",)):
        image = Image.open(BytesIO(file.stream.read()))
        
        frames = []   

        try:
            while 1:
                image.seek(image.tell() + 1)
                duration = image.info["duration"]
                image.convert("RGBA")
                frame = flat_image(resize_image(image, width, height), width, height)
                frames.append({"duration": duration, "frame": frame})
        except EOFError:
                pass
        
        requests.post(url=IP+"/animate/", json={"frames": frames})
        return redirect("/image/"),200

    else:
        return "some problem happend", 400 
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
from AppApiConnector import AppApiConnector
from AppController import AppController 
from AppController import NoImageSendedException
from AppController import WrongExtensionsOfImageException

path.append("")


IP = "http://192.168.1.41:5000"
height, width = requests.get(url=IP+"/size/", verify=False).json().values()

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"jpg", "png", "webp", 'jpeg'}
ANIMATED_ALLOWED_EXTESIONS = {"gif",}

appApiConnector = AppApiConnector()
appController = AppController(IP, ALLOWED_EXTENSIONS, ANIMATED_ALLOWED_EXTESIONS, width, height, appApiConnector) 
 

@app.get("/image/")
def get_image():
    with open("./forms/image-form.html") as form:
        return form.read() 

@app.post("/image/")
def post_image():

    try:
        appController.post_image(request)
        return app.redirect("/image/"), 200
    except NoImageSendedException:
        return "No image was sended ;(", 400
    except WrongExtensionsOfImageException:
        return "Wrong Extesion of image ;(", 400
    except:
        return "some error happend idk what :3c", 500



    # if "image" not in request.files:
    #     return "No image was sended ;("
    
    # file = request.files["image"]

    # if file and allowd_file(file.filename, ALLOWED_EXTENSIONS):
    #     filename = secure_filename(file.filename)
    #     image = Image.open(BytesIO(file.stream.read())).convert("RGBA")
    #     image = resize_image(image, width, height)
    #     image = flat_image(image, width, height)

    #     requests.post(json={"image": image}, url=IP+"/set-all/")

    #     return redirect("/image/"), 200
    
    # elif file and allowd_file(file.filename, ("gif",)):
    #     image = Image.open(BytesIO(file.stream.read()))
        
    #     frames = []   


    #     image_copy = image.copy().convert("RGBA")
    #     first_frame_duration = image_copy.info["duration"]
    #     first_frame = flat_image(resize_image(image_copy, width, height), width, height)
    #     frames.append({"duration": first_frame_duration/1000, "frame": first_frame})

    #     try:
    #         while 1:
    #             image.seek(image.tell() + 1)
    #             duration = image.info["duration"]
    #             image.convert("RGBA")
    #             frame = flat_image(resize_image(image, width, height), width, height)
    #             frames.append({"duration": duration/1000, "frame": frame})
    #     except EOFError:
    #             pass
        
    #     requests.post(url=IP+"/animate/", json={"frames": frames})
    #     return redirect("/image/"),200

    # else:
    #     return "some problem happend", 400 

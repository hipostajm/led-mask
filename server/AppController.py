from flask import Request
from io import BytesIO
from PIL import Image
from resize_image import resize_image
from flat_image import flat_image
from AppApiConnector import AppApiConnector
import requests

class NoImageSendedException(Exception):
    pass

class WrongExtensionsOfImageException(Exception):
    pass

class AppController:
    def __init__(self, IP: str, ALLOWED_EXTENSIONS: set|list|tuple, ANIMATED_ALLOWED_EXTENSIONS: list|tuple|set, width: int, height: int, appApiConnector:AppApiConnector):
        self.IP = IP
        self.ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS
        self.ANIMATED_ALLOWED_EXTENSIONS = ANIMATED_ALLOWED_EXTENSIONS
        self.width = width
        self.height = height
        self.appApiConnector = appApiConnector
    
    def allowd_file(self, filename: str, extensions: list|tuple|set):
        return '.' in filename and filename.rsplit('.', 1)[-1].lower() in extensions
    
    def post_image(self, request: Request):
        
        if "image" not in request.files:
            raise NoImageSendedException
        
        file = request.files["image"]
        image = Image.open(BytesIO(file.stream.read()))

        if self.allowd_file(file.filename, self.ALLOWED_EXTENSIONS):
            image = self.addapt_image(image)
            self.appApiConnector.send_image(self.IP, image)
        
        elif self.allowd_file(file.filename, self.ANIMATED_ALLOWED_EXTENSIONS):
            animeted_image = self.addapt_animated_image(image)
            self.appApiConnector.send_animated_image(self.IP, animeted_image)
        
        else:
            raise WrongExtensionsOfImageException

    def addapt_image(self, image: Image):
        image.convert("RGBA")
        image = resize_image(image, self.width, self.height)
        image = flat_image(image, self.width, self.height)
        return image

    def addapt_animated_image(self, image: Image):        
        frames = []   

        image_copy = image.copy().convert("RGBA")
        first_frame_duration = image_copy.info["duration"]
        first_frame = resize_image(image_copy, self.width, self.height)
        first_frame = flat_image(first_frame, self.width, self.height)

        frames.append({"duration": first_frame_duration/1000, "frame": first_frame})

        try:
            while 1:
                image.seek(image.tell() + 1)
                duration = image.info["duration"]
                image.convert("RGBA")
                frame = resize_image(image, self.width, self.height)
                frame = flat_image(frame, self.width, self.height)
                frames.append({"duration": duration/1000, "frame": frame})
        except EOFError:
                pass
        
        return frames
                


from PIL import Image
from server.resize_image import resize_image
from server.flat_image import flat_image

image = Image.open("./assets/kitty-hi.gif").convert("RGBA")
width, height = image.size

resized = flat_image(resize_image(image, 64, 32), 64, 32)
uwu = image.info["delay"]


try:
    while 1:
        image.seek(image.tell() + 1)
        duration = image.info["duration"]
        frame = flat_image(resize_image(image, 64, 32),64,32)
except EOFError:
        pass
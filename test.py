import math
from PIL import Image
import requests

im = Image.open('./assets/image.png').convert("RGB")
im2 = Image.open('./assets/test.png').convert("RGB")
im3 = Image.open('./assets/tesssst-export.png').convert("RGB")

pixels = list(im.getdata())
pixels2 = list(im2.getdata())
pixels3 = list(im3.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
pixels2 = [pixels2[i * width:(i + 1) * width] for i in range(height)]
pixels3 = [pixels3[i * width:(i + 1) * width] for i in range(height)]

colors = ((0,0,0),(255, 2, 1,),(0, 255, 28),(255,255,29), (2, 0, 253),(255, 2, 253),(2,255,255),(255,255,255))

def flatter(pixels, width, height):

    new_pixels = []

    for y in range(height):
        new_pixels.append([])
        for x in range(width):
            new_pixels[y].append(0)

    for y in range(height):
        for x in range(width):
            minimal = math.inf
            picked_color = 0
            for i, color in enumerate(colors):
                distance = math.sqrt((color[0]-pixels[y][x][0])**2+(color[1]-pixels[y][x][1])**2+(color[2]-pixels[y][x][2])**2)
                if distance < minimal:
                    minimal = distance
                    picked_color = i

            new_pixels[y][x] = picked_color

    return new_pixels

pixels = flatter(pixels, width, height)
pixels2 = flatter(pixels2, width, height)
pixels3 = flatter(pixels3, width, height)
# print(*pixels, sep='\n')
1
requests.put(verify=False,url="https://192.168.1.41:5000/set-all/", json={"pixels": pixels, "delay": 1})
# requests.put(url="http://192.168.1.41:5000/animate/", json={"frames": [pixels2, pixels3], "delay": 1})
# requests.put(url="http://192.168.1.41:5000/animate/", json={"frames": [pixels], "delay": 1})
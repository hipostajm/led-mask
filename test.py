import math
from PIL import Image
im = Image.open('test.png').convert("RGB")

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

# print(*pixels, sep="\n")

colors = ((0,0,0), (2, 0, 253), (255, 2, 1,), (255, 2, 253), (0, 255, 28), (2, 255, 255), (255, 255, 29), (225,255,255))

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
                dif_sum = abs(sum(color) - sum(pixels[y][x]))
                if dif_sum < minimal:
                    minimal = dif_sum
                    picked_color = i

            new_pixels[y][x] = picked_color

    return new_pixels

pixels = flatter(pixels, width, height)
print(*pixels, sep='\n')
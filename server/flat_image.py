import math 

colors = ((0,0,0),(255, 2, 1,),(0, 255, 28),(255,255,29), (2, 0, 253),(255, 2, 253),(2,255,255),(255,255,255))

def flat_image(pixels, width, height):

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
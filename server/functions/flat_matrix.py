from functions.flat_color import flat_color 

colors = ((0,0,0),(255, 2, 1,),(0, 255, 28),(255,255,29), (2, 0, 253),(255, 2, 253),(2,255,255),(255,255,255))

def flat_image(pixels, width, height):

    new_pixels = []

    for y in range(height):
        new_pixels.append([])
        for x in range(width):
            new_pixels[y].append(0)

    for y in range(height):
        for x in range(width):
            new_pixels[y][x] = flat_color(pixels[y][x], colors)

    return new_pixels
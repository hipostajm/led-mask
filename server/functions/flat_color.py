import math

def flat_color(given_color: list[int,int,int]|tuple[int,int,int], colors: list[list[int,int,int]]):
    minimal = math.inf
    picked_color = 0
    for i, color in enumerate(colors):
        distance = math.sqrt((given_color[0]-color[0])**2+(given_color[1]-color[1])**2+(given_color[2]-color[2])**2)
        if distance < minimal:
            minimal = distance
            picked_color = i


    return picked_color
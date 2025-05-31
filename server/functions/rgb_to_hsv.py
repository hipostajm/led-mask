from math import ceil

def rgb_to_hsv(color):
    temp = min(color[0], color[1], color[2])
    hsv = [0,0,0] # h, s, v
    hsv[2] = max(color[0], color[1], color[2])
    
    if temp != hsv[2]:
        if color[0] == hsv[2]:
            hsv[0] = ((color[1]-color[2])*60 / (hsv[2]-temp))
        elif color[1] == hsv[2]:
            hsv[0] = 120 + ((color[2]-color[0])*60 / (hsv[2]-temp))
        elif color[2] == hsv[2]:
            hsv[0] =  240 + ((color[1]-color[2])*60 / (hsv[2]-temp))
    
    if hsv[0] < 0:
        hsv[0] + 360
    
    if hsv[2] == 0:
        hsv[1] = 0
    else:
        hsv[1] = (hsv[2]-temp)*100 / hsv[2]
        
    hsv[2] = (100*hsv[2]) / 255

    hsv[0] = round(hsv[0])
    hsv[1] = round(hsv[1])
    hsv[2] = round(hsv[2])

    return hsv   
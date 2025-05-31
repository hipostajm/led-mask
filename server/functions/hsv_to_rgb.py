def hsv_to_rgb(hsv: list[int,int,int]|tuple[int,int,int]) -> list[int,int,int]:
    # h, s, v
    
    maximal = ((hsv[2]*255)/100) #this one is r or g or b but idk which one so I need to check it
    
    if maximal == 0:
        return [0,0,0]
    else:
        minimal = ((-1*maximal*hsv[1])/100 + maximal)

    if hsv[0] >= 300:
        h_prim = (hsv[0]-360)/60
    else:
        h_prim = hsv[0]/60
        
    c = maximal-minimal
        
    if h_prim >= -1 and h_prim <1:
        if h_prim < 0:
            rgb = [maximal, minimal, minimal-h_prim*c]
        else:
            rgb = [maximal, minimal+h_prim*c, minimal]
    elif h_prim >= 1 and h_prim < 3:
        if h_prim < 2:
            rgb = [minimal - (h_prim - 2)*c, maximal, minimal]
        else:
            rgb = [minimal, maximal, minimal+(h_prim-2)*c]
    
    else:
        if h_prim < 4:
            rgb = [minimal, minimal - (h_prim-4)*c, maximal]
        else:
            rgb = [minimal+(h_prim-4)*c,minimal, maximal]
    
    rgb[0] = round(rgb[0])
    rgb[1] = round(rgb[1])
    rgb[2] = round(rgb[2])
    
    return rgb
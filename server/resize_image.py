from PIL import Image
from math import ceil

def resize_image(img: Image, new_width = 64, new_height = 32):

    width, height = img.size
    img = list(img.getdata())
    img = [img[i * width:(i + 1) * width] for i in range(height)]

    x_scaling_factor = new_width/(width-1)
    y_scaling_factor = new_height/(height-1)

    new_img = [[(0,0,0)]*new_width for _ in range(new_height)]


    for y in range(height):
        for x in range(width):
            if x+1 >= width:
                continue

            curvecure_r = (img[y][x+1][0]-img[y][x][0])/(x_scaling_factor-1)
            curvecure_g = (img[y][x+1][1]-img[y][x][1])/(x_scaling_factor-1)
            curvecure_b = (img[y][x+1][2]-img[y][x][2])/(x_scaling_factor-1)

            if y+1 >= height:
                continue

            for xi in range(ceil(x_scaling_factor)):
                if len(img[y][x]) == 4 and img[y][x][3] == 0:
                    new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)] = (0,0,0)
                else:
                    current_pixel = img[y][x]
                    new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)] = (
                                                            int(curvecure_r*xi+current_pixel[0])
                                                            ,int(curvecure_g*xi+current_pixel[1])
                                                            ,int(curvecure_b*xi+current_pixel[2])
                                                            )
            
            curvecure_r = (img[y+1][x+1][0]-img[y+1][x][0])/(x_scaling_factor-1)
            curvecure_g = (img[y+1][x+1][1]-img[y+1][x][1])/(x_scaling_factor-1)
            curvecure_b = (img[y+1][x+1][2]-img[y+1][x][2])/(x_scaling_factor-1)

            for xi in range(ceil(x_scaling_factor)):
                if len(img[y][x]) == 4 and img[y][x][3] == 0:
                    new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)] = (0,0,0)
                else:
                    current_pixel = img[y+1][x]
                    new_img[int((y+1)*y_scaling_factor)-1][xi+int(x*x_scaling_factor)] = (
                                                            int(curvecure_r*xi+current_pixel[0])
                                                            ,int(curvecure_g*xi+current_pixel[1])
                                                            ,int(curvecure_b*xi+current_pixel[2])
                                                            )

                curvecure_r_for_y = (new_img[int((y+1)*y_scaling_factor)-1][xi+int(x*x_scaling_factor)][0] - new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)][0])/(y_scaling_factor-1)
                curvecure_g_for_y = (new_img[int((y+1)*y_scaling_factor)-1][xi+int(x*x_scaling_factor)][1] - new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)][1])/(y_scaling_factor-1)
                curvecure_b_for_y = (new_img[int((y+1)*y_scaling_factor)-1][xi+int(x*x_scaling_factor)][2] - new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)][2])/(y_scaling_factor-1)

                for yi in range(ceil(y_scaling_factor)-2):
                    yi += 1

                    new_img[yi+int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)] = (
                        int(curvecure_r_for_y * yi + new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)][0]),
                        int(curvecure_g_for_y * yi + new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)][1]),
                        int(curvecure_b_for_y * yi + new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)][2]))
    
    return new_img


# output = Image.new("RGB", (new_width,  new_height))
# for y in range(new_height):
#     for x in range(new_width):
#         output.putpixel((x,y), new_img[y][x])

# output.save("out.png")
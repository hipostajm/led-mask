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

            first_pixel = img[y][x]
            secound_pixel = img[y][x+1]

            curvecure_r = (secound_pixel[0]-first_pixel[0])/(x_scaling_factor-1)
            curvecure_g = (secound_pixel[1]-first_pixel[1])/(x_scaling_factor-1)
            curvecure_b = (secound_pixel[2]-first_pixel[2])/(x_scaling_factor-1)

            if y+1 >= height:
                continue
            
            current_y = int(y*y_scaling_factor)
            current_x = int(x*x_scaling_factor)

            for xi in range(ceil(x_scaling_factor)):
                if len(first_pixel) == 4 and first_pixel[3] == 0:
                    new_img[current_y][xi+current_x] = (0,0,0)
                else:
                    new_img[current_y][xi+current_x] = (
                                                            int(curvecure_r*xi+first_pixel[0])
                                                            ,int(curvecure_g*xi+first_pixel[1])
                                                            ,int(curvecure_b*xi+first_pixel[2])
                                                            )
            
            curvecure_r = (img[y+1][x+1][0]-img[y+1][x][0])/(x_scaling_factor-1)
            curvecure_g = (img[y+1][x+1][1]-img[y+1][x][1])/(x_scaling_factor-1)
            curvecure_b = (img[y+1][x+1][2]-img[y+1][x][2])/(x_scaling_factor-1)

            current_pixel = img[y+1][x]

            for xi in range(ceil(x_scaling_factor)):
                if len(first_pixel) == 4 and first_pixel[3] == 0:
                    new_img[int(y*y_scaling_factor)][xi+int(x*x_scaling_factor)] = (0,0,0)
                else:
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
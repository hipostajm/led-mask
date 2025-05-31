from PIL import Image

def image_to_matrix(img: Image) -> list:
    width, height = img.size
    img = list(img.getdata())
    matirx = [img[i * width:(i + 1) * width] for i in range(height)]
    
    return matirx
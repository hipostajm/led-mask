from PIL import Image

with Image.open("./assets/cat-cat-kiss.gif") as im:
    im.seek(1)  # skip to the second frame

    try:
        while 1:
            im.seek(im.tell() + 1)
            print(im.info["duration"])
    except EOFError:
        pass  # end of sequence
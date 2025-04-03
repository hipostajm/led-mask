class Pixels:
    def __init__(self, width: int , hight: int):
        self.hight = hight
        self.width = width

        self.pixels = [[0]*width for _ in range(hight)]
    
    def set_pixel(self, x: int, y: int, value: int):
        self.pixels[y][x] = value
    
    def get_pixel(self, x: int, y: int):
        return self.pixels[y][x]
        
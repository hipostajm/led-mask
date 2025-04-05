class Pixels:
    def __init__(self, width: int = 64, hight: int = 32, initial_value: int = 0):
        self.hight: int = hight
        self.width: int = width
        self.initial_value: int = initial_value

        self.pixels = [[initial_value]*width for _ in range(hight)]
    
    def set_pixel(self, x: int, y: int, value: int):
        self.pixels[y][x] = value
    
    def get_pixel(self, x: int, y: int):
        return self.pixels[y][x]
        
    def get_pixels(self):
        return self.pixels

    def set_all(self, new_pixels: list):
        self.pixels = new_pixels

    def clear(self):
        self.pixels = [[self.initial_value]*self.width for _ in range(self.hight)]
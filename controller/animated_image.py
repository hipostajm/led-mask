from pixels import Pixels
from condictional import Condictional
import time

class AnimatedImage():
    def __init__(self, delay: float|int, frames: list[list[list[int]]]):
        self.delay = delay
        self.frames: list[list[list[int]]] = frames

    def animate(self, pixels: Pixels, condictional: Condictional):
        while condictional.condiction:
            for frame in self.frames:
                if not condictional.condiction:
                    break     
                pixels.set_all(frame)
                time.sleep(self.delay)
from pixels import Pixels
from condictional import Condictional
import time

class AnimatedImage():
    def __init__(self, frames: list[list[list[int]]]):
        self.frames: list[list[list[int]]] = frames

    def animate(self, pixels: Pixels, condictional: Condictional):
        while condictional.condiction:
            for frame_info in self.frames:
                if not condictional.condiction:
                    break     
                pixels.set_all(frame_info["frame"])
                time.sleep(frame_info["duration"])
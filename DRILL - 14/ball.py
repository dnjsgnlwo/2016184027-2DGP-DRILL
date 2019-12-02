import random
from pico2d import *

import game_world
import game_framework

class Ball:
    image = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1900 - 100), random.randint(0, 1200 - 100)

    def set_background(self, bg):
        self.bg = bg

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(cx, cy)


    def update(self):
        pass

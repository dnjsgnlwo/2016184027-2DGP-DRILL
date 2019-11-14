import random
from pico2d import *
import game_world
import game_framework


class Block:
    image = None

    def __init__(self):
        if Block.image is None:
            Block.image = load_image('brick180x40.png')
        self.x, self.y = 500, 250
        self.dir = 1
        self.speed = 150


    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        if self.x + 90 >= 1600:
            self.dir = 1
        elif self.x - 90 <= 0:
            self.dir = -1
        self.x += self.dir * self.speed * game_framework.frame_time


    def get_dir(self):
        return self.dir


    def get_speed(self):
        return self.speed
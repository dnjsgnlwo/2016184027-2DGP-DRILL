from pico2d import *
import game_world

class Ball:
    image = None
    def __init_(self, x = 800, y= 300, velocity = 1):
        if Ball.image == None:
            
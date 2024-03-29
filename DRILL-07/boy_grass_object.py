from pico2d import *
import random


class SBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0,10)
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(1, 10)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class BBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0,10)
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(1, 10)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

count = random.randint(1, 19)
grass = Grass()
team = [Boy() for i in range(11)]
sball = [SBall() for i in range(count)]
bball = [BBall() for i in range(20-count)]

running = True

while running:
    handle_events()

    for boy in team:
        boy.update()

    for sb in sball:
        sb.update()

    for bb in bball:
        bb.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for sb in sball:
        sb.draw()

    for bb in bball:
        bb.draw()
    update_canvas()

    delay(0.05)

close_canvas()

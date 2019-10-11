from pico2d import *
import random


def Move():
    global x, y
    global array
    for i in range(0, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * array[0][0] + (-4 * t ** 2 + 4 * t) * array[1][0] + (2 * t ** 2 - t) * array[2][
            0]
        y = (2 * t ** 2 - 3 * t + 1) * array[0][1] + (-4 * t ** 2 + 4 * t) * array[1][1] + (2 * t ** 2 - t) * array[1][
            1]
        delay(0.01)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * array[0][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * array[1][0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * array[2][0] + (t ** 3 - t ** 2) * array[3][0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * array[0][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * array[1][1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * array[2][1] + (t ** 3 - t ** 2) * array[3][1]) / 2
        delay(0.01)
    # draw p3-p4


def handle_events():
    global running

    Events = get_events()

    for event in Events:

        if event.type == SDL_QUIT:

            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:

            running = False


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')

character = load_image('animation_sheet.png')

running = True

animation = 1

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

array = [[0] * 2 for i in range(10)]
for i in array:
    for j in i:
        j = random.randint(0, 1024)

i = 0

frame = 0

hide_cursor()

while running:
    Move()
    clear_canvas()

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    character.clip_draw(frame * 100, 100 * animation, 100, 100, x, y)
    update_canvas()

    frame = (frame + 1) % 8

    handle_events()

    delay(0.01)

    close_canvas()

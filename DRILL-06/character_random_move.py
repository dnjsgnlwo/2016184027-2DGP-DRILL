from pico2d import *


def handle_events():
    global running

    global x, y

    global move_x, move_y

    global i

    global animation_line

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

mouse_x, mouse_y = 0, 0

animation_line = 1

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

move_x, move_y = x, y

i = 0

frame = 0

hide_cursor()

while running:
    clear_canvas()

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    character.clip_draw(frame * 100, 100 * animation_line, 100, 100, x, y)

    update_canvas()

    frame = (frame + 1) % 8

    handle_events()

    delay(0.01)

close_canvas()

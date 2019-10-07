from pico2d import *


def handle_events():
    global move
    global running
    global dir
    global x
    Events = get_events()
    for event in Events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                move = 100
            elif event.key == SDLK_LEFT:
                dir -= 1
                move = 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                move = 300
            elif event.key == SDLK_LEFT:
                dir += 1
                move = 200

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0
move = 300

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, move, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x += dir * 5
    if x > 785:
        x = 785
    if x < 15:
        x = 15
    delay(0.01)

close_canvas()


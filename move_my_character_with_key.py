from pico2d import *

open_canvas(1280, 1024)

sprite_sheet = load_image('walk.png')
background = load_image('TUK_GROUND.png')

frame = 0
dir_x, dir_y = 0, 0
direction = 'front'
idle = True
x, y = 640, 512
running = True


def handle_events():
    global dir_x, dir_y, direction, running, idle
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x = 1
                direction = 'right'
                idle = False
            elif event.key == SDLK_LEFT:
                dir_x = -1
                direction = 'left'
                idle = False
            elif event.key == SDLK_UP:
                dir_y = 1
                direction = 'front'
                idle = False
            elif event.key == SDLK_DOWN:
                dir_y = -1
                direction = 'back'
                idle = False
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x = 0
            elif event.key == SDLK_LEFT:
                dir_x = 0
            elif event.key == SDLK_UP:
                dir_y = 0
            elif event.key == SDLK_DOWN:
                dir_y = 0

            if dir_x == 0 and dir_y == 0:
                idle = True


while running:
    clear_canvas()
    background.draw(640, 512)

    if idle:
        if direction == 'back':
            sprite_sheet.clip_draw(5 * 95, 159 * 3, 95, 159, x, y)
        elif direction == 'right':
            sprite_sheet.clip_draw(5 * 95, 159, 95, 159, x, y)
        elif direction == 'left':
            sprite_sheet.clip_draw(5 * 95, 159 * 2, 95, 159, x, y)
        elif direction == 'front':
            sprite_sheet.clip_draw(5 * 95, 0, 95, 159, x, y)
    else:
        if direction == 'back':
            sprite_sheet.clip_draw(frame * 95, 159 * 3, 95, 159, x, y)
        elif direction == 'right':
            sprite_sheet.clip_draw(frame * 95, 159, 95, 159, x, y)
        elif direction == 'left':
            sprite_sheet.clip_draw(frame * 95, 159 * 2, 95, 159, x, y)
        elif direction == 'front':
            sprite_sheet.clip_draw(frame * 95, 0, 95, 159, x, y)

    update_canvas()
    handle_events()

    if not idle:
        frame = (frame + 1) % 12

    x += dir_x * 10
    y += dir_y * 10

    delay(0.05)

close_canvas()

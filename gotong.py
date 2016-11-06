import random
from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Rockman:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('character.png')

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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

open_canvas()

grass = Grass()
rockman = Rockman()

running = True

x = 0
while running:
    handle_events()

    rockman.update()

    clear_canvas()
    grass.draw()
    rockman.draw()
    update_canvas()
    delay(0.01)

close_canvas()
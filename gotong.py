import random
from pico2d import *

running = None
Rockman = None

class Shot:
    def __init__(self):
        self.image = load_image('Buster.png')

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Rockman:

    image = None

    RIGHT_STAND, LEFT_STAND, RIGHT_RUN, LEFT_RUN = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 3)
        self.state = 0
        if self.image == None:
            self.image = load_image('Rockman4.png')

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN):
                    self.state = self.RIGHT_RUN
            elif event.key == SDLK_LEFT:
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN):
                    self.state = self.LEFT_RUN
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                if self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_STAND
            elif event.key == SDLK_LEFT:
                if self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_STAND


    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x - 5)

    def draw(self):
        self.image.clip_draw(self.frame*32, self.state * 30, 32, 30, self.x, self.y)




def handle_events():

    global running
    global rockman
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False
        else:
            rockman.handle_events(event)

def main():

    open_canvas()

    global rockman
    global running

    rockman = Rockman()
    grass = Grass()

    running = True
    while running:
        handle_events()

        rockman.update()

        clear_canvas()
        grass.draw()
        rockman.draw()
        update_canvas()

        delay(0.01)

    close_canvas()


if __name__ == '__main__':
    main()
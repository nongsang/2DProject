import random
from pico2d import *

running = None
Rockman = None

class Buster:
    def __init__(self):
        self.image = load_image('Buster.png')

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Rockman:

    image = None

    RIGHT_STAND, LEFT_STAND, RIGHT_RUN, LEFT_RUN, RIGHT_RUN_SHOT, LEFT_RUN_SHOT = 0, 1, 2, 3, 4, 5
    RIGHT_STAND_SHOT, LEFT_STAND_SHOT, RIGHT_JUMP, LEFT_JUMP, RIGHT_JUMP_SHOT, LEFT_JUMP_SHOT = 6, 7, 8, 9, 10, 11
    RIGHT_JUMP_RIGHT, LEFT_JUMP_LEFT, RIGHT_JUMP_SHOT_RIGHT, LEFT_JUMP_SHOT_LEFT = 12, 13, 14, 15
    RIGHT_DEAD, LEFT_DEAD = 16, 17

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 3)
        self.state = 0
        if self.image == None:
            self.image = load_image('Rockman.png')

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:                                                                           # 키 다운일 때
            if event.key == SDLK_RIGHT:                                                                         # 키 다운이고 오른쪽 화살표
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN,):
                    self.state = self.RIGHT_RUN
                elif self.state in (self.RIGHT_STAND_SHOT, self.LEFT_STAND_SHOT, self.LEFT_RUN_SHOT,):
                    self.state = self.RIGHT_RUN_SHOT
                elif self.state in (self.RIGHT_JUMP, self.LEFT_JUMP, self.LEFT_JUMP_LEFT):
                    self.state = self.RIGHT_JUMP_RIGHT
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.RIGHT_JUMP_SHOT
                elif self.state in (self.RIGHT_JUMP_SHOT, self.LEFT_JUMP_SHOT, self.LEFT_JUMP_SHOT_LEFT):
                    self.state = self.RIGHT_JUMP_SHOT_RIGHT
            elif event.key == SDLK_LEFT:                                                                        # 키 다운이고 왼쪽 화살표
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN,):
                    self.state = self.LEFT_RUN
                elif self.state in (self.RIGHT_STAND_SHOT, self.LEFT_STAND_SHOT, self.RIGHT_RUN_SHOT,):
                    self.state = self.LEFT_RUN_SHOT
                elif self.state in (self.RIGHT_JUMP, self.LEFT_JUMP, self.RIGHT_JUMP_RIGHT):
                    self.state = self.LEFT_JUMP_LEFT
                elif self.state in (self.RIGHT_JUMP_SHOT,):
                    self.state = self.LEFT_JUMP_SHOT
                elif self.state in (self.RIGHT_JUMP_SHOT, self.LEFT_JUMP_SHOT, self.RIGHT_JUMP_SHOT_RIGHT):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
            elif event.key == SDLK_x:                                                                           # 키 다운이고 x키
                if self.state in (self.RIGHT_STAND,):
                    self.state = self.RIGHT_STAND_SHOT
                elif self.state in (self.LEFT_STAND,):
                    self.state = self.LEFT_STAND_SHOT
                elif self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_RUN_SHOT
                elif self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_RUN_SHOT
                elif self.state in (self.RIGHT_JUMP,):
                    self.state = self.RIGHT_JUMP_SHOT
                elif self.state in (self.LEFT_JUMP,):
                    self.state = self.LEFT_JUMP_SHOT
                elif self.state in (self.RIGHT_JUMP_RIGHT,):
                    self.state = self.RIGHT_JUMP_SHOT_RIGHT
                elif self.state in (self.LEFT_JUMP_LEFT,):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
            elif event.key == SDLK_z:                                                                           # 키 다운이고 z키
                if self.state in (self.RIGHT_STAND,):
                    self.state = self.RIGHT_JUMP
                elif self.state in (self.LEFT_STAND,):
                    self.state = self.LEFT_JUMP
                elif self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_JUMP_RIGHT
                elif self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_JUMP_LEFT
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
                elif self.state in (self.RIGHT_JUMP_SHOT,):
                    self.state = self.RIGHT_JUMP_SHOT_RIGHT
        elif event.type == SDL_KEYUP:                                                                           # 키 업일 때
            if event.key == SDLK_RIGHT:                                                                         # 키 업이고 오른쪽 화살표
                if self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_STAND
                elif self.state in (self.RIGHT_RUN_SHOT,):
                    self.state = self.RIGHT_STAND_SHOT
                elif self.state in (self.RIGHT_JUMP_RIGHT,):
                    self.state = self.RIGHT_JUMP
                elif self.state in (self.RIGHT_JUMP_SHOT_RIGHT,):
                    self.state = self.RIGHT_JUMP_SHOT
            elif event.key == SDLK_LEFT:                                                                        # 키 업이고 왼쪽 화살표
                if self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_STAND
                elif self.state in (self.LEFT_RUN_SHOT,):
                    self.state = self.LEFT_STAND_SHOT
                elif self.state in (self.LEFT_JUMP_LEFT,):
                    self.state = self.LEFT_JUMP
                elif self.state in (self.LEFT_JUMP_SHOT_LEFT,):
                    self.state = self.LEFT_JUMP_SHOT
            elif event.key == SDLK_x:                                                                           # 키 업이고 x키
                if self.state in (self.RIGHT_STAND_SHOT,):
                    self.state = self.RIGHT_STAND
                elif self.state in (self.LEFT_STAND_SHOT,):
                    self.state = self.LEFT_STAND
                elif self.state in (self.RIGHT_RUN_SHOT,):
                    self.state = self.RIGHT_RUN
                elif self.state in (self.LEFT_RUN_SHOT,):
                    self.state = self.LEFT_RUN
                elif self.state in (self.RIGHT_JUMP_SHOT,):
                    self.state = self.RIGHT_JUMP
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.LEFT_JUMP
                elif self.state in (self.RIGHT_JUMP_SHOT_RIGHT,):
                    self.state = self.RIGHT_JUMP_RIGHT
                elif self.state in (self.LEFT_JUMP_SHOT_LEFT,):
                    self.state = self.LEFT_JUMP_LEFT
            elif event.key == SDLK_z:                                                                           # 키 업이고 z키
                if self.state in (self.RIGHT_JUMP,):
                    self.state = self.RIGHT_STAND
                elif self.state in (self.LEFT_JUMP,):
                    self.state = self.LEFT_STAND
                elif self.state in (self.RIGHT_JUMP, self.RIGHT_JUMP_RIGHT):
                    self.state = self.RIGHT_RUN
                elif self.state in (self.LEFT_JUMP, self.LEFT_JUMP_LEFT):
                    self.state = self.LEFT_RUN
                elif self.state in (self.RIGHT_JUMP_RIGHT,):
                    self.state = self.RIGHT_JUMP
                elif self.state in (self.LEFT_JUMP_LEFT,):
                    self.state = self.LEFT_JUMP



    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.state in (self.RIGHT_RUN, self.RIGHT_RUN_SHOT,):
            self.x = min(800, self.x + 5)
        elif self.state in (self.LEFT_RUN, self.LEFT_RUN_SHOT,):
            self.x = max(0, self.x - 5)
        elif self.state in (self.RIGHT_JUMP_RIGHT, self.RIGHT_JUMP_SHOT_RIGHT,):
            self.x = min(800, self.x + 5)
        elif self.state in (self.LEFT_JUMP_LEFT, self.LEFT_JUMP_SHOT_LEFT,):
            self.x = max(0, self.x - 5)
        elif self.state in (self.RIGHT_JUMP, self.LEFT_JUMP, self.RIGHT_JUMP_SHOT, self.LEFT_JUMP_SHOT, self.RIGHT_JUMP_SHOT_RIGHT, self.LEFT_JUMP_SHOT_LEFT):
            self.y += 5

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
# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 40.0  # 20km/h
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60  # m/m
RUN_SPEED_MPS = RUN_SPEED_MPM / 60
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.6  # 한번 애니메이션 재생하는 시간
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4
MAX_FRAME = [4,5,5]

FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ACTION

BIRD_SIZE = [200,200]

class Bird:
    def __init__(self,pos_x,pos_y):
        self.x, self.y = pos_x, pos_y
        self.frame = 0
        self.action = 0
        self.face_dir = 1
        self.dir = 1
        self.speed = 100
        self.image = load_image('bird_animation.png')

    def update(self):
        if self.frame > MAX_FRAME[self.action] :
            self.action += 1
            print(self.action)
            if self.action > 2:
                self.action = 0

        self.frame = (self.frame + FRAMES_PER_TIME * game_framework.frame_time) % MAX_FRAME[self.action]

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)

        if self.x == 1600-25 :
            self.dir = -1
        elif self.x == 25 :
            self.dir = 1


    def handle_event(self, event):
        pass

    def draw(self):
        if self.dir == 1 :
            self.image.clip_draw(int(self.frame) * 182, self.action * 168, 182, 163, self.x, self.y,BIRD_SIZE[0],BIRD_SIZE[1])
        if self.dir == -1 :
            self.image.clip_composite_draw(int(self.frame) * 182, self.action * 168, 182, 163,0,'h', self.x, self.y,BIRD_SIZE[0],BIRD_SIZE[1])


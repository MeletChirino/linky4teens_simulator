import os
import pygame
from numpy import cos, sin

# local modules
from events import RELAY_EVENT

class Player:
    def __init__(self, x, y, pic):
        self.x = x
        self.y = y
        self.angle = -90
        self.speed = 0
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        logo = pygame.image.load(F'{BASE_DIR}/{pic}')
        self.logo = pygame.transform.scale(logo, (50, 50))

    def update_params(self, params):
        self.params = params

    def move_forward(self):
        self.speed = self.params['speed']

    def stop_move(self):
        self.speed = 0

    def dynamics(self):
        self.x += self.speed
        x_limit = self.params['screen_size'][0]
        if self.x >= x_limit:
            self.x = 10

    def keystroke_movements(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                #up
                self.move_forward()
            if event.key == pygame.K_d:
                #up
                self.stop_move()
            if event.key == pygame.K_SPACE:
                RELAY_EVENT.happen(1)

START_ZONE_DELIMITER = 0
END_ZONE_DELIMITER = 1
START_RACE_DELIMITER = 2
END_RACE_DELIMITER = 3
class ZoneDelimiter:
    def __init__(self, x, type_, screen):
        self.x = x
        self.y = 100
        self.type = type_
        if self.type == START_ZONE_DELIMITER:
            self.color = (255, 0, 0)
        elif self.type == END_ZONE_DELIMITER:
            self.color = (0, 255, 134)
        elif self.type == START_RACE_DELIMITER:
            self.color = (0, 134, 255)
        elif self.type == END_RACE_DELIMITER:
            self.color = (255, 255, 134)
        self.screen = screen

    def cross(self, x):
        margin = 0.1
        lim_in = self.x - margin
        lim_sup = self.x + margin
        if x > lim_in and x < lim_sup:
            return True
        else:
            return False

    def show(self):
        pygame.draw.polygon(
                surface = self.screen,
                color = self.color,
                points = [
                    (self.x, self.y),
                    (self.x + 30, self.y + 60),
                    (self.x - 30, self.y + 60)
                    ]
                )

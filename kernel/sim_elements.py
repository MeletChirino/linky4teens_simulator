import os
import pygame
from numpy import cos, sin

class Player:
    def __init__(self, x, y, pic):
        self.x = x
        self.y = y
        self.angle = -90
        self.angle_speed = 0
        self.speed_x = 0
        self.speed_y = 0
        self.speed = 0
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        logo = pygame.image.load(F'{BASE_DIR}/{pic}')
        self.logo = pygame.transform.scale(logo, (50, 50))

    def update_params(self, params):
        self.params = params

    def move_forward(self):
        self.speed = -self.params['speed']

    def move_backward(self):
        self.speed = self.params['speed']

    def turn_left(self):
        self.angle_speed = -self.params['angle_speed']

    def turn_right(self):
        self.angle_speed = self.params['angle_speed']

    def stop_move(self):
        self.speed = 0

    def stop_rotating(self):
        self.angle_speed = 0

    def dynamics(self):
        self.x += self.speed
        self.y += 0

    def keystroke_movements(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                #up
                self.move_forward()
            if event.key == pygame.K_j:
                #down
                self.move_backward()
            if event.key == pygame.K_h:
                #left
                self.turn_left()
            if event.key == pygame.K_l:
                #right
                self.turn_right()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_k:
                #up
                self.stop_move()
            if event.key == pygame.K_j:
                #down
                self.stop_move()
            if event.key == pygame.K_h:
                #left
                self.stop_rotating()
            if event.key == pygame.K_l:
                #right
                self.stop_rotating()

START_ZONE_DELIMITER = 0
END_ZONE_DELIMITER = 1
class ZoneDelimiter:
    def __init__(self, x, y, type_, screen):
        self.x = x
        self.y = y
        self.type = type_
        if self.type == START_ZONE_DELIMITER:
            self.color = (255, 0, 0)
        elif self.type == END_ZONE_DELIMITER:
            self.color = (0, 255, 134)
        self.screen = screen

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

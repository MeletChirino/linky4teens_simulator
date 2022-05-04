# this is encharge of creating all of the temoin graphs and tasks
import pygame
import time

class LedPWM:
    def __init__(self):
        self.color = (255, 255, 255)
        self.blink = False
        self.i_blink = 0

    def reset_blink(self):
        self.i_blink = 0

    def set_color(self, color):
        self.color = color

    def set_blue(self):
        self.color = (0, 0, 255)

    def set_yellow(self):
        self.color = (255, 255, 0)

    def set_red(self):
        self.color = (255, 0, 0)

    def set_green(self):
        self.color = (0, 255, 0)

    def blink_red(self):
        if self.i_blink <= 11:
            self.blink = not self.blink
            if self.blink:
                self.set_red()
            else:
                self.set_blue()
            self.i_blink += 1
        else:
            self.set_blue()

    def blink_green(self):
        self.blink = not self.blink
        if self.blink:
            self.set_green()
        else:
            self.set_yellow()
        self.i_blink += 1
        if self.i_blink >= 11:
            self.i_blink = 0
            BLINK_GREEN_TASK.disable()

    def blink_yellow(self):
        self.blink = not self.blink
        if self.blink:
            self.set_blue()
        else:
            self.set_yellow()

class Temoin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.led = LedPWM()
        self.led.set_blue()
        self.radius = 10
        self.vibrating = False
        self.vibrate_power = 10

    def set_screen(self, screen):
        self.screen = screen

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                self.rect
                )
        self.calc_center()
        pygame.draw.circle(
                self.screen,
                self.led.color,
                self.center,
                self.radius
                )

    def calc_center(self):
        x = (self.width / 2) + self.x
        y = self.y - (self.radius / 2)
        self.center = (x, y)

    def vibrate(self):
        self.vibrating = not self.vibrating
        if self.vibrating:
            self.x += self.vibrate_power
        else:
            self.x -= self.vibrate_power

TEMOIN_HL = Temoin(30, 130)

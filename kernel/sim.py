# python modules
import pygame
import os

# local modules
from .sim_elements import *
from components.temoin import TEMOIN_HL
from events import *

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
class RaceGame:
    def __init__(self, **kwargs):
        self.screen_size = kwargs['screen_size']
        self.params = {
                'speed': 0.2,
                'screen_size': self.screen_size
                }

        pygame.init()

        self.frame = [30, 30]
        self.screen = pygame.display.set_mode(
                (self.screen_size[0],
                self.screen_size[1]
                ))
        self.running = True

        # title and icon
        pygame.display.set_caption("Linky4Teens")
        icon = pygame.image.load(F"{BASE_DIR}/athletics.png")
        pygame.display.set_icon(icon)

        # player
        self.athlete = Player(30, 30, 'athletics.png')
        self.athlete.update_params(self.params)

        # obstacles
        self.delimiters = [
                ZoneDelimiter(100, START_RACE_DELIMITER, self.screen),
                ZoneDelimiter(300, START_ZONE_DELIMITER, self.screen),
                ZoneDelimiter(700, END_ZONE_DELIMITER, self.screen),
                ZoneDelimiter(1000, END_RACE_DELIMITER, self.screen),
                ]
        self.temoin = TEMOIN_HL
        self.temoin.set_screen(self.screen)
        self.button = Button(1200, 150, 'Connect', self.screen)


    def gameloop(self):
        self.screen.fill((230, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_c:
                    # se conecta al computador
                    DISCONNECT_EVENT.happen(1)
                if event.key == pygame.K_v:
                    DATA_REQUEST_EVENT.happen(1)
            self.athlete.keystroke_movements(event)
            if self.button.pressing(event):
                CONNECT_EVENT.happen(1)

        self.athlete.dynamics()
        self.draw_element(self.athlete)
        self.temoin.draw()
        self.button.show()


        for cone in self.delimiters:
            cone.show()

        pygame.display.update()

    def draw_element(self, element, **kwargs):
        try:
            if kwargs['mode'] == "obstacle":
                # Initialing Color
                color = (0,0,0)
                # Drawing Rectangle
                pygame.draw.rect(
                        self.screen,
                        color,
                        pygame.Rect(
                            element.x,
                            element.y,
                            element.width,
                            element.height
                            )
                        )
        except:
            pass
        logo_rotated = pygame.transform.rotate(
            element.logo, element.angle + 90
            )
        self.screen.blit(
            logo_rotated,
            (element.x, element.y)
            )#drawing


if __name__ == "__main__":
    game = RaceGame(
        screen_size = [1300, 200]
        )
    while game.running:
        game.gameloop()
#<a href="https://www.flaticon.com/free-icons/athlete" title="athlete icons">Athlete icons created by Vitaly Gorbachev - Flaticon</a>

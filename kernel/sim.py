# python modules
import pygame
import os

# local modules
from .sim_elements import Player, ZoneDelimiter, START_ZONE_DELIMITER, END_ZONE_DELIMITER

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
class RaceGame:
    def __init__(self, **kwargs):
        self.screen_size = kwargs['screen_size']
        self.params = {
                'speed': 2,
                'angle_speed': 10,
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
                ZoneDelimiter(300, 100, START_ZONE_DELIMITER, self.screen),
                ZoneDelimiter(600, 100, END_ZONE_DELIMITER, self.screen),
                ]


    def gameloop(self):
        self.screen.fill((230, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_SPACE:
                    #aqui se hace el relevo
                    pass
            self.athlete.keystroke_movements(event)

        self.athlete.dynamics()
        self.draw_element(self.athlete)

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

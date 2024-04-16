import pygame
from pygame.locals import *
from asteroid import Asteroid
from galaxy import Galaxy
from utils import *

COLOR_DEPTH = 8
FPS = 60
NUMBER_ASTEROIDS = 7


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            flags=pygame.FULLSCREEN, depth=COLOR_DEPTH)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Asteróides, O jogo")
        self.clock = pygame.time.Clock()

    def run(self):
        self.galaxy = Galaxy(self.screen_rect)
        for i in range(NUMBER_ASTEROIDS):
            self.galaxy.add_entity(Asteroid(self.galaxy))
        done = False
        while not done:

            event_list = pygame.event.get()
            for event in event_list:
                if (event.type == KEYDOWN and event.key == K_q) or event.type == QUIT:
                    done = True

            time_passed = self.clock.tick(FPS)
            self.galaxy.update(time_passed, event_list)
            self.galaxy.render(self.screen)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Game().run()

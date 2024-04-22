import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

def nav_color(level):
    if level == 1:
        return GREEN



NEW_GAME = pygame.USEREVENT + 1
START_GAME = pygame.USEREVENT + 2
UNSHIELD_EVENT = pygame.USEREVENT + 3
COUNT_DOWN_EVENT = pygame.USEREVENT + 4

GAME_NOT_RUNNING: int = 1
GAME_RUNNING: int = 2

CLOCKWISE = 1
CCLOCKWISE = -1
FORWARD = 1
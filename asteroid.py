from wentity import WEntity
from random import random
from pygame.math import Vector2
from utils import *


WIDTH = 3
SCALE_FACTOR = 2
SPEED = 150.0
ANGULAR_SPEED = 90.0

ASTEROID_WIREFRAME = [
    Vector2(-20.0, 20.0), Vector2(-25.0, 5.0), Vector2(-25.0, -10.0),
    Vector2(-5.0, -10.0), Vector2(-10.0, -20.0), Vector2(5.0, -20.0),
    Vector2(20.0, -10.0), Vector2(20.0, -5.0), Vector2(0.0, 0.0),
    Vector2(20.0, 10.0), Vector2(10.0, 20.0), Vector2(0.0, 15.0)
]


class Asteroid(WEntity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "Asteroid", WHITE, ASTEROID_WIREFRAME, WIDTH)

        self.position = Vector2(random() * self.galaxy.rect.width, random() * self.galaxy.rect.height)

        self.velocity = Vector2(0.0, SPEED).rotate(random()*360)

        self.angular_speed = ANGULAR_SPEED
        self.rotating = CLOCKWISE

        self.size = SCALE_FACTOR

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

    def render(self, surface):
        super().render(surface)

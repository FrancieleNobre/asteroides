from sound import Sound
from wentity import WEntity
from random import random
from pygame.math import Vector2
from utils import *


WIDTH = 5
SCALE_FACTOR = 5
SPEED = 50.0
ANGULAR_SPEED = 60.0

COMET_WIREFRAME = [
    Vector2(0, -20),
    Vector2(10, -10),
    Vector2(20, -20),
    Vector2(30, -10),
    Vector2(20, 0),
    Vector2(30, 10),
    Vector2(10, 20),
    Vector2(0, 10),
    Vector2(-10, 20),
    Vector2(-30, 10),
    Vector2(-20, 0),
    Vector2(-30, -10),
    Vector2(-20, -20)
]


class Comet(WEntity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "comet", RED, COMET_WIREFRAME, WIDTH)

        self.position = Vector2(random() * self.galaxy.rect.width, random() * self.galaxy.rect.height)

        self.velocity = Vector2(
            0.0, SPEED * galaxy.get_entity_by_name("score").game_difficulty).rotate(random()*360)

        self.angular_speed = ANGULAR_SPEED
        self.rotating = CCLOCKWISE
        self.size = SCALE_FACTOR
        self.times_hit = 0
        self.exploding = False

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        for entity in self.galaxy.get_entities_by_name("blast"):
            if self.collide(entity):
                self.exploding = True
                self.times_hit += 50
                entity.dead = True

    def render(self, surface):
        super().render(surface)

        if self.exploding:
            Sound().play('bang')
            self.exploding = False

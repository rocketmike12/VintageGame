import pygame
from settings import *
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.x -= math.cos(self.angle) * player_speed
            self.y -= math.sin(self.angle) * player_speed

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.x += math.cos(self.angle) * player_speed
            self.y += math.sin(self.angle) * player_speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += 0.03

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= 0.03


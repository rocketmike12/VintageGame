import pygame
from settings import *
from map import world_map
import math


def raycast(surface, plr_pos, plr_angle):
    cur_angle = plr_angle - half_fov
    xo, yo = plr_pos
    for ray in range(num_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(max_depth):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            pygame.draw.line(surface, (0, 255, 0), plr_pos, (x, y), 2)
            if (x // tile * tile, y // tile * tile) in world_map:
                break
        cur_angle += delta_angle

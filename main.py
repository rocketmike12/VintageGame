import pygame
from settings import *
from player import Player
import math
from map import world_map
from raycasting import raycast

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Game')

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    screen.fill((0, 0, 0))

    raycast(screen, player.pos, player.angle)

    player.movement()
    pygame.draw.circle(screen, (0, 180, 0), player.pos, 12)
    pygame.draw.line(screen, (0, 255, 0), player.pos, (player.x + width * math.cos(player.angle),
                                                       player.y + width * math.sin(player.angle)))

    for x, y in world_map:
        pygame.draw.rect(screen, (180, 0, 180), (x, y, tile, tile), 2)

    pygame.display.flip()
    clock.tick(fps)

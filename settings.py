import math

width = 1200
height = 800
half_width = width / 2
half_height = height / 2
tile = 100
fps = 60

fov = math.pi / 3
half_fov = fov / 2
num_rays = 120
max_depth = 800
delta_angle = fov / num_rays

player_pos = (float(half_width), float(half_height))
player_angle = 0
player_speed = 2

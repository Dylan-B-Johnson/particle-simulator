import sys
import time
import pygame
import numpy as np
import actor as act

n = 150
screen_width, screen_hieght = 1440, 900
res = (screen_width, screen_hieght)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_hieght))
done = False
clock = pygame.time.Clock()
msElapsed = clock.tick(30)
positions = act.actor_positions(n, res)
actors = [act.Actor(screen, np.array(positions[i]), act.actor_directions(positions, res)[i], {'r': 10, 's': 10, 'm': 1},
                    res=res) for i in range(n)]
while not done:
    screen.fill((10, 10, 10))
    a = np.array([i.x for i in actors])
    d_actors = np.linalg.norm(a - a[:, None], axis=-1)
    for i in range(len(actors)):
        actors[i].calc_next(d_actors[i], actors)
        actors[i].update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

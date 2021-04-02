import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import numpy as np
import actor as act

act.h = 2
n = 100
screen_width, screen_height = 1920, 1080
res = (screen_width, screen_height)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
clock = pygame.time.Clock()
msElapsed = clock.tick(30)
positions = act.actor_positions(n, res)
actors = [
    act.Actor(screen, np.array(positions[i]), act.actor_directions(positions, res)[i], chars={'r': 10, 's': 1, 'm': 1},
              res=res) for i in range(n)]
while not done:
    screen.fill((10, 10, 10))
    for i in actors: i.update()
    a = np.array([i.x for i in actors])
    d_actors = np.linalg.norm(a - a[:, None], axis=-1)
    for i in range(len(Lactors)): actors[i].calc_next(d_actors[i], actors)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

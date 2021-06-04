"""
Copyright [2021] [Dylan Johnson]
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
	http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import numpy as np
import actor as act
import pygame
import random

# controls:
# w/s (while mousing over circle): increase/decrease circle radius
# a/d (while mousing over circle): decrease/increase circle speed
# up arrow/down arrow: increase/decrease all circle radii
# left arrow/right arrow: decrease/increase all circle speeds

act.h = 2
n = 200
screen_width, screen_height = 1920, 1080
res = (screen_width, screen_height)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
clock = pygame.time.Clock()
msElapsed = clock.tick(30)
positions = act.actor_positions(n, res)
rand = [random.random() * 5 for i in range(n)]
rand_s = [random.random() * 5 ** 0.5 for i in range(n)]
actors = [
    act.Actor(screen, np.array(positions[i]), act.actor_directions(positions, res)[i], s=1 + rand_s[i],
              chars={'r': 10 + rand[i] ** 0.5, 'm': 1 + rand[i]},
              res=res) for i in range(n)]
while not done:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        for i in actors: i.v *= 1.05
    if pressed[pygame.K_LEFT]:
        for i in actors: i.v /= 1.05
    if pressed[pygame.K_w]:
        for i in actors:
            if np.linalg.norm(i.x - np.array(pygame.mouse.get_pos())) < i.chars['r']:
                i.chars['m'] *= 1.05
                i.chars['r'] *= 1.05 ** 0.5
    if pressed[pygame.K_s]:
        for i in actors:
            if np.linalg.norm(i.x - np.array(pygame.mouse.get_pos())) < i.chars['r']:
                i.chars['m'] /= 1.05
                i.chars['r'] /= 1.05 ** 0.5
    if pressed[pygame.K_a]:
        for i in actors:
            if np.linalg.norm(i.x - np.array(pygame.mouse.get_pos())) < i.chars['r']:
                i.v /= 1.05
    if pressed[pygame.K_d]:
        for i in actors:
            if np.linalg.norm(i.x - np.array(pygame.mouse.get_pos())) < i.chars['r']:
                i.v *= 1.05
    if pressed[pygame.K_UP]:
        for i in actors:
            i.chars['m'] *= 1.05
            i.chars['r'] *= 1.05 ** 0.5
    if pressed[pygame.K_DOWN]:
        for i in actors:
            i.chars['m'] /= 1.05
            i.chars['r'] /= 1.05 ** 0.5
    screen.fill((10, 10, 10))
    for i in actors: i.update()
    a = np.array([i.x for i in actors])
    d_actors = np.linalg.norm(a - a[:, None], axis=-1)
    for i in range(len(actors)): actors[i].calc_next(d_actors[i], actors)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

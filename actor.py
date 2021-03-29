import pygame
import numpy as np
import random
import math as m


# generates initial positions around the screen clockwise
def actor_positions(n, res=(1920, 1080)):
    perimeter = 2 * res[0] + 2 * res[1]
    separation = perimeter / n
    pos = []
    for i in range(n):
        if i * separation < res[0]:
            pos.append((i * separation, 0))
        elif i * separation - res[0] < res[1]:
            pos.append((res[0], i * separation - res[0]))
        elif i * separation - res[0] - res[1] < res[0]:
            pos.append((i * separation - res[0] - res[1], res[1]))
        elif i * separation - 2 * res[0] - res[1] < res[0]:
            pos.append((0, i * separation - 2 * res[0] - res[1]))
    return pos


def actor_directions(positions, res=(1920, 1080)):
    d = []
    for i in positions:
        if i[1] == 0:
            theta = random.random() * m.pi
        if i[0] == res[0]:
            theta = random.random() * 1.5 * m.pi + m.pi * 0.5
        if i[1] == res[1]:
            theta = random.random() * m.pi * -1
        if i[0] == 0:
            theta = random.random() * 1.5 * m.pi + m.pi * 0.5 * -1
        d.append((m.cos(theta), m.sin(theta)))
    return d


class Actor:

    def __init__(self, screen, x, d, chars, res=(1920, 1080)):
        self.x = x
        self.res = res
        # random.random()
        self.d = np.array(d)
        self.chars = chars
        self.r = 14
        self.g = 242
        self.b = 208
        self.screen = screen
        pygame.draw.circle(self.screen, (self.r, self.g, self.b), (self.x[0], self.x[1]), self.chars['r'])

    def calc_next(self, d_actors, actors):
        i2=0
        for i in d_actors:
            if i == 0:
                pass
            elif i <= 20:
                x2 = actors[i2].x[0]
                y2 = actors[i2].x[1]
                x1 = self.x[0]
                y1 = self.x[1]
                p1x = self.d[0]
                p1y = self.d[1]
                self.d[1] = (y1 - y2 + p1y)
                self.d[0] = (x2 - x1 + p1x)
                self.d/=(self.d[0]**2+self.d[1]**2)**0.5
                # TODO this is messed up because the direction is being calculated with the already changed direction of the other particle
            i2+=1


            # TODO here in elif's we will program the conditions which decide where the balls will go
            # actors will be used for nearest actor characteristics
        if self.x[0] < 0:
            self.x[0] = 0
        if self.x[1] < 0:
            self.x[1] = 0
        if self.x[0] > self.res[0]:
            self.x[0] = self.res[0]
        if self.x[1] > self.res[1]:
            self.x[1] = self.res[1]
        if self.x[1] == 0:
            self.d[1] *= -1
        if self.x[0] == self.res[0]:
            self.d[0] *= -1
        if self.x[1] == self.res[1]:
            self.d[1] *= -1
        if self.x[0] == 0:
            self.d[0] *= -1

    def set_x(self, x):
        self.x = x

    def update(self):
        tmp = self.x + self.d * self.chars['s']
        self.x = tmp
        pygame.draw.circle(self.screen, (self.r, self.g, self.b), (tmp[0], tmp[1]), self.chars['r'])

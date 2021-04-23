from functions import *
import pygame
import math
pygame.font.init()
f = pygame.font.SysFont('palatinolinotype', 25)
s = pygame.font.SysFont('palatinolinotype', 15)


class Fib:
    def __init__(self, n, angle=0, pos=None):
        self.n = n
        self.angle = angle
        self.fib = fib(n)
        self.color = color(n)
        self.text = f.render(str(self.fib), False, (0, 0, 0))
        self.n_text = s.render(str(self.n), False, (0, 0, 0))
        if pos:
            self.pos = pos
        else:
            self.pos = (250 + round(math.cos(self.angle) * 200), round(250 + math.sin(self.angle) * 200))

        self.text_pos = self.pos[0] - self.text.get_width() // 2, self.pos[1] - self.text.get_height() // 2
        self.n_text_pos = self.pos[0] - self.n_text.get_width() // 2, self.pos[1] - self.n_text.get_height() // 2 + 15

    def draw(self, window):
        pygame.draw.circle(window, (0, 0, 0), self.pos, 27)
        pygame.draw.circle(window, self.color, self.pos, 25)
        window.blit(self.text, self.text_pos)
        window.blit(self.n_text, self.n_text_pos)



from fib import *
import random
from functions import *

go = pygame.font.SysFont('palatinolinotype', 45)
go_texts = [go.render('Fim de jogo', False, (255, 255, 255)),
            go.render('Novo Jogo [N]', False, (255, 255, 255)),
            go.render('Modo Zen [Z]', False, (255, 255, 255))]


class Game:
    def __init__(self, fibs=None):
        if fibs is None:
            fibs = []
        self.fibs = fibs
        self.standby = None
        self.lim = 16
        self.eg = False

    def draw_all(self, window):
        window.fill((0, 0, 0))
        self.standby.draw(window)
        self.rearrange()
        for fi in self.fibs:
            fi.draw(window)
        if self.eg:
            for n, t in enumerate(go_texts):
                window.blit(t, (100, 120 + 100 * n))

    def rearrange(self):
        for n, fi in enumerate(self.fibs):
            self.fibs[n] = Fib(fi.n, n / len(self.fibs) * 2 * math.pi)

    def gen(self):
        try:
            a = [x.n for x in self.fibs][4]
            self.standby = Fib(random.randint(min([x.n for x in self.fibs]) + 1, max([x.n for x in self.fibs]) // 2),
                               pos=(250, 250))
        except:
            self.standby = Fib(random.choice([0, 1]), pos=(250, 250))

    def add(self, ind):
        self.fibs.insert(ind, Fib(self.standby.n))
        self.standby = None

    def game_is_over(self):
        return len(self.fibs) > self.lim

    def end_game(self):
        a = sum([x.fib for x in self.fibs])
        self.fibs = []
        self.standby = Fib(reverse_fib(a) - 1, pos=(250, 250))
        self.eg = True

    def collapse(self):
        for n in range(len(self.fibs)):
            try:
                if self.fibs[n].n + 1 == self.fibs[n - 1].n or self.fibs[n].n - 1 == self.fibs[n - 1].n:
                    self.fibs[n] = Fib(max(self.fibs[n].n, self.fibs[n - 1].n) + 1)
                    self.fibs.pop(n - 1)
                    return True
            except IndexError:
                return False
from game import *
from fib import *
import time

win = pygame.display.set_mode((500, 500))

game = Game()
game.gen()

chain_counter = 0
while True:
    a = game.collapse()
    if a:
        chain_counter += 1
    else:
        chain_counter = 0

    if game.game_is_over():
        game.end_game()
    game.draw_all(win)
    if chain_counter > 1:
        time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if game.eg:
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_n]:
                    game = Game()
                    game.gen()
                if pressed[pygame.K_z]:
                    game.eg = False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                sorted_fibs = sorted(game.fibs, key=lambda x: distance_to_fib(pos, x))
                try:
                    a = game.fibs.index(sorted_fibs[0])
                    b = game.fibs.index(sorted_fibs[1])

                    if min(a, b) == 0 and max(a, b) != 1:
                        game.add(0)
                    else:
                        if a < b:
                            game.add(b)
                        else:
                            game.add(a)
                except IndexError:
                    game.add(0)
                game.gen()

    pygame.display.update()

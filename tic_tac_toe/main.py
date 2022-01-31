import sys
import pygame as pg
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import settings

from utils import game_opening, reset_game, user_click

# Initialize global variables
settings.init()

# Initializing pygame window
pg.init()
CLOCK = pg.time.Clock()
pg.display.set_caption("Tic Tac Toe")

# Loading images
opening_img = pg.image.load('./images/opening.png')
x_img = pg.image.load('./images/x.png')
o_img = pg.image.load('./images/o.png')

# Resizing images
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
opening = pg.transform.scale(opening_img, (settings.width, settings.height + 100))

game_opening(opening, settings)

# Run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # The user clicked place an X or O
            user_click(x_img, o_img, settings)
            print(settings.winner)
            if(settings.winner or settings.draw):
                reset_game(opening, settings)
    pg.display.update()
    CLOCK.tick(settings.fps)

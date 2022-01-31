import pygame as pg


def init():

    global XO, winner, draw, width, height, white, line_color, TTT, fps, screen
    XO = 'x'
    winner = None
    draw = False
    width = 400
    height = 400
    white = (255, 255, 255)
    line_color = (10, 10, 10)
    TTT = [[None] * 3, [None] * 3, [None] * 3]
    fps = 30
    screen = pg.display.set_mode((width, height+100), 0, 32)

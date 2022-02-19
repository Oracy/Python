import pygame as pg
import time


def draw_status(settings):
    if settings.winner is None:
        message = settings.XO.upper() + "'s Turn"
    else:
        message = settings.winner.upper() + " won!"
    if settings.draw:
        message = 'Game Draw!'
    
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # Copy the rendered message onto the board
    settings.screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center = (settings.width/2, 500-50))
    settings.screen.blit(text, text_rect)
    pg.display.update()


def game_opening(opening, settings):
    settings.screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(1)
    settings.screen.fill(settings.white)

    # Drawing vertical lines
    pg.draw.line(settings.screen, settings.line_color, (settings.width/3, 0), (settings.width/3, settings.height), 7)
    pg.draw.line(settings.screen, settings.line_color, (settings.width/3*2, 0), (settings.width/3*2, settings.height), 7)

    # Drawing horizontal lines
    pg.draw.line(settings.screen, settings.line_color, (0, settings.height/3), (settings.width, settings.height/3), 7)
    pg.draw.line(settings.screen, settings.line_color, (0, settings.height/3*2), (settings.width, settings.height/3*2), 7)

    draw_status(settings)


def check_win(settings):
    # Check for winning rows
    for row in range(0, 3):
        if ((settings.TTT[row][0] == settings.TTT[row][1] == settings.TTT[row][2]) and (settings.TTT[row][0] is not None)):
            # This row won
            settings.winner = settings.TTT[row][0]
            pg.draw.line(
                settings.screen,
                (255, 0, 0),
                (0, (row + 1) * settings.height/3-settings.height/6),
                (settings.width, (row + 1) * settings.height/3 - settings.height/6),
                4
            )

    # Check for winning columns
    for col in range(0, 3):
        if (settings.TTT[0][col] == settings.TTT[1][col] == settings.TTT[2][col]) and (settings.TTT[0][col] is not None):
            # This column won
            settings.winner = settings.TTT[0][col]
            # Draw winning line
            pg.draw.line(
                settings.screen,
                (255, 0, 0),
                ((col + 1) * settings.width/3 - settings.width/6, 0),
                ((col + 1) * settings.width/3 - settings.width/6, settings.height),
                4
            )
            break

    # Check for diagonal winners
    if (settings.TTT[0][0] == settings.TTT[1][1] == settings.TTT[2][2]) and (settings.TTT[0][0] is not None):
        # Game won diagonally left to right
        settings.winner = settings.TTT[0][0]
        pg.draw.line(
            settings.screen,
            (250, 70, 70),
            (50, 50),
            (350, 350),
            4
        )

    if (settings.TTT[0][2] == settings.TTT[1][1] == settings.TTT[2][0]) and (settings.TTT[0][2] is not None):
        #Game won diagonally right to left
        settings.winner = settings.TTT[0][2]
        pg.draw.line(
            settings.screen,
            (250, 70, 70),
            (350, 50),
            (50, 350),
            4
        )

    if(all([all(row) for row in settings.TTT]) and settings.winner is None):
        settings.draw = True
    draw_status(settings)


def draw_xo(row, col, x_img, o_img, settings):
    config_col = {
        "col_1": {
            "pos_y": 30
        },
        "col_2": {
            "pos_y": settings.height/3 + 30
        },
        "col_3": {
            "pos_y": settings.height/3*2 + 30
        }
    }

    config_row = {
        "row_1": {
            "pos_x": 30
        },
        "row_2": {
            "pos_x": settings.width/3 + 30
        },
        "row_3": {
            "pos_x": settings.width/3*2 + 30
        }
    }

    config_col_list = list(config_col)
    config_row_list = list(config_row)

    settings.TTT[row-1][col-1] = settings.XO
    if (settings.XO == 'x'):
        settings.screen.blit(x_img, (config_col[config_col_list[col-1]]['pos_y'], config_row[config_row_list[row-1]]['pos_x']))
        settings.XO = 'o'
    else:
        settings.screen.blit(o_img, (config_col[config_col_list[col-1]]['pos_y'], config_row[config_row_list[row-1]]['pos_x']))
        settings.XO = 'x'
    pg.display.update()


def user_click(x_img, o_img, settings):
    # Get coordinates of mouse click
    x, y = pg.mouse.get_pos()

    # Get column of mouse click (1-3)
    if (x < settings.width/3):
        col = 1
    elif (x < settings.width/3*2):
        col = 2
    elif (x < settings.width):
        col = 3
    else:
        col = None

    # Get row of mouse click (1-3)
    if (y < settings.height/3):
        row = 1
    elif (y < settings.height/3*2):
        row = 2
    elif (y < settings.height):
        row = 3
    else:
        row = None

    if row and col and settings.TTT[row-1][col-1] is None :
        settings.XO
        # Draw the x or o on screen
        draw_xo(row, col, x_img, o_img, settings)
        check_win(settings)


def reset_game(opening, settings):
    time.sleep(3)
    settings.XO = 'x'
    settings.draw = False
    game_opening(opening, settings)
    settings.winner = None
    settings.TTT = [[None] * 3, [None] * 3, [None] * 3]

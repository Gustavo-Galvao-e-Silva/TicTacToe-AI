import pygame as pg
from Engine import GameEngine

window_dimensions = 300
board_spaces = 3
space_size = window_dimensions // board_spaces
max_fps = 15
image_dictionary = {"Board": pg.transform.scale(pg.image.load("tictactoe_board.png"), (window_dimensions, window_dimensions)),
                    "x": pg.transform.scale(pg.image.load("tictactoe_x.png"), (space_size, space_size)),
                    "o": pg.transform.scale(pg.image.load("tictactoe_o.png"), (space_size, space_size))}


def main():
    pg.init()
    screen = pg.display.set_mode((window_dimensions, window_dimensions))
    screen.fill((pg.Color("white")))
    running = True
    gs = GameEngine()
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.MOUSEBUTTONDOWN:
                mouse_position = pg.mouse.get_pos()
                column = mouse_position[0] // space_size
                row = mouse_position[1] // space_size
                gs.move(row, column)
        pg.display.flip()
        draw_game_state(screen, gs.game_state)
        if gs.check_winner(gs.game_state)[0]:
            print(f"The winner is: {gs.check_winner(gs.game_state)[1]}!")
            running = False


def draw_game_state(screen, board):
    screen.blit(image_dictionary["Board"], pg.Rect(0, 0, window_dimensions, window_dimensions))
    for i in range(board_spaces):
        for j in range(board_spaces):
            drawing = board[i][j]
            if drawing != '-':
                screen.blit(image_dictionary[drawing], pg.Rect(j * space_size, i * space_size, space_size, space_size))


if __name__ == '__main__':
    main()

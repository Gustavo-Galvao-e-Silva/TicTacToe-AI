from Engine import GameEngine

gs = GameEngine()


def main():
    while not gs.check_winner(gs.game_state)[0]:
        print(gs)
        row = int(input(f"In what row would you like to place {"x" if gs.x_turn else "o"}? (0-2) "))
        column = int(input(f"And which column?(0-2) "))
        if gs.game_state[row][column] != "-":
            print("Invalid move. Enter an empty space.")
            continue
        gs.move(row, column)
    else:
        print(gs)
        print(f"The winner is: {gs.check_winner(gs.game_state)[1]}!")


if __name__ == '__main__':
    main()
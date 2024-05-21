from Engine import GameEngine

gs = GameEngine()


def main():
    play_against_ai = input("Would you like to play against the AI?(Y or N) ")
    if play_against_ai == 'N':
        while not gs.game_finished(gs.game_state)[0]:
            print(gs)
            row = int(input(f"In what row would you like to place {"x" if gs.x_turn else "o"}? (0-2) "))
            column = int(input(f"And which column?(0-2) "))
            if gs.game_state[row][column] != "-":
                print("Invalid move. Enter an empty space.")
                continue
            gs.move(row, column)
        else:
            print(gs)

    elif play_against_ai == 'Y':
        while not gs.game_finished(gs.game_state)[0]:
            if gs.x_turn:
                print(gs)
                row = int(input(f"In what row would you like to place the x? (0-2) "))
                column = int(input(f"And which column?(0-2) "))
                if gs.game_state[row][column] != "-":
                    print("Invalid move. Enter an empty space.")
                    continue
                gs.move(row, column)
            else:
                gs.best_move(gs.game_state)
        else:
            print(gs)


if __name__ == '__main__':
    main()

class GameEngine:
    def __init__(self):
        self.game_state = [["-", "-", "-"],
                           ["-", "-", "-"],
                           ["-", "-", "-"]]
        self.x_turn = True

    def move(self, row, column):
        if self.x_turn and self.game_state[row][column] == '-':
            self.game_state[row][column] = 'x'
            self.x_turn = False
        elif not self.x_turn and self.game_state[row][column] == '-':
            self.game_state[row][column] = 'o'
            self.x_turn = True

    def check_winner(self, board):
        lines = [[board[0][0], board[1][1], board[2][2]], [board[2][0], board[1][1], board[0][2]],
                 board[0], board[1], board[2], [board[0][0], board[1][0], board[2][0]],
                 [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]]]
        for ele in ["x", "o"]:
            for line in lines:
                if line == [ele, ele, ele]:
                    return [True, ele]
        return [False, None]

    def __str__(self):
        return f'{self.game_state[0]}\n{self.game_state[1]}\n{self.game_state[2]}'

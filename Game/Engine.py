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

    def game_finished(self, board):
        lines = [[board[0][0], board[1][1], board[2][2]], [board[2][0], board[1][1], board[0][2]],
                 board[0], board[1], board[2], [board[0][0], board[1][0], board[2][0]],
                 [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]]]
        for ele in ["x", "o"]:
            for line in lines:
                if line == [ele, ele, ele]:
                    return [True, ele]
        if sum([x.count('-') for x in board]) == 0:
            return [True, 'no one']
        return [False, None]

    def __str__(self):
        return f'{self.game_state[0]}\n{self.game_state[1]}\n{self.game_state[2]}'

    def minimax_ai(self, board, depth, is_maximizing):
        if self.game_finished(self.game_state)[0] and self.game_finished(self.game_state)[1] == 'o':
            return float('inf')
        elif self.game_finished(self.game_state)[0] and self.game_finished(self.game_state)[1] == 'x':
            return float('-inf')
        elif sum([x.count('-') for x in board]) == 0:
            return 0

        if is_maximizing:
            best_score = -1000

            for row in range(3):
                for col in range(3):
                    if board[row][col] == '-':
                        board[row][col] = 'o'
                        score = self.minimax_ai(board, depth + 1, False)
                        board[row][col] = '-'
                        best_score = max(best_score, score)
            return best_score

        else:
            best_score = 1000

            for row in range(3):
                for col in range(3):
                    if board[row][col] == '-':
                        board[row][col] = 'x'
                        score = self.minimax_ai(board, depth + 1, True)
                        board[row][col] = '-'
                        best_score = min(best_score, score)
            return best_score

    def best_move(self, board):
        best_score = -1000
        best_move = (3, 3)

        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = 'o'
                    score = self.minimax_ai(board, 0, False)
                    board[row][col] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move != (3, 3):
            self.move(best_move[0], best_move[1])

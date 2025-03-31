import copy
from src.pyAISearch.pyAISearchProblem.pyProblem import AISearchProblem

class MinMaxState:
    def _init_(self, max_pos=1, min_pos=5, player="Max"):
        self.max_pos = max_pos
        self.min_pos = min_pos
        self.player = player
        self.depth = 0

    def move_player(self, new_pos):
        new_state = MinMaxState(self.max_pos, self.min_pos, self.player)
        new_state.depth = self.depth + 1
        if self.player == "Max":
            new_state.max_pos = new_pos
        else:
            new_state.min_pos = new_pos
        new_state.change_player()
        return new_state

    def change_player(self):
        self.player = "Min" if self.player == "Max" else "Max"

    def is_terminal(self):
        return self.max_pos == 5 or self.min_pos == 1

    def utility(self):
        if self.max_pos == 5:
            return float('inf')
        if self.min_pos == 1:
            return float('-inf')
        d_max = abs(5 - self.max_pos)
        d_min = abs(1 - self.min_pos)
        return d_min - d_max

    def get_possible_moves(self):
        moves = []
        current_pos = self.max_pos if self.player == "Max" else self.min_pos
        opponent_pos = self.min_pos if self.player == "Max" else self.max_pos

        for delta in [-1, 1]:
            new_pos = current_pos + delta
            if 1 <= new_pos <= 5:
                if new_pos != opponent_pos:
                    moves.append(new_pos)
                else:
                    jump_pos = new_pos + delta
                    if 1 <= jump_pos <= 5 and jump_pos != current_pos:
                        moves.append(jump_pos)
        return moves

    def _str_(self):
        board = ["-"] * 5
        board[self.max_pos - 1] = "A"
        board[self.min_pos - 1] = "B"
        return f"Board: {''.join(board)} | Player: {self.player} | Depth: {self.depth}"

class MinMaxProblem:
    def _init_(self):
            self.current_state = MinMaxState(max_pos=1, min_pos=5, player="Max")

    def expand(self, state):
            successors = []
            possible_moves = state.get_possible_moves()
            for new_pos in possible_moves:
                new_state = state.move_player(new_pos)
                successors.append(new_state)
            return successors


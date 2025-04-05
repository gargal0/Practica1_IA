import copy

class ExpectiMaxState(object):
    def __init__(self, startPlayer="A", possible_moves_count=None):
        # Board: 5 positions, A starts at 1, B starts at 5
        self.board = ["A", " ", " ", " ", "B"]  # Ajustado al estado inicial de la salida
        self.player = startPlayer  # "A" or "B"
        self.depth = 0
        self.possible_moves_count = possible_moves_count

    def setPiece(self, pos, player):
        self.board[pos] = player

    def movePlayer(self, newPos):
        newState = copy.deepcopy(self)
        currentPos = newState.board.index(self.player)
        newState.board[currentPos] = " "
        newState.setPiece(newPos, self.player)
        newState.incDepth()
        newState.changePlayer()
        newState.possible_moves_count = len(self.getPossibleMoves())
        return newState

    def changePlayer(self):
        self.player = "B" if self.player == "A" else "A"

    def incDepth(self):
        self.depth += 1

    def isFree(self, pos):
        if 0 <= pos < len(self.board):
            return self.board[pos] == " "
        return False

    def getPossibleMoves(self):
        pos = self.board.index(self.player)
        moves = []
        direction = 1 if self.player == "A" else -1

        nextPos = pos + direction
        if self.isFree(nextPos):
            moves.append(nextPos)
        elif 0 <= nextPos < len(self.board) and self.board[nextPos] != " ":
            jumpPos = nextPos + direction
            if self.isFree(jumpPos):
                moves.append(jumpPos)

        return moves

    def isTerminal(self):
        if self.board[4] == "A" or self.board[0] == "B":
            return True
        if not self.getPossibleMoves():
            return True
        return False

    def utility(self):
        if self.board[4] == "A":  # A wins
            return 1000
        if self.board[0] == "B":  # B wins
            return -1000
        posA = self.board.index("A")
        posB = self.board.index("B")
        d_max = 4 - posA
        d_min = posB
        return d_min - d_max

    def getProbability(self):
        if self.possible_moves_count is None or self.possible_moves_count == 0:
            return 1.0
        return 1.0 / self.possible_moves_count

    def __str__(self):
        return " ".join(self.board) + f" | Player: {self.player} | Depth: {self.depth}"
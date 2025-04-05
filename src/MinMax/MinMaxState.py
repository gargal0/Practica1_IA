import copy

class MinMaxState(object):
    def __init__(self, startPlayer="A"):
        # Board: 5 positions, A starts at 1, B starts at 5
        self.board = ["A", " ", " ", " ", "B"]
        self.player = startPlayer  # "A" or "B"
        self.depth = 0

    def setPiece(self, pos, player):
        self.board[pos] = player

    def movePlayer(self, newPos):
        # Create a new state for the move
        newState = copy.deepcopy(self)
        currentPos = newState.board.index(self.player)
        newState.board[currentPos] = " "  # Clear current position
        newState.setPiece(newPos, self.player)  # Move to new position
        newState.incDepth()
        newState.changePlayer()
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
        direction = 1 if self.player == "A" else -1  # A moves right, B moves left

        # Check adjacent position
        nextPos = pos + direction
        if self.isFree(nextPos):
            moves.append(nextPos)
        # Check jump over if adjacent is occupied
        elif 0 <= nextPos < len(self.board) and self.board[nextPos] != " ":
            jumpPos = nextPos + direction
            if self.isFree(jumpPos):
                moves.append(jumpPos)

        return moves

    def isTerminal(self):
        # A wins if at position 5, B wins if at position 1
        if self.board[4] == "A" or self.board[0] == "B":
            return True
        # If the current player has no moves, the game ends
        if not self.getPossibleMoves():
            return True
        return False

    def utility(self):
        if self.board[4] == "A":  # A wins
            return float('inf')
        if self.board[0] == "B":  # B wins
            return float('-inf')
        # If no moves are available, evaluate based on current positions
        posA = self.board.index("A")
        posB = self.board.index("B")
        d_max = 4 - posA  # Distance of A to position 5 (index 4)
        d_min = posB  # Distance of B to position 1 (index 0)
        return d_min - d_max

    def __str__(self):
        return " ".join(self.board) + f" | Player: {self.player} | Depth: {self.depth}"


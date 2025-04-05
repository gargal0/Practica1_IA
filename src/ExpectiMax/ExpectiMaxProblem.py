from ExpectiMaxState import ExpectiMaxState
from src.pyAISearch.pyAISearchProblem.pyProblem import AISearchProblem


class ExpectiMaxProblem(AISearchProblem):
    def __init__(self, startPlayer="A"):
        super().__init__()
        self.currentState = ExpectiMaxState(startPlayer)

    def expand(self, state):
        successors = []
        for pos in state.getPossibleMoves():
            newState = state.movePlayer(pos)
            successors.append(newState)
        return successors
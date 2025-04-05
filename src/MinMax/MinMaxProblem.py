from MinMaxState import MinMaxState
from src.pyAISearch.pyAISearchProblem.pyProblem import AISearchProblem


class MinMaxProblem(AISearchProblem):
    def __init__(self, startPlayer="A"):
        super().__init__()
        self.currentState = MinMaxState(startPlayer)

    def expand(self, state):
        successors = []
        for pos in state.getPossibleMoves():
            newState = state.movePlayer(pos)
            successors.append(newState)
        return successors
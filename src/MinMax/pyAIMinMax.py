"""
Created on 25 Feb 2021
@author: Francisco Dominguez
"""
from src.pyAISearch.pyAISearchSolver import AISearchSolver

class AIMinMax(AISearchSolver):
    def __init__(self, problem):
        super().__init__(problem)

    def maxValue(self, state):
        if state.depth >= 6 or state.isTerminal():  # Cortar en profundidad 6
            return state.utility()

        maxUpToNow = float('-inf')
        successors = self.problem.expand(state)
        for s in successors:
            maxUpToNow = max(maxUpToNow, self.minValue(s))
        return maxUpToNow

    def minValue(self, state):
        if state.depth >= 6 or state.isTerminal():  # Cortar en profundidad 6
            return state.utility()

        minUpToNow = float('inf')
        successors = self.problem.expand(state)
        for s in successors:
            minUpToNow = min(minUpToNow, self.maxValue(s))
        return minUpToNow
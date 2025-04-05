'''
Created on 25 Feb 2021

@author: Francisco Dominguez
'''
from src.pyAISearch.pyAISearchSolver import AISearchSolver

class AIExpectiMax(AISearchSolver):
    def __init__(self, problem):
        super().__init__(problem)

    def maxValue(self, state):
        if state.depth >= 6 or state.isTerminal():  # Cortar en profundidad 6
            return state.utility()

        maxUpToNow = float('-inf')  # Inicializar localmente
        successors = self.problem.expand(state)
        for s in successors:
            maxUpToNow = max(maxUpToNow, self.expectiValue(s))
        return maxUpToNow

    def expectiValue(self, state):
        if state.depth >= 6 or state.isTerminal():  # Cortar en profundidad 6
            return state.utility()

        successors = self.problem.expand(state)
        if not successors:
            return state.utility()

        expectation = 0
        for s in successors:
            p = s.getProbability()
            expectation += p * self.maxValue(s)
        return expectation
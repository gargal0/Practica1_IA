'''
Created on 25 Feb 2021

@author: Francisco Dominguez
'''
from pyAISearchSolver import AISearchSolver

class AIExpectiMax(AISearchSolver):
    def __init__(self, problem):
        super(AISearchSolver).__init__(problem)
        self.maxUpToNow=-10e100
    def maxValue(self,state):
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        for s in succesors:
            self.maxUpToNow=max(self.maxUpToNow,self.expectiValue(s))
        return self.maxUpToNow
    def expectiValue(self,state):
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        expectation=0
        for s in succesors:
            p=s.getProbability()
            expectation+=p*self.maxValue(s)
        return expectation
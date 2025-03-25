'''
Created on 25 Feb 2021

@author: Francisco Dominguez
'''
from pyAISearchSolver import AISearchSolver

class AIMinMaxAlphaBeta(AISearchSolver):
    def __init__(self, problem):
        super(AISearchSolver).__init__(problem)
    def maxValue(self,state,alpha,beta):
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        for s in succesors:
            alpha=max(alpha,self.minValue(s,alpha,beta))
            if alpha>beta:
                return alpha;
        return alpha
    def minValue(self,state,alpha,beta):
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        for s in succesors:
            beta=min(beta,self.maxValue(s,alpha,beta))
            if beta<alpha:
                return beta
        return beta
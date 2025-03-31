from src.pyAISearch.pyAISearchSolver import AISearchSolver


class AIMinMax(AISearchSolver):
    def __init__(self, problem):
        super().__init__(problem)

    def maxValue(self,state):
        maxUpToNow=-10e100
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        for s in succesors:
            maxUpToNow=max(maxUpToNow,self.minValue(s))
        return maxUpToNow
    def minValue(self,state):
        minUpToNow= 10e100
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        for s in succesors:
            minUpToNow=min(minUpToNow,self.maxValue(s))
        return minUpToNow

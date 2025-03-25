'''
Created on 21 Feb 2021

@author: Francisco Dominguez
'''
from pyAISearchSolver import AISearchSolver
from pyAISearchCollections.pyAISearchCollection import AISearchCollection
from pyAISearchNode import AISearchNode

class AISearchSolverGraph(AISearchSolver):
    def __init__(self, problem):
        super().__init__(problem)
        self.frontier=AISearchCollection()
        self.explored=[]
        self.currentNode=None
    def getCurrentNode(self): return self.currentNode
    def expandIfNotIn(self,currentNode):
        currentState=currentNode.getState()
        for action,state,cost in self.problem.sucessors(currentState):        
            node=AISearchNode()
            node.setState(state)
            node.setFather(currentNode)
            node.setAction(action)
            node.setCostPath(currentNode.getCostPath()+cost)
            node.setDepth(currentNode.getDepth()+1)
            if self.frontier.contains(node) or node in self.explored:
                continue
            self.frontier.insert(node)
    def getInitNode(self):
        state=self.problem.getStateInit()
        node=AISearchNode(state)
        return node
    def search(self):
        self.frontier.insert(self.getInitNode())
        while not self.frontier.isEmpty():
            self.currentNode=self.frontier.selectNode()
            currentState=self.currentNode.getState()
            if self.problem.isGoal(currentState):
                return True
            self.explored.append(self.currentNode)
            self.expandIfNotIn(self.currentNode)
        return False

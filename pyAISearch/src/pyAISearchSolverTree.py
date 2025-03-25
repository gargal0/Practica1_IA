'''
Created on 15 Feb 2021

@author: Francisco Dominguez
'''
from pyAISearchSolver import AISearchSolver
from pyAISearchCollections.pyAISearchCollection import AISearchCollection
from pyAISearchNode import AISearchNode

class AISearchSolverTree(AISearchSolver):
    def __init__(self, problem):
        super(AISearchSolver).__init__(problem)
        self.frontier=AISearchCollection()
        self.currentNode=None
    def expand(self,currentNode):
        currentState=currentNode.getState()
        for action,state,cost in self.problem.sucessors(currentState):
            node=AISearchNode()
            node.setState(state)
            node.setFather(currentNode)
            node.setAction(action)
            node.setCostPath(currentNode.getCostPath()+cost)
            node.setDepth(currentNode.getDepth()+1)
            self.frontier.insert(node)
    def getInitNode(self):
        state=self.problem.getStateInit()
        node=AISearchNode(state)
        return node
    def search(self):
        self.frontier.insert(self.getInitNode())
        while self.frontier.isEmpty():
            self.currentNode=self.frontier.selectNode()
            currentState=self.currentNode.getState()
            if self.problem.isGoal(currentState):
                return True
            self.expand(self.currentNode)
        return False
    
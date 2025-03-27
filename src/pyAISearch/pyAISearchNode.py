'''
Created on 14 Feb 2021

@author: Francisco Dominguez
'''
class AISearchNode(object):
    def __init__(self,state=None,father=None,action=None,cost=1):
        self.state=state
        self.father=father
        self.action=action
        self.costPath=0
        self.depth=0
        if father!=None: 
            self.costPath=father.getCostPath()+cost
            self.depth=father.getDepth()+1
    def setState(self,s):    self.state=s
    def setFather(self,f):   self.father=f
    def setAction(self,a):   self.action=a
    def setCostPath(self,c): self.costPath=c
    def setDepth(self,d):    self.depth=d
    def getState(self):    return self.state
    def getFather(self):   return self.father
    def getAction(self):   return self.action
    def getCostPath(self): return self.costPath
    def getDepth(self):    return self.depth
    ''' return f=g+h (cost path + heuristic) '''
    def getF(self):
        return self.getCostPath()+self.getState().getH()
    ''' By default two nodes are equal if theirs states are equals '''
    def __eq__(self,n):
        return self.getState()==n.getState()
    def __lt__(self,n):
        return self.getF()<n.getF()

    def __str__(self):
        """
        Devuelve una representación del nodo con su estado, la acción realizada,
        el valor de f*, g y h.
        """
        return (f"Estado: \n {self.state}\n"
                f"Acción: {self.action}\n"
                f"f*: {self.getF()}\n"
                f"g (coste acumulado): {self.getCostPath()}\n")


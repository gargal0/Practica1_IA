'''
Created on 7 Mar 2021

@author: Francisco Dominguez
'''
import math
import copy
import numpy as np
from pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearchProblem.pyState import AISearchState

class PathPlanningState(AISearchState):
    def __init__(self):
        self.map=np.array([
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,1,1,1,0,0,0],
            [0,0,1,0,0,0,1,0,0,0],
            [0,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,1,0,0,0],
            [0,0,0,1,1,1,1,0,0,0]
            ]) 
        self.location=(0,0)
    def setLocation(self,l): self.location=l
    def getLocation(self): return self.location
    def getLocationX(self): return self.location[0]
    def getLocationY(self): return self.location[1]
    def notWall(self,p):
        v=self.map[p[1],p[0]]
        return v==0;
    def __str__(self):
        s=" 0123456789\n"
        for row in range(self.map.shape[0]):
            s+=str(row)
            for col in range(self.map.shape[1]):
                if (col,row)==self.location:
                    s+="@"
                    continue
                if self.map[row,col]==0:
                    s+=" "
                if self.map[row,col]==1:
                    s+="#"
            s+="\n"
        return s
    ''' return heuristic '''
    def getH(self):
        l=self.getLocation()
        return math.sqrt((l[0]-9)**2+(l[1]-9)**2)
    ''' compare two states 
        in this case two states are equal if their location is the same '''
    def __eq__(self,s):
        return self.getLocation()==s.getLocation()
        
class PathPlanning(AISearchProblem):
    '''
    Find a path from origin to target location
    '''
    def __init__(self):
        self.state=PathPlanningState()
        self.origin=(0,0)
        self.target=(9,9)
        self.state.setLocation(self.origin)
        self.actions=["U","D","L","R"]
    def getStateInit(self):
        return self.state
    def canTakeAction(self,a,state):
        if a=="U":
            if state.getLocationY()==0:
                return False
            newLocation=(state.getLocationX(),state.getLocationY()-1)
            if state.notWall(newLocation):
                return True
        if a=="D":
            if state.getLocationY()==state.map.shape[0]-1:
                return False
            newLocation=(state.getLocationX(),state.getLocationY()+1)
            if state.notWall(newLocation):
                return True
        if a=="L":
            if state.getLocationX()==0:
                return False
            newLocation=(state.getLocationX()-1,state.getLocationY())
            if state.notWall(newLocation):
                return True
        if a=="R":
            if state.getLocationX()==state.map.shape[1]-1:
                return False
            newLocation=(state.getLocationX()+1,state.getLocationY())
            if state.notWall(newLocation):
                return True
        return False
    def takeAction(self,a,state):
        if a=="U":
            if state.getLocationY()==0:
                return False
            newLocation=(state.getLocationX(),state.getLocationY()-1)
            if state.notWall(newLocation):
                newState=copy.deepcopy(state)
                newState.setLocation(newLocation)
                return newState
        if a=="D":
            if state.getLocationY()==state.map.shape[0]:
                return False
            newLocation=(state.getLocationX(),state.getLocationY()+1)
            if state.notWall(newLocation):
                newState=copy.deepcopy(state)
                newState.setLocation(newLocation)
                return newState
        if a=="L":
            if state.getLocationX()==0:
                return False
            newLocation=(state.getLocationX()-1,state.getLocationY())
            if state.notWall(newLocation):
                newState=copy.deepcopy(state)
                newState.setLocation(newLocation)
                return newState
        if a=="R":
            if state.getLocationX()==state.map.shape[1]:
                return False
            newLocation=(state.getLocationX()+1,state.getLocationY())
            if state.notWall(newLocation):
                newState=copy.deepcopy(state)
                newState.setLocation(newLocation)
                return newState
        raise RuntimeError("I can't take action in takeAction()")
    #return a collection of action,state,cost
    def sucessors(self,state):
        sucessors=[]
        for a in self.actions:
            if self.canTakeAction(a,state):
                newState=self.takeAction(a,state)
                sucessors.append((a,newState,1))
        return sucessors
    def isGoal(self,state):
        return state.getLocation()==self.target
  
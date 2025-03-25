'''
Created on 9 Apr 2021

@author: Francisco Dominguez
'''
import copy
from pyAISearchProblem.pyProblem import AISearchProblem
class AITicTocState(object):
    def __init__(self,startPlayer="X"):
        self.board=[[" "," "," "],
                    [" "," "," "],
                    [" "," "," "]]
        self.depth=0
        self.player=startPlayer #can be "O"
    def setPiece(self,loc,c):
        self.board[loc[0]][loc[1]]=c
    def setPlayer(self,loc):
        self.setPiece(loc,self.player)
    def movePlayer(self,pos):
        newState=copy.deepcopy(self)
        newState.setPlayer(pos)
        newState.incDepth()
        newState.changePlayer()
        return newState
    def winColum(self,col,c):
        if self.board[0][col]==c and self.board[1][col]==c and self.board[2][col]==c :
            return True         
        return False
    def winColums(self,c):
        for col in range(3):
            if self.winColum(col,c): return True
        return False
    def winRow(self,row,c):
        if self.board[row][0]==c and self.board[row][1]==c and self.board[row][2]==c :
            return True         
        return False
    def winRows(self,c):
        for row in range(3):
            if self.winRow(row,c): return True
        return False
    def winDiags(self,c):
        if self.board[0][0]==c and self.board[1][1]==c and self.board[2][2]==c :
            return True         
        if self.board[2][0]==c and self.board[1][1]==c and self.board[0][2]==c :
            return True         
        return False
    def win(self,c):
        return self.winColums(c) or self.winRows(c) or self.winDiags(c)
    def count(self,c):
        counter=0
        for row in range(3):
            for col in range(3):
                if self.board[row][col]==c:
                    counter+=1
        return counter
    def isFree(self,loc):
        return self.board[loc[0]][loc[1]]==" "
    def freeLocations(self):
        holes=[]
        for row in range(3):
            for col in range(3):
                if self.isFree((row,col)):
                    holes.append((row,col))
        return holes
    def boardFull(self):
        return self.freeLocations()==[]
    def changePlayer(self):
        if self.player=="X": 
            self.player="O"
            return
        self.player="X"
    def incDepth(self):
        self.depth+=1
    def isTerminal(self):
        return self.win("X") or self.win("O") or self.boardFull()
    def utility(self):
        if self.win("X"): return  100
        if self.win("O"): return -100
        if self.boardFull(): return 0
    def __str__(self):
        s=""
        for row in range(3):
            for col in range(3):
                s+=self.board[row][col]
            s+="\n"
        s+=str(self.depth)+"---"+self.player
        return s
class AITicTocProblem(AISearchProblem):
    def __init__(self, startPlayer="X"):
        self.currentState=AITicTocState(startPlayer)
    def expand(self,state):
        successors=[]
        for pos in state.freeLocations():
            newState=state.movePlayer(pos)
            successors.append(newState)
        return successors
        
'''
Created on 9 Apr 2021

@author: Francisco Dominguez
'''
from pyAITicTocProblem import AITicTocProblem,AITicTocState
from pyAIMinMax import AIMinMax
def chooseMaxLocation(mm,state):
    maxV=-1000
    for pos in state.freeLocations():
        newState=state.movePlayer(pos)
        v=mm.minValue(newState)
        if v>maxV:
            maxV=v
            maxP=pos
    return maxP,v   
def play(mm):
    s=AITicTocState("O")
    while not s.isTerminal():
        print(s)
        r=int(input("row="))
        c=int(input("col="))
        while not s.isFree((r,c)):
            r=int(input("row="))
            c=int(input("col="))
        s.setPlayer((r,c))
        s.changePlayer()
        if s.isTerminal(): break
        print(s)
        pos,v=chooseMaxLocation(mm, s)
        s.setPlayer(pos)
        s.changePlayer()
    print(s)
    if s.win("X"):
        print("X wins")
    if s.win("O"):
        print("O wins")
    if not s.win("X") and not s.win("O"):
        print("Draw")
if __name__ == '__main__':
    p=AITicTocProblem()
    mm=AIMinMax(p)
    play(mm)

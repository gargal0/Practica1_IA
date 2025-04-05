from ExpectiMaxProblem import ExpectiMaxProblem
from pyAIExpectiMax import AIExpectiMax

def chooseBestMove(em, state, isMax):
    possibleMoves = state.getPossibleMoves()
    print(f"Possible moves for {state.player}: {possibleMoves}")

    if not possibleMoves:
        return None, float('-inf') if isMax else float('inf')

    if isMax:
        # Para A (max), maximizamos
        bestValue = float('-inf')
        bestMove = None
        for pos in possibleMoves:
            newState = state.movePlayer(pos)
            value = em.maxValue(newState)
            print(f"Evaluating move to {pos}: value = {value}")
            if value > bestValue:
                bestValue = value
                bestMove = pos
        return bestMove, bestValue
    else:
        # Para B (expectativa), calculamos el valor esperado de cada movimiento
        # y elegimos el primero (o podríamos usar una política diferente)
        values = []
        for pos in possibleMoves:
            newState = state.movePlayer(pos)
            value = em.expectiValue(newState)
            print(f"Evaluating move to {pos}: value = {value}")
            values.append((pos, value))
        # Elegimos el primer movimiento (podríamos usar otra estrategia)
        bestMove, bestValue = values[0]
        return bestMove, bestValue

def play():
    problem = ExpectiMaxProblem(startPlayer="A")
    em = AIExpectiMax(problem)
    state = problem.currentState

    print("Initial State:")
    print(state)

    while not state.isTerminal():
        isMax = (state.player == "A")
        possibleMoves = state.getPossibleMoves()
        if not possibleMoves:
            break
        pos, value = chooseBestMove(em, state, isMax)
        state = state.movePlayer(pos)
        print("\nAfter move:")
        print(state)
        move_value = state.utility()
        print(f"Move value (e(s)): {move_value}")

    print("\nGame Over!")
    if state.board[4] == "A":
        print("Player A (Max) wins!")
    elif state.board[0] == "B":
        print("Player B (Min) wins!")
    else:
        if state.player == "A":
            print("Player A (Max) has no moves. Player B (Min) wins!")
        else:
            print("Player B (Min) has no moves. Player A (Max) wins!")

if __name__ == "__main__":
    play()
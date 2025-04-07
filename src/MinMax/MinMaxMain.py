from MinMaxProblem import MinMaxProblem
from pyAIMinMax import AIMinMax

def chooseBestMove(mm, state, isMax):
    bestValue = float('-inf') if isMax else float('inf')
    bestMove = None
    possibleMoves = state.getPossibleMoves()
    print(f"Possible moves for {state.player}: {possibleMoves}")  # Debugging

    if not possibleMoves:
        return None, bestValue  # No moves available

    for pos in possibleMoves:
        newState = state.movePlayer(pos)
        value = mm.minValue(newState) if isMax else mm.maxValue(newState)
        if isMax and value > bestValue:
            bestValue = value
            bestMove = pos
        elif not isMax and value < bestValue:
            bestValue = value
            bestMove = pos

    if bestMove is None:
        # If no better move was found, pick the first possible move
        bestMove = possibleMoves[0]
        newState = state.movePlayer(bestMove)
        bestValue = mm.minValue(newState) if isMax else mm.maxValue(newState)
        print(f"No better move found, defaulting to {bestMove} with value {bestValue}")  # Debugging

    return bestMove, bestValue

def play():
    problem = MinMaxProblem(startPlayer="A")  # A (max) starts
    mm = AIMinMax(problem)
    state = problem.currentState

    print("Initial State:")
    print(state)

    while not state.isTerminal():
        isMax = (state.player == "A")  # A is max
        possibleMoves = state.getPossibleMoves()
        if not possibleMoves:
            break  # No moves available, game should end (handled by isTerminal)
        pos, _ = chooseBestMove(mm, state, isMax)  # Ignoramos el valor devuelto por MinMax
        state = state.movePlayer(pos)
        print("\nAfter move:")
        print(state)
        # Calculamos e(s) del nuevo estado para imprimirlo como "move value"
        move_value = state.utility()
        print(f"Move value (e(s)): {move_value}")

    print("\nGame Over!")
    if state.board[4] == "A":
        print("Player A (Max) wins!")
    elif state.board[0] == "B":
        print("Player B (Min) wins!")
    else:
        # If neither reached the goal, the player who couldn't move loses
        if state.player == "A":
            print("Player A (Max) has no moves. Player B (Min) wins!")
        else:
            print("Player B (Min) has no moves. Player A (Max) wins!")

if __name__ == "__main__":
    play()
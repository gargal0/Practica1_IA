from src.BlockState import BlockState
from src.pyAISearch.pyAISearchProblem.pyProblem import AISearchProblem


class BlockProblem(AISearchProblem):
    def __init__(self, init: BlockState, goal: BlockState):
        self.stateInit = init
        self.goal = goal

    def getStateInit(self):
        return self.stateInit

    def successors(self, state): #TODO
        """
        Genera los sucesores de un estado, moviendo bloques entre pilas.
        """
        succ = []
        for i, stack in enumerate(state.stacks):
            if stack:  # Si la pila no está vacía
                top = stack[-1]  # Bloque superior de la pila
                for j in range(1, len(state.stacks)):  # Evitamos mover bloques dentro de la misma pila
                    if i == j: continue
                    new_state = BlockState([list(s) for s in state.stacks])  # Copia del estado
                    new_state.moveBlock(i, j)  # Mueve el bloque de la pila i a la pila j
                    action = f"Move {top} from {i}→{j}"
                    succ.append((action, new_state, 1))  # Coste de la acción es 1
        return succ

    def isGoal(self, state):
        """
        Verifica si el estado actual es el objetivo.
        """
        return state == self.goal

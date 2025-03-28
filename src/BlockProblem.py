from src.BlockState import BlockState
from src.pyAISearch.pyAISearchProblem.pyProblem import AISearchProblem


class BlockProblem(AISearchProblem):
    def __init__(self, init: BlockState, goal: BlockState):
        self.stateInit = init
        self.goal = goal

    def getStateInit(self):
        return self.stateInit

    def successors(self, state):
        """
        Genera los sucesores de un estado, moviendo bloques entre pilas.
        Ahora se consideran todos los movimientos posibles entre pilas,
        excepto mover un bloque a la misma pila de origen.
        """
        succ = []
        for i, stack in enumerate(state.stacks):
            if stack:  # Solo se consideran pilas que no estén vacías
                top = stack[-1]  # Bloque superior de la pila
                for j in range(len(state.stacks)):  # Considera todas las pilas (0 a n-1)
                    if i == j:  # Evita mover el bloque a la misma pila
                        continue
                    new_state = BlockState([list(s) for s in state.stacks])  # Crea una copia del estado actual
                    new_state.moveBlock(i, j)  # Mueve el bloque de la pila i a la pila j
                    action = f"Move {top} from {i}→{j}"
                    succ.append((action, new_state, 1))  # Añade el sucesor con coste 1
        return succ

    def isGoal(self, state):
        """
        Verifica si el estado actual es el objetivo.
        """
        return state == self.goal

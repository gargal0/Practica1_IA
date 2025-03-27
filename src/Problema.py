from pyAISearch.src.pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearch.src.pyAISearchProblem.pyState import AISearchState
from pyAISearch.src.pyAISearchSolver import AISearchSolver
from pyAISearch.src.pyAISearchCollections.pyAISearchCollection import AISearchCollection
from  pyAISearch.src.pyAISearchNode import AISearchNode

class BlockState(AISearchState):
    def __init__(self, state):
        self.state = state  # Estado representado por tuplas de bloques
        self.goal = ('A', 'B', 'C')  # Definir el estado objetivo (por ejemplo)

    def getH(self):
        # Heurística: número de bloques descolocados
        return sum(1 for i, block in enumerate(self.state) if block != self.goal[i])

    def __eq__(self, other):
        return self.state == other.state

class BlockProblem(AISearchProblem):
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def getStateInit(self):
        return BlockState(self.initial_state)

    def successors(self, state):
        successors = []
        for i in range(len(state) - 1):
            if state[i] != state[i + 1]:
                # Mover cubo de la parte superior
                new_state = list(state)
                new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                successors.append((tuple(new_state), f'Mover {state[i]} arriba', 1))
        return successors

    def isGoal(self, state):
        return state == ('A', 'B', 'C')  # Estado objetivo

class AISearchSolverTree(AISearchSolver):
    def __init__(self, problem):
        super(AISearchSolver).__init__(problem)
        self.frontier = AISearchCollection()
        self.explored = []

    def expand(self, currentNode):
        currentState = currentNode.getState()
        for action, state, cost in self.problem.successors(currentState):
            node = AISearchNode()
            node.setState(state)
            node.setFather(currentNode)
            node.setAction(action)
            node.setCostPath(currentNode.getCostPath() + cost)
            node.setDepth(currentNode.getDepth() + 1)
            self.frontier.insert(node)

    def getInitNode(self):
        state = self.problem.getStateInit()
        node = AISearchNode(state)
        return node

    def search(self):
        self.frontier.insert(self.getInitNode())
        while not self.frontier.isEmpty():
            self.currentNode = self.frontier.selectNode()
            currentState = self.currentNode.getState()
            if self.problem.isGoal(currentState):
                return True
            self.explored.append(self.currentNode)
            self.expand(self.currentNode)
        return False

# Inicializamos el problema con un estado de ejemplo
initial_state = ('C', 'A', 'B')  # Ejemplo de estado inicial
problem = BlockProblem(initial_state)
solver = AISearchSolverTree(problem)

# Realizamos la búsqueda
solver.search()

# Imprimir el árbol de decisiones
node = solver.currentNode
while node:
    print(f"Estado: {node.getState()} | Acción: {node.getAction()}")
    node = node.getFather()
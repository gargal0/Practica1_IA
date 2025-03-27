from pyAISearch.src.pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearch.src.pyAISearchProblem.pyState import AISearchState
from pyAISearch.src.pyAISearchSolver import AISearchSolver
from pyAISearch.src.pyAISearchCollections.pyAISearchCollection import AISearchCollection
from pyAISearch.src.pyAISearchNode import AISearchNode

class BlockState(AISearchState):
    def __init__(self, stacks):
        # stacks es un iterable de tuplas, p.ej: (('A',), ('C', 'B'), ())
        self.stacks = tuple(tuple(s) for s in stacks)

    def getH(self):
        # Heurística: número de bloques descolocados
        goal_order = tuple(sorted(sum(self.stacks, ())))
        count = 0
        for stack in self.stacks:
            for i, block in enumerate(stack):
                if i > 0 and stack[i - 1] != block:
                    count += 1
                if i == 0 and block != goal_order[0]:
                    count += 1
        return count

    def __eq__(self, other):
        return isinstance(other, BlockState) and self.stacks == other.stacks

class BlockProblem(AISearchProblem):
    def __init__(self, init: BlockState, goal: BlockState):
        self.stateInit = init
        self.goal = goal

    def getStateInit(self):
        return self.stateInit

    def successors(self, state):
        succ = []
        for i, stack in enumerate(state.stacks):
            if not stack:
                continue
            top = stack[-1]
            for j in range(len(state.stacks)):
                if i == j:
                    continue
                new_stacks = [list(s) for s in state.stacks]
                new_stacks[j].append(new_stacks[i].pop())
                new_state = BlockState(new_stacks)
                action = f"Move {top} from {i}→{j}"
                succ.append((action, new_state, 1))
        return succ

    def isGoal(self, state):
        return state == self.goal

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
init = BlockState((('A',), ('C', 'B'), ()))
goal = BlockState(((), ('C',), ('B', 'A')))
problem = BlockProblem(init, goal)
solver = AISearchSolverTree(problem)

# Realizamos la búsqueda
solver.search()

# Imprimir el árbol de decisiones
node = solver.currentNode
while node:
    print(f"Estado: {node.getState()} | Acción: {node.getAction()}")
    node = node.getFather()
#que paso primiko
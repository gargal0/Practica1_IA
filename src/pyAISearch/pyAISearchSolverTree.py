from src.pyAISearch.pyAISearchNode import AISearchNode
from src.pyAISearch.pyAISearchSolver import AISearchSolver
from src.pyAISearch.pyAISearchCollections.pyAISearchCollection import AISearchCollection

class AISearchSolverTree(AISearchSolver):
    def __init__(self, problem):
        super(AISearchSolverTree, self).__init__(problem)
        self.frontier = AISearchCollection()
        self.explored = set()  # Conjunto de nodos explorados
        self.currentNode = None

    def expand(self, currentNode):
        """
        Expande el nodo actual generando sus sucesores
        y asegurándonos de que no se repitan nodos ya explorados.
        """
        currentState = currentNode.getState()
        for action, state, cost in self.problem.successors(currentState):
            node = AISearchNode()
            node.setState(state)
            node.setFather(currentNode)
            node.setAction(action)
            node.setCostPath(currentNode.getCostPath() + cost)
            node.setDepth(currentNode.getDepth() + 1)

            # Asegurarse de que el estado no haya sido explorado anteriormente
            if state not in self.explored:
                self.frontier.insert(node)
                self.explored.add(state)  # Marcamos el estado como explorado

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
            self.expand(self.currentNode)
        return False

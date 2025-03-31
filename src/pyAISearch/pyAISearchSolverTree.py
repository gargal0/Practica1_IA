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
            print(node)

            # Asegurarse de que el estado no haya sido explorado anteriormente
            if state not in self.explored:
                self.frontier.insert(node)
                self.explored.add(state)  # Marcamos el estado como explorado

    def getInitNode(self):
        state = self.problem.getStateInit()
        node = AISearchNode(state)
        return node

    def search(self): #TODO mal print
        self.frontier.insert(self.getInitNode())
        seen_nodes = list()  # Para almacenar los nodos visitados
        i = 1
        while not self.frontier.isEmpty():
            print("######################\tSTEP " + str(i) + "\t###############################\n")
            self.currentNode = self.frontier.selectNode()
            currentState = self.currentNode.getState()
            seen_nodes.append(self.currentNode)
            print("------------ Current node -----------\n")
            print(self.currentNode) #Esto imprime todos los nodos posibles
            if self.problem.isGoal(currentState):
                print("\n--------------------------------------------------------------\n")
                return True
            print("\n------------ Sucessors -----------\n")
            self.expand(self.currentNode)
            i += 1
            print("\n--------------------------------------------------------------\n")

        return False



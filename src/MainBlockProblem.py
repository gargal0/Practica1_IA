from src.pyAISearch.pyAISearchSolverTree import AISearchSolverTree
from src.BlockProblem import BlockProblem
from src.BlockState import BlockState

if __name__ == "__main__":
    # Estado inicial y objetivo usando tuplas de tuplas
    init = BlockState([('B', 'C', 'A'), (), ()])
    goal = BlockState([('A','B','C'), (), ()])

    # Definir el problema
    problem = BlockProblem(init, goal)

    # Resolver el problema con A* usando un solver de árbol
    solver = AISearchSolverTree(problem)

    print("Comenzando la búsqueda...\n")

    # Buscar solución y mostrar el proceso
    solution = solver.search()

    # Si se encuentra una solución, muestra el resultado
    if solution:
        print("\nSolución encontrada!")
    else:
        print("\nNo se encontró solución.")

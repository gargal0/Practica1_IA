from src.pyAISearch.pyAISearchSolverTree import AISearchSolverTree
from src.BlockProblem import BlockProblem
from src.BlockState import BlockState
import random

def generate_random_initial_state():
    # Lista de bloques
    blocks = ['A', 'B', 'C']
    # Generamos una permutación aleatoria de los bloques
    random.shuffle(blocks)

    # Decidimos aleatoriamente cómo apilar los bloques
    stacks = [[], [], []]  # Tres pilas vacías

    # Distribuimos los bloques en las pilas
    for block in blocks:
        # Elegimos una pila aleatoria que sea válida
        # Una pila es válida si el bloque puede apilarse (no hay restricciones en este caso)
        while True:
            stack_idx = random.randint(0, 2)  # Elegimos una pila (0, 1, o 2)
            # El bloque puede apilarse en la pila (no hay restricciones de "clear" aquí)
            stacks[stack_idx].append(block)
            break

    # Convertimos las pilas a tuplas y las ordenamos "al revés"
    # En el formato de BlockState, el primer elemento de la tupla es el bloque en la mesa
    formatted_stacks = []
    for stack in stacks:
        if stack:
            # Invertimos la pila para que el primer elemento sea el que está en la mesa
            stack.reverse()
            formatted_stacks.append(tuple(stack))
        else:
            formatted_stacks.append(())

    return BlockState(formatted_stacks)

if __name__ == "__main__":
    # Estado inicial y objetivo usando tuplas de tuplas
    init = generate_random_initial_state()
    goal = BlockState([('C','B','A'), (), ()])

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

from pyAIMinMax import AIMinMax
from pyAITicTocProblem import MinMaxProblem



def choose_max_location(mm, state):
    max_v = float('-inf')
    best_pos = None
    for new_state in mm.problem.expand(state):
        v = mm.minValue(new_state)
        if v > max_v:
            max_v = v
            best_pos = new_state.max_pos
    return best_pos, max_v


def choose_min_location(mm, state):
    min_v = float('inf')
    best_pos = None
    for new_state in mm.problem.expand(state):
        v = mm.maxValue(new_state)
        if v < min_v:
            min_v = v
            best_pos = new_state.min_pos
    return best_pos, min_v


def play(mm):
    state = mm.problem.current_state
    print("¡Simulación del juego MinMax con dos IAs!")
    print("Max (ficha A) comienza en la posición 1 y quiere llegar a 5.")
    print("Min (ficha B) comienza en la posición 5 y quiere llegar a 1.")
    print("En cada turno, un jugador mueve su ficha a un espacio adyacente vacío.")
    print("Si el espacio adyacente está ocupado, puede saltar sobre el oponente si el siguiente espacio está libre.\n")

    while not state.is_terminal():
        print(state)
        if state.player == "Max":
            print("Turno de Max (IA):")
            pos, v = choose_max_location(mm, state)
            state = state.move_player(pos)
            print(f"Max mueve a la posición {pos} (valor: {v})")
        else:
            print("Turno de Min (IA):")
            pos, v = choose_min_location(mm, state)
            state = state.move_player(pos)
            print(f"Min mueve a la posición {pos} (valor: {v})")

    print(state)
    if state.max_pos == 5:
        print("¡Max gana! Llegó a la posición 5.")
    elif state.min_pos == 1:
        print("¡Min gana! Llegó a la posición 1.")


def show_possible_actions(mm, max_depth=6):
    state = mm.problem.current_state
    print("Explorando acciones posibles hasta profundidad 6:")

    def explore(state, depth=0):
        if depth > max_depth or state.is_terminal():
            return
        print(f"\nProfundidad {depth}: {state}")
        successors = mm.problem.expand(state)
        for s in successors:
            v = mm.minValue(s) if s.player == "Min" else mm.maxValue(s)
            print(f"  Movimiento: {s}, Valor: {v}")
            explore(s, depth + 1)

    explore(state)


if __name__ == "_main_":
    problem = MinMaxProblem()
    mm = AIMinMax(problem)
    show_possible_actions(mm)
    print("\n--- Comenzando el juego ---\n")
    play(mm)
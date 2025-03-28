from src.pyAISearch.pyAISearchProblem.pyState import AISearchState


class BlockState(AISearchState):
    def __init__(self, stacks, params=None):
        super().__init__(params)
        # Convertimos las pilas a tuplas de tuplas para mantener la inmutabilidad
        self.stacks = tuple(tuple(stack) for stack in stacks)

    def getH(self): # TODO
        """
        Calcula la heurística: el número de bloques fuera de lugar.
        """
        current_blocks = tuple(sum([list(stack) for stack in self.stacks], []))
        goal_order = tuple(sorted(current_blocks))  # El orden correcto de los bloques

        count = 0
        for current, goal in zip(current_blocks, goal_order):
            if current != goal:
                count += 1
        return count

    def moveBlock(self, from_stack, to_stack):
        """
        Mueve el bloque de la cima de la pila `from_stack` a la pila `to_stack`.
        """
        # Convertimos las pilas a listas para modificarlas
        new_stacks = [list(stack) for stack in self.stacks]

        # Extraer el bloque de la pila `from_stack` (de la cima)
        block = new_stacks[from_stack].pop()

        # Agregar el bloque a la pila `to_stack` (a la cima)
        new_stacks[to_stack].append(block)

        # Convertir las pilas de nuevo a tuplas (porque las pilas deben ser inmutables)
        self.stacks = tuple(tuple(stack) for stack in new_stacks)

    def __hash__(self):
        """
        Devuelve el valor hash del estado (basado en las pilas de bloques).
        """
        return hash(self.stacks)

    def __eq__(self, other):
        """
        Compara dos objetos `BlockState` basándose en el estado de las pilas.
        """
        if isinstance(other, BlockState):
            return self.stacks == other.stacks
        return False

    def __str__(self): # TODO
        """
        Representación visual del estado usando las pilas.
        """
        lines = []
        max_height = max(len(stack) for stack in self.stacks)
        for level in range(max_height - 1, -1, -1):
            row = []
            for stack in self.stacks:
                row.append(stack[level] if level < len(stack) else ' ')
            lines.append(' '.join(row))
        return '\n'.join(lines)

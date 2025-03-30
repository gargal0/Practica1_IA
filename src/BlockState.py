from src.pyAISearch.pyAISearchProblem.pyState import AISearchState


class BlockState(AISearchState):
    def __init__(self, stacks, params=None):
        super().__init__(params)
        # Convertimos las pilas a tuplas de tuplas para mantener la inmutabilidad
        self.stacks = tuple(tuple(stack) for stack in stacks)

    def getH(self):
        """
        Heurística: número de bloques fuera de lugar (no tiene bloque correcto debajo).
        """
        misplaced = 0
        block_below = {}
        block_on_table = None

        for stack in self.stacks:
            if not stack:
                continue
            block_on_table = stack[0]
            for i in range(len(stack) - 1):
                block = stack[i + 1]
                below = stack[i]
                block_below[block] = below

        if block_on_table != 'C':
            misplaced += 1
        if block_below.get('B') != 'C':
            misplaced += 1
        if block_below.get('A') != 'B':
            misplaced += 1

        return misplaced

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
        return hash(tuple(sorted(self.stacks)))

    def __eq__(self, other):
        """
        Compara dos objetos `BlockState` basándose en el estado de las pilas.
        """
        if isinstance(other, BlockState):
            return tuple(sorted(self.stacks)) == tuple(sorted(other.stacks))
        return False

    def __str__(self):
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

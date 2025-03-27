import math
import copy
import numpy as np
from collections import deque
from pyAISearch.src.pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearch.src.pyAISearchProblem.pyState import AISearchState

class BlockState(AISearchState):
    def __init__(self, stacks):
        self.stacks = [deque(stack) for stack in stacks]

    def getH(self):
        # Aplanar las pilas actuales
        current_blocks = tuple(sum([list(stack) for stack in self.stacks], []))

        # Aplanar el estado objetivo (goal)
        goal_blocks = tuple(sorted(sum([list(stack) for stack in self.stacks], [])))

        # Contar los bloques fuera de lugar
        count = 0
        for current, goal in zip(current_blocks, goal_blocks):
            if current != goal:
                count += 1
        return count

    def __eq__(self, other):
        return isinstance(other, BlockState) and all(self.stacks[i] == other.stacks[i] for i in range(len(self.stacks)))

    def __hash__(self):
        return hash(tuple(tuple(stack) for stack in self.stacks))


    def moveBlock(self, fromst, to):
        if self.stacks[fromst]:
            block = self.stacks[fromst].pop()
            self.stacks[to].append(block)

    def __str__(self):
        lines = []
        max_height = max(len(stack) for stack in self.stacks)
        for level in range(max_height - 1, -1, -1):
            row = []
            for stack in self.stacks:
                row.append(stack[level] if level < len(stack) else ' ')
            lines.append(' '.join(row))
        return '\n'.join(lines)
import math
import copy
import numpy as np
from collections import deque
from pyAISearch.src.pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearch.src.pyAISearchProblem.pyState import AISearchState

class BlockState(AISearchState):
    def __init__(self, stack):
        self.block = [deque(stack) for stack in stack]
from typing import Generator

from aima.search import Problem
from operadors import Operador
from estat import Estat


class ProblemaBICING(Problem):
    def __init__(self, initial_state: Estat, use_entropy: bool = False):
        self.use_entropy = use_entropy
        super().__init__(initial_state)

    def actions(self, state: Estat) -> Generator[Operador, None, None]:
        return state.genera_accions()

    def result(self, state: Estat, action: Operador) -> Estat:
        return state.aplica_operador(action)

    def value(self, state: Estat) -> float:
        if self.use_entropy:
            return -state.h()
        else:
            return -state.h()

    def goal_test(self, state: Estat) -> bool:
        return False
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
        #print(action)
        '''try:
            furgo = state.ruta[action.num_furgo]
        except:
            furgo = state.ruta[action.num_furgo1]
        try:
            if furgo.descarrega1 == 0 and furgo.descarrega2 > 0:
                print(f'ERROR: {furgo.descarrega1} i {furgo.descarrega2}')
        except:
            pass'''
        return state.aplica_operador(action)

    def value(self, state: Estat) -> float:
        return state.h()


    def goal_test(self, state: Estat) -> bool:
        return False
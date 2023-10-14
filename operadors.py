from abia_bicing import Estacion, Estaciones
from furgonetes import Furgonetes


class Operador():
    pass

class Modificar_estacio_carrega(Operador):
    def __init__(self, furgoneta: Furgonetes, est1: Estacion, est2:Estacion):
        self.furgo = furgoneta
        self.est1 = est1
        self.est2 = est2
    def __repr__(self):
        return f"La furgo {self.furgo} ja no carregarà a {self.est1} sinó a {self.est2}"
        
class Carrega_mes_bicicletes(Operador):
    def __init__(self, furgoneta: Furgonetes, bicicletes: int):
        self.furgo = furgoneta
        self.estacio_carrega = self.furgo.estacio_carrega
        self.bicicletes = bicicletes
    def __repr__(self):
        return f"La furgo {self.furgo} modifica la seva càrrega en {self.bicicletes} bicicletes a l'estació {self.estacio_carrega}"

class Modificar_sentit_ruta(Operador):
    def __init__(self, furgoneta: Furgonetes):
        self.furgo = furgoneta
        self.estacio_descarrega1 = self.furgo.estacio_descarrega1
        self.estacio_descarrega2 = self.furgo.estacio_descarrega2
    def __repr__(self):
        return f"La furgo {self.furgo} modificarà el sentit de la ruta, anirà de {self.estacio_descarrega2} a {self.estacio_descarrega1}"


class Eliminar_estacio_descarrega(Operador):
    def __init__(self, furgoneta: Furgonetes):
        self.furgo = furgoneta
        if self.furgo.estacio_descarrega2 is not None:
            self.estacio = self.furgo.estacio_descarrega2
        else:
            self.estacio = self.furgo.estacio_descarrega1
    def __repr__(self):
        return f"La furgo {self.furgo} ja no descarrega a l'estació {self.estacio}"
    
class Descarrega_mes_bicicletes(Operador):
    def __init__(self, furgoneta: Furgonetes, estacio: Estacion,bicicletes: int):
        self.furgo = furgoneta
        self.estacio_descarrega = estacio
        self.bicicletes = bicicletes
    def __repr__(self):
        return f"La furgo {self.furgo} modifica la seva descarrega en {self.bicicletes} bicicletes a l'estació {self.estacio_descarrega}"
    
class Descarrega_en_nova_estacio(Operador):
    def __init__(self, furgoneta: Furgonetes, estacio: Estacion):
        self.furgo = furgoneta
        self.estacio_descarrega = estacio
    def __repr__(self):
        return f"La furgo {self.furgo} afegeix l'estació {self.estacio_descarrega} a la seva ruta de descàrrega"
from abia_bicing import Estacion, Estaciones
from furgonetes import Furgonetes


class Operador():
    pass

class Carrega_en_nova_estacio(Operador): #Perjudica
    def __init__(self, num_furgo: int, est_nova:Estacion):
        self.num_furgo = num_furgo
        self.est_nova = est_nova
    def __repr__(self):
        return f"La furgo {self.num_furgo} modifica l'estació de càrrega a {self.est_nova.coordX}, {self.est_nova.coordY}"
    
class Intercanviar_estacions(Operador): #Dins de la classe ESTAT
    def __init__(self, num_furgo1: int, num_furgo2: int, est_intercanvi1: int, est_intercanvi2: int):
        self.num_furgo1 = num_furgo1
        self.num_furgo2 = num_furgo2
        self.est_intercanvi1 = est_intercanvi1
        self.est_intercanvi2 = est_intercanvi2
    def __repr__(self):
        return f"Les furgonetes {self.num_furgo1} i {self.num_furgo2} s'intercanvien una estació"
        
'''class Carrega_mes_bicicletes(Operador): #Dins de la classe ESTAT
    def __init__(self, num_furgo: int):
        self.num_furgo = num_furgo
        #self.num_bicicletes = 5
    def __repr__(self):
        return f"La furgo {self.num_furgo} carregarà més bicicletes a l'estació de càrrega"'''

class Carrega_menys_bicicletes(Operador): #Dins de la classe ESTAT
    def __init__(self, num_furgo: int):
        self.num_furgo = num_furgo
    def __repr__(self):
        return f"La furgo {self.num_furgo} carregarà menys bicicletes a l'estació de càrrega"

class Modificar_sentit_ruta(Operador): #Dins de la classe ESTAT
    def __init__(self, num_furgo: int):
        self.num_furgo = num_furgo
    def __repr__(self):
        return f"La furgo {self.num_furgo} modificarà el sentit de la ruta de descàrrega"


class Eliminar_estacio_descarrega(Operador): #Dins de la classe ESTAT
    def __init__(self, num_furgo: int, estacio_eliminada:int):
        self.num_furgo = num_furgo
        self.estacio_eliminada = estacio_eliminada
    def __repr__(self):
        return f"La furgo {self.num_furgo} elimina l'estació de descàrrega {self.estacio_eliminada}"
    
class Descarrega_mes_bicicletes(Operador):
    def __init__(self, num_furgo: int, estacio_descarrega: int):
        self.num_furgo = num_furgo
        self.estacio_descarrega = estacio_descarrega
        self.bicicletes = 1
    def __repr__(self):
        return f"La furgo {self.num_furgo} descarregarà més bicicletes a l'estació de descàrrega {self.estacio_descarrega}"
    
    
class Descarrega_menys_bicicletes(Operador):
    def __init__(self, num_furgo: int, estacio_descarrega: int):
        self.num_furgo = num_furgo
        self.estacio_descarrega = estacio_descarrega
        self.bicicletes = -1
    def __repr__(self):
        return f"La furgo {self.num_furgo} descarregarà menys bicicletes a l'estació de descàrrega {self.estacio_descarrega}"
    
class Descarrega_en_nova_estacio(Operador): #Dins de la classe ESTAT
    def __init__(self, num_furgo: int, estacio: Estacion):
        self.num_furgo = num_furgo
        self.estacio_descarrega = estacio
    def __repr__(self):
        return f"La furgo {self.num_furgo} afegeix l'estació {self.estacio_descarrega.coordX}, {self.estacio_descarrega.coordY} a la seva ruta de descàrrega"

class Intercanviar_bicicletes(Operador): #No aporta cap benefici
    def __init__(self, num_furgo : int, est: int):
        self.num_furgo = num_furgo
        self.est = est
    def __repr__(self):
        return f"La furgo {self.num_furgo} modifica la descàrrega en les seves estacions"
    
    
'''Proposta del chat:
    
Los operadores propuestos hasta ahora son:

1. Carrega_en_nova_estacio: Esta operación carga bicicletas en una nueva estación. Perjudica porque reduce la cantidad de bicicletas en la estación de origen y aumenta la cantidad en la estación de destino.

2. Descarrega_en_estacio1: Esta operación descarga bicicletas en la estación 1. Beneficia porque aumenta la cantidad de bicicletas en la estación de destino y reduce la cantidad en la furgoneta.

3. Descarrega_en_estacio2: Esta operación descarga bicicletas en la estación 2. Beneficia porque aumenta la cantidad de bicicletas en la estación de destino y reduce la cantidad en la furgoneta.

4. Intercanvi_entre_estacions: Esta operación intercambia bicicletas entre dos estaciones. Beneficia porque aumenta la cantidad de bicicletas en una estación y reduce la cantidad en la otra.

5. Intercanvi_entre_furgonetes: Esta operación intercambia bicicletas entre dos furgonetas. Beneficia porque aumenta la cantidad de bicicletas en una furgoneta y reduce la cantidad en la otra.

Es importante tener en cuenta que cada operador debe respetar las restricciones del problema, como la capacidad máxima de las furgonetas y el número máximo de estaciones que pueden visitar. Además, se pueden proponer otros operadores según las necesidades específicas del problema.
'''
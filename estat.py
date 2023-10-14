from abia_bicing import Estacion, Estaciones
from typing import List, Set, Generator
from parametres import Parametres
from furgonetes import Furgonetes
from operadors import *

        
class Estat(object):
    """
    Classe que representa un estat
    """
    def __init__(self, parametres: Parametres,  ruta: List[Furgonetes], estacions: Estaciones, estacions_de_carrega: set):
        self.params = parametres
        self.ruta =  ruta
        self.estacions = estacions
        self.estacions_de_carrega = estacions_de_carrega
        
    def copia(self):
        return Estat(self.params, self.ruta.copy(), self.estacions, self.estacions_de_carrega.copy())
    def genera_accions(self) -> Generator[Operador, None, None]:
        for furgo in self.ruta:
            for est_nova in self.estacions.lista_estaciones:
                if est_nova not in self.estacions_de_carrega:
                    yield Modificar_estacio_carrega(furgo, est_nova)
                yield Descarrega_en_nova_estacio(furgo, est_nova)
            if furgo.estacio_descarrega1 is not None and furgo.estacio_descarrega2 is not None:
                yield Modificar_sentit_ruta(furgo)
            if furgo.estacio_descarrega1 is not None:
                yield Eliminar_estacio_descarrega(furgo)
            yield Carrega_mes_bicicletes(furgo)
            yield Carrega_menys_bicicletes(furgo)
            if furgo.estacio_descarrega1 is not None:
                yield Descarrega_mes_bicicletes(furgo, furgo.estacio_descarrega1)
            if furgo.estacio_descarrega2 is not None:
                yield Descarrega_mes_bicicletes(furgo, furgo.estacio_descarrega2)
    
    def genera_accions(self) -> Generator[Operador, None, None]:
        quant_furgos = self.params.n_furgonetes
        for num_furgo in quant_furgos:
            for est_nova in self.estacions.lista_estaciones:
                if est_nova not in self.estacions_de_carrega:
                    yield Modificar_estacio_carrega(num_furgo, est_nova)
                yield Descarrega_en_nova_estacio(num_furgo, est_nova)
                
            if self.ruta[num_furgo].estacio_descarrega1 is not None:
                yield Eliminar_estacio_descarrega(num_furgo)
                if self.ruta[num_furgo].estacio_descarrega2 is not None:
                    yield Modificar_sentit_ruta(num_furgo)
                
            yield Carrega_mes_bicicletes(num_furgo)
            yield Carrega_menys_bicicletes(num_furgo)
            if self.ruta[num_furgo].estacio_descarrega1 is not None:
                yield Descarrega_mes_bicicletes(self.ruta[num_furgo], self.ruta[num_furgo].estacio_descarrega1)
            if self.ruta[num_furgo].estacio_descarrega2 is not None:
                yield Descarrega_mes_bicicletes(self.ruta[num_furgo], self.ruta[num_furgo].estacio_descarrega2)


    def aplica_operador(self, operador: Operador):
        nou_estat = copia(self)
        if isinstance(operador, Modificar_estacio_carrega):
            nou_estat.ruta[operador.num_furgo].estacio_carrega = operador.est_nova
         
        elif isinstance(operador, Carrega_mes_bicicletes):
            nou_estat.ruta[operador.num_furgo].carrega += operador.num_bicicletes
           
        elif isinstance(operador, Carrega_menys_bicicletes):
            nou_estat.ruta[operador.num_furgo].carrega -= operador.num_bicicletes
        
        elif isinstance(operador, Modificar_sentit_ruta):
            furgo = nou_estat.ruta[operador.num_furgo]
            furgo.estacio_descarrega1, furgo.estacio_descarrega2 = furgo.estacio_descarrega2, furgo.estacio_descarrega1
        
        elif isinstance(operador, Eliminar_estacio_descarrega):
            est_descarrega1 = nou_estat.ruta[operador.num_furgo].estacio_descarrega1
            est_descarrega2 = nou_estat.ruta[operador.num_furgo].estacio_descarrega2
            if est_descarrega2 is not None:
                est_descarrega2.estacio_carrega = None
                est_descarrega2.descarrega2 = 0
            elif est_descarrega1 is not None:
                est_descarrega1.estacio_carrega = None
                est_descarrega2.descarrega1 = 0
            
         
        
        elif isinstance(operador, Descarrega_mes_bicicletes):
            pass
        elif isinstance(operador, Descarrega_en_nova_estacio):
            pass
        else:
            pass
        
    def h(self):
        return sum(furgo.cost_gasolina() for furgo in self.ruta)
    
    
    def __repr__(self):
        return f"Ruta: {self.ruta}"
        #return f"Parametres: n_estacions={self.params.n_estacions}, n_bicis={self.params.n_bicis}, llavor={self.params.llavor}, n_furgonetes={self.params.n_furgonetes}"   
    
    #Per implementar ruta com a Set
    '''def __eq__(self, other):
        if isinstance(other, Estat):
            return (self.params == other.params and
                    self.ruta == other.ruta and
                    self.estacions == other.estacions and
                    self.estacions_de_carrega == other.estacions_de_carrega)
        return False

    def __hash__(self):
        return hash((self.params, tuple(self.ruta), self.estacions, frozenset(self.estacions_de_carrega)))'''

def genera_estat_inicial(params: Parametres, estacions: Estaciones) -> Estat:
    iterador_est = iterar_estacions(estacions)
    ruta = []
    estacions_de_carrega = set()
    while True:
        try:
            est_carrega = next(iterador_est)
            estacions_de_carrega.add(est_carrega)
            est_descarrega1 = next(iterador_est)
            if est_carrega.num_bicicletas_no_usadas < 30:
                bicis_no_usades = est_carrega.num_bicicletas_no_usadas
            else:
                bicis_no_usades = 30
            carrega = bicis_no_usades

            try:
                est_descarrega2 = next(iterador_est)
                descarrega1 = bicis_no_usades // 2
                descarrega2 = bicis_no_usades - (bicis_no_usades // 2) 
                ruta.append(Furgonetes(est_carrega, carrega, est_descarrega1, descarrega1, est_descarrega2, descarrega2))
            except:
                descarrega1 = bicis_no_usades
                ruta.append(Furgonetes(est_carrega, carrega, est_descarrega1, descarrega1))

        except StopIteration:
            #No hi ha més estacions
            break

    return Estat(params, ruta, estacions, estacions_de_carrega) #Instància d'Estat




     


def iterar_estacions(estacions: Estaciones) ->Generator[Estacion, None, None]:
    return (estacio for estacio in estacions.lista_estaciones)


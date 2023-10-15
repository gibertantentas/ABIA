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
        quant_furgos = len(self.ruta)
        for num_furgo in range(quant_furgos):
            for est_nova in self.estacions.lista_estaciones:
                if est_nova not in self.estacions_de_carrega:
                    yield Modificar_estacio_carrega(num_furgo, est_nova)
                    yield Descarrega_en_nova_estacio(num_furgo, est_nova)
                
            if self.ruta[num_furgo].estacio_descarrega1 is not None:
                yield Eliminar_estacio_descarrega(num_furgo)
                if self.ruta[num_furgo].estacio_descarrega2 is not None:
                    yield Modificar_sentit_ruta(num_furgo)
                
            #yield Carrega_mes_bicicletes(num_furgo)
            #yield Carrega_menys_bicicletes(num_furgo)
            if self.ruta[num_furgo].estacio_descarrega1 is not None and self.ruta[num_furgo].carrega <= 30:
                yield Descarrega_mes_bicicletes(num_furgo, 1)
                yield Descarrega_menys_bicicletes(num_furgo, 1)
            if self.ruta[num_furgo].estacio_descarrega2 is not None and self.ruta[num_furgo].carrega <= 30:
                yield Descarrega_mes_bicicletes(num_furgo, 2)
                yield Descarrega_menys_bicicletes(num_furgo, 2)
            for num_furgo2 in range(num_furgo + 1, quant_furgos):
                if num_furgo != num_furgo2:
                    for i in range(2):
                        for j in range(2):
                            yield Intercanviar_estacions(num_furgo, num_furgo2, i, j)

    def comprova_ruta(self):
        for furgo in self.ruta:
            if furgo.estacio_descarrega1 is None:
                if furgo.estacio_descarrega2 is not None:
                    furgo.estacio_descarrega1 = furgo.estacio_descarrega2
                    furgo.descarrega1 = furgo.carrega
                    furgo.estacio_descarrega2 = None
                    furgo.descarrega2 = 0
                else:
                    furgo.descarrega1, furgo.descarrega2 = 0, 0
            elif furgo.estacio_descarrega2 is None and furgo.descarrega2 != 0:
                furgo.descarrega2 = 0
                furgo.descarrega1 = furgo.carrega
                    
                return False
    def aplica_operador(self, operador: Operador):
        nou_estat = self.copia()
        if isinstance(operador, Modificar_estacio_carrega):
            nou_estat.ruta[operador.num_furgo].estacio_carrega = operador.est_nova
            nou_estat.comprova_ruta()
            '''
            furgo = nou_estat.ruta[operador.num_furgo]
            if operador.est_nova is furgo.estacio_descarrega1:
                furgo.estacio_descarrega1 = furgo.estacio_descarrega2
                furgo.descarrega1 = furgo.carrega
                furgo.estacio_descarrega2 = None
                furgo.descarrega2 = 0
            elif operador.est_nova is furgo.estacio_descarrega2:
                furgo.descarrega1 = furgo.carrega
                furgo.estacio_descarrega2 = None
                furgo.descarrega2 = 0
            '''
        
        elif isinstance(operador, Intercanviar_estacions):
            if operador.est_intercanvi1 == 0 and operador.est_intercanvi2 == 0:
                nou_estat.ruta[operador.num_furgo1].carrega, nou_estat.ruta[operador.num_furgo2].carrega = nou_estat.ruta[operador.num_furgo2].carrega, nou_estat.ruta[operador.num_furgo1].carrega
            
            elif operador.est_intercanvi1 == 0 and operador.est_intercanvi2 == 1:
                nou_estat.ruta[operador.num_furgo1].carrega, nou_estat.ruta[operador.num_furgo2].descarrega1 = nou_estat.ruta[operador.num_furgo2].descarrega1, nou_estat.ruta[operador.num_furgo1].carrega
            
            elif operador.est_intercanvi1 == 0 and operador.est_intercanvi2 == 2:
                nou_estat.ruta[operador.num_furgo1].carrega, nou_estat.ruta[operador.num_furgo2].descarrega2 = nou_estat.ruta[operador.num_furgo2].descarrega2, nou_estat.ruta[operador.num_furgo1].carrega
            
            elif operador.est_intercanvi1 == 1 and operador.est_intercanvi2 == 0:
                nou_estat.ruta[operador.num_furgo1].descarrega1, nou_estat.ruta[operador.num_furgo2].carrega = nou_estat.ruta[operador.num_furgo2].carrega, nou_estat.ruta[operador.num_furgo1].descarrega1
            
            elif operador.est_intercanvi1 == 1 and operador.est_intercanvi2 == 1:
                nou_estat.ruta[operador.num_furgo1].descarrega1, nou_estat.ruta[operador.num_furgo2].descarrega1 = nou_estat.ruta[operador.num_furgo2].descarrega1, nou_estat.ruta[operador.num_furgo1].descarrega1
            
            elif operador.est_intercanvi1 == 1 and operador.est_intercanvi2 == 2:
                nou_estat.ruta[operador.num_furgo1].descarrega1, nou_estat.ruta[operador.num_furgo2].descarrega2 = nou_estat.ruta[operador.num_furgo2].descarrega2, nou_estat.ruta[operador.num_furgo1].descarrega1
            
            elif operador.est_intercanvi1 == 2 and operador.est_intercanvi2 == 0:
                nou_estat.ruta[operador.num_furgo1].descarrega2, nou_estat.ruta[operador.num_furgo2].carrega = nou_estat.ruta[operador.num_furgo2].carrega, nou_estat.ruta[operador.num_furgo1].descarrega2
            
            elif operador.est_intercanvi1 == 2 and operador.est_intercanvi2 == 1:
                nou_estat.ruta[operador.num_furgo1].descarrega2, nou_estat.ruta[operador.num_furgo2].descarrega1 = nou_estat.ruta[operador.num_furgo2].descarrega1, nou_estat.ruta[operador.num_furgo1].descarrega2
            
            elif operador.est_intercanvi1 == 2 and operador.est_intercanvi2 == 2:
                nou_estat.ruta[operador.num_furgo1].descarrega2, nou_estat.ruta[operador.num_furgo2].descarrega2 = nou_estat.ruta[operador.num_furgo2].descarrega2, nou_estat.ruta[operador.num_furgo1].descarrega2

            
        #elif isinstance(operador, Carrega_mes_bicicletes):
        #    nou_estat.ruta[operador.num_furgo].carrega += 1
           
        #elif isinstance(operador, Carrega_menys_bicicletes):
        #    nou_estat.ruta[operador.num_furgo].carrega -= 1
        

        elif isinstance(operador, Modificar_sentit_ruta):
            furgo = nou_estat.ruta[operador.num_furgo]
            furgo.estacio_descarrega1, furgo.estacio_descarrega2 = furgo.estacio_descarrega2, furgo.estacio_descarrega1
            furgo.descarrega1, furgo.descarrega2 = furgo.descarrega2, furgo.descarrega1
        
        elif isinstance(operador, Eliminar_estacio_descarrega):
            furgo = nou_estat.ruta[operador.num_furgo]
            if furgo.estacio_descarrega2 is not None:
                furgo.estacio_descarrega2 = None
                furgo.descarrega1 = furgo.carrega
                furgo.descarrega2 = 0
            elif furgo.estacio_descarrega1 is not None:
                furgo.estacio_descarrega1 = None
                furgo.descarrega1 = 0
        
        elif isinstance(operador, Descarrega_mes_bicicletes):
            if operador.estacio_descarrega == 1:
                nou_estat.ruta[operador.num_furgo].descarrega1 += operador.bicicletes
                nou_estat.ruta[operador.num_furgo].carrega += operador.bicicletes
            elif operador.estacio_descarrega == 2:
                nou_estat.ruta[operador.num_furgo].descarrega2 += operador.bicicletes
                nou_estat.ruta[operador.num_furgo].carrega += operador.bicicletes
        
        elif isinstance(operador, Descarrega_menys_bicicletes):
            if operador.estacio_descarrega == 1:
                nou_estat.ruta[operador.num_furgo].descarrega1 -= operador.bicicletes
                nou_estat.ruta[operador.num_furgo].carrega -= operador.bicicletes
            elif operador.estacio_descarrega == 2:
                nou_estat.ruta[operador.num_furgo].descarrega2 -= operador.bicicletes
                nou_estat.ruta[operador.num_furgo].carrega -= operador.bicicletes
                
        elif isinstance(operador, Descarrega_en_nova_estacio):
            furgo = nou_estat.ruta[operador.num_furgo]
            if furgo.estacio_descarrega1 is None:
                nou_estat.ruta[operador.num_furgo].estacio_descarrega1 = operador.estacio_descarrega
            elif furgo.estacio_descarrega2 is None:
                nou_estat.ruta[operador.num_furgo].estacio_descarrega2 = operador.estacio_descarrega
        return nou_estat
    '''def h(self):
        return sum(furgo.cost_gasolina() for furgo in self.ruta)
    
    def h2(self):
        guanys = sum(furgo.guanys() for furgo in self.ruta)
        perdues = sum(furgo.perdues() for furgo in self.ruta)
        return guanys - perdues'''
    def h_total(self):
        cost_gasolina = sum(furgo.cost_gasolina() for furgo in self.ruta)
        guanys = sum(furgo.guanys() for furgo in self.ruta)
        perdues = sum(furgo.perdues() for furgo in self.ruta)
        return guanys - perdues - cost_gasolina
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




def genera_estat_inicial2(params: Parametres, estaciones: Estaciones) -> Estat:
    ruta = []
    llista_ordenada = sorted(estaciones.lista_estaciones, key=lambda x: min(x.num_bicicletas_no_usadas, max(0,x.num_bicicletas_next-x.demanda)), reverse=True)
    estacions_carrega = llista_ordenada[0:params.n_furgonetes]
    estacions_descarrega = llista_ordenada[params.n_furgonetes:]

    for est_carrega in estacions_carrega:
        distancia_minima, est_descarrega_propera = float('inf'), None
        distancia_minima2, est_descarrega2_propera = float('inf'), None

        carrega = min(est_carrega.num_bicicletas_no_usadas, 30)
        for est_descarrega in estacions_descarrega:
            distancia = distancia_estacions(est_carrega, est_descarrega)
            if distancia < distancia_minima:
                distancia_minima, est_descarrega_propera = distancia, est_descarrega
              
        if est_descarrega_propera in estacions_descarrega:
            estacions_descarrega.remove(est_descarrega_propera) 

        for est_descarrega2 in estacions_descarrega: 
            distancia2 = distancia_estacions(est_descarrega_propera, est_descarrega2)
            if distancia2 < distancia_minima2:
                distancia_minima2, est_descarrega2_propera = distancia2, est_descarrega2
        if est_descarrega2_propera in estacions_descarrega:
            estacions_descarrega.remove(est_descarrega2_propera)
            
        if est_descarrega_propera: 
            diferencia = est_descarrega_propera.num_bicicletas_next - est_descarrega_propera.demanda
            if diferencia >= 0:
                est_descarrega_propera, est_descarrega2_propera = est_descarrega2_propera, None
                descarrega = carrega
                descarrega2 = 0
            else:
                descarrega = min(abs(diferencia), carrega)
                descarrega2 = min((carrega - descarrega), carrega)
                
            ruta.append(Furgonetes(est_carrega, carrega, est_descarrega_propera, descarrega, est_descarrega2_propera, descarrega2))
    return Estat(params, ruta, estaciones, estacions_carrega)


     
def distancia_estacions(origen: Estacion, desti: Estacion):
    return abs(origen.coordX - desti.coordX) + abs(origen.coordY - desti.coordY)

def iterar_estacions(estacions: Estaciones) ->Generator[Estacion, None, None]:
    return (estacio for estacio in estacions.lista_estaciones)


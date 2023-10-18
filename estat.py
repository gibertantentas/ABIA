from abia_bicing import Estacion, Estaciones
from typing import List, Set, Generator
from parametres import Parametres
from furgonetes import Furgonetes
from operadors import *
import copy


        
class Estat(object):
    """
    Classe que representa un estat
    """
    def __init__(self, parametres: Parametres,  ruta: List[Furgonetes], estacions: Estaciones, estacions_de_carrega: set()):
        self.params = parametres
        self.ruta =  ruta
        self.estacions = estacions
        self.estacions_de_carrega = estacions_de_carrega
        
    '''def copia(self):
        return Estat(self.params, self.ruta.copy(), self.estacions, self.estacions_de_carrega )'''
    def copia(self):
        # Crea una nueva instancia de Estat con los mismos valores de atributos
        return Estat(self.params, [copy.copy(furgo) for furgo in self.ruta], self.estacions, copy.copy(self.estacions_de_carrega))
        #

    
    def genera_accions(self) -> Generator[Operador, None, None]:
        quant_furgos = len(self.ruta)
        for num_furgo in range(quant_furgos):
            
            for num_furgo2 in range(num_furgo + 1, quant_furgos):
                if num_furgo != num_furgo2:
                    if self.ruta[num_furgo].estacio_carrega is not None:
                        yield Intercanviar_estacions(num_furgo, num_furgo2, 0, 0)
                        if self.ruta[num_furgo2].estacio_descarrega1 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 0, 1)
                        if self.ruta[num_furgo2].estacio_descarrega2 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 0, 2)
                    if self.ruta[num_furgo].estacio_descarrega1 is not None:
                        yield Intercanviar_estacions(num_furgo, num_furgo2, 1, 0)
                        if self.ruta[num_furgo2].estacio_descarrega1 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 1, 1)
                        if self.ruta[num_furgo2].estacio_descarrega2 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 1, 2)
                    if self.ruta[num_furgo].estacio_descarrega2 is not None:
                        yield Intercanviar_estacions(num_furgo, num_furgo2, 2, 0)
                        if self.ruta[num_furgo2].estacio_descarrega1 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 2, 1)
                        if self.ruta[num_furgo2].estacio_descarrega2 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 2, 2)
                            
            if self.ruta[num_furgo].estacio_descarrega1 is not None:
                if self.ruta[num_furgo].carrega > 0:
                    yield Descarrega_menys_bicicletes(num_furgo, 1)
                if self.ruta[num_furgo].carrega < 30:
                    yield Descarrega_mes_bicicletes(num_furgo, 1)
                    
                if self.ruta[num_furgo].estacio_descarrega2 is not None:
                    #yield Modificar_sentit_ruta(num_furgo)
                    yield Eliminar_estacio_descarrega(num_furgo,1)
                    yield Eliminar_estacio_descarrega(num_furgo,2)
                    if self.ruta[num_furgo].descarrega1 > 0:
                        yield Intercanviar_bicicletes(num_furgo,2) #Estació 1 dóna a estació 2
                    if self.ruta[num_furgo].descarrega2 > 0:
                        yield Intercanviar_bicicletes(num_furgo,1) #Estacio 2 dóna a estació 1

            if self.ruta[num_furgo].estacio_descarrega2 is not None:
                if self.ruta[num_furgo].carrega > 0:
                    yield Descarrega_menys_bicicletes(num_furgo, 2)
                if self.ruta[num_furgo].carrega < 30:
                    yield Descarrega_mes_bicicletes(num_furgo, 2)
            


            if self.ruta[num_furgo].carrega > self.ruta[num_furgo].descarrega1 + self.ruta[num_furgo].descarrega2:
                yield Carrega_menys_bicicletes(num_furgo)
                
            for est_nova in self.estacions.lista_estaciones:
                if est_nova not in self.estacions_de_carrega:
                    yield Carrega_en_nova_estacio(num_furgo, est_nova)
                    
                if self.ruta[num_furgo].carrega < 30:
                    yield Descarrega_en_nova_estacio(num_furgo, est_nova)
                

            

    '''def comprova_ruta(self):
        for furgo in self.ruta:
                if furgo.estacio_descarrega1 is None and furgo.descarrega1 != 0 or furgo.estacio_descarrega2 is None and furgo.descarrega2 != 0:
                    print(f'{furgo.estacio_descarrega1}  DESCARREGA {furgo.descarrega1}   i   {furgo.estacio_descarrega2} DESCARREGA {furgo.descarrega2}')'''
    def aplica_operador(self, operador: Operador):
        nou_estat = self.copia()
        if isinstance(operador, Carrega_en_nova_estacio):
            nou_estat.estacions_de_carrega.add(operador.est_nova)
            if nou_estat.ruta[operador.num_furgo].estacio_carrega in nou_estat.estacions_de_carrega:
                nou_estat.estacions_de_carrega.remove(nou_estat.ruta[operador.num_furgo].estacio_carrega)
            nou_estat.ruta[operador.num_furgo].estacio_carrega = operador.est_nova

        
        elif isinstance(operador, Intercanviar_estacions):
            if operador.est_intercanvi1 == 0 and operador.est_intercanvi2 == 0:
                nou_estat.ruta[operador.num_furgo1].estacio_carrega, nou_estat.ruta[operador.num_furgo2].estacio_carrega = nou_estat.ruta[operador.num_furgo2].estacio_carrega, nou_estat.ruta[operador.num_furgo1].estacio_carrega
            
            elif operador.est_intercanvi1 == 0 and operador.est_intercanvi2 == 1:
                nou_estat.ruta[operador.num_furgo1].estacio_carrega, nou_estat.ruta[operador.num_furgo2].estacio_descarrega1 = nou_estat.ruta[operador.num_furgo2].estacio_descarrega1, nou_estat.ruta[operador.num_furgo1].estacio_carrega
            
            elif operador.est_intercanvi1 == 0 and operador.est_intercanvi2 == 2:
                nou_estat.ruta[operador.num_furgo1].estacio_carrega, nou_estat.ruta[operador.num_furgo2].estacio_descarrega2 = nou_estat.ruta[operador.num_furgo2].estacio_descarrega2, nou_estat.ruta[operador.num_furgo1].estacio_carrega
            
            elif operador.est_intercanvi1 == 1 and operador.est_intercanvi2 == 0:
                nou_estat.ruta[operador.num_furgo1].estacio_descarrega1, nou_estat.ruta[operador.num_furgo2].estacio_carrega = nou_estat.ruta[operador.num_furgo2].estacio_carrega, nou_estat.ruta[operador.num_furgo1].estacio_descarrega1
            
            elif operador.est_intercanvi1 == 1 and operador.est_intercanvi2 == 1:
                nou_estat.ruta[operador.num_furgo1].estacio_descarrega1, nou_estat.ruta[operador.num_furgo2].estacio_descarrega1 = nou_estat.ruta[operador.num_furgo2].estacio_descarrega1, nou_estat.ruta[operador.num_furgo1].estacio_descarrega1
            
            elif operador.est_intercanvi1 == 1 and operador.est_intercanvi2 == 2:
                nou_estat.ruta[operador.num_furgo1].estacio_descarrega1, nou_estat.ruta[operador.num_furgo2].estacio_descarrega2 = nou_estat.ruta[operador.num_furgo2].estacio_descarrega2, nou_estat.ruta[operador.num_furgo1].estacio_descarrega1
            
            elif operador.est_intercanvi1 == 2 and operador.est_intercanvi2 == 0:
                nou_estat.ruta[operador.num_furgo1].estacio_descarrega2, nou_estat.ruta[operador.num_furgo2].estacio_carrega = nou_estat.ruta[operador.num_furgo2].estacio_carrega, nou_estat.ruta[operador.num_furgo1].estacio_descarrega2
            
            elif operador.est_intercanvi1 == 2 and operador.est_intercanvi2 == 1:
                nou_estat.ruta[operador.num_furgo1].estacio_descarrega2, nou_estat.ruta[operador.num_furgo2].estacio_descarrega1 = nou_estat.ruta[operador.num_furgo2].estacio_descarrega1, nou_estat.ruta[operador.num_furgo1].estacio_descarrega2
            
            elif operador.est_intercanvi1 == 2 and operador.est_intercanvi2 == 2:
                nou_estat.ruta[operador.num_furgo1].estacio_descarrega2, nou_estat.ruta[operador.num_furgo2].estacio_descarrega2 = nou_estat.ruta[operador.num_furgo2].estacio_descarrega2, nou_estat.ruta[operador.num_furgo1].estacio_descarrega2
           
        elif isinstance(operador, Carrega_menys_bicicletes):
            nou_estat.ruta[operador.num_furgo].carrega -= 1
        

        elif isinstance(operador, Modificar_sentit_ruta): #ELIMINABLE
            furgo = nou_estat.ruta[operador.num_furgo]
            furgo.estacio_descarrega1, furgo.estacio_descarrega2 = furgo.estacio_descarrega2, furgo.estacio_descarrega1
            furgo.descarrega1, furgo.descarrega2 = furgo.descarrega2, furgo.descarrega1
        
        elif isinstance(operador, Eliminar_estacio_descarrega):
            furgo = nou_estat.ruta[operador.num_furgo]
            if operador.estacio_eliminada == 1:
                furgo.estacio_descarrega1 = None
                furgo.carrega -= furgo.descarrega1
                furgo.descarrega1 = 0
            elif operador.estacio_eliminada == 2:
                furgo.estacio_descarrega2 = None
                furgo.carrega -= furgo.descarrega2
                furgo.descarrega2 = 0
        
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
                nou_estat.ruta[operador.num_furgo].descarrega1 = 1
                nou_estat.ruta[operador.num_furgo].carrega += 1
            elif furgo.estacio_descarrega2 is None:
                nou_estat.ruta[operador.num_furgo].estacio_descarrega2 = operador.estacio_descarrega
                nou_estat.ruta[operador.num_furgo].descarrega2 = 1
                nou_estat.ruta[operador.num_furgo].carrega += 1
                
        elif isinstance(operador, Intercanviar_bicicletes):
            if operador.est == 2:
                nou_estat.ruta[operador.num_furgo].descarrega1 -= 1
                nou_estat.ruta[operador.num_furgo].descarrega2 += 1
            elif operador.est == 1:
                nou_estat.ruta[operador.num_furgo].descarrega2 -= 1
                nou_estat.ruta[operador.num_furgo].descarrega1 += 1
        #nou_estat.comprova_ruta()
        return nou_estat

    def h(self):
        cost_gasolina = sum(furgo.cost_gasolina() for furgo in self.ruta)
        guanys = sum(furgo.guanys() for furgo in self.ruta)
        perdues = sum(furgo.perdues() for furgo in self.ruta)
        return guanys - perdues - cost_gasolina
        
    def __repr__(self):
        return f"Ruta: {self.ruta}"
        #return f"Parametres: n_estacions={self.params.n_estacions}, n_bicis={self.params.n_bicis}, llavor={self.params.llavor}, n_furgonetes={self.params.n_furgonetes}"   
    
    #Per implementar ruta com a Set


def genera_estat_inicial(params: Parametres, estacions: Estaciones) -> Estat:
    iterador_est = iterar_estacions(estacions)
    ruta = []
    estacions_de_carrega = set()
    
    for i in range(params.n_furgonetes):
        est_carrega = next(iterador_est)
        estacions_de_carrega.add(est_carrega)
        carrega = est_carrega.num_bicicletas_no_usadas
        est_descarrega1 = next(iterador_est)
        descarrega1 = carrega
        ruta.append(Furgonetes(est_carrega, carrega))


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
    return Estat(params, ruta, estaciones, set(estacions_carrega))


 
def distancia_estacions(origen: Estacion, desti: Estacion):
    return abs(origen.coordX - desti.coordX) + abs(origen.coordY - desti.coordY)

def iterar_estacions(estacions: Estaciones) ->Generator[Estacion, None, None]:
    return (estacio for estacio in estacions.lista_estaciones)


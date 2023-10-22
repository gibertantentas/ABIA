from abia_bicing import Estacion, Estaciones
from typing import List, Set, Generator
from parametres import Parametres
from furgonetes import Furgonetes
from operadors import *
from visual import visualitzar


comptador = 0
        
class Estat(object):
    """
    Classe que representa un estat
    """
    def __init__(self, parametres: Parametres,  ruta: List[Furgonetes], estacions: Estaciones, estacions_de_carrega: set()):

        self.params = parametres
        self.ruta =  ruta
        self.estacions = estacions
        self.estacions_de_carrega = estacions_de_carrega
        
        global comptador
        
        #print('Comptador',comptador)
        comptador += 1
   
    

    
    def genera_accions(self) -> Generator[Operador, None, None]:
        quant_furgos = len(self.ruta)

        if quant_furgos < self.params.n_furgonetes:
            yield Nova_furgo()
        
        for num_furgo in range(quant_furgos):
            for num_furgo2 in range(num_furgo + 1, quant_furgos):
                if num_furgo != num_furgo2:
                    if self.ruta[num_furgo].estacio_carrega is not None:
                        if self.ruta[num_furgo2].estacio_carrega is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 0, 0)
                        if self.ruta[num_furgo2].estacio_descarrega1 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 0, 1)
                        if self.ruta[num_furgo2].estacio_descarrega2 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 0, 2)
                    if self.ruta[num_furgo].estacio_descarrega1 is not None:
                        if self.ruta[num_furgo2].estacio_carrega is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 1, 0)
                        if self.ruta[num_furgo2].estacio_descarrega1 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 1, 1)
                        if self.ruta[num_furgo2].estacio_descarrega2 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 1, 2)
                    if self.ruta[num_furgo].estacio_descarrega2 is not None:
                        if self.ruta[num_furgo2].estacio_carrega is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 2, 0)
                        if self.ruta[num_furgo2].estacio_descarrega1 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 2, 1)
                        if self.ruta[num_furgo2].estacio_descarrega2 is not None:
                            yield Intercanviar_estacions(num_furgo, num_furgo2, 2, 2)
                            
            if self.ruta[num_furgo].estacio_descarrega1 is not None:
                yield Descarrega_menys_bicicletes(num_furgo, 1)
                yield Descarrega_mes_bicicletes(num_furgo, 1)
                yield Eliminar_estacio_descarrega(num_furgo,1)
                if self.ruta[num_furgo].estacio_descarrega2 is not None:
                    #yield Modificar_sentit_ruta(num_furgo)
                    yield Eliminar_estacio_descarrega(num_furgo,2)
                    if self.ruta[num_furgo].descarrega1 > 0:
                        yield Intercanviar_bicicletes(num_furgo,2) #Estació 1 dóna a estació 2
                    if self.ruta[num_furgo].descarrega2 > 0:
                        yield Intercanviar_bicicletes(num_furgo,1) #Estacio 2 dóna a estació 1

            if self.ruta[num_furgo].estacio_descarrega2 is not None:
                yield Descarrega_menys_bicicletes(num_furgo, 2)
                yield Descarrega_mes_bicicletes(num_furgo, 2)


            '''if self.ruta[num_furgo].carrega > self.ruta[num_furgo].descarrega1 + self.ruta[num_furgo].descarrega2:
                yield Carrega_menys_bicicletes(num_furgo)'''

            for est_nova in self.estacions.lista_estaciones:

                if est_nova not in self.estacions_de_carrega:

                    yield Carrega_en_nova_estacio(num_furgo, est_nova)
                    
                if self.ruta[num_furgo].carrega < 30:
                    yield Descarrega_en_nova_estacio(num_furgo, est_nova)
                    

                

            

    '''def comprova_ruta(self):
        for furgo in self.ruta:
                if furgo.descarrega1 == 0 and furgo.estacio_descarrega1 is not None:
                    furgo.estacio_descarrega1 = None
                
                if furgo.descarrega2 == 0 and furgo.estacio_descarrega2 is not None:
                    furgo.estacio_descarrega2 = None'''
                
    def aplica_operador(self, operador: Operador):
        nou_estat = self.copia()
        if isinstance(operador, Carrega_en_nova_estacio):
            nou_estat.estacions_de_carrega.add(operador.est_nova)
            if nou_estat.ruta[operador.num_furgo].estacio_carrega in nou_estat.estacions_de_carrega:
                nou_estat.estacions_de_carrega.remove(nou_estat.ruta[operador.num_furgo].estacio_carrega)
            nou_estat.ruta[operador.num_furgo].estacio_carrega = operador.est_nova

        elif isinstance(operador, Nova_furgo):        
            estacio_carrega, est_descarrega_propera, est_descarrega_propera2 = None, None, None
            carrega, descarrega1, descarrega2 = 0,0,0
            llista_ordenada = sorted(nou_estat.estacions.lista_estaciones, key=lambda x: min(x.num_bicicletas_no_usadas, max(0,x.num_bicicletas_next-x.demanda)), reverse=True)
            for i in llista_ordenada:
                if i not in nou_estat.estacions_de_carrega:
                    estacio_carrega = i
                    break

            if estacio_carrega in llista_ordenada:
                llista_ordenada.remove(estacio_carrega)


            if estacio_carrega:  
                carrega = min(estacio_carrega.num_bicicletas_no_usadas, 30)              
                distancia_minima, est_descarrega_propera = float('inf'), None
                
                for est in llista_ordenada:
                        if est.num_bicicletas_next - est.demanda < 0:
                            distancia = distancia_estacions(estacio_carrega, est)
                            if distancia < distancia_minima:
                                distancia_minima, est_descarrega_propera = distancia, est

            if est_descarrega_propera in llista_ordenada:
                llista_ordenada.remove(est_descarrega_propera)         

            if est_descarrega_propera:     
                diferencia = est_descarrega_propera.num_bicicletas_next - est_descarrega_propera.demanda
                descarrega1 = min(abs(diferencia), carrega)           
                distancia_minima2, est_descarrega_propera2 = float('inf'), None
                
                for est_des in llista_ordenada:
                        if est_des.num_bicicletas_next - est_des.demanda < 0:
                            distancia = distancia_estacions(est_descarrega_propera, est_des)
                            if distancia < distancia_minima2:
                                distancia_minima2, est_descarrega_propera2 = distancia, est_des
           
            if est_descarrega_propera2:
                descarrega2 = min((carrega - descarrega1), carrega)
            else:
                carrega = descarrega1   
            #carrega = min(carrega, estacio_descarrega.demanda - estacio_descarrega.num_bicicletas_next) 
            nou_estat.ruta.append(Furgonetes(estacio_carrega, carrega, est_descarrega_propera, descarrega1, est_descarrega_propera2, descarrega2))
            nou_estat.estacions_de_carrega.add(estacio_carrega)
             
            '''carrega_max = 0
            for est in nou_estat.estacions.lista_estaciones:
                if est not in nou_estat.estacions_de_carrega and est.num_bicicletas_no_usadas > carrega_max:
                    estacio_carrega = est
                    carrega = est.num_bicicletas_no_usadas
                    carrega_max = carrega
                    
            if estacio_carrega:
                dist_max = float('inf')
                for est2 in nou_estat.estacions.lista_estaciones:
                    if est2 is not estacio_carrega and est2 not in nou_estat.estacions_de_carrega and distancia_estacions(est2, estacio_carrega) < dist_max and (est2.demanda - est2.num_bicicletas_next) > 0:
                        dist_max = distancia_estacions(est2, estacio_carrega)
                        estacio_descarrega1 = est2
                carrega = min(carrega, estacio_descarrega1.demanda - estacio_descarrega1.num_bicicletas_next) 
                nou_estat.ruta.append(Furgonetes(estacio_carrega, carrega, estacio_descarrega1, carrega))
                nou_estat.estacions_de_carrega.add(estacio_carrega)'''
            
              


            
                   
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
           
            '''elif isinstance(operador, Carrega_menys_bicicletes):
            nou_estat.ruta[operador.num_furgo].carrega -= 1'''
        

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
            furgo = nou_estat.ruta[operador.num_furgo]
            if operador.estacio_descarrega == 1:
                bicis_necessaries = furgo.estacio_descarrega1.demanda - furgo.estacio_descarrega1.num_bicicletas_next if furgo.estacio_descarrega1.demanda > furgo.estacio_descarrega1.num_bicicletas_next else 0
                n_bicis = min(bicis_necessaries ,30 - furgo.carrega)
                #n_bicis = 30 - furgo.carrega
                furgo.descarrega1 += n_bicis
                furgo.carrega += n_bicis
            elif operador.estacio_descarrega == 2:
                bicis_necessaries = furgo.estacio_descarrega2.demanda - furgo.estacio_descarrega2.num_bicicletas_next if furgo.estacio_descarrega2.demanda > furgo.estacio_descarrega2.num_bicicletas_next else 0
                n_bicis = min(bicis_necessaries ,30 - furgo.carrega)
                #n_bicis = 30 - furgo.carrega
                furgo.descarrega2 += n_bicis
                furgo.carrega += n_bicis
            

        elif isinstance(operador, Descarrega_menys_bicicletes):
            furgo = nou_estat.ruta[operador.num_furgo]
            if furgo.carrega > 0:
                if operador.estacio_descarrega == 1:
                    bicis_innecessaries = furgo.estacio_descarrega1.num_bicicletas_next - furgo.estacio_descarrega1.demanda if furgo.estacio_descarrega1.demanda < furgo.estacio_descarrega1.num_bicicletas_next else 0
                    bicis_a_treure = min(bicis_innecessaries, furgo.carrega)

                    #furgo.descarrega1 -= bicis_a_treure
                    #furgo.carrega -= bicis_a_treure
                    furgo.descarrega1 -= 1
                    furgo.carrega -= 1
                elif operador.estacio_descarrega == 2:
                    bicis_innecessaries = furgo.estacio_descarrega2.num_bicicletas_next - furgo.estacio_descarrega2.demanda if furgo.estacio_descarrega2.demanda < furgo.estacio_descarrega2.num_bicicletas_next else 0
                    bicis_a_treure = min(bicis_innecessaries, furgo.carrega - furgo.descarrega1)

                    #furgo.descarrega2 -= bicis_a_treure
                    #furgo.carrega -= bicis_a_treure
                    furgo.descarrega1 -= 1
                    furgo.carrega -= 1
            
        elif isinstance(operador, Descarrega_en_nova_estacio):
            
            furgo = nou_estat.ruta[operador.num_furgo]
            if nou_estat.ruta[operador.num_furgo].carrega < 30:
                if furgo.estacio_descarrega1 is None:
                    furgo.estacio_descarrega1 = operador.estacio_descarrega
                    #bicis_necessaries = furgo.estacio_descarrega1.demanda - furgo.estacio_descarrega1.num_bicicletas_next if furgo.estacio_descarrega1.demanda > furgo.estacio_descarrega1.num_bicicletas_next else 0
                    #n_bicis = min(bicis_necessaries ,30 - nou_estat.ruta[operador.num_furgo].carrega)
                    n_bicis = 30 - nou_estat.ruta[operador.num_furgo].carrega
                    furgo.descarrega1 = n_bicis
                    furgo.carrega += n_bicis
                elif furgo.estacio_descarrega2 is None and furgo.estacio_descarrega1 is not operador.estacio_descarrega:
                    furgo.estacio_descarrega2 = operador.estacio_descarrega
                    #bicis_necessaries = furgo.estacio_descarrega2.demanda - furgo.estacio_descarrega2.num_bicicletas_next if furgo.estacio_descarrega2.demanda > furgo.estacio_descarrega2.num_bicicletas_next else 0
                    #n_bicis = min(bicis_necessaries ,30 - nou_estat.ruta[operador.num_furgo].carrega)
                    n_bicis = 30 - nou_estat.ruta[operador.num_furgo].carrega
                    furgo.descarrega2 = n_bicis
                    furgo.carrega += n_bicis

        elif isinstance(operador, Intercanviar_bicicletes):
            if operador.est == 2:
                nou_estat.ruta[operador.num_furgo].descarrega1 -= 1
                nou_estat.ruta[operador.num_furgo].descarrega2 += 1
            elif operador.est == 1:
                nou_estat.ruta[operador.num_furgo].descarrega2 -= 1
                nou_estat.ruta[operador.num_furgo].descarrega1 += 1

        for furgo in nou_estat.ruta:
                if furgo.descarrega1 == 0 and furgo.estacio_descarrega1 is not None:
                    furgo.estacio_descarrega1 = None
                
                if furgo.descarrega2 == 0 and furgo.estacio_descarrega2 is not None:
                    furgo.estacio_descarrega2 = None    
        return nou_estat
    def recalcular_estat(self):
        for furgo in self.ruta:
            furgo.estacio_carrega.num_bicicletas_next -= furgo.carrega
            try:
                furgo.estacio_descarrega1.num_bicicletas_next += furgo.descarrega1
            except:
                pass
            try:
                furgo.estacio_descarrega2.num_bicicletas_next += furgo.descarrega2
            except:
                pass
    def h(self):
        diners = 0
        for est in self.estacions.lista_estaciones:
            bicis_finals = 0
            carrega = 0
            descarrega1 = 0
            descarrega2 = 0
            for furgo in self.ruta:
                if furgo.estacio_carrega is est:
                    carrega = furgo.carrega
                    '''if furgo.estacio_carrega.num_bicicletas_next - furgo.carrega < furgo.estacio_carrega.demanda:
                        carrega += furgo.carrega'''
                if furgo.estacio_descarrega1 is est:
                    descarrega1 += furgo.descarrega1
                if furgo.estacio_descarrega2 is est:
                    descarrega2 += furgo.descarrega2
            bicis_finals += descarrega1 + descarrega2 - carrega
            if est.num_bicicletas_next > est.demanda:
                if est.num_bicicletas_next + bicis_finals < est.demanda:
                    diners -= abs(est.num_bicicletas_next + bicis_finals - est.demanda)
            
            elif est.num_bicicletas_next < est.demanda:
                if est.num_bicicletas_next + bicis_finals > est.demanda:
                    diners += abs(est.demanda - est.num_bicicletas_next)
                elif est.num_bicicletas_next + bicis_finals < est.demanda:
                    diners += bicis_finals
                    
            elif est.num_bicicletas_next == est.demanda:
                if est.num_bicicletas_next + bicis_finals < est.demanda:
                    diners -= bicis_finals
        
        diners -= sum(furgo.cost_gasolina() for furgo in self.ruta)
        return diners
    
    def h2(self):
        cost_gasolina = sum(furgo.cost_gasolina() for furgo in self.ruta)
        guanys = sum(furgo.guanys() for furgo in self.ruta)
        perdues = sum(furgo.perdues() for furgo in self.ruta)
        #print(f'Guanys: {guanys}, perdues {perdues}, cost gasolina {cost_gasolina}')
        return guanys - perdues - cost_gasolina
        
    def __repr__(self):
        return f"Ruta: {self.ruta}"

    def copia(self):
        nou_estat = Estat(self.params, [furgo.__copy__() for furgo in self.ruta], self.estacions, set(self.estacions_de_carrega))
        if nou_estat != self:
            print('DIFERENT')
        if nou_estat is self:
            print('ES')
        return nou_estat

    def __eq__(self, __value):
        return self.params == __value.params and self.ruta == __value.ruta and self.estacions == __value.estacions and  self.estacions_de_carrega == __value.estacions_de_carrega


def genera_estat_inicial1(params: Parametres, estacions: Estaciones) -> Estat:
    return Estat(params, [], estacions, set())
def genera_estat_inicial0(params: Parametres, estacions: Estaciones) -> Estat:
    iterador_est = iterar_estacions(estacions)
    ruta = []
    estacions_de_carrega = set()
    
    for i in range(params.n_furgonetes):
        est_carrega = next(iterador_est)
        estacions_de_carrega.add(est_carrega)
        carrega = est_carrega.num_bicicletas_no_usadas
        '''est_descarrega1 = next(iterador_est)
        descarrega1 = carrega'''
        ruta.append(Furgonetes(est_carrega, carrega))


    return Estat(params, ruta, estacions, estacions_de_carrega) #Instància d'Estat


def genera_estat_inicial2(params: Parametres, estacions: Estaciones) -> Estat:
    possibles_furgos = []
    estacions_descarrega = set(estacions.lista_estaciones)
    for est_carrega in estacions.lista_estaciones:
        if est_carrega.num_bicicletas_next - est_carrega.demanda > 3:
            ratio_max, est_descarrega1_optima = float('-inf'), None
            ratio_max2, est_descarrega2_optima = float('-inf'), None

            carrega = min(est_carrega.num_bicicletas_no_usadas, 30)#, max(0,est_carrega.num_bicicletas_next-est_carrega.demanda))
            for est_descarrega in estacions_descarrega:
                if est_carrega is not est_descarrega and est_descarrega.num_bicicletas_next - est_descarrega.demanda < 0:
                    bicis_faltants = abs(est_descarrega.num_bicicletas_next - est_descarrega.demanda)
                    
                    cost_transport = ((bicis_faltants + 9) // 10) * (distancia_estacions(est_carrega, est_descarrega) / 1000)

                    ratio = bicis_faltants - cost_transport
                    if ratio > ratio_max:
                        ratio_max = ratio
                        est_descarrega1_optima = est_descarrega
                    #else: estacions_descarrega.remove(est_descarrega)
            
            if est_descarrega1_optima in estacions_descarrega:
                estacions_descarrega.remove(est_descarrega1_optima)
            
            
            if est_descarrega1_optima:
                diferencia = est_descarrega1_optima.num_bicicletas_next - est_descarrega1_optima.demanda
                descarrega1 = min(abs(diferencia), carrega)           
                
                if descarrega1 < carrega:
                    
                    for est_descarrega2 in estacions_descarrega:
                        if est_carrega is not est_descarrega2:
                            if est_descarrega2.num_bicicletas_next - est_descarrega2.demanda < 0:
                                bicis_faltants = abs(est_descarrega2.num_bicicletas_next - est_descarrega2.demanda)
                                cost_transport = ((bicis_faltants + 9) // 10) * (distancia_estacions(est_descarrega1_optima, est_descarrega2) / 1000)
                                ratio = bicis_faltants - cost_transport
                                #print(ratio, est_descarrega2.num_bicicletas_next- est_descarrega2.demanda, distancia_estacions(est_descarrega1_optima, est_descarrega2)) 
                                if ratio > ratio_max2:
                                    ratio_max2 = ratio
                                    est_descarrega2_optima = est_descarrega2
                    #print('ratio ecollit', ratio_max2)
                    if est_descarrega2_optima in estacions_descarrega:
                        estacions_descarrega.remove(est_descarrega2_optima)
                

            if est_descarrega2_optima:
                descarrega2 = carrega - descarrega1
            else: 
                carrega = descarrega1
            if est_descarrega2_optima:
               possibles_furgos.append(Furgonetes(est_carrega, carrega, est_descarrega1_optima, descarrega1, est_descarrega2_optima, descarrega2))
            if est_descarrega1_optima and not est_descarrega2_optima:
                possibles_furgos.append(Furgonetes(est_carrega, carrega, est_descarrega1_optima, descarrega1))

    
    #ruta_ordenada = sorted(possibles_furgos, key=lambda furgoneta: furgoneta.cost_gasolina() - furgoneta.carrega, reverse=True)
    ruta_ordenada = sorted(possibles_furgos, key=lambda furgoneta: furgoneta.carrega - furgoneta.cost_gasolina(), reverse=True)
    ruta_optima = ruta_ordenada[:params.n_furgonetes]
    estacions_carrega = set()
    
    for furgo in ruta_optima:
        estacions_carrega.add(furgo.estacio_carrega)
    estat = Estat(params, ruta_optima, estacions, set(estacions_carrega))
    for furgo in estat.ruta:
        print(furgo.carrega, furgo.descarrega1, furgo.descarrega2)
        print(furgo.estacio_carrega.num_bicicletas_next - furgo.estacio_carrega.demanda, furgo.estacio_descarrega1.num_bicicletas_next - furgo.estacio_descarrega1.demanda)
        print(distancia_estacions(furgo.estacio_carrega, furgo.estacio_descarrega1))
        print('ERROR' if furgo.estacio_carrega is furgo.estacio_descarrega1 or furgo.estacio_carrega is furgo.estacio_descarrega2 or furgo.estacio_descarrega1 is furgo.estacio_descarrega2 else '')
    print('heuristica',estat.h())
    #visualitzar(estacions,estat)
    return estat
def genera_estat_inicial__(params: Parametres, estaciones: Estaciones) -> Estat:
    ruta = []
    est_carrega, est_descarrega_propera, est_descarrega_propera2 = None, None, None
    carrega, descarrega, descarrega2 = 0,0,0
    llista_ordenada = sorted(estaciones.lista_estaciones, key=lambda x: min(x.num_bicicletas_no_usadas, max(0,x.num_bicicletas_next-x.demanda)), reverse=True)
    estacions_carrega = llista_ordenada[0:params.n_furgonetes]
    estacions_descarrega = llista_ordenada[params.n_furgonetes:]

    for est_carrega in estacions_carrega:
        distancia_minima, est_descarrega_propera = float('inf'), None
        distancia_minima2, est_descarrega2_propera = float('inf'), None

        carrega = min(est_carrega.num_bicicletas_no_usadas, 30)#, max(0,est_carrega.num_bicicletas_next-est_carrega.demanda))
        for est_descarrega in estacions_descarrega:
            if est_descarrega.num_bicicletas_next - est_descarrega.demanda < 0:
                distancia = distancia_estacions(est_carrega, est_descarrega)
                if distancia < distancia_minima:
                    distancia_minima, est_descarrega_propera = distancia, est_descarrega
            else: estacions_descarrega.remove(est_descarrega)
              
        if est_descarrega_propera in estacions_descarrega:
            estacions_descarrega.remove(est_descarrega_propera) 

        if est_descarrega_propera:     
            diferencia = est_descarrega_propera.num_bicicletas_next - est_descarrega_propera.demanda
            descarrega = min(abs(diferencia), carrega)           
            
            
        if est_descarrega_propera2:
            descarrega2 = carrega - descarrega
        else: 
            carrega = descarrega

        if est_carrega and est_descarrega_propera:       
            ruta.append(Furgonetes(est_carrega, carrega, est_descarrega_propera, descarrega, est_descarrega2_propera, descarrega2))

    estat =Estat(params, ruta, estaciones, set(estacions_carrega))
    for furgo in estat.ruta:
        print(furgo.carrega, furgo.descarrega1, furgo.descarrega2)
    return estat 
    return Estat(params, ruta, estaciones, set(estacions_carrega))

    


 
def distancia_estacions(origen: Estacion, desti: Estacion):
    return abs(origen.coordX - desti.coordX) + abs(origen.coordY - desti.coordY)

def iterar_estacions(estacions: Estaciones) ->Generator[Estacion, None, None]:
    return (estacio for estacio in estacions.lista_estaciones)



    
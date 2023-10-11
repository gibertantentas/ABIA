from estacions import Estacio, Estacions, iterar_estacions
from typing import List, Set, Generator
from parametres import Parametres
from operadors import Carrega, Descarrega
from furgonetes import Furgonetes
        

def distancia_2_estacions():
    pass
    
    
class Estat():
    """
    Classe que representa un estat
    """

    def __init__(self, parametres: Parametres,  ruta: List[Furgonetes]):
        self.params = parametres
        self.ruta =  ruta
       
    
    '''
    def h(self):
        #REVISAR EL PROBLEMA 15 I LES OPTIMITZACIONS APLICADES
        cost_total = 0
        for furgo in self.ruta:
            cost_km_1 = ((furgo.carrega + 9) // 10)
            km_1 = furgo.estacio_carrega.distancia_estacions(furgo.estacio_descarrega1)
            cost_1 = km_1 * cost_km_1
            if furgo.estacio_descarrega2 is not None:
                cost_km_2 = (( (furgo.carrega - furgo.descarrega1) + 9) // 10)
                km_2 = furgo.estacio_descarrega1.distancia_estacions(furgo.estacio_descarrega2)
                cost_2 = km_2 * cost_km_2
                cost_km_3 = (( (furgo.carrega - furgo.descarrega1 - furgo.descarrega2) + 9) // 10)
                km_3 = furgo.estacio_descarrega2.distancia_estacions(furgo.estacio_carrega)
                cost_3 = km_3 * cost_km_3
                cost_total += cost_1 + cost_2 + cost_3
            else:
                cost_km_3 = (( (furgo.carrega - furgo.descarrega1 - furgo.descarrega2) + 9) // 10)
                km_3 = furgo.estacio_descarrega2.distancia_estacions(furgo.estacio_carrega)
                cost_3 = km_3 * cost_km_3
                cost_total += cost_1 + cost_3
        return cost_total
    '''    
    def h(self):
        #REVISAR EL PROBLEMA 15 I LES OPTIMITZACIONS APLICADES
        cost_total = 0
        for furgo in self.ruta:
            cost_km_1 = ((furgo.carrega + 9) // 10)
            km_1 = furgo.estacio_carrega.distancia_estacions(furgo.estacio_descarrega1)
            cost_1 = km_1 * cost_km_1
            if furgo.estacio_descarrega2 is not None:
                cost_km_2 = (( (furgo.carrega - furgo.descarrega1) + 9) // 10)
                km_2 = furgo.estacio_descarrega1.distancia_estacions(furgo.estacio_descarrega2)
                cost_2 = km_2 * cost_km_2
                cost_km_3 = (( (furgo.carrega - furgo.descarrega1 - furgo.descarrega2) + 9) // 10)
                km_3 = furgo.estacio_descarrega2.distancia_estacions(furgo.estacio_carrega)
                cost_3 = km_3 * cost_km_3
                cost_total += cost_1 + cost_2 + cost_3
            else:
                cost_km_3 = (( (furgo.carrega - furgo.descarrega1 - furgo.descarrega2) + 9) // 10)
                km_3 = furgo.estacio_descarrega2.distancia_estacions(furgo.estacio_carrega)
                cost_3 = km_3 * cost_km_3
                cost_total += cost_1 + cost_3
        return cost_total
    
    def __repr__(self):
        return f"Ruta: {self.ruta}"
        #return f"Parametres: n_estacions={self.params.n_estacions}, n_bicis={self.params.n_bicis}, llavor={self.params.llavor}, n_furgonetes={self.params.n_furgonetes}"   
        
def genera_estat_inicial(estacions: Estacions, params: Parametres) -> Estat:
    print('GENERANT ESTAT INICIAL...')
    iterador_est = iterar_estacions(estacions)
    ruta = []
    while True:
        try:
            est_carrega = next(iterador_est)
            est_descarrega1 = next(iterador_est)
            if est_carrega.num_bicicletes_no_usades < 30:
                bicis_no_usades = est_carrega.num_bicicletes_no_usades
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

    return Estat(params, ruta) #Instància d'Estat
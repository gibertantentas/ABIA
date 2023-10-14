from abia_bicing import Estacion, Estaciones
from typing import List, Set, Generator
from parametres import Parametres
from furgonetes import Furgonetes

        




class Estat():
    """
    Classe que representa un estat
    """
    def __init__(self, parametres: Parametres,  ruta: List[Furgonetes]):
        self.params = parametres
        self.ruta =  ruta
    def h(self):
        return sum(furgo.cost_gasolina() for furgo in self.ruta)
    
    
    def __repr__(self):
        return f"Ruta: {self.ruta}"
        #return f"Parametres: n_estacions={self.params.n_estacions}, n_bicis={self.params.n_bicis}, llavor={self.params.llavor}, n_furgonetes={self.params.n_furgonetes}"   
        
def genera_estat_inicial(params: Parametres, estacions: Estaciones) -> Estat:
    iterador_est = iterar_estacions(estacions)
    ruta = []
    while True:
        try:
            est_carrega = next(iterador_est)
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

    return Estat(params, ruta) #Instància d'Estat




     


def iterar_estacions(estacions: Estaciones) ->Generator[Estacion, None, None]:
    return (estacio for estacio in estacions.lista_estaciones)


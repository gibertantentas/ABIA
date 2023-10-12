from estacions import Estacio

class Furgonetes(object):

    def __init__(self, est_carrega: Estacio, carrega: int, est_descarrega1: Estacio, descarrega1: int , est_descarrega2: Estacio = None , descarrega2: int = 0):
        self.estacio_carrega = est_carrega
        self.estacio_descarrega1 = est_descarrega1
        self.estacio_descarrega2 = est_descarrega2
        self.carrega: int = carrega
        self.descarrega1: int = descarrega1
        self.descarrega2: int = descarrega2
        #assert (self.carrega == self.descarrega1 + self.descarrega2)

    def distancia_recorregut(self):        
        ################
        '''NO CAL''' #Això sí, podríem fer un mètode amb aquesta mateixa utilitat aquest mètode perquè fes el càlcul del recorregut de la furgo i d'aquesta manera 
                     #l'heurística de la classe estat simplement seria retornar el valor resultant d'aquest mètode
        ################
        dist = self.estacio_carrega.distancia_estacions(self.estacio_descarrega1)
        if self.estacio_descarrega2 != None:
            dist = dist + self.estacio_descarrega1.distancia_estacions(self.estacio_descarrega2) \
                + self.estacio_descarrega2.distancia_estacions(self.estacio_carrega) 
        else:
            dist = dist + self.estacio_descarrega1.distancia_estacions(self.estacio_carrega)
        return dist
        
        
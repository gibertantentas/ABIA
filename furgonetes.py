from abia_bicing import Estacion


def distancia_estacions(est1: Estacion, est2: Estacion) -> int:
    distancia = abs(est1.coordX - est2.coordX) + abs(est1.coordY - est2.coordY)
    return distancia
class Furgonetes(object):

    def __init__(self, est_carrega: Estacion, carrega: int, est_descarrega1: Estacion, descarrega1: int , est_descarrega2: Estacion = None , descarrega2: int = 0):
        self.estacio_carrega = est_carrega
        self.estacio_descarrega1 = est_descarrega1
        self.estacio_descarrega2 = est_descarrega2
        self.carrega: int = carrega
        self.descarrega1: int = descarrega1
        self.descarrega2: int = descarrega2
        #assert (self.carrega == self.descarrega1 + self.descarrega2)

    def cost_gasolina(self):        
        ################
        '''NO CAL''' #Això sí, podríem fer un mètode amb aquesta mateixa utilitat aquest mètode perquè fes el càlcul del recorregut de la furgo i d'aquesta manera 
                     #l'heurística de la classe estat simplement seria retornar el valor resultant d'aquest mètode
        ################
        cost_1 = ((self.carrega + 9) // 10) * distancia_estacions(self.estacio_carrega, self.estacio_descarrega1)

        if self.estacio_descarrega2 is not None:
            cost_2 = (( (self.carrega - self.descarrega1) + 9) // 10) * distancia_estacions(self.estacio_descarrega1, self.estacio_descarrega2)
            cost_3 = (( (self.carrega - self.descarrega1 - self.descarrega2) + 9) // 10) * distancia_estacions(self.estacio_descarrega2, self.estacio_carrega)
            cost_total += cost_1 + cost_2 + cost_3
        else:
            cost_3 = (( (self.carrega - self.descarrega1 - self.descarrega2) + 9) // 10) * distancia_estacions(self.estacio_descarrega2, self.estacio_carrega)
            cost_total = cost_1 + cost_3
        return cost_total
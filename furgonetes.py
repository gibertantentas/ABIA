from abia_bicing import Estacion


def distancia_estacions(est1: Estacion, est2: Estacion) -> int:
    distancia = abs(est1.coordX - est2.coordX) + abs(est1.coordY - est2.coordY)
    return distancia
class Furgonetes(object):

    def __init__(self, est_carrega: Estacion, carrega: int, est_descarrega1: Estacion = None, descarrega1: int = 0 , est_descarrega2: Estacion = None , descarrega2: int = 0):
        self.estacio_carrega = est_carrega
        self.estacio_descarrega1 = est_descarrega1
        self.estacio_descarrega2 = est_descarrega2
        self.carrega: int = carrega
        self.descarrega1: int = descarrega1
        self.descarrega2: int = descarrega2
        if est_descarrega1 is None:
            assert (descarrega1 == 0)
        if est_descarrega2 is None:
            assert (descarrega2 == 0)
    
    def cost_gasolina(self):
        cost_total = 0
        carrega = self.carrega
        descarrega1 = self.descarrega1
        descarrega2 = self.descarrega2
        estacio_carrega = self.estacio_carrega
        estacio_descarrega1 = self.estacio_descarrega1
        estacio_descarrega2 = self.estacio_descarrega2

        if estacio_descarrega1 is not None:
            cost_1 = ((carrega + 9) // 10) * (distancia_estacions(estacio_carrega, estacio_descarrega1) / 1000)
            cost_total += cost_1
            
            if estacio_descarrega2 is not None:
                cost_2 = (((carrega - descarrega1) + 9) // 10) * (distancia_estacions(estacio_descarrega1, estacio_descarrega2) / 1000)
                cost_total += cost_2
                
        return cost_total

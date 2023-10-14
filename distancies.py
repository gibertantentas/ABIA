'''from abia_bicing import Estacion, Estaciones
class Distancies():
    def __init__(self, estacions: Estaciones):
        self.num_estacions = len(estacions.lista_estaciones)
        self.distancies = [[0] * self.num_estacions for _ in range(self.num_estacions)]
        for i in range(self.num_estacions):
            for j in range(i, self.num_estacions):
                est1 = self.llista_estacions[i]
                est2 = self.llista_estacions[j]
                dist = abs(est1.coordX - est2.coordX) + abs(est1.coordY - est2.coordY)
                #dist = est1.distancia_estacions(est2)
                self.distancies[est1.id][est2.id] = dist
                self.distancies[est2.id][est1.id] = dist
    def distancia(self, est1: Estacion, est2: Estacion):
        return self.distancies[est1.id][est2.id]'''
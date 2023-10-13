def distancia_estacions(self, estacio: 'Estacio'):
        return abs(self.coordX - estacio.coordX) + abs(self.coordY - estacio.coordY)
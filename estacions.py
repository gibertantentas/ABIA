import random
from typing import List, Set, Generator
from parametres import Parametres

class Estacio(object):
    """
    Clase que representa una estación de Bicing
    """

    def __init__(self, x: int, y: int):
        """
        * coordX y coordY son atributos públicos que representan las
          coordenadas X e Y de la estación Bicing en metros
          bicicletas para la siguiente hora
        * num_bicicletas_next es un atributo público que guarda
          el número de bicicletas que habrá en la siguiente hora
          sin contar con los traslados
        * num_bicicletas_no_usadas es un atributo público que guarda
          el número de bicicletas que no se moverán en la hora actual
        """
        self.id: int
        self.coordX: int = x * 100
        self.coordY: int = y * 100
        self.num_bicicletes_no_usades: int
        self.num_bicicletes_next: int
        self.demanda_next: int 
        self.diferencia: int
        self.excedent: int
        
    def distancia_estacions(self, estacio: 'Estacio'):
        return abs(self.coordX - estacio.coordX) + abs(self.coordY - estacio.coordY)


        
    def __repr__(self):
        return f"Estación {self.id}: {self.coordX}, {self.coordY}, {self.num_bicicletes_no_usades}, {self.num_bicicletes_next}, {self.demanda_next}, {self.diferencia}, {self.excedent}"




class Estacions(object):
    """
    Clase que representa una lista ordenada de estaciones (instancias de Estacion)
    """

    def __init__(self, num_estacions: int, num_bicicletes: int, llavor: int):
        """
        Constructora de Estaciones
        * num_estaciones: número de estaciones a generar
        * num_bicicletas: número de bicicletas a repartir
        * semilla: semilla del generador de números aleatorios
        """
        self.num_bicicletes: int = num_bicicletes
        self.rng: random.Random = random.Random(llavor)
        meitat_estacions: int = int(num_estacions / 2)
        self.llista_estacions: list[Estacio] = []

        for _ in range(meitat_estacions):
            est = Estacio(self.rng.randint(0, 99), self.rng.randint(0, 99))
            self.llista_estacions.append(est)

        for _ in range(meitat_estacions, num_estacions):
            est = Estacio(self.rng.randint(0, 49) + 25, self.rng.randint(0, 49) + 25)
            self.llista_estacions.append(est)

        self.__genera_estado_actual()
        self.__genera_estado_movimientos()
        self.__genera_proxima_demanda()

    def __genera_estado_actual(self):
        for est in self.llista_estacions:
            est.num_bicicletes_no_usades = 0

        i = self.num_bicicletes
        while i > 0:
            asignadas = self.rng.randint(0, 1)
            id_est = self.rng.randint(0, len(self.llista_estacions) - 1)
            self.llista_estacions[id_est].num_bicicletes_no_usades = \
                self.llista_estacions[id_est].num_bicicletes_no_usades + asignadas
            i = i - asignadas

    def __genera_estado_movimientos(self):
        num_movimientos: int = int(float(self.num_bicicletes) * 0.8)

        for est in self.llista_estacions:
            est.num_bicicletes_next = 0

        for id_est in range(num_movimientos):
            var3 = self.rng.randint(0, len(self.llista_estacions) - 1)
            var2 = self.rng.randint(0, len(self.llista_estacions) - 1)
            if self.llista_estacions[var3].num_bicicletes_no_usades > 0:
                self.llista_estacions[var3].num_bicicletes_no_usades = \
                    self.llista_estacions[var3].num_bicicletes_no_usades - 1
                self.llista_estacions[var2].num_bicicletes_next = \
                    self.llista_estacions[var2].num_bicicletes_next + 1

        for est in self.llista_estacions:
            est.num_bicicletes_next = est.num_bicicletes_next + est.num_bicicletes_no_usades

    def __genera_proxima_demanda(self):
        media_bicicletas: int = int(self.num_bicicletes / len(self.llista_estacions))

        for est in self.llista_estacions:
            if self.rng.random() > 0.5:
                factor = 1
            else:
                factor = -1
            est.demanda = media_bicicletas + factor * self.rng.randint(0, int(float(media_bicicletas) * 0.5) - 1)


def genera_estacions(params: Parametres) -> Estacions:
    return Estacions(params.n_estacions, params.n_bicis, params.llavor)

def calcul_demanda(estacions: Estacions):
        
    acum_bicicletes = 0
    acum_demanda = 0
    acum_disponibles = 0
    acum_necessaries = 0
    
    
    for id_estacio, estacio in enumerate(estacions.llista_estacions):
        num_bicicletes_no_usades = estacio.num_bicicletes_no_usades
        num_bicicletes_next = estacio.num_bicicletes_next
        demanda = estacio.demanda
        acum_bicicletes = acum_bicicletes + num_bicicletes_next
        acum_demanda = acum_demanda + demanda
        diferencia = num_bicicletes_next - demanda
        if diferencia > 0:
            if diferencia > num_bicicletes_no_usades:
                excedent = num_bicicletes_no_usades
            else:
                excedent = diferencia
            acum_disponibles = acum_disponibles + excedent
        else:
            excedent = 0
            acum_necessaries = acum_necessaries - diferencia

        estacio.id = id_estacio
        estacio.num_bicicletes_no_usades = num_bicicletes_no_usades
        estacio.num_bicicletes_next = num_bicicletes_next
        estacio.demanda_next = demanda
        estacio.diferencia = diferencia
        estacio.excedent = excedent
            
    #print("Bicis= %3d Demanda= %3d Disponibles= %3d Necesitan= %3d" %
    #      (self.acum_bicicletas, self.acum_demanda, self.acum_disponibles, self.acum_necesarias))

def iterar_estacions(estacions: Estacions) ->Generator[Estacio, None, None]:
    return (estacio for estacio in estacions.llista_estacions)



'''
if __name__ == '__main__':
    """
    Prueba de funcionamiento:
    Creación de una instancia de estaciones y escritura a consola de:
    * Información de cada estacion
    * Datos por estacion de bicicletas presentes, demandadas, diferencia y excedente
    * Datos globales de bicicletas demandadas, disponibles para mover
      y bicicletas que es necesario mover
    """
    estaciones = Estaciones(25, 1250, 42)
    acum_bicicletas = 0
    acum_demanda = 0
    acum_disponibles = 0
    acum_necesarias = 0
    ###Modificat
    llista_estacions = []
    ###
    
    
    print("Sta Cur Dem Dif Exc")
    for id_estacion, estacion in enumerate(estaciones.lista_estaciones):
        num_bicicletas_no_usadas = estacion.num_bicicletas_no_usadas
        num_bicicletas_next = estacion.num_bicicletas_next
        demanda = estacion.demanda
        acum_bicicletas = acum_bicicletas + num_bicicletas_next
        acum_demanda = acum_demanda + demanda
        diferencia = num_bicicletas_next - demanda
        if diferencia > 0:
            if diferencia > num_bicicletas_no_usadas:
                excedente = num_bicicletas_no_usadas
            else:
                excedente = diferencia
            acum_disponibles = acum_disponibles + excedente
        else:
            excedente = 0
            acum_necesarias = acum_necesarias - diferencia
        llista_estacions.append(Estacio(id_estacion, estacion.coordX, estacion.coordY, num_bicicletas_no_usadas, num_bicicletas_next, demanda, diferencia, excedente))
        print("est %2s = %2d %2d" % (id_estacion, estacion.coordX, estacion.coordY))
        print("%3d %3d %3d %3d %3d" % (num_bicicletas_no_usadas, num_bicicletas_next, demanda, diferencia, excedente))

    print("Bicis= %3d Demanda= %3d Disponibles= %3d Necesitan= %3d" %
          (acum_bicicletas, acum_demanda, acum_disponibles, acum_necesarias))
    ###
    
    
  
    

'''
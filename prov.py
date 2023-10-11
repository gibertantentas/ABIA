
'''

Stone = namedtuple('Stone', ('x', 'y', 'color'))

furgo1 = Stone(2, 3, 'red')
Moure_bici = namedtuple('Moure_bici', ('x', 'y', 'quantitat'))
moviment = Moure_bici(2, 3, -5)


Estacio = namedtuple('Estacio', 'Id', 'X', 'Y')
Estacio2 = namedtuple('Estacio2', 'Id', 'X', 'Y', 'no_usades', 'num_next', 'demanda', 'diferencia', 'excedent')
est1 = Estacio2(1, 3, 4, 0, 0, 0, 0, 0)
#Podem fer que l'id sigui el nom de la namedtuple directament
estacions = []
estacions.append(est1)
estacions.append(Estacio2(5, 2, 7, 0, 0, 0, 0, 0))


#Podem fer servir un diccionari o bé una llista de llistes

#Diccionari
furgonetes = {
    'origen' : (2,3),
    1: {
        'recollida': (estacions[0], +5),
        'desti': (estacions[0], -5),
        'codigo_postal': '28001'

}}


#Llista de llistes
furgonetes = [(2,3), \
              [(estacions[0], +5),(estacions[0], -5)], \
              [], \
              []]
'''

from collections import namedtuple
Estacio = namedtuple('Estacio', ['Id', 'X', 'Y', 'no_usades', 'num_next', 'demanda', 'diferencia', 'excedent'])
est1 = Estacio(1, 3, 4, 0, 0, 0, 0, 0)

'''
class Carrega():
    def __init__(self, estacio: namedtuple, quantitat: int):
        self.estacio = estacio
        self.quantitat = quantitat
        print(self.estacio)
        print(self.estacio.num_next)
        self.estacio._replace(num_next = self.estacio.num_next - self.quantitat)  
        print(self.estacio.num_next)
        print(self.estacio)
        #Fer que resti el nombre de bicis carregades a l'estacio

        #(int,int,int,int,int,int,int,int)
        
        
moviment1 = Carrega(est1, 5)
'''
from collections import namedtuple

Estacio = namedtuple('Estacio', ['Id', 'X', 'Y'])

estaciones = {}

# Ejemplo de cómo agregar una estación al diccionario
estacion1 = Estacio(Id=1, X=10, Y=20)
estaciones[estacion1.Id] = {
    'no_usades': 0,
    'num_next': 0,
    'demanda': 0,
    'diferencia': 0,
    'excedent': 0
}


estacion2 = Estacio(Id=2, X=15, Y=25)
estaciones[estacion2.Id] = {
    'no_usades': 0,
    'num_next': 0,
    'demanda': 0,
    'diferencia': 0,
    'excedent': 0
}

print(estaciones)


class Furgonetes():
    def __init__(self, est_carrega: Estacio, num_carrega: int, est_descarrega1: Estacio, num_decarrega1: int , est_descarrega2: Estacio = None , num_descarrega2: int = 0):
        pass

    def carrega(self, Estacion, num: int):
        pass
    def descarrega(self, Estacion, num: int):
        pass
    

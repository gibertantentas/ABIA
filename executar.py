from abia_bicing import Estacion, Estaciones
from parametres import Parametres
from estat import genera_estat_inicial, genera_estat_inicial2
from aima.search import hill_climbing
from Problema import ProblemaBICING



params = Parametres(25, 1250, 42, 5, 30)
estacions = Estaciones(25, 1250, 42)


estat_inicial = genera_estat_inicial2(params, estacions) #Necessari executar per crear l'estat inicial



print('Heurística estat inicial: ',estat_inicial.h())

n = hill_climbing(ProblemaBICING(estat_inicial))
print('\nRUTA:')
for i in range(len(n.ruta)):
    print(f'\n\nFurgoneta {i}: \n')
    print(f"Carrega: {n.ruta[i].carrega} bicicletes a l'estació {n.ruta[i].estacio_carrega.coordX, n.ruta[i].estacio_carrega.coordY} \
        \nDescarrega {n.ruta[i].descarrega1} bicicletes a l'estació {n.ruta[i].estacio_descarrega1.coordX, n.ruta[i].estacio_descarrega1.coordY}\
        \nDescarrega 2: {n.ruta[i].descarrega2} bicicletes a l'estació {n.ruta[i].estacio_descarrega2.coordX, n.ruta[i].estacio_descarrega2.coordY}")
#print ('Estat final: ', n ) # Estat final

print ('\nHeurística estat inicial', n.h() ) # Valor de l’estat final


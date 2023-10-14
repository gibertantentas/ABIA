from abia_bicing import Estacion, Estaciones
from parametres import Parametres
from estat import genera_estat_inicial
from furgonetes import Furgonetes
#from distancies import Distancies


params = Parametres(25, 1250, 42, 10, 30, 5)
estacions = Estaciones(25, 1250, 42)
#distancies = Distancies(estacions)

estat_inicial = genera_estat_inicial(params, estacions) #Necessari executar per crear l'estat inicial
print(estat_inicial.h())


#print(estat_inicial.h())




'''

n = hill_climbing ( BinPackingProblem ( initial_state ) )
print ( n ) # Estat final
print ( n . heuristic () ) # Valor de l’estat final




'''


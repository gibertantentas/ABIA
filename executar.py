from abia_bicing import Estacion, Estaciones
from parametres import Parametres
from estat import genera_estat_inicial
from furgonetes import Furgonetes
#from aima.search import hill_climbing
#from Problema import ProblemaBICING



params = Parametres(25, 1250, 42, 10, 30, 5)
estacions = Estaciones(25, 1250, 42)


estat_inicial = genera_estat_inicial(params, estacions) #Necessari executar per crear l'estat inicial
gen = estat_inicial.genera_accions()
for i in gen:
    print(i)
#print(estat_inicial.h()) ###Mostra el valor de l'heurística


#print(estat_inicial.h())



#n = hill_climbing ( ProblemaBICING ( estat_inicial ) )
#print ( n ) # Estat final
#print ( n.h() ) # Valor de l’estat final




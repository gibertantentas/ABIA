from abia_bicing import Estacion, Estaciones
from parametres import Parametres
from estat import genera_estat_inicial, genera_estat_inicial2
from furgonetes import Furgonetes
#from aima.search import hill_climbing
#from Problema import ProblemaBICING



params = Parametres(25, 1250, 42, 10, 30)
estacions = Estaciones(25, 1250, 42)


estat_inicial = genera_estat_inicial(params, estacions) #Necessari executar per crear l'estat inicial

estat_inicial2 = genera_estat_inicial2(params, estacions) #Necessari executar per crear l'estat inicial


gen = estat_inicial.genera_accions()
gen2 = estat_inicial2.genera_accions()
compt1 = 0
for i in gen:
    compt1 +=1 

compt2 = 0
for i in gen2:
    compt2 +=1 



print('Possibles accions: ', '\n Bo:',compt2, '\n Dolent:',compt1)
print('Heurística 1: ', '\n Bo:',estat_inicial2.h(), '\n Dolent:',estat_inicial.h())
print('Heurística 2: ', '\n Bo:',estat_inicial2.h2(), '\n Dolent:',estat_inicial.h2())

#print(estat_inicial.h()) ###Mostra el valor de l'heurística



#print(estat_inicial.h())



#n = hill_climbing ( ProblemaBICING ( estat_inicial ) )
#print ( n ) # Estat final
#print ( n.h() ) # Valor de l’estat final




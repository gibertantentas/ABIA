from parametres import Parametres
from estacions import Estacions, genera_estacions, iterar_estacions, calcul_demanda
from estat import genera_estat_inicial
from furgonetes import Furgonetes

params = Parametres(25, 1250, 42, 10, 30)
estacions = genera_estacions(params)

calcul_demanda(estacions) #És necessari executar-lo per calcular els ID i els excedents, etc.

estat_inicial = genera_estat_inicial(estacions, params)

print(estat_inicial.h())
#print(estacions.distancies)

s = estacions.distancia_entre_estacions()
j = 0
for i in s:
    print(i ==  estacions.llista_estacions[j].distancies)
    print(i, '\n ',estacions.llista_estacions[j].distancies)
    
    j += 1
#print('\n', len(s))
'''
for furgo in estat_inicial.ruta:
    print(furgo.estacio_carrega.id, '\n')
'''

    

###Prova per saber si funciona el mètode per calcular la distància entre estacions: ----- print(estacions.llista_estacions[0].distancia_estacions(estacions.llista_estacions[1]))


'''
n = hill_climbing ( BinPackingProblem ( initial_state ) )
print ( n ) # Estat final
print ( n . heuristic () ) # Valor de l’estat final
'''
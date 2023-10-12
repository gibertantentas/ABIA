from parametres import Parametres
from estacions import Estacions, genera_estacions, iterar_estacions, calcul_demanda
from estat import genera_estat_inicial
from furgonetes import Furgonetes

params = Parametres(25, 1250, 42, 10, 30)
estacions = genera_estacions(params)
acum_inicial = calcul_demanda(estacions) #Necessari executar per calcular els ID i els excedents, etc.
                                        # acum_inicial contindra la suma de tots els excedents acum_bicicletes, acum_demanda, acum_disponibles, acum_necessaries
estat_inicial = genera_estat_inicial(estacions, params) #Necessari executar per crear l'estat inicial
estacions.distancia_entre_estacions() #Necessari executar per calcular les distàncies entre totes les estacions


print(estat_inicial.h())



'''
n = hill_climbing ( BinPackingProblem ( initial_state ) )
print ( n ) # Estat final
print ( n . heuristic () ) # Valor de l’estat final
'''
from abia_bicing import Estacion, Estaciones
from parametres import Parametres
from estat import genera_estat_inicial, genera_estat_inicial2, genera_estat_inicial0
from aima.search import hill_climbing
from Problema import ProblemaBICING
import random
import time



#random.randint(2,5000)
params = Parametres(25, 1250, 42 , 5, 30)
estacions = Estaciones(params.n_estacions, params.n_bicis, params.llavor)
estat_inicial = genera_estat_inicial2(params, estacions) #Necessari executar per crear l'estat inicial
h_inicial = estat_inicial.h()
gen = estat_inicial.genera_accions()
time_start = time.time()
n = hill_climbing(ProblemaBICING(estat_inicial))
dist_total = sum(furgo.distancia_recorregut() for furgo in n.ruta)
time_end = time.time()

total_time = time_end - time_start

print(f'\nDistància total recorreguda per les furgonetes: {dist_total /1000 } km')
print(f"Guanys de l'estat inicial: {h_inicial} euros")
print(f"Guanys de l'estat final: {n.h()} euros")
print(f"Temps de cerca: {round(total_time * 1000, 2)} ms")



'''

for i in range(n):
    params = Parametres(25, 1250, 42, 5, 30)
    estacions = Estaciones(params.n_estacions, params.n_bicis, params.llavor)

    estat_inicial = genera_estat_inicial2(params, estacions) #Necessari executar per crear l'estat inicial

    n = hill_climbing(ProblemaBICING(estat_inicial))

    print(n.h())'''
    
    
  
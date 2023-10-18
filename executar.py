from abia_bicing import Estacion, Estaciones
from parametres import Parametres
from estat import genera_estat_inicial1, genera_estat_inicial2, genera_estat_inicial0
from aima.search import hill_climbing
from Problema import ProblemaBICING
import random
import time



'''#random.randint(2,5000)
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
print(f"Temps de cerca: {round(total_time * 1000, 2)} ms")'''





estat_inici = input('Quin estat inicial vols utilitzar? Introdueix 1 o 2')
params = Parametres(25, 1250, 42, 5, 30)
estacions = Estaciones(params.n_estacions, params.n_bicis, params.llavor)
time_start = time.time()
if estat_inici == '0':
    estat_inicial1 = genera_estat_inicial0(params, estacions) #Necessari executar per crear l'estat inicial
    h_inicial1 = estat_inicial1.h()
    n1 = hill_climbing(ProblemaBICING(estat_inicial1))
    print(f"\nEstat 1: \n  Inicial: {h_inicial1} euros Final: {n1.h()} euros")
    
    
elif estat_inici == '1':
    estat_inicial2 = genera_estat_inicial1(params, estacions) #Necessari executar per crear l'estat inicial
    h_inicial2 = estat_inicial2.h()
    n2 = hill_climbing(ProblemaBICING(estat_inicial2))
    print(f"\nEstat 2: \n  Inicial: {h_inicial2} euros Final: {n2.h()} euros")
    
elif estat_inici == '2':
    estat_inicial3 = genera_estat_inicial2(params, estacions) #Necessari executar per crear l'estat inicial
    h_inicial3 = estat_inicial3.h()
    n3 = hill_climbing(ProblemaBICING(estat_inicial3))
    print(f"\nEstat 3: \n  Inicial: {h_inicial3} euros Final: {n3.h()} euros")
time_end = time.time()
total_time = time_end - time_start
print('TEMPS:',total_time)
        
    
from abia_bicing import Estacion, Estaciones
from parametres import Parametres
from estat import genera_estat_inicial1, genera_estat_inicial2, genera_estat_inicial0
from aima.search import hill_climbing, simulated_annealing
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





params = Parametres(25, 1250, 42, 5, 30)
estacions = Estaciones(params.n_estacions, params.n_bicis, params.llavor)

'''if estat_inici == '0':
    estat_inicial1 = genera_estat_inicial0(params, estacions) #Necessari executar per crear l'estat inicial
    h_inicial1 = estat_inicial1.h()
    n1 = hill_climbing(ProblemaBICING(estat_inicial1))
    print(f"\nEstat 1: \n  Inicial: {h_inicial1} euros Final: {n1.h()} euros")'''
    
time_start1 = time.time()
estat_inicial1 = genera_estat_inicial1(params, estacions) #Necessari executar per crear l'estat inicial
h_inicial2 = estat_inicial1.h()
n2 = hill_climbing(ProblemaBICING(estat_inicial1))
time_end1 = time.time()
total_time1 = time_end1 - time_start1
print(f"\nEstat 2: \n  Inicial: {h_inicial2} euros Final: {n2.h()} euros")
print('TEMPS:',total_time1)

print(n2.ruta)
'''for furgo in n2.ruta:
    try:
        print('\n\nFurgo: ',furgo.estacio_carrega.coordX, furgo.estacio_carrega.coordY, '\n', furgo.estacio_descarrega1.coordX, furgo.estacio_descarrega1.coordY, '\nDescarrega2', furgo.estacio_descarrega2.coordX, furgo.estacio_descarrega2.coordY)
    except:
        try:
            print('\n\nFurgo: ',furgo.estacio_carrega.coordX, furgo.estacio_carrega.coordY, '\n', furgo.estacio_descarrega1.coordX, furgo.estacio_descarrega1.coordY)
        except:
            pass'''
        
            
'''time_start2 = time.time()
estat_inicial2 = genera_estat_inicial2(params, estacions) #Necessari executar per crear l'estat inicial
h_inicial3 = estat_inicial2.h()
n3 = hill_climbing(ProblemaBICING(estat_inicial2))
time_end2 = time.time()
total_time2 = time_end2 - time_start2
print(f"\nEstat 3: \n  Inicial: {h_inicial3} euros Final: {n3.h()} euros")
print('TEMPS:',total_time2)'''
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        
'''import matplotlib.pyplot as plt

# Supongamos que tienes una instancia de la clase Estaciones llamada 'estacions'

# Extrae las coordenadas de las estaciones
coordX = [estacion.coordX for estacion in estacions.lista_estaciones]
coordY = [estacion.coordY for estacion in estacions.lista_estaciones]

# Crea un gráfico de dispersión para mostrar las estaciones en el mapa
plt.figure(figsize=(8, 8))  # Ajusta el tamaño del gráfico según tus preferencias
plt.scatter(coordX, coordY, label="Estaciones", color="blue")

# Personaliza el gráfico (etiquetas, título, ejes, etc.)
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Mapa de Estaciones")

# Agrega etiquetas a las estaciones
for i, estacion in enumerate(estacions.lista_estaciones):
    plt.text(coordX[i], coordY[i], f"Estacion {i+1}", fontsize=8, ha='center', va='bottom')

# Muestra el gráfico
plt.legend()
plt.grid()
plt.show()


#########


import matplotlib.pyplot as plt

# Supongamos que tienes una instancia de la clase Estaciones llamada 'estacions'
# y una instancia de la clase Estat llamada 'n2'

# Extrae las coordenadas de las estaciones
coordX = [estacion.coordX for estacion in estacions.lista_estaciones]
coordY = [estacion.coordY for estacion in estacions.lista_estaciones]

# Crea un gráfico de dispersión para mostrar las estaciones en el mapa
plt.figure(figsize=(8, 8))  # Ajusta el tamaño del gráfico según tus preferencias
plt.scatter(coordX, coordY, label="Estaciones", color="blue")

# Personaliza el gráfico (etiquetas, título, ejes, etc.)
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Mapa de Estaciones")

# Agrega etiquetas a las estaciones
for i, estacion in enumerate(estacions.lista_estaciones):
    plt.text(coordX[i], coordY[i], f"Estacion {i+1}", fontsize=8, ha='center', va='bottom')

# Recorre las instancias de Furgonetes en n2.ruta
for furgoneta in n2.ruta:
    if furgoneta.estacio_carrega is not None and furgoneta.estacio_descarrega1 is not None:
        # Trazar una línea desde estacio_carrega a estacio_descarrega1
        x1, y1 = furgoneta.estacio_carrega.coordX, furgoneta.estacio_carrega.coordY
        x2, y2 = furgoneta.estacio_descarrega1.coordX, furgoneta.estacio_descarrega1.coordY
        plt.plot([x1, x2], [y1, y2], color="red", linewidth=1)

    if furgoneta.estacio_descarrega1 is not None and furgoneta.estacio_descarrega2 is not None:
        # Trazar una línea desde estacio_descarrega1 a estacio_descarrega2
        x1, y1 = furgoneta.estacio_descarrega1.coordX, furgoneta.estacio_descarrega1.coordY
        x2, y2 = furgoneta.estacio_descarrega2.coordX, furgoneta.estacio_descarrega2.coordY
        plt.plot([x1, x2], [y1, y2], color="green", linewidth=1)

# Muestra el gráfico
plt.legend()
plt.grid()
plt.show()
'''
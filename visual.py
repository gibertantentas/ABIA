from furgonetes import Furgonetes
from typing import List, Set, Generator
def visualitzar(estacions, n2):
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

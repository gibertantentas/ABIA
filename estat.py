from estacions import Estacio, Estacions, iterar_estacions
from typing import List, Set, Generator
from parametres import Parametres
from operadors import Carrega, Descarrega
from furgonetes import Furgonetes
        

    
class Estat():
    """
    Classe que representa un estat
    """

    def __init__(self, parametres: Parametres,  ruta: List[Furgonetes]):
        #self.num_estacions = len(estacions.lista_estaciones)
        self.params = parametres
        self.ruta =  ruta #Proposo que la ruta sigui una llista de llistes, on cada subllista representi la ruta d'una furgoneta.
        #          D'aquesta manera no ens cal crear una classe de Furgonetes. Simplement en podem anar afegint segons convingui.
        #          Dins de cada subllista hi hauria una instancia de Carrega(Estacio, quantitat) i una o dues instancies
        #           de Descarrega(Estacio, quantitat).
        
    
       
    
    def __repr__(self):
        return f"Ruta: {self.ruta}"
        #return f"Parametres: n_estacions={self.params.n_estacions}, n_bicis={self.params.n_bicis}, llavor={self.params.llavor}, n_furgonetes={self.params.n_furgonetes}"   
    def h(self):
        cost_total = 0
        for furgo in self.ruta:
            cost_km_1 = ((furgo.carrega + 9) // 10)
            km_1 = furgo.estacio_carrega.distancia_estacions(furgo.estacio_descarrega1)
            cost_1 = km_1 * cost_km_1
            if furgo.estacio_descarrega2 is not None:
                cost_km_2 = (( (furgo.carrega - furgo.descarrega1) + 9) // 10)
                km_2 = furgo.estacio_descarrega1.distancia_estacions(furgo.estacio_descarrega2)
                cost_2 = km_2 * cost_km_2
                cost_km_3 = (( (furgo.carrega - furgo.descarrega1 - furgo.descarrega2) + 9) // 10)
                km_3 = furgo.estacio_descarrega2.distancia_estacions(furgo.estacio_carrega)
                cost_3 = km_3 * cost_km_3
                cost_total += cost_1 + cost_2 + cost_3
            else:
                cost_km_3 = (( (furgo.carrega - furgo.descarrega1 - furgo.descarrega2) + 9) // 10)
                km_3 = furgo.estacio_descarrega2.distancia_estacions(furgo.estacio_carrega)
                cost_3 = km_3 * cost_km_3
                cost_total += cost_1 + cost_3
        return cost_total
    '''
    def moure_bici(self, estacio: Estacio, quantitat: int):
        estacio.num_bicicletes_next = estacio.num_bicicletes_next - quantitat
    '''



        
def genera_estat_inicial(estacions: Estacions, params: Parametres) -> Estat:
    print('GENERANT ESTAT INICIAL...')
    iterador_est = iterar_estacions(estacions)
    ruta = []
    while True:
        try:
            est_carrega = next(iterador_est)
            est_descarrega1 = next(iterador_est)
            if est_carrega.num_bicicletes_no_usades < 30:
                bicis_no_usades = est_carrega.num_bicicletes_no_usades
            else:
                bicis_no_usades = 30
            carrega = bicis_no_usades
            ###carrega = Carrega(est_carrega, bicis_no_usades)

            try:
                # Si excedent es par, hay suficiente para dos descargas
                est_descarrega2 = next(iterador_est)
                descarrega1 = bicis_no_usades // 2
                descarrega2 = bicis_no_usades - (bicis_no_usades // 2) 
                ###ruta.append([carrega, descarga1, descarga2])
                ruta.append(Furgonetes(est_carrega, carrega, est_descarrega1, descarrega1, est_descarrega2, descarrega2))
            except:
                # Si excedent es impar, solo hay suficiente para una descarga
                descarrega1 = bicis_no_usades
                ###ruta.append([carrega, descarga1])
                ruta.append(Furgonetes(est_carrega, carrega, est_descarrega1, descarrega1))

        except StopIteration:
            # El iterador se ha agotado, salir del bucle
            break

    return Estat(params, ruta) #ruta

#est.num_bicicletes_next = est.num_bicicletes_next + est.num_bicicletes_no_usades
    
'''
for est in estacions
    ruta_furgo.append()
'''



'''
llista1 = []
llista2 = []
print(prova)

def generate_initial_state(params: ProblemParameters) -> StateRepresentation:
    assert (params.p_max <= params.c_max)
    v_c = [{p_i} for p_i in range(params.p_max)]
    return StateRepresentation(params, v_c)

'''







'''

for est in prova.estacions.llista_estacions:
    llista1.append([est.coordX, est.coordY, est.num_bicicletes_no_usades ,est.num_bicicletes_next, est.demanda_next, est.diferencia, est.excedent])
prova.calcul_demanda()


for est in prova.estacions.llista_estacions:
    llista2.append([est.coordX, est.coordY, est.num_bicicletes_no_usades ,est.num_bicicletes_next, est.demanda_next, est.diferencia, est.excedent])

for i in range(len(llista1)):
    print(llista1[i], '\n' ,llista2[i])
    if llista1[i] == llista2[i]:
        print('TRUE')
'''
    
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
    
    
    def moure_bici(self, estacio: Estacio, quantitat: int):
        estacio.num_bicicletes_next = estacio.num_bicicletes_next - quantitat

    def genera_estat_inicial(estacions: Estacions, params: Parametres) -> Estat:
        print('GENERANT ESTAT INICIAL...')
        iterador_est = iterar_estacions(estacions)
        ruta = []


        
        '''
        mida = len(estacions.llista_estacions)
        particio1 = estacions.llista_estacions[0:mida//3]
        particio2 = estacions.llista_estacions[mida//3:(2*(mida//3))]
        particio3 = estacions.llista_estacions[(2*(mida//3)):mida]
        
        for i in particio1:
            est_carrega = i
        
        '''
        
            
        
        
        
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
w
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
        
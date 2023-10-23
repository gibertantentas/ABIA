from abia_bicing import Estacion


def distancia_estacions(est1: Estacion, est2: Estacion) -> int:
    distancia = abs(est1.coordX - est2.coordX) + abs(est1.coordY - est2.coordY)
    return distancia
class Furgonetes(object):

    def __init__(self, est_carrega: Estacion = None, carrega: int = 0, est_descarrega1: Estacion = None, descarrega1: int = 0 , est_descarrega2: Estacion = None , descarrega2: int = 0):
        self.estacio_carrega = est_carrega
        self.estacio_descarrega1 = est_descarrega1
        self.estacio_descarrega2 = est_descarrega2
        self.carrega: int = carrega
        self.descarrega1: int = descarrega1
        self.descarrega2: int = descarrega2
        #assert (self.carrega == self.descarrega1 + self.descarrega2)
        '''if est_descarrega1 is None:
            assert (descarrega1 == 0)
        if est_descarrega2 is None:
            assert (descarrega2 == 0)'''
    
    def cost_gasolina(self):
        cost_total = 0
        carrega = self.carrega
        descarrega1 = self.descarrega1
        descarrega2 = self.descarrega2
        estacio_carrega = self.estacio_carrega
        estacio_descarrega1 = self.estacio_descarrega1
        estacio_descarrega2 = self.estacio_descarrega2
        
        if estacio_descarrega1 is not None and estacio_carrega is not None and descarrega1 != 0:
            cost_1 = ((carrega + 9) // 10) * (distancia_estacions(estacio_carrega, estacio_descarrega1) / 1000)
            cost_total += cost_1
            
            if estacio_descarrega2 is not None and descarrega2 != 0:
                cost_2 = (((carrega - descarrega1) + 9) // 10) * (distancia_estacions(estacio_descarrega1, estacio_descarrega2) / 1000)
                cost_total += cost_2
            
        elif estacio_descarrega1 is None and estacio_carrega is not None and estacio_descarrega2 is not None and descarrega1 == 0 and descarrega2 != 0:
            cost_3 = (((carrega) + 9) // 10) * (distancia_estacions(estacio_carrega, estacio_descarrega2) / 1000)
            cost_total += cost_3
            
        return cost_total

    def distancia_recorregut(self):
        dist_total = 0
        if self.estacio_descarrega1 is not None and self.estacio_carrega is not None:
            dist_total += distancia_estacions(self.estacio_carrega, self.estacio_descarrega1)
            if self.estacio_descarrega2 is not None:
                dist_total += distancia_estacions(self.estacio_descarrega1, self.estacio_descarrega2)
        return dist_total
    
    def guanys(self):
        estacio_descarrega1 = self.estacio_descarrega1
        estacio_descarrega2 = self.estacio_descarrega2
        descarrega1 = self.descarrega1
        descarrega2 = self.descarrega2
        guanys = 0

        if estacio_descarrega1 is not None and estacio_descarrega1.num_bicicletas_next < estacio_descarrega1.demanda:
            possibles_guanys = (estacio_descarrega1.demanda - estacio_descarrega1.num_bicicletas_next) 
            guanys += min(descarrega1,  possibles_guanys)
        if estacio_descarrega2 is not None and estacio_descarrega2.num_bicicletas_next < estacio_descarrega2.demanda: 
            possibles_guanys2 = (estacio_descarrega2.demanda - estacio_descarrega2.num_bicicletas_next) 
            guanys += min(descarrega2,  possibles_guanys2)
        return guanys  
        #assegurar que dues furgos no tinguin guanys per deixar bicis en una estacio
        
        
    
    def perdues(self):
        if self.estacio_carrega is not None:
            estacio_carrega = self.estacio_carrega
            carrega = self.carrega
            demanda = estacio_carrega.demanda
            perdues = 0
            if estacio_carrega.num_bicicletas_next <= demanda:
                perdues += carrega
            else:
                sobrants = estacio_carrega.num_bicicletas_next - demanda
                if sobrants < carrega:
                    perdues += carrega-sobrants
            return perdues
        else:
            return 0
    def __repr__(self):
        return f"Furgonetes({self.estacio_carrega}, {self.carrega}, {self.estacio_descarrega1}, {self.descarrega1}, {self.estacio_descarrega2}, {self.descarrega2})"
    def __eq__(self, __value: object) -> bool:
        return self.estacio_carrega == __value.estacio_carrega and self.carrega == __value.carrega and self.descarrega1 == __value.descarrega1 and self.descarrega2 == __value.descarrega2 and self.estacio_descarrega1 == __value.estacio_descarrega1 and self.estacio_descarrega2 == __value.estacio_descarrega2
    def __copy__(self):
        return Furgonetes(self.estacio_carrega, self.carrega, self.estacio_descarrega1, self.descarrega1, self.estacio_descarrega2 , self.descarrega2)




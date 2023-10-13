from abia_bicing import Estacion, Estaciones


################
'''NO CAL'''
################


class Carrega():
    def __init__(self, estacio: Estacion, quantitat: int):
        self.estacio = estacio
        self.quantitat = quantitat
        #Fer que resti el nombre de bicis carregades a l'estacio
    def __repr__(self):
        return f"Carrega {self.quantitat} bicis a l'estació {self.estacio.id}"
    
class Descarrega():
    def __init__(self, estacio: Estacion, quantitat: int):
        #(int,int,int,int,int,int,int,int)
        #Fer que sumi el nombre de bicis carregades a l'estacio
        self.estacio = estacio
        self.quantitat = quantitat
    def __repr__(self):
        return f"Descarrega {self.quantitat} bicis a l'estació {self.estacio.id}"
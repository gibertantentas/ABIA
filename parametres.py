class Parametres():
    def __init__(self, n_estacions: int, n_bicis: int, llavor: int, n_furgonetes: int, max_bicicletes: int, num_furgonetes: int): #, p_min: List[int], p_max: int, c_max: int):
        self.n_estacions = n_estacions
        self.n_bicis = n_bicis
        self.llavor =  llavor
        self.n_furgonetes =  n_furgonetes
        self.max_bicicletes = max_bicicletes
        self.num_furgonetes = num_furgonetes
    def __repr__(self):
        return f"Parametres(n_estacions={self.n_estacions}, n_bicis={self.n_bicis}, llavor={self.llavor}, n_furgonetes={self.n_furgonetes}"
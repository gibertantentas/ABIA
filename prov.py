'''PROU BO'''
'''while True:
    try:
        est_carrega = next(iterador_est)
        estacions_de_carrega.add(est_carrega)
        est_descarrega1 = next(iterador_est)
        if est_carrega.num_bicicletas_no_usadas < 30:
            bicis_no_usades = est_carrega.num_bicicletas_no_usadas
        else:
            bicis_no_usades = 30
        carrega = bicis_no_usades

        try:
            est_descarrega2 = next(iterador_est)
            descarrega1 = bicis_no_usades // 2
            descarrega2 = bicis_no_usades - (bicis_no_usades // 2) 
            ruta.append(Furgonetes(est_carrega, carrega, est_descarrega1, descarrega1, est_descarrega2, descarrega2))
        except:
            descarrega1 = bicis_no_usades
            ruta.append(Furgonetes(est_carrega, carrega, est_descarrega1, descarrega1))

    except StopIteration:
        #No hi ha més estacions
        break'''



'''def genera_estat_inicial(params: Parametres, estacions: Estaciones) -> Estat:
    iterador_est = iterar_estacions(estacions)
    ruta = []
    estacions_de_carrega = set()
    while True:
        try:
            est_carrega = next(iterador_est)
            estacions_de_carrega.add(est_carrega)
            est_descarrega1 = next(iterador_est)
            if est_carrega.num_bicicletas_no_usadas < 30:
                bicis_no_usades = est_carrega.num_bicicletas_no_usadas
            else:
                bicis_no_usades = 30
            carrega = bicis_no_usades

            try:
                est_descarrega2 = next(iterador_est)
                descarrega1 = bicis_no_usades // 2
                descarrega2 = bicis_no_usades - (bicis_no_usades // 2) 
                ruta.append(Furgonetes(est_carrega, carrega, est_descarrega1, descarrega1, est_descarrega2, descarrega2))
            except:
                descarrega1 = bicis_no_usades
                ruta.append(Furgonetes(est_carrega, carrega, est_descarrega1, descarrega1))

        except StopIteration:
            #No hi ha més estacions
            break

    return Estat(params, ruta, estacions, estacions_de_carrega) #Instància d'Estat'''
    
    
     def __eq__(self, other):
        if isinstance(other, Estat):
            return (self.params == other.params and
                    self.ruta == other.ruta and
                    self.estacions == other.estacions and
                    self.estacions_de_carrega == other.estacions_de_carrega)
        return False

    def __hash__(self):
        return hash((self.params, tuple(self.ruta), self.estacions, frozenset(self.estacions_de_carrega)))
    
    
    
    
    
    
       
    
    
    
    
CODI 'Executar.py':


from abia_bicing import Estacion, Estaciones
from parametres import Parametres
from estat import genera_estat_inicial, genera_estat_inicial2
from aima.search import hill_climbing
from Problema import ProblemaBICING



params = Parametres(25, 1250, 42, 10, 30)
estacions = Estaciones(25, 1250, 42)


estat_inicial = genera_estat_inicial2(params, estacions) #Necessari executar per crear l'estat inicial


'''estat_inicial = genera_estat_inicial(params, estacions) #Necessari executar per crear l'estat inicial

estat_inicial2 = genera_estat_inicial2(params, estacions) #Necessari executar per crear l'estat inicial


gen = estat_inicial.genera_accions()
gen2 = estat_inicial2.genera_accions()
compt1 = 0
for i in gen:
    compt1 +=1 

compt2 = 0
for i in gen2:
    compt2 +=1 

print('Possibles accions: ', '\n Bo:',compt2, '\n Dolent:',compt1)

print('Heurística 1: ', '\n Bo:',estat_inicial2.h(), '\n Dolent:',estat_inicial.h())'''


print('Heurística Estat Inicial: ',estat_inicial.h())

for furgo in estat_inicial.ruta:
    print (furgo.carrega, furgo.descarrega1, furgo.descarrega2)
print('-------------')
n = hill_climbing(ProblemaBICING(estat_inicial))
#print ( n ) # Estat final
'''for furgo in n.ruta:
    print('\n','FURGO')
    print (furgo.carrega, furgo.descarrega1, furgo.descarrega2)
    try:
        try:
            print(furgo.estacio_descarrega1.num_bicicletas_next - furgo.estacio_descarrega1.demanda, furgo.estacio_descarrega2.num_bicicletas_next - furgo.estacio_descarrega2.demanda)
        except:
            pass
        print(furgo.estacio_descarrega1.num_bicicletas_next - furgo.estacio_descarrega1.demanda)
    except:
        pass'''

print ('final', n.h() ) # Valor de l’estat final


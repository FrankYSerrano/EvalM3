import time 
class bodega: 
#ATRIBUTOS
    
#METODOS:
    def __init__ (self):
        #se debe añadir al diccionario una key con cada letra del abc
        self.flores = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 
                        'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
#        self._disenos = []
#        self._ramos_despachados = {}
#        self._ramo_encargado = {}

# DATOS CARGADOS SOLO PARA PRUEBA DESPUES ELIMINAR Y DESCOMENTAR 3 LINEAS SUPERIORES
        self._disenos = ['As8y7t2w_17','Cs8y7t1w_16','DL6p7z5a_18','Cs4y3t2w_9','GL8U7P5X_20']
        self._ramos_despachados = {}
        self._ramo_encargado = {'De_A_para_B':'As8y7t2w_17', 'De_C_para_A':'Cs8y7t1w_16'}
#        self._ramo_encargado = {'De_A_para_B':'As8y7t2w_17', 'De_C_para_A':'Cs8y7t1w_16', 'De_C_para_B':'DL6p7z5a_18',
#                                'De_Z_para_H':'Cs4y3t2w_9', 'De_C_para_D':'Cs8y7t1w_16', 'De_F_para_B':'GL8U7P5X_20'}
        print("Cree instancia bodega")
#ramos = {'Cs8y7t15w30':5,'DL68p17z5a90':30, 'Cs4y3t2w9':14, 'GL8U7P5X20':5}
# METODOS: 
        #### recibir flores, recibe como parametro 1 letra y la cantidad de flores ######

    def Inv_bodega(self):
        print("_______________________________________________________________________________")
        print("stock de flores")
        print("-------------------------------------------------------------------------------")
        for flr in self.flores:
            cuenta = 0
            print("cantidad flor ", str(flr),"=",self.flores[flr])
            cuenta +=1
        time.sleep(3)
        return

    def ramos_pendientes(self):
        print("_______________________________________________________________________________")
        print("ramos por entregar")
        print("--------------------------------------------------------------------------------")
        for rmo in self._ramo_encargado:
            cuenta = 0
            print("cliente :", str(rmo)," diseño de ramo :",self._ramo_encargado[rmo])
            cuenta +=1
        print("-------------------------------------------------------------------------------")
        time.sleep(3)
        return
        
    def ramos_entregados(self): 
        print("_______________________________________________________________________________")
        print("ramos entregados")
        print("--------------------------------------------------------------------------------")
        for rmo in self._ramos_despachados:
            cuenta = 0
            print("cliente ", str(rmo),"diseño de ramo : ",self._ramos_despachados[rmo])
            cuenta +=1
        print("-------------------------------------------------------------------------------")
        time.sleep(3)
        return

    def recibir_flores (self,letra, cantidad):
        self.flores[letra] = self.flores[letra] + cantidad
        print(self.flores)
        print("añadi una flor a la lista")

    def anti(self):
        print(self._ramo_encargado)

    def disenar_ramos (self, diseno):
        self.disenos.append(diseno)
        print("Clase 01 Metodo 2")

    def despachar_ramos (self, ramo):
        self.ramos_despachados.append(ramo)
        print("Clase 01 Metodo 3")

    def encargar_ramos (self, ramo):
        self._ramo_encargado.append(ramo)
        print("Clase 01 Metodo 3")

###########################################################################
#_ramos_despachados Y _ramo_encargado DEBEN SER DICCIONARIOS YA QUE TIENE UN DUENO Y UN DISENO!!!!!
    def evaluar_ramos(self):
        for ramo in self._ramo_encargado:            
            print(ramo, " encargo el diseno: ", self._ramo_encargado[ramo])
            #Trabajando sobre el diseno encargado!
            #procede = verdadero hasta que no haya disponibilidad de alguna flor en el diseno
            procede = True
            disenoAevaluar = self._ramo_encargado[ramo]
            while procede:
                #Se analiza desde el 3er caracter en adelante hasta que consiga _; Va de 2 en 2
                #Al salir de este for si PROCEDE
                for letra in range(2, disenoAevaluar.find("_"), 2):
                    cantx = int(disenoAevaluar[letra])
                    florx = disenoAevaluar[letra +1].lower()
                    print("Evaluando disponibilidad de flor: ", florx, " necesito: ", cantx)

#INCLUIR ACA LA VALIDACION DE SI HAY SUFICIENTE EN BODEGA Y REMPLAZAR EL "if not procede:"!!!!                    
                    if self.flores[florx] < cantx:
                        print("NO HAY SUFICIENTE")
                        #Se modifica procede para salir del while
                        procede = False
                        #se usa break para salir del for
                        break
                    else:
                        print("HAY SUFICIENTE, EVALUA LA OTRA FLOR")
# En este punto procede indica si se puede procesar el ramo o no!
                if not procede:
                    print("Sorry! No se puede procesar")
                else:
                    print("ALELUYA!!!! Se puede despachar el ramo!")
#                    self.rebaja_stock(ramo)
#                    self.despachar_ramos(ramo)
#                    self._ramo_encargado.QUITAR(ramo)
                    procede = False

###########################################################################

###############Manejo Stock###########
    def carga_stock(self):
        print("Estamos revistando el stock en bodega...")
        time.sleep(3)
        for flor in self.flores:
            while self.flores[flor] < 20:
                if self.flores[flor] < 20:
                    self.flores[flor] = self.flores[flor] + 20
#                    print("Añadimos flores con stock bajo")
#                    time.sleep(0.1)
                else:
                    pass

        print("listo...")
        print("Gracias por la espera")

  ############# Propiedad flores #############

  
    @property ## propiedad getter
    def flores (self):
        return self._flores

    @flores.setter ## propiedad setter
    def flores (self, nuevo):

        print("modificando letra..")
        self._flores = nuevo
        print("la letra ha sido modificada")
        print(self._flores)
    

    @flores.deleter ## propiedad deleter
    def flores(self):
        print("Borrando tamaño")
        del self._flores

  ############# Propiedad ramos encargados #############

  
    @property ## propiedad getter
    def ramo_encargado (self):
        return self._ramo_encargado

    @ramo_encargado.setter ## propiedad setter
    def ramo_encargado (self, nuevo):
        print("modificando letra..")
        self._ramo_encargado = nuevo
        print("la letra ha sido modificada")
        print(self._ramo_encargado)

    @ramo_encargado.deleter ## propiedad deleter
    def ramo_encargado(self):
        print("Borrando tamaño")
        del self._ramo_encargado

 
 ############## Propiedad  diseños ##############


    @property ## propiedad getter
    def disenos (self):
        return self._disenos

    @disenos.setter ## propiedad setter
    def disenos (self, nuevo):

        print("modificando letra..")
        self._disenos = nuevo
        print("la letra ha sido modificada")
        print(self._disenos)
    

    @disenos.deleter ## propiedad deleter
    def disenos(self):
        print("Borrando tamaño")
        del self._disenos


##########  propiedad ramos_despachados ###########


    @property ## propiedad getter
    def ramos_despachados (self):
        return self._ramos_despachados

    @ramos_despachados.setter ## propiedad setter
    def ramos_despachados (self, nuevo):

        print("modificando letra..")
        self._ramos_despachados = nuevo
        print("la letra ha sido modificada")
        print(self._ramos_despachados)
    

    @ramos_despachados.deleter ## propiedad deleter
    def ramos_despachados(self):
        print("Borrando tamaño")
        del self._ramos_despachados



if __name__ == "__main__":
    bodega1 = bodega()
    bodega1.evaluar_ramos()
    bodega1.carga_stock()
    print(bodega1.anti())
    bodega1.evaluar_ramos()

    #print(bodega1.flores)
    # bodega1.encargar_ramos('As8y7t2w17')
    # bodega1.encargar_ramos('Cs8y7t15w30')
    # bodega1.encargar_ramos('DL68p17z5a90')
    # bodega1.encargar_ramos('Cs4y3t2w9')
    # bodega1.encargar_ramos('GL8U7P5X20')
#    print(bodega1._ramo_encargado)

    pass
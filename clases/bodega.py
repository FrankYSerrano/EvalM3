import time 
class bodega: 
#ATRIBUTOS
    
#METODOS:
    def __init__ (self):
        #se debe añadir al diccionario una key con cada letra del abc
        self.flores = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 
                        'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

        self._disenos = ['As8y7t2w17','Cs8y7t15w30','DL68p17z5a90','Cs4y3t2w9','GL8U7P5X20']
        self._ramos_despachados = []
        self._ramo_encargado = []
        print("Cree instancia bodega")

# METODOS: 
        #### recibir flores, recibe como parametro 1 letra y la cantidad de flores ######

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

    def evaluar_ramos(self):
        for ramo in self._ramo_encargado:            
            print(ramo)


###############Manejo Stock###########
    def carga_stock(self):
        print("Estamos revistando el stock en bodega...")
        time.sleep(5)
        for flor in self.flores:
            while self.flores[flor] < 20:
                if self.flores[flor] < 20:
                    self.flores[flor] = self.flores[flor] + 20
                    print("Añadimos flores con stock bajo")
                    time.sleep(0.2)
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
    bodega1.carga_stock()
    print(bodega1.flores)
    bodega1.encargar_ramos('As8y7t2w17')
    bodega1.encargar_ramos('Cs8y7t15w30')
    bodega1.encargar_ramos('DL68p17z5a90')
    bodega1.encargar_ramos('Cs4y3t2w9')
    bodega1.encargar_ramos('GL8U7P5X20')
    print(bodega1.anti())
    bodega1.evaluar_ramos()

#    print(bodega1._ramo_encargado)

    pass
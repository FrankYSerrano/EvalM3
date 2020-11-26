#CLASE
class bodega: 
#ATRIBUTOS
    
#METODOS:
    def __init__ (self):
        #se debe añadir al diccionario una key con cada letra del abc
        self.flores = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 
                        'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

        self._disenos = []
        self._ramos_despachados = []
        self._ramo_encargado = []
        print("Cree instancia bodega")



# METODOS: 
        #### recibir flores, recibe como parametro 1 letra y la cantidad de flores ######

    def recibir_flores (self,letra, cantidad):
        self.flores[letra] = self.flores[letra] + cantidad
        print(self.flores)
        print("añadi una flor a la lista")


    def disenar_ramos (self, diseno):
        self.disenos.append(diseno)
        print("Clase 01 Metodo 2")

    def despachar_ramos (self, ramo):
        self.ramos_despachados.append(ramo)
        print("Clase 01 Metodo 3")

    def carga_stock(self):
#        self.flores = self.flores
#        for flor in self.flores:
            print("Fernando")
#            print(self.flores[flor] , " ->")


### Getter, setters and  Del

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
    bodega1.recibir_flores("a",15)
    bodega1.recibir_flores("a",25)
    bodega1.recibir_flores("b",15)
    bodega1.carga_stock()
    
    pass
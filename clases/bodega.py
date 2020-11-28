import time 
import os
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
        self._disenos = ['As8y7t2w_17','Cs8y7t1w_16','DL6p7z5a_18','Cs4y3t2w_9','GL8U7P5X_20',
                        'Cs9y9t9p9y9u9e1w_54', 'As2h7l1r_10']
        self._ramos_despachados = {}
        self._ramo_encargado = {'De_A_para_B':'As8y7t2w_17', 'De_C_para_A':'Cs8y7t1w_16',
                                'De_H_para_Q':'As2h7l1r_10', 'De_Z_para_A':'Cs9y9t9p9y9u9e1w_54'}
        print("Cree instancia bodega")
# METODOS: 

    def Inv_bodega(self):
        print("_______________________________________________________________________________")
        print("Stock de flores")
        print("-------------------------------------------------------------------------------")
        for flr in self.flores:
            cuenta = 0
            t = ""
            if self.flores[flr] < 5:
                t = " ---> Se sugiere reabastecer!!!"
            print("Cantidad disponible de flor ", str(flr),"=",self.flores[flr], t)
            cuenta +=1
        time.sleep(2)
        return

    def ramos_pendientes(self):
        print("_______________________________________________________________________________")
        print("Ramos por entregar")
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
        print("Ramos entregados")
        print("--------------------------------------------------------------------------------")
        for rmo in self._ramos_despachados:
            cuenta = 0
            print("cliente ", str(rmo),"diseño de ramo : ",self._ramos_despachados[rmo])
            cuenta +=1
        print("-------------------------------------------------------------------------------")
        time.sleep(3)
        return

    #### recibir flores, recibe como parametro 1 letra y la cantidad de flores ######
    def recibir_flores (self,letra, cantidad):
        self.flores[letra] = self.flores[letra] + cantidad
        print(self.flores)
        print("añadi una flor a la lista")

    def anti(self):
        print("Ramos encargados: ", self._ramo_encargado)

    def disenar_ramos (self, diseno):
        self.disenos.append(diseno)
#        print("Clase 01 Metodo 2")

    def despachar_ramos (self, ramo):
        self.ramos_despachados.append(ramo)
#        print("Clase 01 Metodo 3")

    def encargar_ramos (self, nombre, diseno):
        self._ramo_encargado[nombre] = diseno
#        print("Clase 01 Metodo 3")

    def pregunta(self):    
        print(" Hola soy el Bot Crist_IA_n! Me podrías decir tú nombre? ")
        nombre = input("Ingrese nombre: ") # key
#        print("este es un nombre: ", nombre)
#        print()
        print("            ### Diseños disponibles ### ")
        print(nombre, "  Estos son los diseños disponibles: ")
        condicion = True
        while condicion:
            time.sleep(1)
            os.system("cls")
            seleccion = 1
            for disenos in self._disenos:
                print("Diseño N° ",str(seleccion), ":", disenos)
                seleccion = seleccion + 1
            z = input("Elige un diseño de ramo: ")
            try:
                if int(z) in range(1,seleccion):
#                    print("lo que sea")
                    self.encargar_ramos(nombre,disenos)
                    condicion = False
                else:
                    print("Selección fuera de rango, try again")
            except Exception:
                print("seleccion invalida ")        

    def evaluar_ramos(self):
        for ramo in self._ramo_encargado.copy():            
            print("El cliente: " , ramo, " encargo el diseno: ", self._ramo_encargado[ramo])
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
#                    print("Evaluando disponibilidad de flor: ", florx, " necesito: ", cantx)
    #VALIDACION DE SI HAY SUFICIENTE EN BODEGA Y REMPLAZAR EL "if not procede:"!!!!                    
                    if self.flores[florx] < cantx:
                        print("No se puede despachar! No tenemos suficientes flores: ", florx)
                        #Se modifica procede para salir del while
                        procede = False
                        #se usa break para salir del for
                        break
                    else:
                        pass
#                        print("HAY SUFICIENTE, EVALUA LA OTRA FLOR")
    # En este punto procede indica si se puede procesar el ramo o no!
                if not procede:
                    print("Enviaremos a Guido a buscar mas!!!")
                else:
                    print("Fernando le entregara su ramo!")
                    #Se rebaja los inventarios
                    self.rebaja_stock(ramo)
                    #Se agrega el ramo a ramos despachados
#                    print("Se agrega el ramo a los despachados!")
                    self._ramos_despachados[ramo] = disenoAevaluar                        
                    #Se elimina el ramo de ramos pendientes
#                    print("Se eliminado el ramo de los pendientes!")
                    self.ramo_encargado.pop(ramo)
                    break
        input("Presione cualquier tecla para volver al MENU")                
###########################################################################
    def rebaja_stock(self,ramo):
       # for ramo in self._ramo_encargado:           
        #    procede = True
        disenoAevaluar = self._ramo_encargado[ramo]
          #while procede:
        for letra in range(2, disenoAevaluar.find("_"), 2):
            cantx = int(disenoAevaluar[letra])
            florx = disenoAevaluar[letra +1].lower()
            minus = cantx
            self.flores[florx] = self.flores[florx] - minus
        #if not procede:
        #    print("Sorry! No se puede procesar")
        #else:
        #    procede = False

###############Manejo Stock###########
    def carga_stock(self):
        print("Frank esta recargando el stock en bodega...")
        time.sleep(3)
        for flor in self.flores:
            while self.flores[flor] < 20:
                if self.flores[flor] < 20:
                    self.flores[flor] = self.flores[flor] + 20
#                    print("Añadimos flores con stock bajo")
#                    time.sleep(0.1)
                else:
                    pass
#        print("listo...")
        print("Stock recargado. Gracias por la espera")

############# Propiedad flores #############
    @property ## propiedad getter
    def flores (self):
        return self._flores

    @flores.setter ## propiedad setter
    def flores (self, nuevo):
#        print("modificando letra..")
        self._flores = nuevo
#        print("la letra ha sido modificada")
#        print(self._flores)

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
#        print("modificando letra..")
        self._ramo_encargado = nuevo
#        print("la letra ha sido modificada")
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
#        print("modificando letra..")
        self._disenos = nuevo
#        print("la letra ha sido modificada")
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


# AREA DE PRUEBAS UNITARIAS
if __name__ == "__main__":
    bodega1 = bodega()
    bodega1.carga_stock()
    print(bodega1.anti())
    bodega1.evaluar_ramos()
    print(bodega1.anti())
    pass
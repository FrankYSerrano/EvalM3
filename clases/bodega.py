#CLASE
class bodega: 
#ATRIBUTOS
    
#METODOS:
    def __init__ (self,
    ):
        #se debe añadir al diccionario una key con cada letra del abc

        self.flores = {'a':0}
        self.disenos = []
        self.ramos_despachados = []
        print("Cree instancia bodega")

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

if __name__ == "__main__":
    bodega1 = bodega()
    bodega1.recibir_flores("a",15)
    bodega1.recibir_flores("a",25)
    bodega1.recibir_flores("b",15)
    pass
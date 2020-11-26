from .especie_flor import especie_flor

#CLASE
class flor (especie_flor):
#ATRIBUTOS
    
#METODOS:
    def __init__ (self, cantidad,letra):
        self.cantidad = cantidad
        super(especie_flor).self.__init__(letra)
        self.letra = letra
        #self.tamano_flor

        #Clase01.__init__(self, arg1, arg2, arg3, arg4)
        #Clase02.__init__(self, arg1, arg2, arg3, arg4)
        print("Cree instancia de clase 03")

    def met1 (self, arg1):
        print("Clase 03 Metodo 1")

    def met2 (self, arg1):
        print("Clase 03 Metodo 2")

    def met3 (self, arg1):
        print("Clase 03 Metodo 3")

if __name__ == "__main__":
    flor1 = flor(5, "a")
    pass
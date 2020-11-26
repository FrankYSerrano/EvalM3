from .especie_flor import especie_flor
from .tamano_flor import tamano_flor

#CLASE
class flor (especie_flor, tamano_flor):
#ATRIBUTOS
    
#METODOS:
    def __init__ (self, letra, tamano):
        super().__init__(letra)
        self.letra = letra
        super().__init__(tamano)
        self.tamano = tamano
        self.nombre = letra + tamano
        #self.tamano_flor
        print("Cree instancia de clase 03", self.nombre)

    def met1 (self, arg1):
        print("Clase 03 Metodo 1")

    def met2 (self, arg1):
        print("Clase 03 Metodo 2")

    def met3 (self, arg1):
        print("Clase 03 Metodo 3")

if __name__ == "__main__":
    flor1 = flor("g", "l")
    pass
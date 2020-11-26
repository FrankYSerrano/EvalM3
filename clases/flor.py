from .especie_flor import especie_flor
from .tamano_flor import tamano_flor

#CLASE
class flor (especie_flor, tamano_flor):
#ATRIBUTOS
    
#METODOS:
    def __init__ (self, letra, tamano):
        super().__init__(letra)
        self._letra = letra
        super().__init__(tamano)
        self._tamano = tamano
        self._nombre = letra + tamano
        #self.tamano_flor
        print("retorno el nombre letra_tamaño", self.nombre)

    ##### getters and setters ######

    @property ## propiedad getter
    def letra (self):
        return self._nombre

    @letra.setter ## propiedad setter
    def letra (self, nuevo):

        print("modificando letra..")
        self._letra = nuevo
        print("la letra ha sido modificada")
        print(self._letra)

    @letra.deleter ## propiedad deleter
    def letra(self):
        print("Borrando letra")
        del self.letra

    
    @property ## propiedad getter
    def tamano (self):
        return self._tamano

    @tamano.setter ## propiedad setter
    def tamano (self, nuevo):

        print("modificando letra..")
        self._tamano = nuevo
        print("la letra ha sido modificada")
        print(self._tamano)
    

    @tamano.deleter ## propiedad deleter
    def tamano(self):
        print("Borrando tamaño")
        del self.tamano

    def met3 (self, arg1):
        print("Clase 03 Metodo 3")

if __name__ == "__main__":
    flor1 = flor("g", "l")
    pass
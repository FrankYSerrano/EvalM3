#CLASE
class especie_flor: 
#ATRIBUTOS
    
#METODOS:
    def __init__ (self, letra):
        self.tamano_flor(letra)
        self.letra = letra
        print("se ha añadido una especie")
        

    def tamano_flor (self, tamano):
        if tamano.upper() == tamano:
            self.tamano = "l"
            print("soy tamaño grande")    
        else:
            self.tamano = "s"
            print("soy tamaño pequeño")
        return self.tamano    
          
if __name__ == "__main__":
    especie_flor("a")
    especie_flor("B")

           
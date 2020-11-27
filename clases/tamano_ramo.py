#CLASE
class tamano_ramo: 
#ATRIBUTOS
    tamanos = ["s", "l"]
#METODOS:
    def __init__ (self, tamano):
        self.tamano = tamano
        print("se ha añadido un tamano de ramo")
                  
if __name__ == "__main__":
    tamano_ramo("L")
    tamano_ramo("s")

           
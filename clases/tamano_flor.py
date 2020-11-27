#CLASE
class tamano_flor: 
#ATRIBUTOS
    tamanos = ["S", "L"]

#METODOS:
    def __init__ (self, tamano):
        self.tamano = tamano
        print("se ha añadido un tamano")
                  
if __name__ == "__main__":
    tamano_flor("L")
    tamano_flor("s")

           
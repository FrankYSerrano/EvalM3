#CLASE
class nombre_ramo: 
#ATRIBUTOS
    nombre_ramo = ["A", "B", "C","D", "E", "F","G", "H", "I","J", "K", "L","M", "N", "O","P", "Q", "R","S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
#METODOS:
    def __init__ (self, letra):
        self.letra = letra
        print("se ha añadido un nombre de ramo")  
          
if __name__ == "__main__":
    nombre_ramo("A")
    nombre_ramo("B")

           
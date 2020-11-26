#CLASE
class nombre_ramo: 
#ATRIBUTOS
#Cambiar a MAYUSCULAS!!!
    nombre_ramo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#METODOS:
    def __init__ (self, letra):
        self.letra = letra
        print("se ha añadido un nombre de ramo")  
          
if __name__ == "__main__":
    nombre_ramo("A")
    nombre_ramo("B")

           
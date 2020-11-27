from .diseno_ramo import diseno_ramo
#CLASE
class ramo(diseno_ramo): 
#ATRIBUTOS
    
#METODOS:
    def __init__ (self):
        
        print(" Buenas, me podrías decir tú nombre? ")
        nombre = print(input("ingrese nombre: ", self.nombre))
        print("este es un nombre: ", nombre)
        print()
        print("            ### Diseños disponibles ### ")
        print("  Estos son los diseños disponibles:       ")
        print("Diseño N° 1: ",diseno[0])
        print("Diseño N° 2: ",diseno[1])
        
        self.nombre = nombre
        

        print()  





    def diseño_disponible(self):
        self.nombre = nombre
        self.diseno = diseno
       

        
    
          
if __name__ == "__main__":
   # especie_flor("a")
   # especie_flor("B")
   ramo1 = ramo()


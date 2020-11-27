#from diseno_ramo import diseno_ramo

#CLASE
class ramo(): 
#ATRIBUTOS
#METODOS:
    def __init__ (self):
        self.nombre = ""
        self.diseno = ""

    def pregunta(self, disenos_disp):    
        print(" Buenas, me podrías decir tú nombre? ")
        self.nombre = input("ingrese nombre: ")
        print("este es un nombre: ", self.nombre)
        print()
        print("            ### Diseños disponibles ### ")
        print("  Estos son los diseños disponibles:       ")
        print("Diseño N° 1: ",disenos_disp[0])
        print("Diseño N° 2: ",disenos_disp[1])        
        print("Diseño N° 2: ",disenos_disp[2])        
        print("Diseño N° 2: ",disenos_disp[3])        
        print("Diseño N° 2: ",disenos_disp[4])        
        print()  
       

if __name__ == "__main__":
   # especie_flor("a")
   # especie_flor("B")
   ramo1 = ramo()
   ramo1.pregunta(['As8y7t2w17','Cs8y7t15w30','DL68p17z5a90','Cs4y3t2w9','GL8U7P5X20'])


    

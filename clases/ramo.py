import os
import time

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
        self.nombre = input("ingrese nombre: ") # key
        print("este es un nombre: ", self.nombre)
        print()
        print("            ### Diseños disponibles ### ")
        print("  Estos son los diseños disponibles:       ")
        print(disenos_disp)

        while True:
            
            time.sleep(1)
            os.system("cls")
            

            seleccion = 1

            for disenos in disenos_disp:
                print("Diseño N° ",str(seleccion), ":", disenos)
                seleccion = seleccion + 1

            z = input("Elige un diseño de ramo: ")
            try:
                if int(z) in range(1,seleccion):
                    print("lo que sea")
                    break
                else:
                    print("Selección fuera de rango, try again")

            except Exception:
                print("seleccion invalida ")
        


        
       

if __name__ == "__main__":
   # especie_flor("a")
   # especie_flor("B")
   ramo1 = ramo()
   ramo1.pregunta(['As8y7t2w17','Cs8y7t15w30','DL68p17z5a90','Cs4y3t2w9','GL8U7P5X20'])


    

import clases as c
import funciones as f
import time

x = ""
#Creacion de Instancia de FLOR
FloresDisp = c.flor("L","l")
#Creacion de Instancia BODEGA
FlorLinda = c.bodega()
#Creacion de instancia NombreRamo
NombresRamos = c.nombre_ramo("A")
#Creacion de Tamanos de RamoPosibles
TamanoRamos = c.tamano_ramo("A")
#Creacion de Instancia RAMO
RamoDeseado = c.ramo()
ciclo = True
while ciclo:
    seleccion = f.menu()
#    print(seleccion)
    if seleccion == '1':
        print("Recepcioando Flores... por favor espere...")
        FlorLinda.carga_stock()
        time.sleep(2)
    elif seleccion =='2': #Disenar ramos
        x  = f.input_diseno_ramo(NombresRamos.nombre_ramo, TamanoRamos.tamanos, FloresDisp.flores)
        FlorLinda.disenar_ramos(x)
    elif seleccion =='3': #Encargar ramo
        FlorLinda.pregunta()
    elif seleccion =='4': #4Reporte de inventario de flores en bodega
        FlorLinda.Inv_bodega()
    elif seleccion =='5': #Reporte de ramos pendientes por procesar
        FlorLinda.ramos_pendientes()
    elif seleccion =='6': #Reporte de ramos ya entregados
        FlorLinda.ramos_entregados() 
    elif seleccion =='7': #Evaluar ramos pendientes y procesar los que se pueda
        FlorLinda.evaluar_ramos()
    else:
        print("G r a c i a s   p o r   s u   c o m p r a!")
        break
    time.sleep(2)
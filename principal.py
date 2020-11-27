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
    print(seleccion)
    if seleccion == '1':
        print("Recepcioanndo Flores... por favor espere...")
        FlorLinda.carga_stock()
        time.sleep(2)
    elif seleccion =='2':
        #LLEVAR EL CODIGO DE LA FUNCION AL METODO DISENAR RAMOS: DEBE QUEDAR >> FlorLinda.disenar_ramos() 
        x  = f.input_diseno_ramo(NombresRamos.nombre_ramo, TamanoRamos.tamanos, FloresDisp.flores)
        FlorLinda.disenar_ramos(x)
        print("CHAO!2")
    elif seleccion =='3':
        RamoDeseado.pregunta(FlorLinda._disenos)
#        print("Seleccione el ramo a ordenar: ", FlorLinda._disenos)
    elif seleccion =='4':
        FlorLinda.Inv_bodega()
    elif seleccion =='5':
        FlorLinda.ramos_pendientes()
    elif seleccion =='6':
        FlorLinda.ramos_entregados() 
    elif seleccion =='7':
        print(FlorLinda._ramo_encargado)
    else:
        print("CHAO!")
        break
    time.sleep(2)


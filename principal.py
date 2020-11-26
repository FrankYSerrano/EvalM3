import clases as c
import funciones as f
import time



#Creacion de Instancia BODEGA
FlorLinda = c.bodega()
NombresRamos = c.nombre_ramo("A")
ciclo = True
while ciclo:
    seleccion = f.menu()
    print(seleccion)
    if seleccion == '1':
        print("Recepcioanndo Flores... por favor espere...")
        time.sleep(2)
    elif seleccion =='2':
        #LLEVAR EL CODIGO DE LA FUNCION AL METODO DISENAR RAMOS: DEBE QUEDAR >> FlorLinda.disenar_ramos() 
        #FlorLinda.disenar_ramos(f.input_diseno_ramo(NombresRamos.nombre_ramo, ['L','S'], FlorLinda.flores))
        print("CHAO!2")
    elif seleccion =='3':
        print("Seleccione el ramo a ordenar: ", FlorLinda.flores)
    elif seleccion =='4':
#        FlorLinda.Metodo1() inventario de Bodega
        print(FlorLinda.flores)
    elif seleccion =='5':
#        FlorLinda. Metodo 2 Reporte de Ramos pendientes
        print(FlorLinda.ramo_encargado)
    elif seleccion =='6':
#        FlorLinda. Metodo 3 Reporte de Ramos entregados 
        print(FlorLinda.ramos_despachados)
    elif seleccion =='7':
        print(FlorLinda.ramo_encargado)
    else:
        print("CHAO!")
    time.sleep(2)


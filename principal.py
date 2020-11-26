import clases as c
import funciones as f
import time



#Creacion de Instancia BODEGA
FlorLinda = c.bodega()
ciclo = True
while ciclo:
    seleccion = f.menu()
    print(seleccion)
    if seleccion == '1':
        print("Recepcioanndo Flores... por favor espere...")
        time.sleep(2)
    elif seleccion =='2':
        #LLEVAR EL CODIGO DE LA FUNCION AL METODO DISENAR RAMOS: DEBE QUEDAR >> FlorLinda.disenar_ramos() 
        FlorLinda.disenar_ramos(f.input_diseno_ramo(['A', 'B', 'C', 'D', 'E'], ['L','S'], FlorLinda.flores))
        print("CHAO!2")
    elif seleccion =='3':
        print("Seleccione el ramo a ordenar: ", FlorLinda.flores)
    elif seleccion =='4':
        print(FlorLinda.flores)
    elif seleccion =='5':
        print(FlorLinda.ramo_encargado)
    elif seleccion =='6':
        print(FlorLinda.ramos_despachados)
    elif seleccion =='7':
        print(FlorLinda.ramo_encargado)
    else:
        print("CHAO!")
    time.sleep(2)


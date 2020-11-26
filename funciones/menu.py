import os

def menu():
    opcion = 'X'
    opciones_posibles = ['1', '2', '3', '4', 'X']
    control = True
    while control: 
        os.system("CLS")
        print("***************** MENU *****************")
        print("*                                      *")
        print("* Recepcion de Flores en Bodega   -> 1 *") # Fernando
        print("* Generar Disenos de Ramos        -> 2 *") # Frank
        print("* Seleccionar (Ordenar) Ramos     -> 3 *") # Guido
        print("* Reporte de inventario de Bodega -> 4 *") # Cristian
        print("* Reporte de Ramos pendientes     -> 5 *") # Cristian
        print("* Reporte de Ramos entregados     -> 6 *") # Cristian
        print("* Evaluar Ramos Procesables       -> 7 *") # Cristian
        print("*       S   A   L   I   R         -> X *")
        print("*                                      *")
        print("****************************************")
        opcion = input("Introduzca su opcion: ")
        if opcion in opciones_posibles:
            control = False
        else:
            print("Opcion invalida")
    return opcion

#PRUEBA UNITARIA
if __name__ == "__main__":
    opc = menu()
    if opc == '1':
        print("UNO")
    else:
        print("Otro")
import os
import time

def menu():
    opcion = 'X'
    opciones_posibles = ['1', '2', '3', '4', '5', '6', '7', 'X', 'x']
    control = True
    while control: 
        os.system("cls")
        print("***************** MENU *****************")
        print("*                                      *")
        print("* Recepcion de Flores en Bodega   -> 1 *") 
        print("* Generar Disenos de Ramos        -> 2 *") 
        print("* Seleccionar (Ordenar) Ramos     -> 3 *")
        print("* Reporte de inventario de Bodega -> 4 *")
        print("* Reporte de Ramos pendientes     -> 5 *")
        print("* Reporte de Ramos entregados     -> 6 *")
        print("* Despachar un Ramo               -> 7 *")
        print("*       S   A   L   I   R         -> X *")
        print("*                                      *")
        print("****************************************")
        opcion = input("Introduzca su opcion: ").upper()
        if opcion in opciones_posibles:
            control = False
        else:
            print("Opcion invalida")
            time.sleep(2)
    return opcion

# AREA DE PRUEBAS UNITARIAS
if __name__ == "__main__":
    opc = menu()
    if opc == '1':
        print("UNO")
    else:
        print("Otro")
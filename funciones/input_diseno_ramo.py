import random
import time
import os

#Esta funcion debe recibir 3 listas por parametro
def input_diseno_ramo(nombresPosibles, tamanosPosibles, floresPosibles):
    condicion1 = True
    ramoDisenado = ""
    totalFlores = 0
#Ingreso de Nombre de RAMO
    while condicion1:
        os.system("cls")
        print("Ramo a definir: ", ramoDisenado)
        print("Seleccione algun nombre de Ramo de los posibes: ", nombresPosibles)
        l=input()
        if not l.upper() in nombresPosibles:
            print("Introdujo un valor invalido")
            time.sleep(2)
        else:
            condicion1 = False
            ramoDisenado = l.upper()
#Ingreso de Tamano de RAMO
    condicion1 = True
    while condicion1:
        os.system("cls")
        print("Ramo a definir: ", ramoDisenado)
        print("Seleccione el Tamano del ramo de los posibes: ", tamanosPosibles)
        l=input()
        if not l.lower() in tamanosPosibles:
            print("Introdujo un valor invalido")
            time.sleep(2)
        else:
            condicion1 = False
            ramoDisenado = ramoDisenado + l.lower()
    #Loop para incluir flores y sus cantidades
    otra = True
    while otra:
    #Ingreso de cantidad de una flor para RAMO
        condicion1 = True
        while condicion1:
            os.system("cls")
            print("Ramo a definir: ", ramoDisenado)
            l=input("Seleccione la cantidad de la flor que desea anadir a su ramo: ")
            try:
                cant = int(l)
                if cant >= 0:
#                    print("Usted introdujo: ", str(cant))
                    totalFlores = totalFlores + cant
                    condicion1 = False
                    ramoDisenado = ramoDisenado + str(cant)
            except:
                print("Introdujo un valor invalido")
                time.sleep(2)
    #Ingreso de Flores para RAMO
        condicion1 = True
        while condicion1:
            os.system("cls")
            print("Ramo a definir: ", ramoDisenado)
            print("Seleccione la flor que desea anadir a su ramo de las posibes: ", floresPosibles)
            l=input()
            if not l.lower() in floresPosibles:
                print("Introdujo un valor invalido")
                time.sleep(2)
            else:
                condicion1 = False
                ramoDisenado = ramoDisenado + l.lower()
        otra2=True
        while otra2:
            l=input("Desea agragar mas flores a su diseno ramo? Y/N: ")
            if l.upper() == 'N':
                otra = False
            otra2 = False
    ramoDisenado = ramoDisenado + "_" + str(totalFlores)
#    print(ramoDisenado)
    return ramoDisenado
    
# AREA DE PRUEBAS UNITARIAS
if __name__ == "__main__":
    x = input_diseno_ramo(['A', 'B', 'C', 'D', 'E'], ['L','S'], ['v', 'w', 'x', 'y', 'z'])
    print(x)
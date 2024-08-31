'''Menú principal - Sala de cine'''
import os
def menu():
    '''Mostrar el menú'''
    while True:
        os.system('cls')
        os.system('clear')
        print("1 - CREAR SALA\n2 - VER SALA\n3 - ASIGNAR PUESTO\n4 - CARGAR SALA\n5 - SALIR")
        opc = input('\nSeleccione la opción deseada:\n')
        os.system('cls')
        os.system('clear')


        if opc == "1":
            print("Prueba opción 1")
        elif opc == '2':
            print("Prueba opción 2")
        elif opc == '3':
            print("Prueba opción 3")
        elif opc == "4":
            print("Prueba opción 4")
        elif opc == "5":
            print("Prueba opción 5")
menu()


'''Menú principal - Sala de cine'''

import os
import pickle 
matriz_sala = []

def clear_screen():
    os.system('cls')
    os.system('clear')

def cre_sala(f, c):
    '''Función - crear sala'''
    conta = 0
    for i in range(f):
        matriz_sala.append([])
        for j in range(c):
            conta += 1
            matriz_sala[i].append(conta)
    return f, c, matriz_sala

def pre_sala(matrizsala):
    '''Función - previsualizar sala'''
    for filas in (matrizsala):
        for columnas in filas:
            print(f"{columnas:>2}", end='  ')
        print()
    return matrizsala

def asig_asiento(asig):
    '''Función - seleccionar asiento'''
    try:
        num_asiento = int(input('Digite el número del asiento seleccionado: '))
        enc = False
        for i, fila in enumerate(matriz_sala):
            for j, asiento in enumerate(matriz_sala[i]):
                if matriz_sala[i][j] == num_asiento:
                    matriz_sala[i][j] = 'x'
                    enc = True
                    print('Asiento asignado correctamente.')
                    break
            if enc:
                break
        if not enc:
            print('El asiento no es valido o está ocupado.')
    except ValueError:
        print('Error, ingrese un número válido.')

def cargar_sala(matrizsala):
    for filas in (matrizsala):
        for columnas in filas:
            print(f"{columnas:>2}", end="  ")          #Correción del espaciado de la x   print(f"{columnas:>2}", end="  ") 
        print() 
    return matrizsala

def guardar_matriz(name, matriz):
    try:  # Log 
        with open(name, 'wb') as file:
            pickle.dump(matriz, file)
        print(f'La matriz se ha guarado correctamente!.')
    except Exception as e:
        print(f'Error al guardar el matriz: ')

def menu():
    '''Mostrar el menú'''
    clear_screen()
    a = 0
    while a == 0:
        clear_screen()
        print("1 - CREAR SALA\n2 - VER SALA\n3 - ASIGNAR PUESTO\n4 - CARGAR SALA\n5 - SALIR")
        opc = int(input('\nSeleccione la opción deseada:\n'))
        clear_screen()

        if opc == 1:
            filas = int(input('Digite el número de filas:\n'))
            columnas = int(input('Digite el número de columnas:\n'))
            cre_sala(filas, columnas)
            print('Sala creada exitosamente.')
            input('\nPresione una tecla para continuar...')
        elif opc == 2:   
            if len(matriz_sala) == 0:
                print('La sala no ha sido creada aún.')
            else:
                pre_sala(matriz_sala)
                input('\nPresione una tecla para continuar...')
        elif opc == 3:
            if len(matriz_sala) == 0:
                print('La sala no ha sido creada aún.')
            else: 
                asig_asiento(matriz_sala)
                input('\nPresione una tecla para continuar...'); 
        
        elif opc ==  4: 
            if len(matriz_sala) == 0:
                print('La sala no ha sido creada aún.')
            else:
                clear_screen()
                cargar_sala(matriz_sala)
                guardar_matriz("Log", matriz_sala)
                input('\nPresione una tecla para continuar...'); 
        elif opc == 5:
            clear_screen()
            a += 1
menu()


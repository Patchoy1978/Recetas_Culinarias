# se importan las librerias necesarias
import os
from os import system
from pathlib import Path
import shutil

# se crean las funciones
def entrada_nombre():
    #se le pide al usuario que ingrese su nombre y sera retornado por la función
    nombre = input('Cual es tu nombre: ').title()

    return nombre

def mostrar_bienvenida (nombre,cantidad):

    '''se limpia la pantalla al ingresar el usuario y se imprime el mensaje de bienvenida,
    esta función recibe los parametros que vienen de las funciones 
    entrada_nombre y cantidad_recetas para estar en el mensaje de bienvenida'''

    system('cls')

    print(f'Bienvenido \033[1m {nombre} \033[0m al software de recetas\n\nEn el encontraras {cantidad} recetas\n\nQue deseas hacer?\n\nElige una opción del siguiente \033[1mMenu\033[0m\n')

def cantidad_recetas(ruta):

    '''Esta funcion se encarga de hacer el conteo de las recetas que estan en el directorio de Recetas'''

    #se inicializa un contador
    cantidad = 0
    # se crea una lista vacia
    lista_recetas = []
    #con el bucle recorremos el directorio para obtener la cantidad de archivos .txt que contiene
    for r in Path(ruta).glob('**/*.txt'):

        lista_recetas.append(r)

        cantidad += 1
    #retornamos la cantidad de archivos
    return cantidad

def menu_categorias(ruta):

    '''En esta funcion optenemos la cantidad de opciones con las que el usuario podra navegar y realizar
    diferentes ooperaciones'''
    #se crea una lista vacio
    lista_opciones = []
    #con el bucle obtenemos las diferentes carpetas que estan en el directorio
    for r in Path(ruta).glob('*'):

        lista_opciones.append(r.name)
    #retornamos el listado de carpetas del directorio en una lista
    return lista_opciones

def menu_lectura_receta(categoria, respuesta, ruta):

    '''En esta función podremos leer los dirferntes archivos .txt que esten almacenados en el directorio'''
    #preguntamos al usuario si desea ver los archivos que estan en la elección que realizó
    respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{respuesta}\033[0m S/N: ').upper()
    #con el bucle hacemos la comprobación de que halla ingresado un caracter valido
    while respuesta1 not in ['N', 'S']:

        print('\nNo has ingresado un caracter valido')

        respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()
        
    if respuesta1 == 'S':
        #tenemos la ruta completa para poder acceder a los archivos .txt
        resultado_categoria1 = ruta / respuesta
        #creamos una lista vacia
        recetas2 = []
        #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
        for recetas1 in resultado_categoria1.glob('*.txt'):

            recetas2.append(recetas1.name)
        #con el bucle se valida que la si la lista esta vacia
        while not recetas2:

            system('cls')

            print(f'\nNo hay recetas para mostrar en \033[1m{respuesta}\033[0m')
            # se le pide al usuario que escoja de nuevo un directorio
            print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')
            # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
            for i,r in enumerate(categoria, start=1):

                lista = [f'{i} = {r}']

                print(''.join(lista))

            opcion = input('\nElige una opción: ')
            # se convierte la opcion del usuario a entero para que podamos obener el nombre de la lista y se le muestra que ha elegido
            opcion2 = categoria[int(opcion) -1]

            print(f'\nHas elegido \033[1m{opcion2}\033[0m')
            #con el bucle se verifica si es un numero lo que el usurio ha ingresado
            while not opcion.isnumeric():

                print('\nLo que has ingresado no es un número intenta de nuevo')

                opcion = input('\nElige una opción: ')
            # se vonvierte la opcion ingresada por el usuario a entero par con el condicional if verificar si la categoria existe
            opcion = int(opcion)

            if opcion > len(categoria) or opcion <= 0:

                print('\nLa categoria seleccionada no existe')

                return
    
            resultado_categoria = categoria[opcion -1]

            respuesta = input(f'\nDeseas ver las recetas que contiene {resultado_categoria} S/N: ').upper()

            while respuesta not in ['N', 'S']:

                print('\nNo has ingresado un caracter valido')

                respuesta = input(f'\nDeseas ver las recetas que contiene {resultado_categoria} S/N: ').upper()
        
            if respuesta == 'S':

                resultado_categoria1 = Path(Path.home(), 'Recetas', resultado_categoria)

                recetas2 = []

                for recetas1 in resultado_categoria1.glob('*.txt'):

                    recetas2.append(recetas1.name)

                for i,r in enumerate(recetas2, start=1):

                    lista = [f'{i} = {r}']

                    print(''.join(lista))

                opcion = input('\nElige una opción: ')

                while not opcion.isnumeric():

                    print('\nLo que has ingresado no es un número intenta de nuevo')

                    opcion = input('\nElige una opción: ')

                opcion = int(opcion)

                if opcion > len(recetas2) or opcion <= 0:

                    print('\nLa receta seleccionada no existe')

                    return
            
                receta = recetas2[opcion - 1]

                archivo = Path(Path.home(), 'Recetas', resultado_categoria, receta)

                if archivo.is_file():

                    print(archivo.stem)

                    archivo = archivo.open('r')

                    print(archivo.read())

                    respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                    system('cls')

                    while respuesta == 'S':

                        resultado_categoria1 = Path(Path.home(), 'Recetas', resultado_categoria)

                        recetas2 = []

                        for recetas1 in resultado_categoria1.glob('*.txt'):

                            recetas2.append(recetas1.name)

                        for i,r in enumerate(recetas2, start=1):

                            lista = [f'{i} = {r}']

                            print(''.join(lista))

                        opcion = input('\nElige una opción: ')

                        while not opcion.isnumeric():

                            print('\nLo que has ingresado no es un número intenta de nuevo')

                            opcion = input('\nElige una opción: ')

                        opcion = int(opcion)

                        if opcion > len(recetas2) or opcion <= 0:
                            
                            print('\nLa receta seleccionada no existe')

                            return
            
                        receta = recetas2[opcion - 1]

                        archivo = Path(Path.home(), 'Recetas', resultado_categoria, receta)

                        if archivo.is_file():

                            print(archivo.stem)

                            archivo = archivo.open('r')

                            print(archivo.read())

                            respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                        system('cls')

                    if respuesta == 'N':

                        entrada_sistema() 

        for i,r in enumerate(recetas2, start=1):

            lista = [f'{i} = {r}']

            print(''.join(lista))

        opcion = input('\nElige una opción: ')

        while not opcion.isnumeric():

            print('\nLo que has ingresado no es un número intenta de nuevo')

            opcion = input('\nElige una opción: ')

        opcion = int(opcion)

        if opcion > len(recetas2) or opcion <= 0:

            print('\nLa receta seleccionada no existe')

            return
            
        receta = recetas2[opcion - 1]

        archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

        if archivo.is_file():

            print(archivo.stem)

            archivo = archivo.open('r')

            print(archivo.read())

            respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

            system('cls')

            while respuesta == 'S':

                for i,r in enumerate(recetas2, start=1):

                    lista = [f'{i} = {r}']

                    print(''.join(lista))

                opcion = input('\nElige una opción: ')

                while not opcion.isnumeric():

                    print('\nLo que has ingresado no es un número intenta de nuevo')

                    opcion = input('\nElige una opción: ')

                opcion = int(opcion)

                if opcion > len(recetas2) or opcion <= 0:

                    print('\nLa receta seleccionada no existe')

                    return
            
                receta = recetas2[opcion - 1]

                archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                if archivo.is_file():

                    print(archivo.stem)

                    archivo = archivo.open('r')

                    print(archivo.read())

                    respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                    system('cls')

            else:

                salir = input('Deseas salir del sistema? s/n. ').upper()

                while salir == 'S':

                    salir_sistema()

                else: 

                    salir = input('Deseas regresar al menu principal? s/n. ').upper()

                    while salir == 'S':

                        entrada_sistema()

                    else:

                        salir_sistema()
            
    else:

        entrada_sistema() 

def crear_receta_directorio (respuesta):

    respuesta1 = input(f'\nDeseas Crear una nueva receta a {respuesta} S/N: ').upper()

    while respuesta1 not in ['N', 'S']:

        print('\nNo has ingresado un caracter valido')

        respuesta1 = input(f'\nDeseas agregar una nueva receta a {respuesta} S/N: ').upper()

    if respuesta1 == 'S':

        archivo_nuevo = input('\nDigita el nombre con el que vas a guardar tu receta y le pones la terminacion \033[1m.txt\033[0m: ')

        while not archivo_nuevo.endswith('.txt'):
            
            print('\nEl archivo debe tener la terminacion \033[1m.txt\033[0m')
            
            archivo_nuevo = input('\nDigita el nombre con el que vas a guardar tu receta y le pones la terminacion \033[1m.txt\033[0m: ')

        ruta = Path(Path.home(), 'Recetas', respuesta)

        ruta = ruta / archivo_nuevo

        mi_archivo = open(ruta, 'w')

        ingredientes = []

        titulo = mi_archivo.write(input("\nIngresa el titulo de la receta: "))

        titulo = mi_archivo.write( f"{titulo}\n\nIngredientes\n\n")

        desicion =input('\nDeseas agregar los ingredientes s/n: ').upper()

        system('cls')

        while desicion not in ['N', 'S']:

            print('\nNo has ingresado un caracter valido')

            desicion =input('\ndeseas agregar los ingredientes s/n: ').upper()

            system('cls')

        while desicion == 'S':

            ingredientes.append(input('\nIngresa los ingredientes de la receta\033[1m uno a uno:\033[0m \n\n'))
            
            desicion =input('\ndeseas agregar mas ingredientes s/n: ').upper()

            system('cls')
           
        for i, v in enumerate(ingredientes, start = 1):
                
            lista = [f'* {v}\n']

            ingredientes = mi_archivo.write(''.join(lista))
            
        mi_archivo.write('\n\nPreparacion\n\n')

        mi_archivo.write(input('\nIngresa la preparacion de la receta: \n\n'))

        system('cls')

        print('\nLa receta se ha creado con exito')

        mi_archivo.close()

        respuesta1 = input(f'Deseas agregar una nueva receta a {respuesta} S/N: ').upper()

        system('cls')

        while respuesta1 == 'S':

            archivo_nuevo = input('\nDigita el nombre con el que vas a guardar tu receta y le pones la terminacion \033[1m.txt\033[0m: ')

            while not archivo_nuevo.endswith('.txt'):
            
                print('\nEl archivo debe tener la terminacion \033[1m.txt\033[0m')
            
                archivo_nuevo = input('\nDigita el nombre con el que vas a guardar tu receta y le pones la terminacion \033[1m.txt\033[0m: ')

            ruta = Path(Path.home(), 'Recetas', respuesta)

            ruta = ruta / archivo_nuevo

            mi_archivo = open(ruta, 'w')

            ingredientes = []

            titulo = mi_archivo.write(input("\nIngresa el titulo de la receta: "))

            titulo = mi_archivo.write( f"{titulo}\n\nIngredientes\n\n")

            desicion =input('\nDeseas agregar los ingredientes s/n: ').upper()

            while desicion not in ['N', 'S']:

                print('\nNo has ingresado un caracter valido')

                desicion =input('\ndeseas agregar los ingredientes s/n: ').upper()

            while desicion == 'S':

                ingredientes.append(input('\nIngresa los ingredientes de la receta\033[1m uno a uno:\033[0m \n\n'))
                
                desicion =input('\ndeseas agregar mas ingredientes s/n: ').upper()

                system('cls')
            
            for i, v in enumerate(ingredientes, start = 1):
                    
                lista = [f'* {v}\n']

                ingredientes = mi_archivo.write(''.join(lista))
                
            mi_archivo.write('\n\nPreparacion\n\n')

            mi_archivo.write(input('\nIngresa la preparacion de la receta: \n\n'))

            system('cls')

            print('\nLa receta se ha creado con exito\n')

            mi_archivo.close()

            respuesta2 = input(f'Deseas agregar una nueva receta a {respuesta} S/N: ').upper()

            print(respuesta2)

            if respuesta2 == 'N':

                salir = input('Deseas salir del sistema? s/n. ').upper()

                if salir == 'S':

                    salir_sistema()

                elif salir == 'N': 

                    salir = input('Deseas regresar al menu principal? s/n. ').upper()

                    if salir == 'S':

                        entrada_sistema()

                    else:

                        salir = input('Deseas salir del sistema? s/n. ').upper()

                        if salir == 'S':

                            salir_sistema()

        if respuesta1 == 'N':

                salir = input('Deseas salir del sistema? s/n. ').upper()

                if salir == 'S':

                    salir_sistema()

                elif salir == 'N': 

                    salir = input('Deseas regresar al menu principal? s/n. ').upper()

                    if salir == 'S':

                        entrada_sistema()

                    else:

                        salir = input('Deseas salir del sistema? s/n. ').upper()

                        if salir == 'S':

                            salir_sistema()

    else:

        salir = input('Deseas salir del sistema? s/n. ').upper()

        if salir == 'S':

            salir_sistema()

        else: 

            salir = input('Deseas regresar al menu principal? s/n. ').upper()

            if salir == 'S':

                entrada_sistema()

            elif salir == 'N':

                salir = input('Deseas salir del sistema? s/n. ').upper()

                if salir == 'S':

                    salir_sistema()

def crear_directorio():

    respuesta = input('\nDeseas crear un directorio s/n: ').upper()

    while respuesta not in ['N', 'S']:

        print('\nHas ingresado un caracter no valido')

        respuesta = input('\nDeseas crear un directorio s/n: ').upper()

    while respuesta == 'S':

        directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

        ruta = Path(Path.home(), 'Recetas', directorio)

        os.makedirs(ruta)

        print('\nEl directorio se ha creado con exito')

        respuesta = input('\nDeseas crear un directorio s/n: ').upper()

        system('cls')

        while respuesta == 'N':

            salir = input('\nDeseas salir del sistema? s/n. ').upper()

            if salir == 'S':

                salir_sistema()

            elif salir == 'N': 

                salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                if salir == 'S':

                    entrada_sistema()

                else:

                    respuesta = input('\nDeseas crear un directorio s/n: ').upper()

                    if respuesta == 'S':

                        directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

                        ruta = Path(Path.home(), 'Recetas', directorio)

                        os.makedirs(ruta)

                        print('\nEl directorio se ha creado con exito')

                        respuesta = input('\nDeseas crear un directorio s/n: ').upper()

                        while respuesta == 'S':

                            directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

                            ruta = Path(Path.home(), 'Recetas', directorio)

                            os.makedirs(ruta)

                            print('\nEl directorio se ha creado con exito')

                            respuesta = input('\nDeseas crear un directorio s/n: ').upper()

                            system('cls')
                    
                    else:

                        print('\nSi eliges \033[1mN\033[0m saldras del sistema')
            
                        salir = input('Deseas regresar al menu principal? s/n. ').upper()

                        if salir == 'S':

                            entrada_sistema()

                        else:

                            salir_sistema()
        
        if respuesta == 'N':

            ruta = Path(Path.home(), 'Recetas')

            respuesta = input('\nDeseas crear un directorio s/n: ').upper()

            while respuesta not in ['N', 'S']:

                print('\nHas ingresado un caracter no valido')

                respuesta = input('\nDeseas crear un directorio s/n: ').upper()

            while respuesta == 'S':

                directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

                os.makedirs(ruta)

                print('\nEl directorio se ha creado con exito')

                respuesta = input('\nDeseas crear un directorio s/n: ').upper()

                system('cls')
    
    if respuesta == 'N':

        salir = input('Deseas salir del sistema? s/n. ').upper()

        if salir == 'S':

            salir_sistema()

        elif salir == 'N': 

            salir = input('Deseas regresar al menu principal? s/n. ').upper()

            if salir == 'S':

                entrada_sistema()

            else:

                respuesta = input('\nDeseas crear un directorio s/n: ').upper()

                if respuesta == 'S':

                    directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

                    ruta = Path(Path.home(), 'Recetas', directorio)

                    os.makedirs(ruta)

                    print('\nEl directorio se ha creado con exito')

                    respuesta = input('\nDeseas crear un directorio s/n: ').upper()

                    while respuesta == 'S':

                        directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

                        ruta = Path(Path.home(), 'Recetas', directorio)

                        os.makedirs(ruta)

                        system('cls')

                        print('\nEl directorio se ha creado con exito')

                        respuesta = input('\nDeseas crear un directorio s/n: ').upper()

                    if respuesta == 'N':

                        salir = input('\nDeseas salir del sistema? s/n. ').upper()

                        if salir == 'S':

                            salir_sistema()

                        elif salir == 'N': 

                            print('\n Si eliges \033[1m N \033[0m saldras del sistema')

                            salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                            if salir == 'S':

                                entrada_sistema()

                            else:

                                salir_sistema()
                
                else:

                    print('\nSi eliges \033[1mN\033[0m saldras del sistema')
            
                    salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                    if salir == 'S':

                        entrada_sistema()

                    else:

                        salir_sistema()
  
def eliminar_receta (categoria, respuesta):

    respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()

    while respuesta1 not in ['N', 'S']:

        print('\nNo has ingresado un caracter valido')

        respuesta1 = input(f'Deseas ver las recetas que contiene {respuesta} S/N: ').upper()
        
    if respuesta1 == 'S':

        resultado_categoria1 = Path(Path.home(), 'Recetas', respuesta)

        recetas2 = []

        for recetas1 in resultado_categoria1.glob('*.txt'):

            recetas2.append(recetas1.name)

        while not recetas2:

            system('cls')

            print("\nNo hay recetas para mostrar")

            print('\nElige otra categoria la anterior esta vacia')

            opcion3 = input('\nSi prefieres puedes regresar al menu principal con\033[1m S \033[0mo regresar y elegir otra categoria con\033[1m N \033[0ms/n: ').upper()

            while opcion3 not in ['N', 'S']:

                    print('\nNo has ingresado un caracter valido')

                    opcion3 = input('\nVuelve a intentar s/n: \n').upper()

            if opcion3 == 'S':

                entrada_sistema()

            else:

                print('\n')

                for i,r in enumerate(categoria, start=1):

                    lista = [f'{i} = {r}']

                    print(''.join(lista))

                opcion = input('\nElige una opción: ')

                while not opcion.isnumeric():

                    print('\nLo que has ingresado no es un número intenta de nuevo')

                    opcion = input('\nElige una opción: ')

                opcion = int(opcion)

                opcion2 = categoria[opcion -1]

                print(f'\nHas elegido \033[1m{opcion2}\033[0m')

                if opcion > len(categoria) or opcion <= 0:

                    print('\nLa categoria seleccionada no existe')

                    return
        
                resultado_categoria = categoria[opcion -1]

                respuesta = input(f'\nDeseas ver las recetas que contiene {resultado_categoria} S/N: ').upper()

                while respuesta not in ['N', 'S']:

                    print('\nNo has ingresado un caracter valido')

                    respuesta = input(f'Deseas ver las recetas que contiene {resultado_categoria} S/N: ').upper()
            
                if respuesta == 'S':

                    resultado_categoria1 = Path(Path.home(), 'Recetas', resultado_categoria)

                    for recetas1 in resultado_categoria1.glob('*.txt'):

                        recetas2.append(recetas1.name)

                else: 

                    entrada_sistema()

        else:
        # Imprime las recetas
            for i, r in enumerate(recetas2, start=1):

                lista = [f'{i} = {r}']

                print(''.join(lista))

            opcion = input('\nElige una opción: ')

            while not recetas2:

                system('cls')

                print("\nNo hay recetas para mostrar")

                for i,r in enumerate(categoria, start=1):

                    lista = [f'{i} = {r}']

                    print(''.join(lista))

                opcion = input('\nElige una opción: ')

                while not opcion.isnumeric():

                    print('\nLo que has ingresado no es un número intenta de nuevo')

                    opcion = input('\nElige una opción: ')

                opcion = int(opcion)

                opcion2 = categoria[opcion -1]

                print(f'\nHas elegido \033[1m{opcion2}\033[0m')

                if opcion > len(categoria) or opcion <= 0:

                    print('\nLa categoria seleccionada no existe')

                    return
            
                resultado_categoria = categoria[opcion -1]

                respuesta = input(f'\nDeseas ver las recetas que contiene {resultado_categoria} S/N: ').upper()

                while respuesta not in ['N', 'S']:

                    print('\nNo has ingresado un caracter valido')

                    respuesta = input(f'Deseas ver las recetas que contiene {resultado_categoria} S/N: ').upper()
                
                if respuesta == 'S':

                    resultado_categoria1 = Path(Path.home(), 'Recetas', resultado_categoria)

                    for recetas1 in resultado_categoria1.glob('*.txt'):

                        recetas2.append(recetas1.name)

                else: 

                    entrada_sistema()

            else:
            # Imprime las recetas
                for i, r in enumerate(recetas2, start=1):

                    lista = [f'{i} = {r}']

                    print(''.join(lista))

                opcion = input('\nElige una opción: ')

                while not opcion.isnumeric():

                    print('\nLo que has ingresado no es un número intenta de nuevo')

                    opcion = input('\nElige una opción: ')

                opcion = int(opcion)

                if opcion > len(recetas2) or opcion <= 0:

                    print('\nLa receta seleccionada no existe')

                    return
                    
                receta = recetas2[opcion - 1]

                archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                if archivo.is_file():

                    archivo1 = archivo.stem

                    archivos = input(f'\nSeguro quieres borrar {archivo1} s/n: ').upper()

                    if archivos == 'S':

                        os.remove(archivo)

                        system('cls')

                        print('\nEl archivo se ha borrado del sistema con exito')

                        borrado = input('\nDeseas borrar otro archivo. s/n: ').upper()

                        if borrado == 'S':

                            respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()
                
                            if respuesta1 == 'S':

                                resultado_categoria1 = Path(Path.home(), 'Recetas', respuesta)

                            recetas2 = []

                            for recetas1 in resultado_categoria1.glob('*.txt'):

                                recetas2.append(recetas1.name)

                            for i, r in enumerate(recetas2, start=1):

                                lista = [f'{i} = {r}']

                                print(''.join(lista))

                            opcion = input('\nElige una opción: ')

                            while not opcion.isnumeric():

                                print('\nLo que has ingresado no es un número intenta de nuevo')

                                opcion = input('\nElige una opción: ')

                            opcion = int(opcion)

                            if opcion > len(recetas2) or opcion <= 0:

                                print('\nLa receta seleccionada no existe')

                                return
                    
                            receta = recetas2[opcion - 1]

                            archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                            if archivo.is_file():

                                archivo1 = archivo.stem

                                archivos = input(f'\nSeguro quieres borrar {archivo1} s/n: ').upper()

                                if archivos == 'S':

                                    os.remove(archivo)

                                    system('cls')

                                    print('\nEl archivo se ha borrado del sistema con exito')

                                    borrado = input('\nDeseas borrar otro archivo. s/n: ').upper()
                                    
                                if borrado == 'N':

                                    print('\nEl archivo no se borrara del sistema')

                                    salir = input('\nDeseas salir del sistema? s/n. ').upper()

                                    if salir == 'S':

                                        salir_sistema()

                                    else: 

                                        print('\nSi eliges \033[1mN\033[0m saldras del sistema')

                                        salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                                        while salir == 'S':

                                            entrada_sistema()

                                        else:

                                            salir_sistema()

                        if borrado == 'N':

                            print('\nEl archivo no se borrara del sistema')

                            salir = input('\nDeseas salir del sistema? s/n. ').upper()

                            if salir == 'S':

                                salir_sistema()

                            else: 

                                print('\nSi eliges \033[1mN\033[0m saldras del sistema')

                                salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                                while salir == 'S':

                                    entrada_sistema()

                                else:

                                    salir_sistema()

                    else:

                        print('\nEl archivo no se borrara del sistema')

                        salir = input('\nDeseas salir del sistema? s/n. ').upper()

                        while salir == 'S':

                            salir_sistema()

                        else: 

                            print('\nSi eliges \033[1mN\033[0m saldras del sistema')

                            salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                            while salir == 'S':

                                entrada_sistema()

                            else:

                                salir_sistema()
    
    if respuesta1 == 'N':

        salir = input('\nDeseas salir del sistema? s/n. ').upper()

        while salir == 'S':

            salir_sistema()

        else:

            respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()

            while respuesta1 not in ['N', 'S']:

                print('\nNo has ingresado un caracter valido')

                respuesta1 = input(f'Deseas ver las recetas que contiene {respuesta} S/N: ').upper()
                
            if respuesta1 == 'S':

                resultado_categoria1 = Path(Path.home(), 'Recetas', respuesta)

                recetas2 = []

                for recetas1 in resultado_categoria1.glob('*.txt'):

                    recetas2.append(recetas1.name)

                while not recetas2:

                    system('cls')

                    print("\nNo hay recetas para mostrar")

                    for i,r in enumerate(categoria, start=1):

                        lista = [f'{i} = {r}']

                        print(''.join(lista))

                    opcion = input('\nElige una opción: ')

                    while not opcion.isnumeric():

                        print('\nLo que has ingresado no es un número intenta de nuevo')

                        opcion = input('\nElige una opción: ')

                    opcion = int(opcion)

                    opcion2 = categoria[opcion -1]

                    print(f'\nHas elegido \033[1m{opcion2}\033[0m')

                    if opcion > len(categoria) or opcion <= 0:

                        print('\nLa categoria seleccionada no existe')

                        return
            
                    resultado_categoria = categoria[opcion -1]

                    respuesta = input(f'\nDeseas ver las recetas que contiene {resultado_categoria} S/N: ').upper()

                    while respuesta not in ['N', 'S']:

                        print('\nNo has ingresado un caracter valido')

                        respuesta = input(f'Deseas ver las recetas que contiene {resultado_categoria} S/N: ').upper()
                
                    if respuesta == 'S':

                        resultado_categoria1 = Path(Path.home(), 'Recetas', resultado_categoria)

                        for recetas1 in resultado_categoria1.glob('*.txt'):

                            recetas2.append(recetas1.name)

                    else: 

                        entrada_sistema()

                else:
                # Imprime las recetas
                    for i, r in enumerate(recetas2, start=1):

                        lista = [f'{i} = {r}']

                        print(''.join(lista))

                    opcion = input('\nElige una opción: ')

                    while not opcion.isnumeric():

                        print('\nLo que has ingresado no es un número intenta de nuevo')

                        opcion = input('\nElige una opción: ')

                    opcion = int(opcion)

                    if opcion > len(recetas2) or opcion <= 0:

                        print('\nLa receta seleccionada no existe')

                        return
                    
                    receta = recetas2[opcion - 1]

                    archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                    if archivo.is_file():

                        archivo1 = archivo.stem

                        archivos = input(f'\nSeguro quieres borrar {archivo1} s/n: ').upper()

                        if archivos == 'S':

                            os.remove(archivo)

                            system('cls')

                            print('\nEl archivo se ha borrado del sistema con exito')

                            borrado = input('\nDeseas borrar otro archivo. s/n: ').upper()

                            if borrado == 'S':

                                respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()
                
                                if respuesta1 == 'S':

                                    resultado_categoria1 = Path(Path.home(), 'Recetas', respuesta)

                                recetas2 = []

                                for recetas1 in resultado_categoria1.glob('*.txt'):

                                    recetas2.append(recetas1.name)

                                for i, r in enumerate(recetas2, start=1):

                                    lista = [f'{i} = {r}']

                                    print(''.join(lista))

                                opcion = input('\nElige una opción: ')

                                while not opcion.isnumeric():

                                    print('\nLo que has ingresado no es un número intenta de nuevo')

                                    opcion = input('\nElige una opción: ')

                                opcion = int(opcion)

                                if opcion > len(recetas2) or opcion <= 0:

                                    print('\nLa receta seleccionada no existe')

                                    return
                    
                                receta = recetas2[opcion - 1]

                                archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                                if archivo.is_file():

                                    archivo1 = archivo.stem

                                    archivos = input(f'\nSeguro quieres borrar {archivo1} s/n: ').upper()

                                    if archivos == 'S':

                                        os.remove(archivo)

                                        system('cls')

                                        print('\nEl archivo se ha borrado del sistema con exito')

                                        borrado = input('\nDeseas borrar otro archivo. s/n: ').upper()
                                    
                                    if borrado == 'N':

                                        print('\nEl archivo no se borrara del sistema')

                                        salir = input('\nDeseas salir del sistema? s/n. ').upper()

                                        if salir == 'S':

                                            salir_sistema()

                                        else: 

                                            print('\nSi eliges \033[1mN\033[0m saldras del sistema')

                                            salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                                            while salir == 'S':

                                                entrada_sistema()

                                            else:

                                                salir_sistema()

                            if borrado == 'N':

                                print('\nEl archivo no se borrara del sistema')

                                salir = input('\nDeseas salir del sistema? s/n. ').upper()

                                if salir == 'S':

                                    salir_sistema()

                                else: 

                                    print('\nSi eliges \033[1mN\033[0m saldras del sistema')

                                    salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                                    while salir == 'S':

                                        entrada_sistema()

                                    else:

                                        salir_sistema()

                        else:

                            print('\nEl archivo no se borrara del sistema')

                            salir = input('\nDeseas salir del sistema? s/n. ').upper()

                            while salir == 'S':

                                salir_sistema()

                            else: 

                                print('\nSi eliges \033[1mN\033[0m saldras del sistema')

                                salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                                while salir == 'S':

                                    entrada_sistema()

                                else:

                                    salir_sistema()

    else:

        salir = input('\nDeseas salir del sistema? s/n. ').upper()

        while salir == 'S':

            salir_sistema()

        print('\nSi eliges \033[1mN\033[0m saldras del sistema') 

        salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

        while salir == 'S':

            entrada_sistema()

        else:

            salir_sistema()

def eliminar_categoria (categoria, resultado):

    respuesta = input(f'\nDeseas eliminar el directorio\033[1m {resultado} \033[0ms/n: ').upper()

    ruta = Path(Path.home(), 'Recetas')

    if respuesta == 'S':

        nombre = resultado

        ruta1 = ruta / nombre

        if ruta1.is_dir():

            if not os.listdir(ruta1):

                os.rmdir(ruta1)

                print('\nEl directorio se ha eliminado con exito')

                categoria.remove(resultado)

            else:

                respuesta2 = input('\nEl directorio no esta vacio, ¿deseas eliminarlo de todas formas s/n: ').upper()

                if respuesta2 == 'S':

                    shutil.rmtree(ruta1)
                    
                    print('\nEl directorio se ha eliminado con exito')

                    categoria.remove(resultado)

                else:

                    print('\nEl directorio no se ha eliminado')

        else:

            print('\nEl directorio no existe')

        respuesta = input('\nDeseas eliminar otro directorio s/n: ').upper()

        system('cls')

        while respuesta not in  ['N', 'S']:

            print('\nHas ingresado un caracter no valido')

            respuesta = input('\nDeseas eliminar otro directorio s/n: ').upper()

        while respuesta == 'S':

            ruta = Path(Path.home(), 'Recetas')

            for i,r in enumerate(categoria, start=1):

                lista = [f'{i} = {r}']

                print(''.join(lista))

            opcion = input('\nElige una opcion: ')

            while not opcion.isnumeric():

                print('\nEL digito ingresado no es un numero')

                opcion = input('\nElige una opcion: ')

            opcion = int(opcion)

            opcion2 = categoria[opcion -1]

            print(f'\nHas elegido \033[1m{opcion2}\033[0m')

            respuesta = input(f'\nDeseas eliminar el directorio\033[1m {opcion2} \033[0ms/n: ').upper()

            while respuesta not in  ['N', 'S']:

                print('\nHas ingresado un caracter no valido')

                respuesta = input('\nDeseas eliminar otro directorio s/n: ').upper()

            if respuesta == 'S':

                nombre = resultado

                ruta1 = ruta / opcion2

                if ruta1.is_dir():

                    if not os.listdir(ruta1):

                        os.rmdir(ruta1)

                        print('\nEl directorio se ha eliminado con exito')

                        categoria.remove(opcion2)

                    else:

                        respuesta2 = input('\nEl directorio no esta vacio, ¿deseas eliminarlo de todas formas s/n: ').upper()

                        if respuesta2 == 'S':

                            shutil.rmtree(ruta1)
                            
                            print('\nEl directorio se ha eliminado con exito')

                            categoria.remove(opcion2)

                        else:

                            print('\nEl directorio no se ha eliminado')

                else:

                    print('\nEl directorio no existe')

            respuesta = input('\nDeseas eliminar otro directorio s/n: ').upper()

            system('cls')

        else:

            salir = input('\nDeseas salir del sistema? s/n. ').upper()

            if salir == 'S':

                salir_sistema()

            elif salir == 'N': 

                salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                while salir not in  ['N', 'S']:

                    print('\nHas ingresado un caracter no valido')

                    salir = input('\nDeseas regresar al menu principal? s/n. ').upper()
                
                if salir == 'S':

                    entrada_sistema()

                if salir == 'N':

                    respuesta = input('\nDeseas eliminar otro directorio s/n: ').upper()

                    system('cls')

                    while respuesta not in  ['N', 'S']:

                        print('\nHas ingresado un caracter no valido')

                        respuesta = input('\nDeseas eliminar otro directorio s/n: ').upper()

                    while respuesta == 'S':

                        ruta = Path(Path.home(), 'Recetas')

                        for i,r in enumerate(categoria, start=1):

                            lista = [f'{i} = {r}']

                            print(''.join(lista))

                        opcion = input('\nElige una opcion: ')

                        while not opcion.isnumeric():

                            print('\nEL digito ingresado no es un numero')

                            opcion = input('\nElige una opcion: ')

                        opcion = int(opcion)

                        opcion2 = categoria[opcion -1]

                        print(f'\nHas elegido \033[1m{opcion2}\033[0m')

                        respuesta = input(f'\nDeseas eliminar el directorio\033[1m {opcion2} \033[0ms/n: ').upper()

                        while respuesta not in  ['N', 'S']:

                            print('\nHas ingresado un caracter no valido')

                            respuesta = input('\nDeseas eliminar otro directorio s/n: ').upper()

                        if respuesta == 'S':

                            nombre = resultado

                            ruta1 = ruta / opcion2

                            if ruta1.is_dir():

                                if not os.listdir(ruta1):

                                    os.rmdir(ruta1)

                                    print('\nEl directorio se ha eliminado con exito')

                                    categoria.remove(opcion2)

                                else:

                                    respuesta2 = input('\nEl directorio no esta vacio, ¿deseas eliminarlo de todas formas s/n: ').upper()

                                    if respuesta2 == 'S':

                                        shutil.rmtree(ruta1)
                                        
                                        print('\nEl directorio se ha eliminado con exito')

                                        categoria.remove(opcion2)

                                    else:

                                        print('\nEl directorio no se ha eliminado')

                            else:

                                print('\nEl directorio no existe')

                        respuesta = input('\nDeseas eliminar otro directorio s/n: ').upper()

                        system('cls')

                    if respuesta == 'N':

                        print('\nSi eliges \033[1mN\033[0m saldras del sistema') 

                        salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                        while salir not in  ['N', 'S']:

                            print('\nHas ingresado un caracter no valido')

                            salir = input('\nDeseas regresar al menu principal? s/n. ').upper()
                        
                        if salir == 'S':

                            entrada_sistema()

                        else:

                            salir_sistema()

            else:

                salir = input('\nDeseas salir del sistema? s/n. ').upper()

                while salir == 'S':

                    salir_sistema()

                print('\nSi eliges \033[1mN\033[0m saldras del sistema') 

                salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                while salir == 'S':

                    entrada_sistema()

                else:

                    salir_sistema()
    
    else:

        salir = input('\nDeseas salir del sistema? s/n. ').upper()

        while salir == 'S':

            salir_sistema()

        print('\nSi eliges \033[1mN\033[0m saldras del sistema') 

        salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

        while salir == 'S':

            entrada_sistema()

        else:

            salir_sistema()

def salir_sistema ():

    system('cls')

    print('\nHas Salido del Sistema')

    print('\n!Hasta pronto¡\n')

    exit()

def comprobar_categoria (categoria):

    if not categoria:

        print('\nNo hay categorias disponibles')

        return

    print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

    for i,r in enumerate(categoria, start=1):

        lista = [f'{i} = {r}']

        print(''.join(lista))

    opcion = input('\nElige una opción: ')

    while not opcion.isnumeric():

        print('\nLo que has ingresado no es un número intenta de nuevo')

        opcion = input('\nElige una opción: ')

    opcion = int(opcion)

    if opcion > len(categoria) or opcion <= 0:

        print('La categoria seleccionada no existe')

        return

    opcion2 = categoria[opcion -1]

    print(f'\nHas elegido \033[1m{opcion2}\033[0m')

    if opcion > len(categoria) or opcion <= 0:

        print('La categoria seleccionada no existe')

    return opcion2

def entrada_sistema ():

    categoria = menu_categorias(recetario)

    mostrar_bienvenida(nombre, cantidad_recetas(recetario))

    opciones = ['Leer Recetas', 'Crear Receta', 'Crear Categoria', 'Eliminar Receta', 'Eliminar Categoria', 'Salir del Sistema']

    for i, r in enumerate(opciones, start=1):

        lista =[f'{i} = {r}']

        print(''.join(lista))

    opcion = input('\nElige una opcion: ')

    while not opcion.isnumeric() or int(opcion) not in range(1, 7):

        print('\nLa eleccion no es correcta, intenta de nuevo')
    
        opcion = input('\nElige una opcion: ')
    
    opcion = int(opcion)

    opcion_elegida = opciones[opcion - 1]

    print(f'\nHas elegido \033[1m{opcion_elegida}\033[0m')

    if opcion == 6:

        salir_sistema()

    if opcion == 3:

        crear_directorio()

    respuesta = (comprobar_categoria(categoria))

    match opcion:

        case 1:
                        
            menu_lectura_receta(categoria, respuesta, recetario)

        case 2:

            crear_receta_directorio(respuesta)
                    
        case 4:

            eliminar_receta(categoria, respuesta)

        case 5:

            eliminar_categoria(categoria, respuesta)

        case _:

            print('\nHas elegido un comando incorrecto, intenta de nuevo')

            opcion = input('Elige una opcion: ')

# se declaran variables
nombre = entrada_nombre()

recetario = Path(Path.home(), 'Recetas')

#respuesta = comprobar_categoria(categoria)
entrada_sistema()
#editar_receta(respuesta)


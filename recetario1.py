# se importan las librerias necesarias
import os
from os import system
from pathlib import Path
import shutil
from turtle import home

import path

# funcion para ingresar el nombre del usuario
def entrada_nombre():
    #se le pide al usuario que ingrese su nombre y sera retornado por la función
    nombre = input('Cual es tu nombre: ').title()

    return nombre

# muestra la bienvenida del usuario nuevo
def mostrar_bienvenida_usuario_nuevo (nombre):

    '''se limpia la pantalla al ingresar el usuario y se imprime el mensaje de bienvenida,
    esta función recibe los parametros que vienen de las funciones 
    entrada_nombre y cantidad_recetas para estar en el mensaje de bienvenida'''

    system('cls')

    print(f'Bienvenido \033[1m {nombre} \033[0m al software de recetas')

def mostrar_bienvenida (nombre,cantidad, ruta):

    '''se limpia la pantalla al ingresar el usuario y se imprime el mensaje de bienvenida,
    esta función recibe los parametros que vienen de las funciones 
    entrada_nombre y cantidad_recetas para estar en el mensaje de bienvenida'''

    system('cls')

    # para tener el nombre del directorio de la ruta
    ruta1 = os.path.basename(ruta)

    print(f'Bienvenido \033[1m {nombre} \033[0m al software de recetas\n\nEstas en el directorio\033[1m {ruta1}\033[0m\n\nEn el encontraras {cantidad} recetas\n\nQue deseas hacer?\n\nElige una opción del siguiente \033[1mMenu\033[0m\n')

# esta funcion verifica la cantidad de recetas que el usuario tiene almacenadas
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

# esta funcion lista las categorias que hay en el directorio del usuario
def menu_categorias(ruta):

    '''En esta funcion obtenemos la cantidad de opciones con las que el usuario podra navegar y realizar
    diferentes ooperaciones'''

    #se crea una lista vacio
    lista_opciones = []

    #con el bucle obtenemos las diferentes carpetas que estan en el directorio
    for r in Path(ruta).glob('*'):

        lista_opciones.append(r.name)

    #retornamos el listado de carpetas del directorio en una lista
    return lista_opciones

def menu_lectura_receta(categoria, respuesta, ruta):

    '''En esta función podremos leer los diferntes archivos .txt que esten almacenados en el directorio'''

    system('cls')

    #preguntamos al usuario si desea ver los archivos que estan en la elección que realizó
    respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{respuesta}\033[0m S/N: ').upper()

    #con el bucle hacemos la comprobación de que halla ingresado un caracter valido
    while respuesta1 not in ['N', 'S']:

        print('\nNo has ingresado un caracter valido')

        respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()
        
    while respuesta1 == 'S':

        #tenemos la ruta completa para poder acceder a los archivos .txt
        resultado_categoria1 = Path(ruta, respuesta)

        #creamos una lista vacia
        recetas2 = []

        #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
        for recetas1 in resultado_categoria1.glob('*.txt'):

            recetas2.append(recetas1.name)

        #con el bucle se valida que la si la lista esta vacia
        if not recetas2:

            #limpiamos la pantalla
            system('cls')

            print(f'\nNo hay recetas para mostrar en \033[1m{respuesta}\033[0m')

            print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')
            # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
            for i,r in enumerate(categoria, start=1):

                lista = [f'{i} = {r}']

                print(''.join(lista))

            opcion = input('\nElige una opción: ')

            while not opcion.isnumeric():

                print('\nEl carater ingresado no es valido, intenta de nuevo')

                opcion = input('\nElige una opción: ')

            while int(opcion) > len(categoria) or int(opcion) <= 0:

                print('\nLa eleccion no se encuentra dentro del directorio, intenta de nuevo')

                opcion = input('\nElige una opción: ')
            
            nombre = categoria[int(opcion - 1)]

            print(f'\nHas elegido\033[1m {nombre}\033[0m')

            print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

        #tenemos la ruta completa para poder acceder a los archivos .txt
        resultado_categoria1 = Path(ruta, nombre)

        #creamos una lista vacia
        recetas2 = []

        #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
        for recetas1 in resultado_categoria1.glob('*.txt'):

            recetas2.append(recetas1.name)

        for i,r in enumerate(recetas2, start=1):

            lista = [f'{i} = {r}']

            print(''.join(lista))

        opcion = input('\nElige una opción: ')

        while not opcion.isnumeric() or int(opcion) > len(recetas2) or int(opcion) <= 0:

            print('\nHas seleccionado un número no valido o un caracter no valido')

            print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

            print('\n')

            for i,r in enumerate(recetas2, start=1):

                lista = [f'{i} = {r}']

                print(''.join(lista))

            opcion = input('\nElige una opción: ')
                    
            receta = recetas2[int(opcion) - 1]

            archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

            print('\n')

            if archivo.is_file():

                print(archivo.stem)

                archivo = archivo.open('r')

                print(archivo.read())

            respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

            system('cls')

            if respuesta == 'N':

                print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')
                # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
                for i,r in enumerate(categoria, start=1):

                    lista = [f'{i} = {r}']

                    print(''.join(lista))

                opcion = input('\nElige una opción: ')

                while not opcion.isnumeric():

                    print('\nEl carater ingresado no es valido, intenta de nuevo')

                    opcion = input('\nElige una opción: ')

        
        # else:

        #     receta = recetas2[int(opcion) - 1]

        #     archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

        #     print('\n')

        #     if archivo.is_file():

        #         print(archivo.stem)

        #         archivo = archivo.open('r')

        #         print(archivo.read())

        #     respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

        #     system('cls')

        #     if respuesta == 'N':

        #         print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')
        #         # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
        #         for i,r in enumerate(categoria, start=1):

        #             lista = [f'{i} = {r}']

        #             print(''.join(lista))

        #         opcion = input('\nElige una opción: ')

        #         while not opcion.isnumeric():

        #             print('\nEl carater ingresado no es valido, intenta de nuevo')

        #             opcion = input('\nElige una opción: ')



        
        # resultado_categoria1 = ruta / respuesta

        # #creamos una lista vacia
        # recetas2 = []

        # #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
        # for recetas1 in resultado_categoria1.glob('*.txt'):

        #     recetas2.append(recetas1.name)
        
        

            #si la respuesta es positiva
            # while elige == 'S':

            #     print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

            #     print('\n')

            #     # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
            #     for i,r in enumerate(categoria, start=1):

            #         lista = [f'{i} = {r}']

            #         print(''.join(lista))

            #     opcion = input('\nElige una opción: ')

            #     while not opcion.isnumeric():

            #         print('\nLo que has ingresado no es un número intenta de nuevo')

            #         opcion = input('\nElige una opción: ')

            #     #traemos el nombre que eligio el usaurio y lo imprimimos
            #     nombre = categoria[int(opcion) - 1]

            #     print(f'\nHas elegido \033[1m{nombre}\033[0m')

            #     # guardamos en una variable las recetas que tiene la eleccion del usuario
            #     respuesta1 = input(f'\nDeseas ver las recetas que contiene\033[1m {nombre}\033[0m S/N: ').upper()

                # #con el bucle se valida que la si la lista esta vacia
                # while not recetas2:

                #     #limpiamos la pantalla
                #     system('cls')

                #     print(f'\nNo hay recetas para mostrar en \033[1m{respuesta}\033[0m')

                #     # se le pide al usuario que escoja de nuevo un directorio
                #     elige1 = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                    # #con el bucle verifico la respuesta del usuario
                    # while elige1 not in ['N', 'S']:

                    #     print('\nEl carater ingresado no es valido, intenta de nuevo')

                    #     elige1 = input('\nDeseas ver el menu nuevamente S/N: ').upper()
                


                    # resultado_categoria1 = ruta / respuesta

                    # #creamos una lista vacia
                    # recetas2 = []

                    # #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                    # for recetas1 in resultado_categoria1.glob('*.txt'):

                    #     recetas2.append(recetas1.name)

                
                # elige == elige1



                # se le pide al usuario que escoja de nuevo un directorio
                # elige = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                # #con el bucle verifico la respuesta del usuario
                # while elige not in ['N', 'S']:

                #     print('\nEl carater ingresado no es valido, intenta de nuevo')

                #     elige = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                # #si la respuesta es positiva
                # while elige == 'S':

                #     print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

                #     print('\n')
                    
                #     # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
                #     for i,r in enumerate(categoria, start=1):

                #         lista = [f'{i} = {r}']

                #         print(''.join(lista))

                #     opcion = input('\nElige una opción: ')

                #     # verificamos si la respuesta del usuario es un número
                #     while not opcion.isnumeric():

                #         print('\nLo que has ingresado no es un número intenta de nuevo')

                #         opcion = input('\nElige una opción: ')

                #     #traemos el nombre que eligio el usaurio y lo imprimimos
                #     nombre = categoria[int(opcion) - 1]

                #     print(f'\nHas elegido \033[1m{nombre}\033[0m')

                #     # guardamos en una variable las recetas que tiene la eleccion del usuario
                #     respuesta1 = input(f'\nDeseas ver las recetas que contiene\033[1m {nombre}\033[0m S/N: ').upper()

                #     #con el bucle verifico la respuesta del usuario
                #     while respuesta1 not in ['N', 'S']:

                #         print('\nEl carater ingresado no es valido, intenta de nuevo')

                #         respuesta1 = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                #     # si la respuesta es positiva
                #     if respuesta1 == 'N':

                #         salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #         if salir == 'S':

                #             salir_sistema()

                #     # si la respuesta es negativa
                #     else: 

                #         print('\nSi eliges\033[1m N\033[0m saldras del sistema')

                #         salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #         if salir == 'S':

                #             entrada_sistema()

                #         else:

                #             salir_sistema()
                
                # si la respuesta es negativa
                # if elige == 'N':

                #     salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #     if salir == 'S':

                #         salir_sistema()

                #     else: 

                #         print('\nSi eliges\033[1m N\033[0m saldras del sistema')

                #         salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #         if salir == 'S':

                #             entrada_sistema()

                #         else:

                #             salir_sistema()

                # while respuesta1 == 'S':

                #     #tenemos la ruta completa para poder acceder a los archivos .txt
                #     resultado_categoria1 = ruta / nombre

                #     #creamos una lista vacia
                #     recetas2 = []

                #     #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                #     for recetas1 in resultado_categoria1.glob('*.txt'):

                #         recetas2.append(recetas1.name)

                #     print('\n')

                #     #con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
                #     for i,r in enumerate(recetas2, start=1):

                #         #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                #         lista = [f'{i} = {r}']

                #         print(''.join(lista))

                #     opcion = input('\nElige una opción: ')

                #     #con este bucle verificamos si la opción ingresada es correcta
                #     while not opcion.isnumeric():

                #             print('\nLo que has ingresado no es un número intenta de nuevo')

                #             opcion = input('\nElige una opción: ')

                #     opcion = int(opcion)

                #     #nombre = recetas2(int(opcion) - 1)

                #     print(f'\nHas elegido \033[1m{nombre}\033[0m')

                #     #con este condicional verificamos si la opcion existe
                #     if opcion > len(recetas2) or opcion <= 0:

                #         print('\nLa receta seleccionada no existe')

                #         print(f'\nElige nuevamente del siguiente\033[1m Menú\033[0m')

                #         resultado_categoria1 = ruta / nombre

                #         #creamos una lista vacia
                #         recetas2 = []

                #         #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                #         for recetas1 in resultado_categoria1.glob('*.txt'):

                #             recetas2.append(recetas1.name)

                #         # con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
                #         for i,r in enumerate(recetas2, start=1):

                #             #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                #             lista = [f'\n{i} = {r}']

                #             print(''.join(lista))

                #         opcion = input('\nElige una opción: ')

                #         #con este bucle verificamos si la opción ingresada es correcta
                #         while not opcion.isnumeric():

                #                 print('\nLo que has ingresado no es un número intenta de nuevo')

                #                 opcion = input('\nElige una opción: ')

                #         opcion = int(opcion)
                                
                #     #creamos la variable para almacenar el nombre de la receta
                #     receta = recetas2[opcion - 1]

                #     #creamos la variable para guardar la ruta de la receta
                #     archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                #     #con este condicional verifiamos que si sea un archivo
                #     if archivo.is_file():

                #         #imprimimos el nombre del archivo sin la extención
                #         print(f'\n{archivo.stem}')

                #         #abrimos el archivo en modo lectura
                #         archivo = archivo.open('r')

                #         #mostramos en pantalla el contenido del archivo
                #         print(f'\n{archivo.read()}')

                #         #preguntamos si desea ver otra receta
                #     respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                #     system('cls')

                #     while respuesta not in ['N', 'S']:

                #         print('\nEl caracter ingresado no es valido, intenta de nuevo')

                #         respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                #     if respuesta == 'N':

                #         salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #         if salir == 'S':

                #             salir_sistema()

                #         else: 

                #             print('\nSi eliges\033[1m N\033[0m saldras del sistema')

                #             salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #             if salir == 'S':

                #                 entrada_sistema()

                #             else:

                #                 salir_sistema()

                # #comprobamos si el nombre esta en la lista y le hacemos otra pregunta
                # while nombre:

                #     respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{nombre}\033[0m S/N: ').upper()

                #     while respuesta1 not in ['N', 'S']:

                #         print('\nNo has ingresado un caracter valido')

                #         respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()
                        
                #     while respuesta1 == 'S':

                #         #tenemos la ruta completa para poder acceder a los archivos .txt
                #         resultado_categoria1 = ruta / nombre

                #         #creamos una lista vacia
                #         recetas2 = []

                #         #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                #         for recetas1 in resultado_categoria1.glob('*.txt'):

                #             recetas2.append(recetas1.name)

                #         # con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
                #         for i,r in enumerate(recetas2, start=1):

                #             #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                #             lista = [f'\n{i} = {r}']

                #             print(''.join(lista))

                #         opcion = input('\nElige una opción: ')

                #         #con este bucle verificamos si la opción ingresada es correcta
                #         while not opcion.isnumeric():

                #                 print('\nLo que has ingresado no es un número intenta de nuevo')

                #                 opcion = input('\nElige una opción: ')

                #         opcion = int(opcion)

                #         #con este condicional verificamos si la opcion existe
                #         if opcion > len(recetas2) or opcion <= 0:

                #             print('\nLa receta seleccionada no existe')

                #             print(f'\nElige nuevamente del siguiente\033[1m Menú\033[0m')

                #             resultado_categoria1 = ruta / nombre

                #             #creamos una lista vacia
                #             recetas2 = []

                #             #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                #             for recetas1 in resultado_categoria1.glob('*.txt'):

                #                 recetas2.append(recetas1.name)

                #             # con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
                #             for i,r in enumerate(recetas2, start=1):

                #                 #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                #                 lista = [f'\n{i} = {r}']

                #                 print(''.join(lista))

                #             opcion = input('\nElige una opción: ')

                #             #con este bucle verificamos si la opción ingresada es correcta
                #             while not opcion.isnumeric():

                #                     print('\nLo que has ingresado no es un número intenta de nuevo')

                #                     opcion = input('\nElige una opción: ')

                #             opcion = int(opcion)
                                
                #         #creamos la variable para almacenar el nombre de la receta
                #         receta = recetas2[opcion - 1]

                #         #creamos la variable para guardar la ruta de la receta
                #         archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                #         #con este condicional verifiamos que si sea un archivo
                #         if archivo.is_file():

                #             #imprimimos el nombre del archivo sin la extención
                #             print(f'\n{archivo.stem}')

                #             #abrimos el archivo en modo lectura
                #             archivo = archivo.open('r')

                #             #mostramos en pantalla el contenido del archivo
                #             print(f'\n{archivo.read()}')

                #             #preguntamos si desea ver otra receta
                #         respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                #         system('cls')

                #         #si la respuesta es negativa
                #         if respuesta == 'N':

                #             salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #             if salir == 'S':

                #                 salir_sistema()

                #             else: 

                #                 print('\nSi eliges\033[1m N\033[0m saldras del sistema')

                #                 salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #                 if salir == 'S':

                #                     entrada_sistema()

                #                 else:

                #                     salir_sistema()

                #     #si la respuesta es negativa
                #     if respuesta1 == 'N':

                #         salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #         if salir == 'S':

                #             salir_sistema()

                #         else: 

                #             salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #             if salir == 'S':

                #                 entrada_sistema()

                #             else:

                #                 elige = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                #             #con el bucle verifico la respuesta del usuario
                #             while elige not in ['N', 'S']:

                #                 print('\nEl carater ingresado no es valido, intenta de nuevo')

                #                 elige = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                #             #si la respuesta es positiva        
                #             if respuesta1 == 'S':

                #                 print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

                #                 # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
                #                 for i,r in enumerate(categoria, start=1):

                #                     lista = [f'{i} = {r}']

                #                     print(''.join(lista))

                #                 opcion = input('\nElige una opción: ')

                #                 #traemos el nombre que eligio el usaurio y lo imprimimos
                #                 nombre = categoria[int(opcion) - 1]

                #                 print(f'\nHas elegido \033[1m{nombre}\033[0m')

                #                 while not opcion.isnumeric():

                #                     print('\nLo que has ingresado no es un número intenta de nuevo')

                #                     opcion = input('\nElige una opción: ')

                #                     opcion = int(opcion)

                #                     #con este condicional verificamos si la opcion existe
                #                     if opcion > len(recetas2) or opcion <= 0:

                #                         print('\nLa receta seleccionada no existe')

                #                         print(f'\nElige nuevamente del siguiente\033[1m Menú\033[0m')

                #                         resultado_categoria1 = ruta / nombre

                #                         #creamos una lista vacia
                #                         recetas2 = []

                #                         #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                #                         for recetas1 in resultado_categoria1.glob('*.txt'):

                #                             recetas2.append(recetas1.name)

                #                         # con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
                #                         for i,r in enumerate(recetas2, start=1):

                #                             #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                #                             lista = [f'\n{i} = {r}']

                #                             print(''.join(lista))

                #                         opcion = input('\nElige una opción: ')

                #                         #con este bucle verificamos si la opción ingresada es correcta
                #                         while not opcion.isnumeric():

                #                                 print('\nLo que has ingresado no es un número intenta de nuevo')

                #                                 opcion = input('\nElige una opción: ')

                #                         opcion = int(opcion)
                                

                #                 #comprobamos si el nombre esta en la lista y le hacemos otra pregunta
                #                 if nombre:

                #                     respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{nombre}\033[0m S/N: ').upper()

                #                 #comprobamos si la eleccion es correcta
                #                 while respuesta1 not in ['N', 'S']:

                #                     print('\nNo has ingresado un caracter valido')

                #                     respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()

                #                 #cuando la respueesta es positiva
                #                 while respuesta1 == 'S':

                #                     #tenemos la ruta completa para poder acceder a los archivos .txt
                #                     resultado_categoria1 = ruta / nombre

                #                     #creamos una lista vacia
                #                     recetas2 = []

                #                     #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                #                     for recetas1 in resultado_categoria1.glob('*.txt'):

                #                         recetas2.append(recetas1.name)

                #                     # con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
                #                     for i,r in enumerate(recetas2, start=1):

                #                         #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                #                         lista = [f'{i} = {r}']

                #                         print(''.join(lista))

                #                     opcion = input('\nElige una opción: ')

                #                     #con este bucle verificamos si la opción ingresada es correcta
                #                     while not opcion.isnumeric():

                #                         print('\nLo que has ingresado no es un número intenta de nuevo')

                #                         opcion = input('\nElige una opción: ')

                #                     opcion = int(opcion)

                #                     #con este condicional verificamos si la opcion existe
                #                     if opcion > len(recetas2) or opcion <= 0:

                #                         print('\nLa receta seleccionada no existe')

                #                         return
                                                
                #                     #creamos la variable para almacenar el nombre de la receta
                #                     receta = recetas2[opcion - 1]

                #                     #creamos la variable para guardar la ruta de la receta
                #                     archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                #                     #con este condicional verifiamos que si sea un archivo
                #                     if archivo.is_file():

                #                         #imprimimos el nombre del archivo sin la extención
                #                         print(archivo.stem)

                #                         #abrimos el archivo en modo lectura
                #                         archivo = archivo.open('r')

                #                         #mostramos en pantalla el contenido del archivo
                #                         print(archivo.read())

                #                     #preguntamos si desea ver otra receta
                #                     respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                #                     #system('cls')
                                    
                #                     if respuesta == 'N':

                #                         salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #                         if salir == 'S':

                #                             salir_sistema()

                #                         else: 

                #                             print('\nSi eliges\033[1m N\033[0m saldras del sistema')

                #                             salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #                             if salir == 'S':

                #                                 entrada_sistema()

                #                             else:

                #                                 salir_sistema()

                #                 #cuando la respuesta es negativa
                #                 if respuesta == 'N':

                #                     salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #                     if salir == 'S':

                #                         salir_sistema()

                #                     else: 

                #                         print('\nSi eliges\033[1m N\033[0m saldras del sistema')

                #                         salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #                         if salir == 'S':

                #                             entrada_sistema()

                #                         else:

                #                             salir_sistema()   

                #             #cuando la respuesta es negativa    
                #             else:

                #                 print('\nSi eliges\033[1m N\033[0m saldras del sistema')
                                        
                #                 salir = input('Deseas regresar al menu principal? s/n. ').upper()

                #                 if salir == 'S':

                #                     entrada_sistema()

                #                 else:

                #                     salir_sistema()
                
                # else:

                #     print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

                #     # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
                #     for i,r in enumerate(categoria, start=1):

                #         lista = [f'{i} = {r}']

                #         print(''.join(lista))

                #     opcion = input('\nElige una opción: ')

                #     #traemos el nombre que eligio el usaurio y lo imprimimos
                #     nombre = categoria[int(opcion) - 1]

                #     print(f'\nHas elegido \033[1m{nombre}\033[0m')

                # #comprobamos si la eleccion es correcta
                # while respuesta1 not in ['N', 'S']:

                #     print('\nNo has ingresado un caracter valido')

                #     respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()
                    
                # while respuesta1 == 'S':

                #     #tenemos la ruta completa para poder acceder a los archivos .txt
                #     resultado_categoria1 = ruta / nombre

                #     #creamos una lista vacia
                #     recetas2 = []

                #     #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                #     for recetas1 in resultado_categoria1.glob('*.txt'):

                #         recetas2.append(recetas1.name)

                #     # con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
                #     for i,r in enumerate(recetas2, start=1):

                #         #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                #         lista = [f'\n{i} = {r}']

                #         print(''.join(lista))

                #     opcion = input('\nElige una opción: ')

                #     #con este bucle verificamos si la opción ingresada es correcta
                #     while not opcion.isnumeric():

                #             print('\nLo que has ingresado no es un número intenta de nuevo')

                #             opcion = input('\nElige una opción: ')

                #     opcion = int(opcion)

                #     #con este condicional verificamos si la opcion existe
                #     if opcion > len(recetas2) or opcion <= 0:

                #         print('\nLa receta seleccionada no existe')

                #         return
                            
                #     #creamos la variable para almacenar el nombre de la receta
                #     receta = recetas2[opcion - 1]

                #     #creamos la variable para guardar la ruta de la receta
                #     archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                #     #con este condicional verifiamos que si sea un archivo
                #     if archivo.is_file():

                #         #imprimimos el nombre del archivo sin la extención
                #         print(f'\n{archivo.stem}')

                #         #abrimos el archivo en modo lectura
                #         archivo = archivo.open('r')

                #         #mostramos en pantalla el contenido del archivo
                #         print(f'\n{archivo.read()}')

                #         #preguntamos si desea ver otra receta
                #     respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                #     system('cls')

                #     if respuesta == 'N':

                #         salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #         if salir == 'S':

                #             salir_sistema()

                #         else: 

                #             salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #             if salir == 'S':

                #                 entrada_sistema()

                #             else:

                #                 elige = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                #             #con el bucle verifico la respuesta del usuario
                #             while elige not in ['N', 'S']:

                #                 print('\nEl carater ingresado no es valido, intenta de nuevo')

                #                 elige = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                #             #si la respuesta es positiva
                                
                #             if respuesta1 == 'S':

                #                 print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

                #                 # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
                #                 for i,r in enumerate(categoria, start=1):

                #                     lista = [f'\n{i} = {r}']

                #                     print(''.join(lista))

                #                 opcion = input('\nElige una opción: ')

                #                 #traemos el nombre que eligio el usaurio y lo imprimimos
                #                 nombre = categoria[int(opcion) - 1]

                #                 print(f'\nHas elegido \033[1m{nombre}\033[0m')

                #                 #comprobamos si el nombre esta en la lista y le hacemos otra pregunta
                #                 if nombre:

                #                     respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{nombre}\033[0m S/N: ').upper()

                #                 #comprobamos si la eleccion es correcta
                #                 while respuesta1 not in ['N', 'S']:

                #                     print('\nNo has ingresado un caracter valido')

                #                     respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()
                        
                #                 while respuesta1 == 'S':

                #                     #tenemos la ruta completa para poder acceder a los archivos .txt
                #                     resultado_categoria1 = ruta / nombre

                #                     #creamos una lista vacia
                #                     recetas2 = []

                #                     #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
                #                     for recetas1 in resultado_categoria1.glob('*.txt'):

                #                         recetas2.append(recetas1.name)

                #                     # con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
                #                     for i,r in enumerate(recetas2, start=1):

                #                         #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                #                         lista = [f'{i} = {r}']

                #                         print(''.join(lista))

                #                     opcion = input('\nElige una opción: ')

                #                     #con este bucle verificamos si la opción ingresada es correcta
                #                     while not opcion.isnumeric():

                #                             print('\nLo que has ingresado no es un número intenta de nuevo')

                #                             opcion = input('\nElige una opción: ')

                #                     opcion = int(opcion)

                #                     #con este condicional verificamos si la opcion existe
                #                     if opcion > len(recetas2) or opcion <= 0:

                #                         print('\nLa receta seleccionada no existe')

                #                         return
                                            
                #                     #creamos la variable para almacenar el nombre de la receta
                #                     receta = recetas2[opcion - 1]

                #                     #creamos la variable para guardar la ruta de la receta
                #                     archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

                #                     #con este condicional verifiamos que si sea un archivo
                #                     if archivo.is_file():

                #                         #imprimimos el nombre del archivo sin la extención
                #                         print(archivo.stem)

                #                         #abrimos el archivo en modo lectura
                #                         archivo = archivo.open('r')

                #                         #mostramos en pantalla el contenido del archivo
                #                         print(archivo.read())

                #                         #preguntamos si desea ver otra receta
                #                     respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

                #                     #system('cls')
                                
                #                     if respuesta == 'N':

                #                         salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #                         if salir == 'S':

                #                             salir_sistema()

                #                         else: 

                #                             print('\nSi eliges\033[1m N\033[0m saldras del sistema')

                #                             salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #                             if salir == 'S':

                #                                 entrada_sistema()

                #                             else:

                #                                 salir_sistema()

                #                 if respuesta == 'N':

                #                         salir = input('\nDeseas salir del sistema? s/n. ').upper()

                #                         if salir == 'S':

                #                             salir_sistema()

                #                         else: 

                #                             print('\nSi eliges\033[1m N\033[0m saldras del sistema')

                #                             salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                #                             if salir == 'S':

                #                                 entrada_sistema()

                #                             else:

                #                                 salir_sistema()   
                            
                #             else:

                #                 print('\nSi eliges\033[1m N\033[0m saldras del sistema')
                                    
                #                 salir = input('Deseas regresar al menu principal? s/n. ').upper()

                #                 if salir == 'S':

                #                     entrada_sistema()

                #                 else:

                #                     salir_sistema()

                # else:

                #     print('\nLa categoria seleccionada no existe')
                
                # elige = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                # print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')
                # # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
                # for i,r in enumerate(categoria, start=1):

                #     lista = [f'{i} = {r}']

                #     print(''.join(lista))

                # opcion = input('\nElige una opción: ')

                # print(opcion)

                # nombre = categoria(int(opcion) - 1)
 
                # respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{nombre}\033[0m S/N: ').upper()

                # opcion = int(opcion)

                # if opcion > len(categoria) or opcion <= 0:

                #     print('\nLa categoria seleccionada no existe')
                
                # elige = input('\nDeseas ver el menu nuevamente S/N: ').upper()

                # print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')
                # # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
                # for i,r in enumerate(categoria, start=1):

                #     lista = [f'{i} = {r}']

                #     print(''.join(lista))

                # opcion = input('\nElige una opción: ')

                # print(opcion)

                # nombre = categoria(int(opcion) - 1)
 
                # respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{nombre}\033[0m S/N: ').upper()

            if elige == 'N':

                salir = input('\nDeseas salir del sistema? s/n. ').upper()

                while salir == 'S':

                    salir_sistema()

                else: 

                    salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

                    while salir == 'S':

                        entrada_sistema()

                    else:

                        salir_sistema()
                        
        print('\n')

        for i,r in enumerate(recetas2, start=1):

            lista = [f'{i} = {r}']

            print(''.join(lista))

        opcion = input('\nElige una opción: ')

        while not opcion.isnumeric():

            print('\nLo que has ingresado no es un número intenta de nuevo')

            opcion = input('\nElige una opción: ')

        print('\n')

        opcion = int(opcion)

        if opcion > len(recetas2) or opcion <= 0:

            print('\nLa receta seleccionada no existe')

            print(f'\nElige nuevamente del siguiente\033[1m Menú\033[0m')

            resultado_categoria1 = ruta / respuesta

            #creamos una lista vacia
            recetas2 = []

            #con el bucle recorremos la ruta y obtenemos los archivos .txt y los almacenamos en la lista
            for recetas1 in resultado_categoria1.glob('*.txt'):

                recetas2.append(recetas1.name)

            system('cls')

            print('\n')

            # con este bucle recorremos la lista y la mostramos al usuario para que elija una opcion
            for i,r in enumerate(recetas2, start=1):

                #creamos la variable para almacenar la respuesta del bucle con ese formato para luego imprimirlo 
                lista = [f'{i} = {r}']

                print(''.join(lista))

            opcion = input('\nElige una opción: ')

            #con este bucle verificamos si la opción ingresada es correcta
            while not opcion.isnumeric():

                    print('\nLo que has ingresado no es un número intenta de nuevo')

                    opcion = input('\nElige una opción: ')

            opcion = int(opcion)
            
        receta = recetas2[opcion - 1]

        archivo = Path(Path.home(), 'Recetas', resultado_categoria1, receta)

        if archivo.is_file():

            print(archivo.stem)

            archivo = archivo.open('r')

            print(archivo.read())

            respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

            system('cls')

            while respuesta == 'S':

                print('\n')

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

                    print(f'Si presionas\033[1m N\033[0m saldras del sistema')

                    salir = input('Deseas regresar al menu principal? s/n. ').upper()

                    while salir == 'S':

                        entrada_sistema()

                    else:

                        salir_sistema()
            
    else:

        entrada_sistema() 

def crear_receta_directorio (respuesta, ruta):

    # se le pregunta al usuario si desea crear una receta
    respuesta1 = input(f'\nDeseas Crear una nueva receta a {respuesta} S/N: ').upper()

    # se valida la respuesta del usuario
    while respuesta1 not in ['N', 'S']:

        print('\nNo has ingresado un caracter valido')

        respuesta1 = input(f'\nDeseas agregar una nueva receta a {respuesta} S/N: ').upper()

    # si la respuesta es positiva
    if respuesta1 == 'S':

        # se le pide al usuario el nombre de la receta
        archivo_nuevo = input('\nDigita el nombre con el que vas a guardar tu receta: ')+ '.txt'

        #ruta = Path(Path.home(), 'Recetas', respuesta)

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

            #ruta = Path(Path.home(), 'Recetas', respuesta)

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

#obtenemos la ruta del recetario creada por el usuario
def obtener_ruta_recetario():

    # Verifica si hay un archivo guardado con la ruta del recetario
    if os.path.exists('ruta_recetario.txt'):

        #abrimos el archivo
        with open('ruta_recetario.txt', 'r') as file:

            #hacemos el retorno quitando los espacios que pueda contener el nombre
            return file.read().strip()
        
    else:

        return None

#guardamos el archivo que hemos creado 
def guardar_ruta_recetario(ruta):

    #guardamos la ruta absoluta en una variable
    ruta_absoluta = os.path.abspath(ruta)

    #abrimos el archivo
    with open('ruta_recetario.txt', 'w') as file:

        #escribimos en el archivo
        file.write(str(ruta_absoluta))

#verificamos si el usuario es nuevo en el sistema o no
def verificar_usuario(nombre):

    #hacemos una pregunta al usuario y la almacenamos en una variable la respuesta
    respuesta = input('\nEres un usuario nuevo? S/N: ').upper()

    #hacemos la verificacion de la respuesta del usuario
    while respuesta not in ['N', 'S']:

        print('\nHas ingresado un caracter no válido')

        respuesta = input('\nEres un usuario nuevo? S/N: ').upper()

    # Verificamos si el usuario es nuevo
    if respuesta == 'S':

        # El usuario es nuevo, creamos el directorio
        recetario = usuario_nuevo()

        guardar_ruta_recetario(recetario)  # Guardar la ruta en el archivo

        #entramos al sistema despues de la verificación
        entrada_sistema(recetario)

    else:

        # El usuario no es nuevo, obtenemos la ruta del archivo
        ruta_recetario = obtener_ruta_recetario()

        # comprobamos si la ruta existe
        if ruta_recetario is None or not os.path.exists(ruta_recetario):

            #informamos al usuario si no existe la ruta
            print("Error: No se encontró la ruta del recetario o la carpeta no existe.")

            # creamos una variable y le preguntamos al usuario si desea crear el directorio porque no existe
            respuesta_creacion = input('\n¿Quieres crear un nuevo recetario? S/N: ').upper()

            #si la respuesta es positiva
            if respuesta_creacion == 'S':

                # creamos el directorio llamando a la funcion de nuevo_usuario
                recetario = usuario_nuevo()

                #guardamos la ruta que ha sido creada en la funcion guardar_ruta_recetario
                guardar_ruta_recetario(recetario)

                # entramos al sistema
                entrada_sistema(recetario)

            else:

                # salimos del sistema
                salir_sistema()

        # Llama a la función de entrada del sistema con la ruta del recetario
        entrada_sistema(ruta_recetario)

        
# esta funcion le pide al usuario que cree su porpio directorio o si ya ha ingrersado tener acceso al menu
def usuario_nuevo ():

    # mensaje de informacion
    print('\nComo eres nuevo en el sistema debes crear el directorio donde vas a guardar tus recetas')

    print('\nSi eliges\033[1m N\033[0m saldras del sistema')

    # preguntamos al usuario si es nuevo el sistema
    nuevo = input('\nDeseas crear el directorio? S/N: ').upper()

    # validamos su respuesta
    while nuevo not in ['N', 'S']:

        print('Has elegido una opcion incorrecta, intenta de nuevo') 

        nuevo = input('Eres nuevo en el sistema S/N: ').upper()

    # si el usuario elije si
    if nuevo == 'S':

        # se le pide al usuario crear la raiz del directorio donde almacenara las recetas
        raiz = input('\nCrea la raiz del directorio donde vas a guardar tus recetas (ejemplo disco C o disco D) solo debes de poner la letra: ').upper() + ':/'

        # se verifica que la raiz elegida existe en el computador
        while not os.path.exists(raiz):

            print('La ruta ingresada no existe')

            raiz = input('\nCrea la raiz del directorio donde vas a guardar tus recetas (ejemplo disco C o disco D) solo debes de poner la letra: ').upper() + ':/'
        
        # se le pide al ususario que cree el directorio para almacenar las categorias de sus recetas
        carpeta = input('\nCrea el nombre de la carpeta donde almacenaras las diferentes categorias: ').title()

        # tnemos la direccion del directorio que se va a crear
        directorio = Path(raiz , carpeta)
        
        # validamos si el directorio ingresado por el usuario existe
        if directorio.exists():

            # mensaje de advertencia
            print('\nEl directorio ya existe, debes cambiar el nombre de la carpeta')

            # se le pide que ungrese un nuevo nombre
            nueva_carpeta = input('\nCrea el nombre de la carpeta donde almacenaras las diferentes categorias: ').title()

            # creamos la nueva direccion
            directorio2 = Path(raiz, nueva_carpeta)

            # creamos el nuevo directorio
            Path.mkdir(directorio2)
        
        # creamos el nuevo directorio
        Path.mkdir(directorio)

        # mensaje de que el directorio ha sido creado
        print('\nEl directorio ha sido creado con éxito')

        return directorio

    # si la respuesta es no
    if nuevo == 'N':

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

    # verificamos que si exista una categoria
    if not categoria:

        print('\nNo hay categorias disponibles')

        return

    print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

    # listamos las categorias que le hemos pasado a la funcion
    for i,r in enumerate(categoria, start=1):

        lista = [f'{i} = {r}']

        print(''.join(lista))

    opcion = input('\nElige una opción: ')

    #verificamos si la opcion ingresada es correcta
    while not opcion.isnumeric() or int(opcion) > len(categoria) or int(opcion) <= 0:

        print('\nLo que has ingresado no esta dentro de la lista o no es un caracter valido, intenta de nuevo')

        opcion = input('\nElige una opción: ')

    opcion2 = categoria[opcion -1]

    print(f'\nHas elegido \033[1m{opcion2}\033[0m')

    return opcion2

def entrada_sistema (ruta):

    categoria = menu_categorias(ruta)

    mostrar_bienvenida(nombre, cantidad_recetas(ruta), ruta)

    opciones = ['Leer Recetas', 'Crear Receta', 'Crear Categoria', 'Eliminar Receta', 'Eliminar Categoria', 'Salir del Sistema']

    for i, r in enumerate(opciones, start=1):

        lista =[f'{i} = {r}']

        print(''.join(lista))

    opcion = input('\nElige una opcion: ')

    while not opcion.isnumeric() or int(opcion) not in range(1, 7):

        print('\nEl número ingresado no es correcto o has digitado un caracter no valido, intenta de nuevo')
    
        opcion = input('\nElige una opcion: ')
    
    opcion = int(opcion)

    opcion_elegida = opciones[opcion - 1]

    system('cls')

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

            crear_receta_directorio(respuesta, recetario)
                    
        case 4:

            eliminar_receta(categoria, respuesta)

        case 5:

            eliminar_categoria(categoria, respuesta)

        case _:

            print('\nHas elegido un comando incorrecto, intenta de nuevo')

            opcion = input('Elige una opcion: ')

# se declaran variables
nombre = entrada_nombre()

verificar_usuario(mostrar_bienvenida_usuario_nuevo(nombre))
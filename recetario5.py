# se importan las librerias necesarias
import os
from os import system
from pathlib import Path
import shutil
from turtle import home
import path

# se crean las funciones

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

    # limpiamos pantalla
    system('cls')

    #preguntamos al usuario si desea ver los archivos que estan en la elección que realizó
    respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{respuesta}\033[0m S/N: ').upper()

    #con el bucle hacemos la comprobación de que halla ingresado un caracter valido
    while respuesta1 not in ['N', 'S']:

        # informamos al usuario
        print('\nNo has ingresado un caracter valido')

        #preguntamos al usuario si desea ver los archivos que estan en la elección que realizó
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

            # informamos al usuario
            print(f'\nNo hay recetas para mostrar en \033[1m{respuesta}\033[0m')

            # informamos al usuario
            print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

            # con el bucle listamos de nuevo el menu para que el usuario eliga una opción nuevamente
            for i,r in enumerate(categoria, start=1):

                lista = [f'{i} = {r}']

                print(''.join(lista))

            # almacenamos la respuesta en una variable
            opcion = input('\nElige una opción: ')

            # verificamos si la opcion es un número
            while not opcion.isnumeric():

                # informamos al usuario
                print('\nEl carater ingresado no es valido, intenta de nuevo')

                # almacenamos la respuesta en una variable
                opcion = input('\nElige una opción: ')

            # verificamos si la opcion esta dentro de la cantidad de opciones del menú
            while int(opcion) > len(categoria) or int(opcion) <= 0:

                # informamos al usuario
                print('\nLa eleccion no se encuentra dentro del directorio, intenta de nuevo')

                # almacenamos la respuesta en una variable
                opcion = input('\nElige una opción: ')
            
            # almacenamos en una variable la eleccion del usuario convertida a lo que corresponde en el menú
            respuesta = categoria[int(opcion) - 1]

            # informamos al usuario
            print(f'\nHas elegido\033[1m {respuesta}\033[0m')

            # pedimos al usuario una respuesta
            respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{respuesta}\033[0m S/N: ').upper()

            #con el bucle hacemos la comprobación de que halla ingresado un caracter valido
            while respuesta1 not in ['N', 'S']:

                # informamos al usuario
                print('\nNo has ingresado un caracter valido')

                # pedimos al usuario una respuesta
                respuesta1 = input(f'\nDeseas ver las recetas que contiene {respuesta} S/N: ').upper()

            # si la respuesta es positiva
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

                    #informamos al usuario 
                    print('\nSi eliges \033[1mN \033[0msaldras del sistema')

                    salir = input('\nDeseas ingresar al sistema S/N: ').upper()

                    # verificamos la respuesta
                    while salir not in ['N', 'S']:

                        #informamos al usuario
                        print('\nNo has ingresado un caracter válido, intenta de nuevo')

                        salir = input('\nDeseas ingresar al sistema S/N: ').upper()

                    # si la respuesta es positiva
                    if salir == 'S':

                        entrada_sistema(ruta) 
                    
                    # si la respuesta es negativa
                    else:

                        salir_sistema()
                
                # un salto de línea para separar
                print('\n')
                
                # con el bucle listmos el menú
                for i,r in enumerate(recetas2, start=1):

                    lista = [f'{i} = {r}']

                    print(''.join(lista))

                # almacenamos la opcion del usuario
                opcion = input('\nElige una opción: ')

                # comprobamos la eleccion del usuario
                while not opcion.isnumeric() or int(opcion) > len(recetas2) or int(opcion) <= 0:

                    # informamos al usuario
                    print('\nHas seleccionado un número no valido o un caracter no valido')

                    # almacenamos la opcion del usuario
                    opcion = input('\nElige una opción: ')
                            
                # pasamos la opcion del usuario al nombre correspondiente en el menú
                receta = recetas2[int(opcion) - 1]

                # almacenamos la ruta 
                archivo = Path(resultado_categoria1, receta)

                # un salto de línea para separar
                print('\n')

                # verificamos si es un archivo
                if archivo.is_file():

                    # imprimimos el nombre del archivo sin la extension
                    print(archivo.stem)

                    # almacemamos el archivo abierto en modo lectura en una variable
                    archivo = archivo.open('r')

                    # mostramos el archivo
                    print(archivo.read())

                # preguntamos la usuario
                respuesta1 = input('\n¿Quieres ver otra receta? S/N: ').upper()

                # limpiamos pantalla
                system('cls')

                # verificamos la respuesta
                while respuesta1 not in ['N', 'S']:

                    print('\nHas seleccionado un caracter no valido, intenta de nuevo')

                    respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

            # si la respuesta es negativa
            else:

                #informamos al usuario 
                print('\nSi eliges \033[1mN \033[0msaldras del sistema')

                salir = input('\nDeseas ingresar al sistema S/N: ').upper()

                # verificamos la respuesta
                while salir not in ['N', 'S']:

                    #informamos al usuario
                    print('\nNo has ingresado un caracter válido, intenta de nuevo')

                    salir = input('\nDeseas ingresar al sistema S/N: ').upper()

                # si la respuesta es positiva
                if salir == 'S':

                    entrada_sistema(ruta) 
                
                # si la respuesta es negativa
                else:

                    salir_sistema()

        print('\n')

        # imprimimos el menú con el bucle
        for i,r in enumerate(recetas2, start=1):

            lista = [f'{i} = {r}']

            print(''.join(lista))

        # almacenamos la eleccion del usuario
        opcion = input('\nElige una opción: ')

        # validamos la eleccion
        while not opcion.isnumeric() or int(opcion) > len(recetas2) or int(opcion) <= 0:

            print('\nHas seleccionado un número no valido o un caracter no valido')

            opcion = input('\nElige una opción: ')
                    
        # pasamos la eleccion del usuario al nombre que tiene en el menú
        receta = recetas2[int(opcion) - 1]

        # almacencamos la direccion del menú
        archivo = Path(resultado_categoria1, receta)

        print('\n')

        # comprobamos si es un archivo
        if archivo.is_file():

            # imprimimos el nombre del archivo sin extension
            print(archivo.stem)

            # almacenamos el archivo que se abre en modo lectura
            archivo = archivo.open('r')

            # mostramos el archivo
            print(archivo.read())

        # preguntamos al usuario
        respuesta1 = input('\n¿Quieres ver otra receta? S/N: ').upper()

        # limpiamos pantalla
        system('cls')

        # compribamos la respuesta
        while respuesta1 not in ['N', 'S']:

            print('\nHas seleccionado un caracter no valido, intenta de nuevo')

            respuesta = input('\n¿Quieres ver otra receta? S/N: ').upper()

        if respuesta1 == 'N':

            #informamos al usuario 
            print('\nSi eliges \033[1mN \033[0msaldras del sistema')

            salir = input('\nDeseas ingresar al sistema S/N: ').upper()

            # verificamos la respuesta
            while salir not in ['N', 'S']:

                #informamos al usuario
                print('\nNo has ingresado un caracter válido, intenta de nuevo')

                salir = input('\nDeseas ingresar al sistema S/N: ').upper()

            # si la respuesta es positiva
            if salir == 'S':

                entrada_sistema(ruta) 
            
            # si la respuesta es negativa
            else:

                salir_sistema()
            
    # si la respuesta es negativa
    else:

        #informamos al usuario 
        print('\nSi eliges \033[1mN \033[0msaldras del sistema')

        salir = input('\nDeseas ingresar al sistema S/N: ').upper()

        # verificamos la respuesta
        while salir not in ['N', 'S']:

            #informamos al usuario
            print('\nNo has ingresado un caracter válido, intenta de nuevo')

            salir = input('\nDeseas ingresar al sistema S/N: ').upper()

        # si la respuesta es positiva
        if salir == 'S':

            entrada_sistema(ruta) 
        
        # si la respuesta es negativa
        else:

            salir_sistema()

#esta funcion crea una receta en el directorio que el uauario ya habia creado
def crear_receta_directorio (respuesta, ruta):

    # se le pregunta al usuario si desea crear una receta
    respuesta1 = input(f'\nDeseas Crear una nueva receta a\033[1m {respuesta}\033[0m S/N: ').upper()

    # se valida la respuesta del usuario
    while respuesta1 not in ['N', 'S']:

        print('\nNo has ingresado un caracter valido')

        respuesta1 = input(f'\nDeseas agregar una nueva receta a\033[1m {respuesta}\033[0m S/N: ').upper()

    # si la respuesta es positiva
    while respuesta1 == 'S':

        # se le pide al usuario el nombre de la receta
        archivo_nuevo = input('\nDigita el nombre con el que vas a guardar tu receta: ') + '.txt'

        #se crea la ruta de donde se va a guardar el archivo
        ruta1 = Path(ruta, respuesta, archivo_nuevo)

        #verificamos si el archivo existe
        if ruta1.exists():

            print('\nEl archivo ya existe')

        #si el archivo no existe
        if not ruta1.exists():

            #abrimos el archivo en modo escritura y lo almacenamos en una variable
            mi_archivo = open(ruta1, 'w')

            #se crea una lista vacia
            ingredientes = []

            #almacemamos el titulo de la receta en un avariabkle al escribirlo
            titulo = (input("\nIngresa el titulo de la receta: "))

            #agregamos el titulo al archivo
            mi_archivo.write( f"{titulo}\n\nIngredientes\n\n")

            #se le pregunta al usuario si va a ingresar los ingredientes de la recetq
            desicion =input('\nDeseas agregar los ingredientes S/N: ').upper()

            #se vallida la respuesta
            while desicion not in ['N', 'S']:

                print('\nNo has ingresado un caracter valido')

                desicion =input('\ndeseas agregar los ingredientes S/N: ').upper()

                system('cls')

            #si la respuesta es positiva
            while desicion == 'S':

                #se agregan los ingredientes a la lista
                ingredientes.append(input('\nIngresa los ingredientes de la receta\033[1m uno a uno:\033[0m \n\n'))
                
                #se pregunta si va a agregar mas ingredientes
                desicion =input('\ndeseas agregar mas ingredientes S/N: ').upper()

                #se llimpia pantalla
                system('cls')
            
            #se recorre la lista con el bucle
            for i, v in enumerate(ingredientes, start = 1):
                    
                #se crea una lista con cada recorrido del bucle
                lista = [f'* {v}\n']

                #se escriben los ingredientes en el archivo
                ingredientes = mi_archivo.write(''.join(lista))
                
            #se escribe en el archivo un mensaje
            mi_archivo.write('\n\nPreparación\n\n')

            #se escribe en el archivo la preparacion de la receta 
            mi_archivo.write(input('\nIngresa la preparacion de la receta: \n\n'))

            #se limpia la pantalla
            system('cls')

            #se informa de que el archivo se ha creado 
            print('\nLa receta se ha creado con exito')

            #se cierra el archivo
            mi_archivo.close()

        #se limpia la pantalla
        system('cls')

        #se pregunta si va a crear mas recetas
        respuesta1 = input(f'\nDeseas agregar una nueva receta a\033[1m {respuesta}\033[0m S/N: ').upper()

        # se valida la respuesta del usuario
        while respuesta1 not in ['N', 'S']:

            print('\nNo has ingresado un caracter valido')

            respuesta1 = input(f'\nDeseas agregar una nueva receta a\033[1m {respuesta}\033[0m S/N: ').upper()

    #si la respuesta es negativa
    else:

        #se le pregunta al usuario si desea salir del sistema
        salir = input('Deseas salir del sistema? S/N. ').upper()

        #si la respuesta es positiva
        if salir == 'S':

            salir_sistema()

        #si la respuesta es negativa
        else: 

            #se le pregunta al usuario si quier ir al menu ppal
            salir = input('Deseas regresar al menu principal? S/N. ').upper()

            #si la respuesta es positiva
            if salir == 'S':

                #entra al menu ppal
                entrada_sistema(ruta)

            #si la respuesta es negativa
            elif salir == 'N':

                # se le pregunta al usuario si desea crear una receta
                respuesta1 = input(f'\nDeseas Crear una nueva receta a\033[1m {respuesta}\033[0m S/N: ').upper()

                # se valida la respuesta del usuario
                while respuesta1 not in ['N', 'S']:

                    print('\nNo has ingresado un caracter valido')

                    respuesta1 = input(f'\nDeseas agregar una nueva receta a\033[1m {respuesta}\033[0m S/N: ').upper()

                # si la respuesta es positiva
                while respuesta1 == 'S':

                    # se le pide al usuario el nombre de la receta
                    archivo_nuevo = input('\nDigita el nombre con el que vas a guardar tu receta: ') + '.txt'

                    #se crea la ruta de donde se va a guardar el archivo
                    ruta1 = Path(ruta, respuesta, archivo_nuevo)

                    #verificamos si el archivo existe
                    if ruta1.exists():

                        print('\nEl archivo ya existe')

                    #si el archivo no existe
                    if not ruta1.exists():

                        #abrimos el archivo en modo escritura y lo almacenamos en una variable
                        mi_archivo = open(ruta1, 'w')

                        #se crea una lista vacia
                        ingredientes = []

                        #almacemamos el titulo de la receta en un avariabkle al escribirlo
                        titulo = (input("\nIngresa el titulo de la receta: "))

                        #formateamos el titulo
                        titulo_formateado = titulo.title()

                        #agregamos el titulo al archivo
                        mi_archivo.write( f"{titulo_formateado}\n\nIngredientes\n\n")

                        #se le pregunta al usuario si va a ingresar los ingredientes de la recetq
                        desicion =input('\nDeseas agregar los ingredientes S/N: ').upper()

                        #se vallida la respuesta
                        while desicion not in ['N', 'S']:

                            print('\nNo has ingresado un caracter valido')

                            desicion =input('\ndeseas agregar los ingredientes S/N: ').upper()

                            system('cls')

                        #si la respuesta es positiva
                        while desicion == 'S':

                            #se agregan los ingredientes a la lista
                            ingredientes.append(input('\nIngresa los ingredientes de la receta\033[1m uno a uno:\033[0m \n\n'))
                            
                            #se pregunta si va a agregar mas ingredientes
                            desicion =input('\ndeseas agregar mas ingredientes S/N: ').upper()

                            #se llimpia pantalla
                            system('cls')
                        
                        #se recorre la lista con el bucle
                        for i, v in enumerate(ingredientes, start = 1):
                                
                            #se crea una lista con cada recorrido del bucle
                            lista = [f'* {v}\n']

                            #se escriben los ingredientes en el archivo
                            ingredientes = mi_archivo.write(''.join(lista))
                            
                        #se escribe en el archivo un mensaje
                        mi_archivo.write('\n\nPreparación\n\n')

                        #se escribe en el archivo la preparacion de la receta 
                        mi_archivo.write(input('\nIngresa la preparacion de la receta: \n\n'))

                        #se limpia la pantalla
                        system('cls')

                        #se informa de que el archivo se ha creado 
                        print('\nLa receta se ha creado con exito')

                        #se cierra el archivo
                        mi_archivo.close()

                    #se limpia la pantalla
                    system('cls')

                    #se pregunta si va a crear mas recetas
                    respuesta1 = input(f'\nDeseas agregar una nueva receta a\033[1m {respuesta}\033[0m S/N: ').upper()

                    # se valida la respuesta del usuario
                    while respuesta1 not in ['N', 'S']:

                        print('\nNo has ingresado un caracter valido')

                        respuesta1 = input(f'\nDeseas agregar una nueva receta a\033[1m {respuesta}\033[0m S/N: ').upper()

                #si la respuesta es negativa
                if respuesta1 == 'N':

                    #se le preguanta al usuario si quiere salir del sistema
                    salir = input('Deseas salir del sistema? S/N. ').upper()

                    #si la respuesta es positiva
                    if salir == 'S':

                        #sale del sistema
                        salir_sistema()

                    #si la respuesta es negativa
                    else:

                        #se le informa al usuario que pasa si elige N
                        print('\nSi eliges\033[1m N\033[0m sales del sistema')

                        #se le preguanta al usuario si quiere regresar al menu ppal
                        salir = input('Deseas regresar al menu principal? S/N. ').upper()

                        #si la respuesta es positiva
                        if salir == 'S':

                            #entra al menu ppal
                            entrada_sistema(ruta)
                        
                        #si la respuesta es negativa
                        else:

                            #sale del sistema
                            salir_sistema()

#obtenemos la ruta del recetario creada por el usuario
def obtener_ruta_recetario():

    # Verifica si hay un archivo guardado con la ruta del recetario
    if os.path.exists('ruta_recetario.txt'):

        # abrimos el archivo  en modo lectura
        with open('ruta_recetario.txt', 'r') as file:

            #retornamos la lectura del archivo
            return file.read().strip()
        
    #si no existe el archivo
    else:

        print('\nEl archivo no existe')

# con esta funcion guardamos la ruta
def guardar_ruta_recetario(ruta):

    # almacenamos la ruta efn una variable de forma que la ruta sea absoluta
    ruta_absoluta = os.path.abspath(ruta)

    # abrimos el archivo en forma de escritura
    with open('ruta_recetario.txt', 'w') as file:

        # guardamos el archivo
        file.write(str(ruta_absoluta))

#con esta funcion guardamos el usuario
def verificar_usuario(bienvenida, nombre):

    # almacenamos la respuesta del usuario en una variable
    respuesta = input(f'\n\033[1m{nombre}\033[0m Eres un usuario nuevo? S/N: ').upper()

    #comprobamos la respuesta del usuario
    while respuesta not in ['N', 'S']:

        print('\nHas ingresado un caracter no válido')

        respuesta = input('\nEres un usuario nuevo? S/N: ').upper()

    # Verificamos si el usuario es nuevo
    if respuesta == 'S':

        # El usuario es nuevo, creamos el directorio
        recetario = usuario_nuevo()

        guardar_ruta_recetario(recetario)  # Guardar la ruta en el archivo

        entrada_sistema(recetario)

    else:

        # El usuario no es nuevo, obtenemos la ruta del archivo
        ruta_recetario = obtener_ruta_recetario()

        #comprobamos si la ruta existe
        if ruta_recetario is None or not os.path.exists(ruta_recetario):

            #si no existe informamos al usuario
            print("Error: No se encontró la ruta del recetario o la carpeta no existe.")

            print('\nSi la respuesta es\033[1m N\033[0m saldras del sistema')

            #preguntamos al usuario si desea crear el directorio porque no existe
            respuesta_creacion = input('\n¿Quieres crear un nuevo recetario? S/N: ').upper()

            #si la respuesta es positiva
            if respuesta_creacion == 'S':

                # cremas la ruta
                recetario = usuario_nuevo()

                # guardamos la ruta
                guardar_ruta_recetario(recetario)

                # entramos al sistema
                entrada_sistema(recetario)

            # si la respuesta es negativa
            else:

                # salimos del sistema
                salir_sistema()

        # Llama a la función de entrada del sistema con la ruta del recetario
        entrada_sistema(ruta_recetario)

# es ka funcion de entrada y se le pide al usuario que cree su porpio directorio o si ya ha ingrersado tener acceso al menu
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

# con esta funcion creamos una categoria en la ruta que el usuario ya ha creado
def crear_directorio(ruta):

    #le preguntamos al usuario si quiere crear una categoria y la almacenamos en una variable
    respuesta = input('\nDeseas crear un directorio S/N: ').upper()

    # comprobamos la respuesta del usuario
    while respuesta not in ['N', 'S']:

        print('\nHas ingresado un caracter no valido')

        respuesta = input('\nDeseas crear un directorio s/n: ').upper()

    #si la respuesta es positiva
    while respuesta == 'S':

        # almacenamos el nombre de la categoria que el usuario ha digitado en una variable
        directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

        # guardamos la ruta en una variable
        ruta1 = Path(ruta, directorio)

        if not os.path.exists(ruta1):

            # creamos el directorio
            os.makedirs(ruta1)

            if os.path.exists(ruta1):

                #informamos de su creacion
                print('\nEl directorio se ha creado con exito')

            else:

                print('\nError al crear el directorio')

        else:

            #informamos que no se ha creado
            print('\nEl directorio ya existe')

        # se le vuelve a pedir al usurario si quiere crear una categoria
        respuesta = input('\nDeseas crear un directorio S/N: ').upper()

        # se limpia la pantalla
        system('cls')

        # si la respuesta es negativa
        if respuesta == 'N':

            # se le pregunta si desea salir del sistema
            salir = input('\nDeseas salir del sistema? S/N. ').upper()

            #si la respuesta es positiva
            if salir == 'S':

                #sale del sistema
                salir_sistema()

            #si la respuesta es negativa
            elif salir == 'N': 

                #se le pregunta si desea regresar al menu ppal
                salir = input('\nDeseas regresar al menu principal? S/N. ').upper()

                # si la respuesta es positiva
                if salir == 'S':

                    #entra al menu ppal
                    entrada_sistema(ruta)

                # si la respuesa es negativa
                else:

                    #se le pregunta si desea crear de nuevo un directorio
                    respuesta = input('\nDeseas crear un directorio S/N: ').upper()

                    # si ls respuesta es positiva
                    while respuesta == 'S':

                        # almacenamos el nombre de la categoria que el usuario ha digitado en una variable
                        directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

                        # guardamos la ruta en una variable
                        ruta1 = Path(ruta, directorio)

                        if not os.path.exists(ruta1):

                            # creamos el directorio
                            os.makedirs(ruta1)

                            if os.path.exists(ruta1):

                                #informamos de su creacion
                                print('\nEl directorio se ha creado con exito')

                            else:

                                print('\nError al crear el directorio')

                        else:

                            #informamos que no se ha creado
                            print('\nEl directorio ya existe')

                        #se le pregunta si desea crear de nuevo un directorio
                        respuesta = input('\nDeseas crear un directorio S/N: ').upper()

                    # si la respuesta es negativa
                    else:

                        # se le informa al usuario de su eleccion
                        print('\nSi eliges \033[1mN\033[0m saldras del sistema')
            
                        #se le pregunta al usuario que quiere hacer
                        salir = input('\nDeseas regresar al menu principal? S/N. ').upper()

                        #si la respuesta es afirmativa
                        if salir == 'S':

                            #entra al menu ppal
                            entrada_sistema(ruta)

                        # si la respuesta es negativa
                        else:

                            #sale del sistema
                            salir_sistema()
    
    # si la respuesta es negativa
    if respuesta == 'N':

        #se le pregunta si quiere salir del ssitema
        salir = input('\nDeseas salir del sistema? S/N. ').upper()

        # si la respuesta es positiva
        if salir == 'S':

            #sale del sistema
            salir_sistema()

        #si la respuesta es  negativa
        elif salir == 'N': 

            #se le pregunta su quiere regresar al menu ppal
            salir = input('\nDeseas regresar al menu principal? S/N. ').upper()

            #si la respuesta es positiva
            if salir == 'S':

                #entra el menu ppal
                entrada_sistema(ruta)

            #si la respuesta es negativa
            else:

                respuesta = input('\nDeseas crear un directorio S/N: ').upper()

                #si la respuesta es negativa
                while respuesta == 'S':

                    # almacenamos el nombre de la categoria que el usuario ha digitado en una variable
                    directorio = input('\nDigite el nombre del directorio o carpeta que quieres realizar: ').title()

                    # guardamos la ruta en una variable
                    ruta1 = Path(ruta, directorio)

                    if not os.path.exists(ruta1):

                        # creamos el directorio
                        os.makedirs(ruta1)

                        if os.path.exists(ruta1):

                            #informamos de su creacion
                            print('\nEl directorio se ha creado con exito')

                        else:

                            print('\nError al crear el directorio')

                    else:

                        #informamos que no se ha creado
                        print('\nEl directorio ya existe')

                    #se le pregunta si quiere crear otro directorio
                    respuesta = input('\nDeseas crear un directorio S/N: ').upper()

                    #si la respuesta es negativa
                    if respuesta == 'N':

                        #se le pregunta que quiere hacer
                        salir = input('\nDeseas salir del sistema? S/N. ').upper()

                        #si la respuesta es positiva
                        if salir == 'S':

                            #sale del sistema
                            salir_sistema()

                        #si la respuesta es negativa
                        elif salir == 'N': 

                            #se le advierte al usuario
                            print('\n Si eliges \033[1m N \033[0m saldras del sistema')

                            #se lef pregunta que quiere hacer
                            salir = input('\nDeseas regresar al menu principal? S/N. ').upper()

                            #si la respuesta es positiva
                            if salir == 'S':

                                #entra al menu ppal
                                entrada_sistema(ruta)

                            #si la respuesta es negativa
                            else:

                                #sale del sistema
                                salir_sistema()
                
                else:

                    #se le advierte al usuario
                    print('\nSi eliges \033[1mN\033[0m saldras del sistema')
            
                    #se lef pregunta que quiere hacer
                    salir = input('\nDeseas regresar al menu principal? S/N. ').upper()

                    #si la respuesta es positiva
                    if salir == 'S':

                        #entra al menu ppal
                        entrada_sistema(ruta)

                    #si la respuesta es negativa
                    else:

                        #sale del sistema
                        salir_sistema()
  
# con esta fucion puedes eliminar recetas de tu directorio
def eliminar_receta (respuesta, ruta):

    # le preguntamos al usuario 
    respuesta1 = input(f'\nDeseas ver las recetas que contiene \033[1m{respuesta} \033[0mS/N: ').upper()

    # verificamos la respuesta
    while respuesta1 not in ['N', 'S']:

        print('\nNo has ingresado un caracter valido')

        respuesta1 = input(f'Deseas ver las recetas que contiene \033[1m{respuesta} \033[0mS/N: ').upper()
        
    #mientras la respuesta sea positiva
    while respuesta1 == 'S':

        # traemos la ruta de donde queremos eliminar el archivo
        resultado_categoria1 = Path(ruta, respuesta)

        # creamos una lista vacia
        recetas2 = []

        # recorremos la ruta para obtener los archivos que tiene 
        for recetas1 in resultado_categoria1.glob('*.txt'):

            # llenamos la lista con cada recorrido
            recetas2.append(recetas1.name)

        # si la lista esta vacia
        if not recetas2:

            # limpiamos pantalla
            system('cls')

            # informamos al usuario
            print(f"\nNo hay recetas para mostrar en \033[1m{respuesta}\033[0m")

            print(f'\nLa categoria \033[1m{respuesta}\033[0m esta vacia')

            # preguntamos al usuario  que quiere hacer
            opcion3 = input('\nSi prefieres puedes regresar al menu principal con\033[1m S \033[0mo salir del sistema con\033[1m N \033[0mS/N: ').upper()

            # verificamos la respuesta del usuario
            while opcion3 not in ['N', 'S']:

                print('\nNo has ingresado un caracter valido')

                opcion3 = input('\nSi prefieres puedes regresar al menu principal con\033[1m S \033[0mo salir del sistema con\033[1m N \033[0mS/N: ').upper()

            # si la respuesta es positiva
            if opcion3 == 'S':

                # entra al menu ppal
                entrada_sistema(ruta)

            # sale del sistema
            else:

                # sale del sistema
                salir_sistema()  

        # sino esta vacia la lista
        else:
            # Imprime las recetas
            while True:

                # recorremos la lista con el bucle y la imprimimos
                for i, r in enumerate(recetas2, start=1):

                    lista = [f'{i} = {r}']

                    print(''.join(lista))

                # se le pide al usuario qeu elija una opcion
                opcion = input('\nElige una opción: ')

                # verificamos si la opcion es un numero
                while not opcion.isnumeric():

                    print('\nHas elegido una opcion no valida, intenta de nuevo')

                    opcion = input('\nElige una opción: ')

                # convertimos lo ingresado por el usuario a entero
                opcion = int(opcion)

                # verificamos que la oopcion este dentro de la lista
                if 1 <= opcion <= len(recetas2):

                    # almacenamos el nombre elegido por el usuario
                    receta = recetas2[opcion - 1]

                    # almacenamos la ruta del archivo
                    archivo = Path(ruta, resultado_categoria1, receta)

                    # verificamos si es un archivo
                    if archivo.is_file():

                        # traemos el nombre del archivo sin extencion
                        archivo1 = archivo.stem

                        # le preguntamos al usuario si quiere realmente eliminar el archivo
                        archivos = input(f'\nSeguro quieres borrar \033[1m{archivo1}\033[0m S/N: ').upper()

                        # si la respuesta es positiva
                        if archivos == 'S':

                            # borramos el archivo
                            os.remove(archivo)

                            # limpiamos la pantalla
                            system('cls')

                            # informamos al usuario
                            print(f'\nEl archivo \033[1m{archivo1}\033[0m se ha borrado del sistema con exito')

                            # actualizamos la lista
                            recetas2 = [receta.name for receta in resultado_categoria1.glob('*.txt')]

                        else: 

                            # informamos al usuario
                            print(f'\nEl archivo \033[1m{archivo1}\033[0m no se ha borrado del sistema')
                        
                    else: 

                        # informamos al usuario
                        print(f'\nEl archivo \033[1m{archivo1}\033[0m no se ha borrado del sistema, porque no existe')

                else:
                    
                    # informamos al usuario
                    print('\nOpción no válida. Ingresa un número válido.')
                
                # preguntamos si se quiere borrar otro archivo
                borrado = input('\nDeseas borrar un archivo. S/N: ').upper()

                # si la respuesta es negativa
                if borrado == 'N':

                    # preguntamos al usuario 
                    salir = input('\nDeseas salir del sistema? S/N. ').upper()

                    # si la respuesta es positiva
                    if salir == 'S':

                        salir_sistema()

                    # si la respuesta es negativa
                    else:

                        # informamos al usuario
                        print('\nSi eliges \033[1mN\033[0m saldras del sistema')

                        # preguntamos al usuario 
                        salir = input('\nDeseas regresar al menu principal? S/N. ').upper()

                        # si la respuesta es positiva
                        if salir == 'S':

                            # entra al menu ppal
                            entrada_sistema(ruta)

                        # si es negativa
                        else:

                            salir_sistema()

                # verificamos si hay archivos
                if not recetas2:

                    # informamos al usuario
                    print(f"\nNo hay recetas para mostrar en \033[1m{respuesta}\033[0m")

                    # le preguntamos que quiere hacer
                    opcion3 = input('\nSi prefieres puedes regresar al menu principal con\033[1m S \033[0mo salir del sistema con\033[1m N \033[0mS/N: ').upper()

                    # comprobamos la respuesta
                    while opcion3 not in ['N', 'S']:

                        print('\nNo has ingresado un carácter válido')

                        opcion3 = input('\nVuelve a intentar s/n: \n').upper()

                    # si la respuesta es positiva
                    if opcion3 == 'S':

                        salir_sistema()

                    # si la respuesta es negativa
                    else:

                        entrada_sistema(ruta)

                # si se desea borrar otro oarchivo y vuelve a empezar el bucle
                borrado = input('\nDeseas borrar un archivo. S/N: ').upper()
    
    # si la respuesta es negativa
    if respuesta1 == 'N':

        # le preguntamos al usuario que desea hacer
        salir = input('\nDeseas salir del sistema? s/n. ').upper()

        # si la respuesta es positiva
        if salir == 'S':

            salir_sistema()

        # si la respuesta es negativa
        else:

            # informamos al usuario
            print('\nSi eliges \033[1mN\033[0m saldras del sistema') 

            # le preguntamos al usuario que desea hacer
            salir = input('\nDeseas regresar al menu principal? s/n. ').upper()

            # si la respuesta es positiva
            if salir == 'S':

                entrada_sistema(ruta)

            # si la respuesta es negativa
            else:

                salir_sistema()

# con esta funcion eliminas las categorias que tengas en tu directorio
def eliminar_categoria (categoria, resultado, ruta):

    # se le pregunta al usuario si va a eliminar esa categoria
    respuesta = input(f'\nDeseas eliminar el directorio\033[1m {resultado} \033[0mS/N: ').upper()

    # guardamos la ruta
    ruta = Path(ruta)

    # guardamos el resultado que queremos borrar
    nombre = resultado

    # obtenemos la ruta completa
    ruta1 = ruta / nombre

    # mientras la respuesta sea positiva
    while respuesta == 'S':

        # verificamos si es un directorio
        if ruta1.is_dir():

            # verificamos si el directorio esta vacio
            if not os.listdir(ruta1):

                # se borra el directorio
                os.rmdir(ruta1)

                # informamos al usuario
                print('\nEl directorio se ha eliminado con exito')

                # actualizamos la lista
                categoria.remove(resultado)

            # si no esta vacio
            else:

                # le preguntamos al usuario 
                respuesta2 = input('\nEl directorio no esta vacio, ¿deseas eliminarlo de todas formas S/N: ').upper()

                # si la respuesta es negativa
                if respuesta2 == 'S':

                    # eliminamos el arbol con su contenido
                    shutil.rmtree(ruta1)
                    
                    # informamos al usuario
                    print('\nEl directorio se ha eliminado con exito')

                    # actualizamos la lista
                    categoria.remove(resultado)

                # si no se borra
                else:

                    # informamos al usuario
                    print('\nEl directorio no se ha eliminado')

        # sie el directorio no existe
        else:

            # informamos al usuario
            print('\nEl directorio no existe')

        # preguntamos al usuario
        respuesta = input('\nDeseas eliminar otro directorio S/N: ').upper()

        # comprobamos la respuesta
        while respuesta not in  ['N', 'S']:

            print('\nHas ingresado un caracter no valido')

            respuesta = input('\nDeseas eliminar otro directorio S/N: ').upper()
        
        # limpiamos pantalla
        system('cls')

        # si la respuesta es positiva
        while respuesta == 'S':

            # guardamos la ruta
            ruta = Path(ruta)

            # informamos al usuario
            print('\nElige una opcion del siguiente \033[1mMenu \033[0m')
           
            print('\n')

            # recorremos la lista con un bucle y lo listamos para imprimirlo
            for i,r in enumerate(categoria, start=1):

                lista = [f'{i} = {r}']

                print(''.join(lista))

            # pedimos la usuario que elija
            opcion = input('\nElige una opcion: ')

            # comprobamos la respuesta
            while not opcion.isnumeric():

                print('\nEL digito ingresado no es un numero')

                opcion = input('\nElige una opcion: ')

            # convertimos a entero la eleccion del usuario
            opcion = int(opcion)

            # traemos el nombre de la eleccion
            opcion2 = categoria[opcion -1]

            # informamos al usuario
            print(f'\nHas elegido \033[1m{opcion2}\033[0m')

            # obtenemos la ruta completa
            ruta1 = ruta / opcion2

            # verificamos si es un directorio
            if ruta1.is_dir():

                # verificamos si el directorio esta vacio
                if not os.listdir(ruta1):

                    # se borra el directorio
                    os.rmdir(ruta1)

                    # infromamos al usuario
                    print('\nEl directorio se ha eliminado con exito')

                    # actualizamaos la lista
                    categoria.remove(opcion2)

                # si el directorio no esta vacio
                else:

                    # informamos al usuario y preguntamos
                    respuesta2 = input('\nEl directorio no esta vacio, ¿deseas eliminarlo de todas formas S/N: ').upper()

                    # si la respuesta es positiva
                    if respuesta2 == 'S':

                        # borramso el arbol completo que se ha seleccionado
                        shutil.rmtree(ruta1)
                        
                        # informamos al usuario
                        print('\nEl directorio se ha eliminado con exito')

                        # actualizamos la lista
                        categoria.remove(opcion2)

                    # si la respuesta es negativa
                    else:

                        # informamos al usuario 
                        print('\nEl directorio no se ha eliminado')

            # si el directorio no existe
            else:

                # informamos al usuario
                print('\nEl directorio no existe')

            # preguntamos al usuario
            respuesta = input('\nDeseas eliminar otro directorio S/N: ').upper()

            # comprobamso la respuesta
            while respuesta not in  ['N', 'S']:

                print('\nHas ingresado un caracter no valido')

                respuesta = input('\nDeseas eliminar otro directorio S/N: ').upper()
    
    # si la respuesta es negativa
    else:

        # se le pregunta al usuario
        salir = input('\nDeseas salir del sistema? S/N: ').upper()

        # se verifica la respuesta
        while salir not in ['N', 'S']:

            print('\nNo has elegido un caracter valido, intenta de nuevo ')

            salir = input('\nDeseas salir del sistema? S/N: ').upper()

        # si la respuesta es positiva
        if salir == 'S':

            salir_sistema()

        # si la respuesta es negativa
        else:

            # informamos al usuario
            print('\nSi eliges \033[1mN\033[0m saldras del sistema') 

            # se le pregunta al usuario
            salir = input('\nDeseas regresar al menu principal? S/N. ').upper()

            # se verifica la respuesta
            while salir not in ['N', 'S']:

                print('\nNo has elegido un caracter valido, intenta de nuevo ')

                salir = input('\nDeseas salir del sistema? S/N: ').upper()

            # si la respuesta es positiva
            if salir == 'S':

                # ingresa al menu ppal
                entrada_sistema(ruta)

            # si la respuesta es negativa
            else:

                # sale del sistema
                salir_sistema()

# con esta funcion se sale del sistema
def salir_sistema ():

    # se limpia pantalla
    system('cls')

    # se le informa al usuario
    print('\nHas Salido del Sistema')

    # mensaje de despedida
    print('\n!Hasta pronto¡\n')

    # sale del sistema
    exit()

# son esta funcion se verifican las categorias
def comprobar_categoria (categoria):

    # verificamos que si exista una categoria
    if not categoria:

        print('\nNo hay categorias disponibles')

        return

    # informamos al usuario
    print('\nElige una opción del siguiente \033[1mMenu\033[0m\n')

    # listamos las categorias que le hemos pasado a la funcion
    for i,r in enumerate(categoria, start=1):

        lista = [f'{i} = {r}']

        print(''.join(lista))

    # le pedimos al usuario que eliga
    opcion = input('\nElige una opción: ')

    #verificamos si la opcion ingresada es correcta
    while not opcion.isnumeric() or int(opcion) > len(categoria) or int(opcion) <= 0:

        print('\nEl directorio no existe o no es un caracter valido, intenta de nuevo')

        opcion = input('\nElige una opción: ')

    # almacenamos el nombre elegido en una variable
    opcion2 = categoria[int(opcion) -1]

    # informamos al usuario
    print(f'\nHas elegido \033[1m{opcion2}\033[0m')

    # retornamos la elección
    return opcion2

# funcion para entrar al sistema de opciones
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

        crear_directorio(ruta)

    respuesta = (comprobar_categoria(categoria))

    match opcion:

        case 1:
                        
            menu_lectura_receta(categoria, respuesta, ruta)

        case 2:

            crear_receta_directorio(respuesta, ruta)
                    
        case 4:

            eliminar_receta( respuesta, ruta)

        case 5:

            eliminar_categoria(categoria, respuesta, ruta)

        case _:

            print('\nHas elegido un comando incorrecto, intenta de nuevo')

            opcion = input('Elige una opcion: ')

# se declaran variables
#almacenamos el nombre que ingresa el usuario
nombre = entrada_nombre()

# llamamos a la funcion de verificar el usuario para poder empezar
verificar_usuario(mostrar_bienvenida_usuario_nuevo(nombre), nombre)
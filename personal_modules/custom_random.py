#-----------------------------------------------------------------------------------------------------------------------
# Importación de las bibliotecas / módulos necesarios para este código

# Importación de la biblioteca / módulo para generar números aleatorios
import random

# Importación de la biblioteca / módulo para realizar pequeñas paradas en el código
import time


#-----------------------------------------------------------------------------------------------------------------------
# Declaración de función para realizar este módulo o biblioteca

def funcion_principal():
    #-------------------------------------------------------------------------------------------------------------------
    # Declaración de variables para esta función

    # Declaración de variable contadora de intentos a 1 por una petición fuera del bucle
    contador_intentos = 1


    #-------------------------------------------------------------------------------------------------------------------
    # Petición de números personalizados por el usuario para establecer la cota inferior y la cota superior

    cota_inferior_usuario = input('Introduzca el primer número para establecer el rango\n')

    # Conversión del tipo de dato de STR a INT o salida al menú si no es posible
    try:
        cota_inferior_usuario = int(cota_inferior_usuario)

    # Si no es posible la conversión, devuelve un mensaje y vuelve al menú principal
    except:
        print('No se ha introducido un número, por lo que se volverá al menú principal')
        time.sleep(4)
        return

    cota_superior_usuario = input('\nIntroduzca el segundo número para establecer el rango\n')

    # Conversión del tipo de dato de STR a INT o salida al menú si no es posible
    try:
        cota_superior_usuario = int(cota_superior_usuario)

    # Si no es posible la conversión, devuelve un mensaje y vuelve al menú principal
    except:
        print('No se ha introducido un número, por lo que se volverá al menú principal')
        time.sleep(4)
        return


    #-------------------------------------------------------------------------------------------------------------------
    # Intercambio de valores por si el primer número fuese mayor al segundo
    if cota_inferior_usuario > cota_superior_usuario:
        aux = cota_inferior_usuario
        cota_inferior_usuario = cota_superior_usuario
        cota_superior_usuario = aux


    #-------------------------------------------------------------------------------------------------------------------
    # Finalización de declaración de variables según los datos introducidos por el usuario

    # Declaración de variable que contendrá un número aleatorio entre los valores establecidos por el usuario
    aleatorio_personalizado = random.randint(cota_inferior_usuario, cota_superior_usuario)

    # Variable para acotar por el extremo inferior al número aleatorio escogido por el usuario
    cota_inferior = cota_inferior_usuario

    # Variable para acotar por el extremo superior al número aleatorio escogido por el usuario
    cota_superior = cota_superior_usuario


    #-------------------------------------------------------------------------------------------------------------------
    # Inicio del código de la función principal de esta biblioteca / módulo

    numero = input(f'\nIntroduzca un número entre el {cota_inferior} y {cota_superior}\n')

    # Conversión del tipo de dato de STR a INT o salida al menú si no es posible
    try:
        numero = int(numero)

    # Si no es posible la conversión, devuelve un mensaje y vuelve al menú principal
    except:
        print('No se ha introducido un número, por lo que se volverá al menú principal')
        time.sleep(4)
        return

    while numero != aleatorio_personalizado:
        contador_intentos = contador_intentos + 1

        # Comparación del número escogido por el usuario con el número aleatorio
        if numero < aleatorio_personalizado:
            print('El número', numero, 'es menor al número a acertar\n')
            
            # Parada de dos segundos para que el usuario lea la última línea generada
            time.sleep(1)

            # Actualización de la cota inferior para indicar en todo momento la última actualización del número
            if numero >= cota_inferior:
                cota_inferior = numero + 1

        elif numero > aleatorio_personalizado:
            print('El número', numero, 'es mayor al número a acertar\n')
            
            # Parada de dos segundos para que el usuario lea la última línea generada
            time.sleep(1)

            # Actualización de la cota superior para indicar en todo momento la última actualización del número
            if numero <= cota_superior:
                cota_superior = numero - 1

        numero = input(f'\nEscoja un número entre {cota_inferior} y {cota_superior}, ambos incluidos\n')

        # Conversión del tipo de dato de STR a INT o salida al menú si no es posible
        try:
            numero = int(numero)

        # Si no es posible la conversión, devuelve un mensaje y vuelve al menú principal
        except:
            print('No se ha introducido un número, por lo que se volverá al menú principal')
            time.sleep(4)
            return

    if numero == aleatorio_personalizado:
        time.sleep(1)

        print('\n¡Has acertado el número aleatorio!\n')

        print(f'\nTe ha costado {contador_intentos} vez/veces\n')

        input('\nPulse la tecla Intro o Enter para continuar...\n')
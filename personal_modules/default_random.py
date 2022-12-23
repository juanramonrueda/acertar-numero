#----------------------------------------------------------------------------------------------------------------------
# Importación de bibliotecas / módulos para el código

# Importación de la biblioteca / módulo para generar números aleatorios
import random

# Importación de la biblioteca / módulo para realizar pequeñas paradas en el código
import time


#----------------------------------------------------------------------------------------------------------------------
# Declaración de función para realizar este módulo o biblioteca

def funcion_principal():
    #------------------------------------------------------------------------------------------------------------------
    # Declaración de variables para esta función
    
    # Declaración de variable contadora de intentos a 1 por una petición fuera del bucle
    contador_intentos = 1

    # Declaración de variable que contendrá un número aleatorio del 0 al 100
    aleatorio_generado = random.randint(0, 100)

    # Variable para acotar por el extremo inferior al número aleatorio
    cota_inferior = 0

    # Variable para acotar por el extremo superior al número aleatorio
    cota_superior = 100


    #------------------------------------------------------------------------------------------------------------------
    # Inicio del código de la función principal de esta biblioteca / módulo

    numero = input('Introduzca un número del 1 al 100\n')

    # Conversión del tipo de dato de STR a INT o salida al menú si no es posible
    try:
        numero = int(numero)

    # Si no es posible la conversión, devuelve un mensaje y vuelve al menú principal
    except:
        print('No se ha introducido un número, por lo que se volverá al menú principal')
        time.sleep(4)
        return

    while numero != aleatorio_generado:
        contador_intentos = contador_intentos + 1

        # Comparación del número escogido por el usuario con el número aleatorio
        if numero < aleatorio_generado:
            print('El número', numero, 'es menor al número a acertar\n')
            
            # Parada de dos segundos para que el usuario lea la última línea generada
            time.sleep(1)

            # Actualización de la cota inferior para indicar en todo momento la última actualización del número
            if numero >= cota_inferior:
                cota_inferior = numero + 1

        elif numero > aleatorio_generado:
            print('El número', numero, 'es mayor al número a acertar\n')
            
            # Parada de dos segundos para que el usuario lea la última línea generada
            time.sleep(1)

            # Actualización de la cota superior para indicar en todo momento la última actualización del número
            if numero <= cota_superior:
                cota_superior = numero - 1

        numero = input(f'Escoja un número entre {cota_inferior} y {cota_superior}, ambos incluidos\n')

        # Conversión del tipo de dato de STR a INT o salida al menú si no es posible
        try:
            numero = int(numero)

        # Si no es posible la conversión, devuelve un mensaje y vuelve al menú principal
        except:
            print('No se ha introducido un número, por lo que se volverá al menú principal')
            time.sleep(4)
            return

    if numero == aleatorio_generado:
        time.sleep(1)

        print('\n¡Has acertado el número aleatorio!')

        print(f'Te ha costado {contador_intentos} vez/veces\n')

        input('Pulse la tecla Intro o Enter para continuar...\n')
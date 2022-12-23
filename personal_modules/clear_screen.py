#-----------------------------------------------------------------------------------------------------------
# Importación de bibliotecas / módulos para el código

# Importación de biblioteca / módulo para conocer el sistema operativo dónde se ejecuta el código
import platform

# Importación de biblioteca / módulo para ejecutar instrucciones según el sistema operativo
import os


#-----------------------------------------------------------------------------------------------------------
# Declaración de funciones

# Función para detectar el sistema operativo dónde se ejecuta el código
def funcion_principal():
    # Detección del sistema operativo mediante platform.system() y guardado en una variable
    os_system = platform.system()

    # En el caso de que no sea ni Linux ni Windows, finalizará la ejecución del código
    if (os_system != 'Linux') and (os_system != 'Windows'):
        print('No es ni Linux ni Windows, por lo que se detendrá la ejecución del programa')
        exit()

    # En el caso de que sea Linux el sistema, usará el comando "clear" para limpiar la pantalla
    elif os_system == "Linux":
        # Ejecución del comando "clear" para limpiar la pantalla mediante os.system()
        os.system('clear')
    
    # En el caso de que sea Windows el sistema, usará el comando "cls" para limpiar la pantalla
    elif os_system == "Windows":
        # Ejecución del comando "cls" para limpiar la pantalla mediante os.system()
        os.system('cls')
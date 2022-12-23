#-------------------------------------------------------------------------------------------------------------------
# Importación de bibliotecas / módulos para el código

# Importación de biblioteca / módulo personal para realizar la limpieza de pantalla
import personal_modules.clear_screen

# Importación de biblioteca / módulo personal para mostrar el menú con las opciones que tiene el código
import personal_modules.show_menu_options

# Importación de biblioteca / módulo personal para acertar el número con opciones por defecto
import personal_modules.default_random

# Importación de biblioteca / módulo personal para acertar el número con valores introducidos por el usuario
import personal_modules.custom_random


#-------------------------------------------------------------------------------------------------------------------
# Declaración de funciones

# Función principal
def main():
    
    #---------------------------------------------------------------------------------------------------------------
    # Se fuerza la entrada en el bucle mediante una variable
    user_option = 0

    #---------------------------------------------------------------------------------------------------------------
    # Inicio del bucle si el valor introducido por el usuario o mediante variable es distinto de 3
    while user_option != 3:
        # Llamada y ejecución del archivo clear_screen.py y su función para limpiar la pantalla
        personal_modules.clear_screen.funcion_principal()

        # Llamada y ejecución del archivo show_menu_options.py y su función para mostrar las opciones disponibles
        personal_modules.show_menu_options.funcion_principal()

        # Petición al usuario de una opción del menú
        user_option = int(input('Introduzca la opción deseada\n'))

        #-----------------------------------------------------------------------------------------------------------
        # Si el valor introducido es 1, limpiará la pantalla y ejecutará la biblioteca por defecto
        if user_option == 1:
            personal_modules.clear_screen.funcion_principal()

            personal_modules.default_random.funcion_principal()

        #-----------------------------------------------------------------------------------------------------------
        # Si el valor introducido es 2, limpiará la pantalla y ejecutará la biblioteca de personalización de rangos
        elif user_option == 2:
            personal_modules.clear_screen.funcion_principal()

            personal_modules.custom_random.funcion_principal()

        #-----------------------------------------------------------------------------------------------------------
        # Al pasar el IF Statement, tanto si se ejecuta como si no, limpia la pantalla y muestra el menú
        elif user_option == 3:
            print('Ejecución finalizada')


#-----------------------------------------------------------------------------------------------------------
# Ejecución de la función principal
if __name__ == "__main__":
    main()
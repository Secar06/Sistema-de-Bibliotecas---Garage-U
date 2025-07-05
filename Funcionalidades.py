def validar_opcion_menu(lista, opcion):
    """Verifica que una opcion se encuentra en una lista de opciones.
            PARAMS
                lista: lista de opciones válidas.
                opcion: número escogido por el usuario.
        Retorna True si efectivamente se encuentra en la lista, de lo contrario retorna False.
    """
    if opcion in lista:
        return True
    else:
        return False

def solicitar_opcion_menu(menu, lista, salir = bool):
    """
            PARAMS
                menú = el menú a mostrar.
                lista = lista de opciones válidas.
            RETURNS
                Retorna la opción del usuario si se encuentra en la lista, None en caso de que se quiera volver al menú principal.
    """
    while True:
        print(menu)
        if salir:
            opcion_usuario = input("Seleccione una opcion del menú o presione Enter para volver al menú principal: ")
            if opcion_usuario == "":
                return None
        else:
            opcion_usuario = input("Seleccione una opcion del menú: ")
            try:
                opcion_usuario = int(opcion_usuario)
            except ValueError:
                print("\nEl tipo de dato ingresado es erróneo, por favor ingrese un número del menú.")
            else:
                if validar_opcion_menu(lista, opcion_usuario):
                    return opcion_usuario
                else:
                    print("\nLa opcion ingresada es incorrecta, por favor intente nuevamente...")

def registrar_recurso_menu():
    """Imprime el menú de Registro de Recursos"""
    return (
        "      Registro de Recurso    \n"
        "\nIngrese el tipo de recurso:\n"
        "1. Libro\n"
        "2. Revista\n"
        "3. Video\n"
        "4. Audio")

def mostrar_menu_usuario():
    """Imprime el menú del usuario."""
    return(
        "==============================\n"
        "         MENÚ DE USUARIO      \n"
        "==============================\n"
        "1. Actualizar datos\n"
        "2. Cerrar sesión")


def mostrar_menu_admin():
    """Imprime el menú del usuario."""
    return (
        "\n==============================\n"
        "     MENÚ DE ADMINISTRADOR    \n"
        "==============================\n"
        "1. Registrar un nuevo usuario\n"
        "2. Modificar un usuario\n" 
        "3. Registrar un nuevo recurso\n"
        "4. Inhabilitar Un recurso\n"
        "5. Cerrar sesión")

def mostrar_menu_biblio():
    """Imprime el menú del bibliotecario."""
    return (
        "\n==============================\n"
        "     MENÚ DE BIBLIOTECARIO    \n"
        "==============================\n"
        "1. Registrar un nuevo recurso\n"
        "2. Inhabilitar Recurso\n"
        "3. Cerrar sesión\n")

def mostrar_menu_principal():
    """Imprime el menú del administrador."""
    return (
    "\n============================\n"
    "       MENÚ PRINCIPAL       \n"
    "============================\n"
    "1. Autenticarse\n"
    "2. Salir de la app")


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

def solicitar_opcion_menu(menu, lista):
    """Solicita al usuario una opción válida de un menú dado como parametro y valida si encuentra en la lista de opciones.
            PARAMS
                menú = el menú a mostrar.
                lista = lista de opciones válidas.
            RETURNS
                Retorna la opción del usuario si se encuentra en la lista, None en caso de que se quiera volver al menú principal.
    """
    while True:
        print(menu)
        opcion_usuario = input("Seleccione una opcion del menú o presione Enter para volver al menú principal: ")
        if opcion_usuario == "":
            return None
        else:
            try:
                opcion_usuario = int(opcion_usuario)
            except ValueError:
                print("El tipo de dato ingresado es erróneo, por favor ingrese un número del menú.")
            else:
                if validar_opcion_menu(lista, opcion_usuario):
                    return opcion_usuario
                else:
                    print("La opcion ingresada es incorrecta, por favor intente nuevamente...")

def registrar_recurso_menu():
    """Imprime el menú de Registro de Recursos"""
    print("  REGISTRO DE RECURSO  ")
    print("\nIngrese el tipo de recurso:\n1. Libro\n2. Revista\n3. Video\n4. Audio")

def mostrar_menu_usuario():
    """Imprime el menú del usuario."""
    print("\n" + "=" * 25)
    print(" MENÚ DE USUARIO ")
    print("=" * 25)
    print("1. Actualizar datos \n2. Cerrar sesión")

def mostrar_menu_admin():
    """Imprime el menú del usuario."""
    print("\n" + "=" * 25)
    print(" MENÚ DE ADMINISTRADOR ")
    print("=" * 25)
    print("1. Registrar un nuevo usuario \n2. Modificar un usuario \n3. Registrar un nuevo recurso \n4. Inhabilitar Un recurso\n5. Cerrar sesión")

def mostrar_menu_biblio():
    """Imprime el menú del bibliotecario."""
    print("\n" + "=" * 25)
    print(" MENÚ DE BIBLIOTECARIO ")
    print("=" * 25)
    print("1. Registrar un nuevo recurso \n2. Inhabilitar Recurso \n3. Cerrar sesión")
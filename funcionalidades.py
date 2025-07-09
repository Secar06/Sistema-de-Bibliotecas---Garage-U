from datetime import date, timedelta

ABECEDARIO = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóú"


def buscar_entidad(arreglo, id):
    for i in range(len(arreglo)):
        entidad = arreglo[i]
        if entidad is None:
            break
        elif entidad.get_id() == id:
            return entidad

def buscar_usuario(arreglo, id):
    for i in range(len(arreglo)):
        entidad = arreglo[i]
        if entidad is None:
            break
        elif entidad.identificacion == id:
            return i
    return None

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
                input("\nEl tipo de dato ingresado es erróneo, presione Enter e intente nuevamente...")
            else:
                if opcion_usuario in lista:
                    return opcion_usuario
                else:
                    input("\nLa opcion ingresada es incorrecta, presione Enter e intente nuevamente...")
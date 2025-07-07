from datetime import date, timedelta

ABECEDARIO = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def buscar_entidad(arreglo, id):
    for i in range(len(arreglo)):
        entidad = arreglo[i]
        if entidad is None:
            break
        elif entidad.get_id() == id:
            return entidad
        
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
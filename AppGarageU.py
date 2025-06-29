import numpy as np
from Recurso import Recurso
from Usuario import Usuario

class AppGarageU():
    """ En esta clase llamada AppGarageU se lleva a cabo las funcionalidades del programa, como registrar un nuevo usuario, verificar el usuario,
    añadir nuevos recursos, entre otros
    00
    Autor: Sebastián Cardona, Elkin Alejandro López, Henry Hincapié
    Fecha: 01/05/2025
    """
    #ATRIBUTOS
    arreglo_recursos = np.ndarray
    arreglo_usuarios = np.ndarray
    contador_usuarios = int
    contador_recursos = int
    usuario_autenticado = Usuario

    # CONSTANTES
    TIPO_ESTUDIANTE = 1
    TIPO_EMPLEADO = 2
    PERFIL_ADMIN = 1
    PERFIL_BIBLIO = 2
    PERFIL_USUARIO = 3
    MAX_RECURSOS = 100
    MAX_USUARIOS = 100

    def __init__(self):
        self.arreglo_usuarios = np.full(self.MAX_RECURSOS, fill_value = None, dtype= object)
        self.arreglo_recursos = np.full(self.MAX_USUARIOS, fill_value = None, dtype= object)

        self.arreglo_usuarios[0] = Usuario(nombre = "Administrador", identificacion=000, contrasenna='000')
        self.arreglo_usuarios[0].cambiar_perfil(self.PERFIL_ADMIN)
        self.contador_usuarios = 1
        self.contador_recursos = 0



        self.usuario_autenticado = None

    def registrar_usuario(self):
        """
        En este método es donde se realiza el registro de usuarios en el sistema. Esto se hace por medio de un arreglo, el cual es el que
        almacena los nuevos usuarios registrados en el sistema, y por medio de un match case se identifica qué tipo de usuario se registra
        """
        if self.contador_usuarios <= self.MAX_USUARIOS:
            user = Usuario()

            user.identificacion = int(input("Ingrese el número de identificación del nuevo usuario: "))

            while self.validar_usuario(user.identificacion):
                print(f"\n[ADMIN] Se encontró un usuario con la identificación {user.identificacion}\n")
                user.identificacion = int(input("Ingrese un número de identificación válido: "))

            user.almacenar_datos()
            self.arreglo_usuarios[self.contador_usuarios] = user
            self.contador_usuarios += 1

            print("\n[ADMIN] ¡Usuario Registrado Exitosamente!")
            print("=" * 50)
            print(f"Identificación: {user.identificacion}")
            print(f"Contraseña: {user.identificacion}")
            print(f"Nombre completo: {user.nombre}")
            print(f"Dirección: {user.direccion.lower()}")
            print(f"Teléfono: {user.telefono}")
            print(f"Email registrado: {user.email.lower()}")
            print("=" * 50)
            match user.tipo_usuario:
                case 1:
                    print(f"Tipo de usuario: Estudiante")
                case 2:
                    print(f"Tipo de usuario: Empleado")

            match user.perfil_usuario:
                case 1:
                    print(f"Perfil de usuario: Administrador")
                case 2:
                    print(f"Perfil de usuario: Bibliotecario")
                case 3:
                    print(f"Perfil de usuario: Usuario")
            print("=" * 40)
            input("Presione Enter para continuar...")
        else:
            print("No se puede realizar el registro del usuario.\nCausa: almacenamiento insuficiente en el sistema.")

    def validar_usuario(self, id_a_buscar):
        for i in range(self.contador_usuarios):
            if self.arreglo_usuarios[i].identificacion == id_a_buscar:
                return True
        return False

    def modificar_usuario(self, id_a_buscar):
        if self.contador_usuarios > 0:
            for i in range(self.contador_usuarios):
                usuario = self.arreglo_usuarios[i]
                if usuario.identificacion == id_a_buscar:
                    return usuario.actualizar_datos(self.usuario_autenticado)
            input(f"\n[ADMIN] No se encontró un usuario identificado con: {id_a_buscar}. Presione Enter para continuar...")
            print("\n"*20)
        else:
            print("No hay usuarios registrados en el sistema.")

    def verificar_usuario(self):
        """
        Es por medio de este método que el sistema podrá verificar si un usuario existe y poder iniciar la sesión del mismo,
        esto por medio de un ciclo for, el cual se encarga de recorrer el arreglo que almacena los datos de los usuarios y
        pide así la identificación y la contraseña del usuario con el fin de verificarlo.
        """
        print("\n" + "=" * 50)
        print("                INICIO DE SESIÓN             ")
        print("=" * 50)


        identificacion = int(input("Ingrese su número de identificación: "))
        for i in range(self.contador_usuarios):
            usuario = self.arreglo_usuarios[i]
            if usuario.identificacion == identificacion:
                contrasenna = input("Ingrese su contraseña: ")
                if usuario.contrasenna == contrasenna:
                    self.usuario_autenticado = self.arreglo_usuarios[i]
                    return True
                else:
                    print("Identificación o contraseña incorrecta. Acceso denegado.")
                    return False
        input(f"El usuario con identificación {identificacion} no está registrado. Presione enter para continuar ...")
        return False

    def registrar_recurso(self):
        """
        Por medio de este método es que un usuario bibliotecario puede registrar nuevos recursos
        gracias a un condicional if que analiza si aún hay espacio para añadir un nuevo recurso
        y en caso de que sí se cumpla esta condición, se pedirán los datos necesarios para añadir
        el recurso nuevo y se mostrará un mensaje avisando que se registró correctamente el recurso,
        junto con su número de inventario.
        """
        print("\n" + "=" * 50)
        print("   MENÚ DE BIBLIOTECARIO - REGISTRO DE RECURSO ")
        print("=" * 50)
        if self.contador_recursos < self.MAX_RECURSOS:
            recurso = Recurso()
            recurso.solicitar_datos()
            recurso.numero_inventario = self.contador_recursos + 1
            self.arreglo_recursos[self.contador_recursos] = recurso
            self.contador_recursos += 1
            print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
            print("=" * 50)
            print(f"Titulo: {recurso.titulo}")
            match recurso.coleccion :
                case 1:
                    print("Tipo de recurso: GENERAL")
                case 2:
                    print("Tipo de recurso: RESERVA")
                case 3:
                    print("Tipo de recurso: HEMEROTECA")
            match recurso.estado:
                case 1:
                    print("Tipo de recurso: PRESTADO")
                case 2:
                    print("Tipo de recurso: DISPONIBLE")
                case 3:
                    print("Tipo de recurso: REPARACION")
                case 4:
                    print("Tipo de recurso: INACTIVO")
            print(f"Código alfanumérico: {recurso.codigo_alfnum}")
            match recurso.tipo_recurso:
                case 1:
                    print("Tipo de recurso: Libro")
                    print("=" * 50)
                case 2:
                    print("Tipo de recurso: Video")
                    print("=" * 50)
                case 3:
                    print("Tipo de recurso: Audio")
                    print("=" * 50)
                case 4:
                    print("Tipo de recurso: Revista")
                    print("=" * 50)
        else:
            print("No se puede realizar el registro del recurso.\n Causa: almacenamiento insuficiente en el sistema.")

    def mostrar_menu_usuario(self):
        """
        En este método se mostrará el menú del usuario regular, el cual por el momento solo
        tiene permitido actualizar sus datos.
        """
        option = -1
        while option != 2:
            print("\n" + "=" * 25)
            print(" MENÚ DE USUARIO ")
            print("=" * 25)

            print("1. Actualizar datos \n2. Cerrar sesión")
            option = int(input("Seleccione una opción del menú: "))

            match option:
                case 1:
                    self.usuario_autenticado.actualizar_datos(self.usuario_autenticado)
                case 2:
                    input("\nSe ha cerrado la sesión correctamente. Presione Enter para continuar...")
                case _:
                    input("\nOpción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...")

    def mostrar_menu_admin(self):
        """
        En este método se mostrará el menú del usuario administrador, el cual por medio de un ciclo while
        permite al usuario escoger entre 3 opciones qué desea hacer, si registrar un usuario nuevo o
        modificar uno ya existente. Al escoger una opción, gracias al match case se podrá ejecutar sin
        problemas la opción elegida por el usuario administrador.
        """
        option = -1
        while option != 5:
            print("\n" + "=" * 25)
            print(" MENÚ DE ADMINISTRADOR ")
            print("=" * 25)
            print("1. Registrar un nuevo usuario \n2. Modificar un usuario \n3. Registrar un nuevo recurso \n4. Inhabilitar Un recurso\n5. Cerrar sesión")
            option = int(input("Seleccione una opción del menú: "))

            match option:
                case 1:
                    input("\n[ADMIN] Ha seleccionado la opción 1. Presione Enter para continuar...")
                    print("\n" + "=" * 50)
                    print("   MENÚ DE ADMINISTRADOR - REGISTRO DE USUARIO ")
                    print("=" * 50)
                    self.registrar_usuario()
                case 2:
                    print("\n" + "=" * 50)
                    print(" MENÚ DE ADMINISTRADOR - MODIFICACIÓN DE REGISTROS ")
                    print("=" * 50)
                    input("\n[ADMIN] Ha seleccionado la opción 2. Presione Enter para continuar...") 
                    user_id = int(input("\nDigite el número de documento del usuario: "))
                    self.modificar_usuario(user_id)
                    print("\n"*20)
                case 3:
                    print("\n" + "=" * 50)
                    print(" MENÚ DE ADMINISTRADOR - REGISTRO DE RECURSO ")
                    print("=" * 50)
                    input("\n[ADMIN] Ha seleccionado la opción 3. Presione Enter para continuar...")
                    self.registrar_recurso()
                case 4:
                    print("\n" + "=" * 50)
                    print(" MENÚ DE ADMINISTRADOR - INHABILITACIÓN DE RECURSO ")
                    print("=" * 50)
                    input("\n[ADMIN] Ha seleccionado la opción 4. Presione Enter para continuar...")
                    self.inhabilitar_recurso()
                case 5:
                    input("\n[ADMIN] Se ha cerrado la sesión correctamente. Presione Enter para continuar...")
                case _:
                    input("\n[ADMIN] Opción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...")


    def mostrar_menu_biblio(self):
        """
        Por medio de este método es que el usuario bibliotecario podrá escoger si desea registrar
        un recurso nuevo o si desea inhabilitarlo. Este método de menú funciona igual que los dos
        anteriores, por medio de un ciclo while se mostrará el menú para que el usuario eliga qué
        quiere hacer y por medio de un match case se ejecutará la funcionalidad correspondiente.
        """
        option = -1
        while option != 3:
            print("\n" + "=" * 25)
            print(" MENÚ DE BIBLIOTECARIO ")
            print("=" * 25)
            print("1. Registrar un nuevo recurso \n2. Inhabilitar Recurso \n3. Cerrar sesión")
            option = int(input("Seleccione una opción del menú: "))

            match option:
                case 1:
                    self.registrar_recurso()
                case 2:
                    self.inhabilitar_recurso()
                case 3:
                    input("\nSe ha cerrado la sesión correctamente. Presione Enter para continuar...")
                case _:
                    input("\n[ADMIN] Opción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...")

    def inhabilitar_recurso(self):
        """
        Es por medio de este método que los usuarios administradores pueden inhabilitar recursos;
        por medio de un ciclo for el cual recorre el arreglo que almacena los recursos luego de
        haber ingresado el numero de inventario del recurso, el sistema analiza si el recurso ya
        se encuentra inhabilitado y en caso de no estarlo se emitirá un mensaje mostrando el número
        de inventario del recurso avisando que ya se ha inhabilitado correctamente.
        """
        print("\n" + "=" * 50)
        print("      ADMINISTRACIÓN - INHABILITAR RECURSO")
        print("=" * 50)

        numero = int(input("Ingrese el número de inventario del recurso que desea inhabilitar: "))

        for i in range(self.contador_recursos):
            recurso = self.arreglo_recursos[i]
            if recurso.numero_inventario == numero:
                if recurso.estado == 4:
                    print("Este recurso ya está inhabilitado.")
                    return
                recurso.estado = 4
                print(f"Recurso con inventario #{numero} ha sido inhabilitado correctamente.")
                return

        print("No se encontró un recurso con ese número de inventario.")

    def main(self):
        opc = 0
        while opc != 2:
            print("\n" + "=" * 40)
            print("\t    MENÚ PRINCIPAL\t  ")
            print("=" * 40)
            print("1. Auntenticarse \n2. Salir de la app")
            opc = int(input("Seleccione una opción del menú: "))

            match opc:
                case 1:
                    if (self.verificar_usuario()):
                        print(f"\n¡Inicio de sesión exitoso! Bienvenid@ {self.usuario_autenticado.nombre.title()}")
                        if (self.usuario_autenticado.perfil_usuario == self.PERFIL_ADMIN):
                            self.mostrar_menu_admin()
                        elif (self.usuario_autenticado.perfil_usuario == self.PERFIL_BIBLIO):
                            self.mostrar_menu_biblio()
                        elif (self.usuario_autenticado.perfil_usuario == self.PERFIL_USUARIO):
                            self.mostrar_menu_usuario()
                        else:
                            print("PERFIL NO RECONOCIDO")
                case 2:
                    self.usuario_autenticado = None
                    print("\nAPLICACIÓN FINALIZADA CORRECTAMENTE.")
                case _:
                    print("opcion incorrecta")

app = AppGarageU()
app.main()
import numpy as np
from Audio import Audio
from Libro import Libro
from Revista import Revista
from Video import Video
from Usuario import Usuario
import Funcionalidades as func

class AppGarageU:
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
        # Carga los usuarios almacenados en el archivo de usuarios
        self.arreglo_usuarios, self.contador_usuarios = self.cargar_datos(Usuario.ARCHIVO, self.MAX_USUARIOS)

        self.arreglo_recursos = np.full(self.MAX_USUARIOS, fill_value = None, dtype= object)

        if self.contador_usuarios == 0:
            self.arreglo_usuarios[0] = Usuario(nombre = "Administrador", identificacion=000, contrasenna='000')
            self.arreglo_usuarios[0].cambiar_perfil(self.PERFIL_ADMIN)
            self.contador_usuarios = 1

        self.contador_recursos = 0

        self.usuario_autenticado = None

    def cargar_datos(self, archivo, num_max_datos):
        """ Este método carga los datos de un archivo, en un arreglo específico

            PARAMS
                archivo = URL relativa del archivo a abrir
                num_max_datos = indica el tamaño máximo de datos que almacena el arreglo

            RETURNS
                arreglo_de_datos = arreglo con los datos cargados
                num_datos = cantidad de datos cargados en el arreglo
        """
        try:
            arreglo_de_datos = np.load(archivo, allow_pickle=True)
            i = 0
            while arreglo_de_datos[i] is not None:
                i += 1
            return arreglo_de_datos, i
        except (FileNotFoundError, EOFError):
            print (f"No se pudo cargar el archivo {archivo}. Se creó un arreglo de datos vacío!")
            arreglo_de_datos = np.full(num_max_datos, fill_value=None, dtype=object)
            return arreglo_de_datos, 0

    def guardar_datos(self, arreglo_de_datos, archivo):
        """ Este método almacena los datos de un arreglo en un archivo

            PARAMS
                arreglo_de_datos = arreglo Numpy con los datos a alamcenar
                archivo = URL relativa del archivo en el que se almacenarán los datos

            RETURNS
                True si almacena los datos correctamente en el archivo
                False si no logra almacenar los datos en el archivo
        """
        try:
            np.save(archivo, arreglo_de_datos)
            return True
        except (FileNotFoundError, EOFError):
            print (f"Error: no se pudieron almacenar los  datos en el archivo {archivo}.")
            return False

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

            # Guarda en el archivo los datos de los usuarios
            if not self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO):
                print("No se pudo guardar el archivo de usaurios")
            else:
                print("\nSe actualizó el archivo de usuarios")

            print(self.arreglo_usuarios)

            print("\n[ADMIN] ¡Usuario Registrado Exitosamente!")
            print("=" * 50)
            user.mostrar_datos()
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
                    usuario.actualizar_datos(self.usuario_autenticado)
                    self.arreglo_usuarios[i] = usuario

                    # Guarda en el archivo los datos de los usuarios
                    if not self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO):
                        print("No se pudo guardar el archivo de usaurios")
                    else:
                        print("\nSe actualizó el archivo de usuarios")

            input(f"\n[ADMIN] No se encontró un usuario identificado con: {id_a_buscar}. Presione Enter para continuar...")
            print("\n"*20)
        else:
            print("No hay usuarios registrados en el sistema.")

    def eliminar_usuario(self, id_usuario):
        """

        """

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
        print("   MENÚ DE BIBLIOTECARIO  ")
        print("=" * 50)
        if self.contador_recursos < self.MAX_RECURSOS:
            tipo_recurso = func.solicitar_opcion_menu(func.registrar_recurso_menu(),[1,2,3,4])
            if tipo_recurso is None:
                return
            else:
                match tipo_recurso:
                    case 1:
                        recurso = Libro()
                        recurso.almacenar_datos()
                        recurso.numero_inventario = self.contador_recursos + 1
                        self.arreglo_recursos[self.contador_recursos] = recurso
                        self.contador_recursos += 1
                        print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
                        print("=" * 50)
                        print(f"Titulo: {recurso.titulo}")
                    case 2:
                        recurso = Revista()
                        recurso.almacenar_datos()
                        recurso.numero_inventario = self.contador_recursos + 1
                        self.arreglo_recursos[self.contador_recursos] = recurso
                        self.contador_recursos += 1
                        print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
                        print("=" * 50)
                        print(f"Titulo: {recurso.titulo}")
                    case 3:
                        recurso = Video()
                        recurso.almacenar_datos()
                        recurso.numero_inventario = self.contador_recursos + 1
                        self.arreglo_recursos[self.contador_recursos] = recurso
                        self.contador_recursos += 1
                        print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
                        print("=" * 50)
                        print(f"Titulo: {recurso.titulo}")
                    case 4:
                        recurso = Audio()
                        recurso.almacenar_datos()
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

    def iniciar_menu_usuario(self):
        """
        En este método se mostrará el menú del usuario regular, el cual por el momento solo
        tiene permitido actualizar sus datos.
        """
        opcion_usuario = -1
        while opcion_usuario != 2:
            while True:
                opcion_usuario = func.solicitar_opcion_menu(func.mostrar_menu_usuario(),[1, 2])
                if opcion_usuario is None:
                    return
                else:
                    match opcion_usuario:
                        case 1:
                            self.usuario_autenticado.actualizar_datos(self.usuario_autenticado)

                            indice = self.usuario_autenticado.consultar_indice(arreglo=self.arreglo_usuarios)

                            self.arreglo_usuarios[indice] = self.usuario_autenticado

                            # Guarda en el archivo los datos de los usuarios
                            if not self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO):
                                print("No se pudo guardar el archivo de usaurios")
                            else:
                                print("\nSe actualizó el archivo de usuarios")
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
        opcion_admin = -1
        while opcion_admin != 5:
            opcion_admin = func.solicitar_opcion_menu(func.mostrar_menu_admin(),[1,2,3,4,5])
            if opcion_admin is None:
                return
            else:
                match opcion_admin:
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


    def iniciar_menu_biblio(self):
        """
        Por medio de este método es que el usuario bibliotecario podrá escoger si desea registrar
        un recurso nuevo o si desea inhabilitarlo. Este método de menú funciona igual que los dos
        anteriores, por medio de un ciclo while se mostrará el menú para que el usuario eliga qué
        quiere hacer y por medio de un match case se ejecutará la funcionalidad correspondiente.
        """
        opcion_biblio = -1
        while opcion_biblio != 3:
            opcion_biblio = func.solicitar_opcion_menu(func.mostrar_menu_biblio(),[1,2,3])
            if opcion_biblio is None:
                return
            else:
                match opcion_biblio:
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
                    if self.verificar_usuario():
                        print(f"\n¡Inicio de sesión exitoso! Bienvenid@ {self.usuario_autenticado.nombre.title()}")
                        if self.usuario_autenticado.perfil_usuario == self.PERFIL_ADMIN:
                            self.mostrar_menu_admin()
                        elif self.usuario_autenticado.perfil_usuario == self.PERFIL_BIBLIO:
                            self.iniciar_menu_biblio()
                        elif self.usuario_autenticado.perfil_usuario == self.PERFIL_USUARIO:
                            self.iniciar_menu_usuario()
                        else:
                            print("PERFIL NO RECONOCIDO")
                case 2:
                    self.usuario_autenticado = None
                    print("\nAPLICACIÓN FINALIZADA CORRECTAMENTE.")
                case _:
                    print("opcion incorrecta")

app = AppGarageU()
app.main()
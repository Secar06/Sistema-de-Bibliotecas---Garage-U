import numpy as np
from Recurso import Recurso
from Audio import Audio
from Libro import Libro
from Revista import Revista
from Video import Video
from Usuario import Usuario
from Prestamo import Prestamo
from datetime import date, timedelta
import Funcionalidades as func

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
    arreglo_prestamos = np.ndarray
    contador_usuarios = int
    contador_recursos = int
    contador_prestamos = int
    usuario_autenticado = Usuario

    # CONSTANTES
    TIPO_ESTUDIANTE = 1
    TIPO_EMPLEADO = 2
    PERFIL_ADMIN = 1
    PERFIL_BIBLIO = 2
    PERFIL_USUARIO = 3
    MAX_RECURSOS = 100
    MAX_USUARIOS = 100
    MAX_PRESTAMOS = 100

    def __init__(self):
        # Carga los usuarios almacenados en el archivo de usuarios
        self.arreglo_usuarios, self.contador_usuarios = self.cargar_datos(Usuario.ARCHIVO, self.MAX_USUARIOS)

        self.arreglo_recursos, self.contador_recursos = self.cargar_datos(Recurso.ARCHIVO, self.MAX_RECURSOS)

        self.arreglo_prestamos, self.contador_prestamos = self.cargar_datos(Prestamo.ARCHIVO, self.MAX_PRESTAMOS)

        if self.contador_usuarios == 0:
            self.arreglo_usuarios[0] = Usuario(nombre = "Administrador", identificacion=000, contrasenna='000')
            self.arreglo_usuarios[0].cambiar_perfil(self.PERFIL_ADMIN)
            self.contador_usuarios = 1


            
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
            while arreglo_de_datos[i] != None:
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
            print("\nIngrese El tipo de recurso:\n1. Libro\n2. Revista\n3. Video\n4. Audio")
            while True:
                try:
                    tipo_recurso = int(input("Seleccione una opcion del menú: "))
                    if tipo_recurso in [1, 2, 3, 4]:
                        break
                    else:
                        print("El estado ingresado es incorrecto, por favor intente nuevamente...")
                except ValueError:
                    print("El tipo de dato ingresado es erróneo, por favor ingrese un número (1, 2, 3 o 4).")
            match tipo_recurso:
                case 1:
                    recurso = Libro()
                    recurso.almacenar_datos()
                    recurso.numero_inventario = self.contador_recursos + 1
                    self.arreglo_recursos[self.contador_recursos] = recurso
                    self.contador_recursos += 1
                    print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
                    print("=" * 50)
                    recurso.mostrar_datos()
                case 2:
                    recurso = Revista()
                    recurso.almacenar_datos()
                    recurso.numero_inventario = self.contador_recursos + 1
                    self.arreglo_recursos[self.contador_recursos] = recurso
                    self.contador_recursos += 1
                    print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
                    print("=" * 50)
                    recurso.mostrar_datos()
                case 3:
                    recurso = Video()
                    recurso.almacenar_datos()
                    recurso.numero_inventario = self.contador_recursos + 1
                    self.arreglo_recursos[self.contador_recursos] = recurso
                    self.contador_recursos += 1
                    print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
                    print("=" * 50)
                    recurso.mostrar_datos()
                case 4:
                    recurso = Audio()
                    recurso.almacenar_datos()
                    recurso.numero_inventario = self.contador_recursos + 1
                    self.arreglo_recursos[self.contador_recursos] = recurso
                    self.contador_recursos += 1
                    print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
                    print("=" * 50)
                    recurso.mostrar_datos()

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
            # Guarda en el archivo los datos de los usuarios
            if not self.guardar_datos(self.arreglo_recursos, recurso.ARCHIVO):
                print("No se pudo guardar el archivo de recursos")
            else:
                print("\nSe actualizó el archivo de recursos")
        else:
            print("No se puede realizar el registro del recurso.\n Causa: almacenamiento insuficiente en el sistema.")


    def modificar_recurso(self):
        if self.contador_recursos > 0:
            print(f"Hay un total de {self.contador_recursos} recursos")
            numero_recurso_arreglo = int(input("Ingrese el numero de inventario del recurso que desea modificar")) 
            place_holder_recurso = self.arreglo_recursos[numero_recurso_arreglo - 1]
            place_holder_recurso.modificar_datos()

        else:
            print("No hay recursos registrados")

    
    def puede_prestar_usuario(self, id_usuario):
        persona = func.buscar_entidad(self.arreglo_usuarios, id_usuario)
        if persona == None:
            print("El usuario no fue encontrado en la base de datos")
        elif persona.multa != 0:
            if func.buscar_entidad(self.arreglo_prestamos, id_usuario) == None:
                return True
        return False
            
    def es_prestable(self, cod_recurso):
        recurso = func.buscar_entidad(self.arreglo_recursos, cod_recurso)
        if recurso == None:
            print("El recurso no fue encontrado en la base de datos")
        elif recurso.estado != 2:
            return False
        else:
            return True
    
    def calcular_fecha_devolucion(self,cod_recurso, id_usuario):
        recurso = func.buscar_entidad(self.arreglo_recursos, cod_recurso)
        usuario = func.buscar_entidad(self.arreglo_usuarios, id_usuario)
        if usuario.tipo_usuario == 1:
            match recurso.coleccion:
                case 1:
                    fecha_devolucion = date.today() + timedelta(days=15)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                case 2:
                    fecha_devolucion = date.today() + timedelta(days=1)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                case 3:
                    fecha_devolucion = date.today() + timedelta(days=3)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
        else:
            match recurso.coleccion:
                case 1:
                    fecha_devolucion = date.today() + timedelta(days=30)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                case 2:
                    fecha_devolucion = date.today() + timedelta(days=15)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                case 3:
                    fecha_devolucion = date.today() + timedelta(days=22)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion

    def registrar_prestamo(self):
        if self.contador_prestamos >= self.MAX_PRESTAMOS:
            print("No se puede realizar el registro del prestamo.\n Causa: almacenamiento insuficiente en el sistema.")
            return
        else:
            while True:
                try:
                    buscar_id = int(input("Ingrese la id del usuario al cual se le va generar el prestamo: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            while True:
                try:
                    buscar_cod = int(input("Ingrese el codigo de inventario del recurso que va a ser prestado: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            if not self.puede_prestar_usuario(buscar_id):
                print("El usuario no puede hacer prestamos.")
            elif not self.es_prestable(buscar_cod):
                print("El recurso no esta disponible para prestamos.")
            else:
                prestamo = Prestamo()
                prestamo.indice_prestamo = self.contador_prestamos + 1
                prestamo.cod_libro = buscar_cod
                prestamo.id_usuario = buscar_id
                prestamo.fecha_prestamo = date.today()
                print(f"La fecha del prestamo es: {prestamo.fecha_prestamo.strftime("%d") + " " + prestamo.fecha_prestamo.strftime("%B") + " " + prestamo.fecha_prestamo.strftime("%Y")}")
                prestamo.fecha_devolucion = self.calcular_fecha_devolucion(buscar_cod, buscar_id)
                self.arreglo_prestamos[self.contador_prestamos] = prestamo
                self.contador_prestamos += 1
                for i in range(self.contador_recursos):
                    """if self.arreglo_recursos[i]. == """
                    pass
                

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
        option = -1
        while option != 6:
            print("\n" + "=" * 25)
            print(" MENÚ DE ADMINISTRADOR ")
            print("=" * 25)
            print("1. Registrar un nuevo usuario \n2. Modificar un usuario \n3. Registrar un nuevo recurso \n4. Inhabilitar Un recurso\n5. Modificar un recurso \n6. Cerrar sesión")
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
                    print("\n" + "=" * 50)
                    print(" MENÚ DE ADMINISTRADOR - MODIFICACIÓN DE RECURSO ")
                    print("=" * 50)
                    input("\n[ADMIN] Ha seleccionado la opción 5. Presione Enter para continuar...")
                    self.modificar_recurso()
                case 6:
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
                    if self.verificar_usuario():
                        print(f"\n¡Inicio de sesión exitoso! Bienvenid@ {self.usuario_autenticado.nombre.title()}")
                        if self.usuario_autenticado.perfil_usuario == self.PERFIL_ADMIN:
                            self.mostrar_menu_admin()
                        elif self.usuario_autenticado.perfil_usuario == self.PERFIL_BIBLIO:
                            self.mostrar_menu_biblio()
                        elif self.usuario_autenticado.perfil_usuario == self.PERFIL_USUARIO:
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
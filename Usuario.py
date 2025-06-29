class Usuario():
    """
    Esta clase represeta el usuario de la biblioteca GarageU y se encarga de almacenar los datos personales del usuario.

    ATRIBUTOS:
    nombre: Nombre completo del usuario.
    direccion: Dirección de residencia del usuario.
    telefono: Número de teléfono del usuario.
    email: Correo electrónico del usuario.
    identificacion: Número de identificación del usuario.
    multa: Valor acumulado de multas del usuario.
    tipo_usuario: Tipo de usuario (1 = Estudiante, 2 = Empleado).
    perfil_usuario: Perfil del usuario (1 = Administrador, 2 = Bibliotecario, 3 = Usuario).
    contrasenna: Contraseña de acceso del usuario.

    CONSTANTES:
    MAX_CONSULTAS: que indica cuál es el número máximo de consultas que pueden ser almacenadas por la aplicación

    Autor: Elkin Alejandro López Clavijo
    Fecha: 01/06/2025
    """
    # ATRIBUTOS
    nombre = str
    direccion =str
    telefono = int
    email = str
    identificacion = int
    multa = int
    tipo_usuario = int
    perfil_usuario= int
    contrasenna = str

    # CONSTRUCTOR
    def __init__(self, nombre="", identificacion=0, contrasenna='', direccion="", telefono="", email="", multa=0, tipo_usuario=-1, perfil_usuario=-1):
        """
        Inicializa los atributos del usuario con valores por defecto.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.contrasenna = contrasenna
        self.identificacion = identificacion
        self.multa = multa
        self.tipo_usuario = tipo_usuario
        self.perfil_usuario = perfil_usuario

    def almacenar_datos(self):
        """
        Permite al usuario ingresar sus datos básicos desde la app.
        Luego llama al método 'determinar_tipo_usuario' para asignar su tipo de usuario.
        """
        self.contrasenna = input("Ingrese una contraseña para el usuario: ")
        self.nombre = input("Ingrese el nombre completo: ")
        self.direccion = input("Ingrese la dirección de residencia: ")
        self.telefono = int(input("Digite el número de teléfono: "))
        self.email = input("Ingrese el correo electrónico: ")
        self.determinar_tipo_usuario()

    def cambiar_perfil(self, nuevo_perfil):
        '''
        Cambia el perfil del usuario por el asignado.
        '''
        self.perfil_usuario = nuevo_perfil

    def determinar_perfil_usuario(self):
        """
        Pide al usuario que seleccione su perfil: Administrador o Bibliotecario.
        Se repite hasta que la entrada sea válida.
        """
        self.perfil_usuario = 0
        while self.perfil_usuario not in [1,2]:
            # Encabezado
            print("")
            print("=" * 25)
            print(" Perfil de Usuario  ")
            print("=" * 25)

            # Opciones
            print("1. Administrador \n2. Bibliotecario")
            self.perfil_usuario = int(input("Seleccione una opción del menú: "))

            # Según sea el caso, se le asigna el valor correspondiente al perfil de usuario seleccionado
            match self.perfil_usuario:
                case 1:
                    self.perfil_usuario = 1
                    self.tipo_usuario = 2
                    return
                case 2:
                    self.perfil_usuario = 2
                    self.tipo_usuario = 2
                    return
                case _:
                    input("\n[ADMIN] Opción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...")
        return

    def determinar_tipo_usuario(self):
        """
        Solicita al usuario que seleccione su tipo (Estudiante o Empleado).
        En caso de seleccionar Empleado, se debe escoger un perfil.
        """
        self.tipo_usuario = 0
        while self.tipo_usuario not in [1,2]:
            # Encabezado
            print("")
            print("=" * 25)
            print(" Tipo de Usuario  ")
            print("=" * 25)
            # Opciones
            print("1. Estudiante \n2. Empleado")
            self.tipo_usuario = int(input("Seleccione una opción del menú: "))

            # Cuando el usuario selecciona empleado, se le pide determinar su perfil llamando al metodo determinar_perfil_usuario.
            match self.tipo_usuario:
                case 1:
                    self.tipo_usuario = 1
                    self.perfil_usuario = 3
                case 2:
                    self.tipo_usuario = 2
                    self.determinar_perfil_usuario()
                case _:
                    input("\n[ADMIN] Opción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...")
        return

    def actualizar_datos(self, usuario_autenticado):
        """
        Permite al usuario (o a un administrador) modificar sus datos personales.
        """
        mensaje = "\n¡Información actualizada exitosamente! Presione Enter para continuar..."
        option = -1
        while option != 7:
            print("")
            print("=" * 25)
            print(" ACTUALIZACIÓN DE DATOS ")
            print("=" * 25)

            # Se verifica el tipo de usuario y perfil para mostrarlo entre las opciones
            match self.tipo_usuario:
                case 1:
                    user_type = "Estudiante"
                case 2:
                    user_type = "Empleado"

            match self.perfil_usuario:
                case 1:
                    user_profile = "Administrador"
                case 2:
                    user_profile = "Bibliotecario"
                case 3:
                    user_profile = "Usuario"

            # Menú de opciones
            print(f"1. Tipo de Usuario: {user_type} \n2. Perfil de Usuario: {user_profile} \n3. Nombre: {self.nombre} \n4. Dirección: {self.direccion}\n5. Teléfono: {self.telefono}\n6. Correo Electrónico: {self.email}\n7. Volver al menú principal")
            option = int(input("Seleccione una opción del menú: "))
            match option:
                case 1:
                    # Se verifica que el usuario autenticado sea administrador. En tal caso, se le permite modificar el tipo de usuario.
                    if usuario_autenticado.perfil_usuario == 1:
                        input("[ADMIN] Seleccionó la opción 1. Presione Enter para continuar")
                        self.determinar_tipo_usuario()
                        input(mensaje)
                    else:
                        input("[ERROR] No cuenta con el acceso para editar su tipo de usuario. Presione Enter para continuar...")
                case 2:
                    # Se verifica que el usuario autenticado sea administrador. En tal caso, se le permite modificar el perfil de un usuario.
                    if usuario_autenticado.perfil_usuario == 1:
                        input("[ADMIN] Seleccionó la opción 2. Presione Enter para continuar")
                        self.determinar_perfil_usuario()
                        input(mensaje)
                    else:
                        input("[ERROR] No cuenta con el acceso para editar su tipo de usuario. Presione Enter para continuar...")
                case 3:
                    self.nombre = input("Ingrese el nombre completo: ").title()
                    input(mensaje)
                case 4:
                    self.direccion = input("Ingrese la dirección de residencia: ").lower()
                    input(mensaje)
                case 5:
                    self.telefono = input("Ingrese el número de teléfono: ")
                    input(mensaje)
                case 6:
                    self.email = input("Ingrese el correo electrónico: ").lower()
                    input(mensaje)
                case 7:
                    input("Regresando al menú principal. Presione Enter para continuar...")
                    return
                case _:
                    input("Opción incorrecta. Inténtelo nuevamente. Presione enter para continuar...")

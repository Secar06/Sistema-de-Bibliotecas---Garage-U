import funcionalidades as func

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
    nombre : str
    direccion : str
    telefono : int
    email : str
    identificacion : int
    multa : int
    tipo_usuario : int
    perfil_usuario : int
    contrasenna : str
    ARCHIVO = "datos_usuarios.npy"

    # CONSTRUCTOR
    def __init__(self, nombre = "", identificacion = 0, contrasenna = '', direccion = "", telefono = 0, email = "",
                 multa = 0, tipo_usuario = -1, perfil_usuario = -1):
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

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre : str):
        nombre_sin_espacios = nombre.strip(' ').split()
        for i in nombre_sin_espacios:
            for j in i:
                if j not in func.ABECEDARIO:
                    raise ValueError
        self._nombre = nombre.title()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def contrasenna(self):
        return self._contrasenna

    @contrasenna.setter
    def contrasenna(self, contrasenna):
        self._contrasenna = contrasenna

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, identificacion):
        self._identificacion = identificacion

    @property
    def multa(self):
        return self._multa

    @multa.setter
    def multa(self, multa):
        self._multa = multa

    @property
    def tipo_usuario(self):
        return self._tipo_usuario

    @tipo_usuario.setter
    def tipo_usuario(self, tipo_usuario):
        self._tipo_usuario = tipo_usuario

    @property
    def perfil_usuario(self):
        return self._perfil_usuario

    @perfil_usuario.setter
    def perfil_usuario(self, nuevo_perfil_usuario):
        self._perfil_usuario = nuevo_perfil_usuario

    def get_perfil_usuario(self):
        match self.perfil_usuario:
            case 1:
                return "Administrador"
            case 2:
                return "Bibliotecario"
            case 3:
                return "Usuario"
        return None

    def get_tipo_usuario(self):
        match self.tipo_usuario:
            case 1:
                return "Estudiante"
            case 2:
                return "Empleado"
        return None

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

            # Cuando el usuario selecciona empleado,
            # se le pide determinar su perfil llamando al metodo determinar_perfil_usuario.
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

    def mostrar_datos(self):
        return(
            "========================================\n"
            f"Identificación: {self.identificacion}\n"
            f"Contraseña: {self.identificacion}\n"
            f"Nombre completo: {self.nombre}\n"
            f"Dirección: {self.direccion.lower()}\n"
            f"Teléfono: {self.telefono}\n"
            f"Email registrado: {self.email.lower()}\n"
            f"Multa: {self.multa}\n"
            "========================================\n"
            f"{self.get_tipo_usuario()}\n"
            f"{self.get_perfil_usuario()}\n"
            "============================")

    def consultar_indice(self, arreglo):
        for i in range(len(arreglo)):
            if arreglo[i].identificacion == self.identificacion:
                return i
        return None
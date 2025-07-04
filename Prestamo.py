class Prestamo:
    """
    Esta clase representa un prestamo de un recurso a un usuario.

    """
    ARCHIVO = "datos_prestamos.npy"
    def __init__(self, indice_prestamo, cod_libro, id_usuario, fecha_prestamo, fecha_devolucion):
            self.indice_prestamo = indice_prestamo
            self.cod_libro = cod_libro
            self.id_usuario = id_usuario
            self.fecha_prestamo = fecha_prestamo
            self.fecha_devolucion = fecha_devolucion
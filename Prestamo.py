class Prestamo:
    """
    Esta clase representa un prestamo de un recurso a un usuario.

    """
    def __init__(self, id, id_libro, id_usuario, fecha_prestamo, fecha_devolucion):
            self.id = id
            self.id_libro = id_libro
            self.id_usuario = id_usuario
            self.fecha_prestamo = fecha_prestamo
            self.fecha_devolucion = fecha_devolucion

    def get_id(self):
        return self.id
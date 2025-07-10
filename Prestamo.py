import datetime as date
class Prestamo:
    """
    Esta clase representa un prestamo de un recurso a un usuario.

    """
    fecha_prestamo = date
    fecha_devolucion_estimada = date
    fecha_devolucion = date
    ARCHIVO = "datos_prestamos.npy"
    def __init__(self, indice_prestamo = -1, cod_recurso = -1, id_usuario = -1, fecha_prestamo = None, fecha_devolucion_estimada = None, fecha_devolucion = None):
            self.indice_prestamo = indice_prestamo
            self.cod_recurso = cod_recurso
            self.id_usuario = id_usuario
            self.fecha_prestamo = fecha_prestamo
            self.fecha_devolucion_estimada = fecha_devolucion_estimada
            self.fecha_devolucion = fecha_devolucion


    def get_id(self):
        return self.indice_prestamo
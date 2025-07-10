from datetime import date

class Historial_usuarios:
    fecha : date
    accion : str
    usuario : str
    recursoid : int
    id_usuario : int
    fecha_devolucion = date
    multa = int
    nombre_recurso = str

    def __init__(self, fecha = None, accion = "", usuario = "", recursoid = -1, id_usuario = 0, fecha_devolucion = None, multa = 0, nombre_recurso =""):
        self.fecha = fecha
        self.accion = accion
        self.usuario = usuario
        self.recursoid = recursoid
        self.id_usuario = id_usuario
        self.multa = multa
        self.nombre_recurso
        self.fecha_devolucion

    def mostrar_datos_usuario(self):
        print(f"Título recurso: {self.nombre_recurso}\nFecha de préstamo: {self.fecha}\nFecha devolución: {self.fecha_devolucion}\nMulta: {self.multa}")
    def mostrar_datos_recurso(self):
        print(f"El usuario {self.usuario} con ID: {self.id_usuario}\nFecha de préstamo: {self.fecha}\nMulta: {self.multa}")
        

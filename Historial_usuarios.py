from datetime import date
class Historial_usuarios:

    fecha : date
    accion : str
    persona : str

    def __init__(self, fecha = None, accion = "", persona = ""):
        self.fecha = fecha
        self.accion = accion
        self.persona = persona
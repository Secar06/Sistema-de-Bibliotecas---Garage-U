from datetime import date, timedelta
def buscar_entidad(arreglo, id):
    for i in range(len(arreglo)):
        entidad = arreglo[i]
        if entidad is None:
            break
        elif entidad.get_id() == id:
            return entidad
        

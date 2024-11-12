from entidadvineria import EntidadVineria
from vinoteca import Vinoteca

class Cepa(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        vinos = Vinoteca.obtenerVinos()
        return [vino for vino in vinos if self.id in vino.cepas]

    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "vinos": [vino.convertirAJSON() for vino in self.obtenerVinos()]
        }

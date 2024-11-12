from entidadvineria import EntidadVineria
from vinoteca import Vinoteca

class Bodega(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        vinos = Vinoteca.obtenerVinos()
        return [vino for vino in vinos if vino.bodega == self.id]

    def obtenerCepas(self):
        vinos = self.obtenerVinos()
        cepas = set()
        for vino in vinos:
            cepas.update(vino.cepas)
        return list(cepas)

    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": self.obtenerCepas(),
            "vinos": [vino.convertirAJSON() for vino in self.obtenerVinos()]
        }

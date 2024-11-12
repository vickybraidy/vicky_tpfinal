from entidadvineria import EntidadVineria
from vinoteca import Vinoteca

class Vino(EntidadVineria):
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self.bodega = bodega
        self.cepas = cepas
        self.partidas = partidas

    def establecerBodega(self, bodega):
        self.bodega = bodega

    def establecerCepas(self, cepas):
        self.cepas = cepas

    def establecerPartidas(self, partidas):
        self.partidas = partidas

    def obtenerBodega(self):
        return Vinoteca.buscarBodega(self.bodega)

    def obtenerCepas(self):
        return [Vinoteca.buscarCepa(cepa) for cepa in self.cepas]

    def obtenerPartidas(self):
        return self.partidas

    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "bodega": self.bodega,
            "cepas": self.cepas,
            "partidas": self.partidas
        }

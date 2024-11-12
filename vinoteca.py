import json
from bodega import Bodega
from cepa import Cepa
from vino import Vino

class Vinoteca:
    archivoDeDatos = "vinoteca.json"
    bodegas = []
    cepas = []
    vinos = []

    @staticmethod
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    @staticmethod
    def obtenerBodegas(orden=None, reverso=False):
        bodegas = sorted(Vinoteca.bodegas, key=lambda b: getattr(b, orden), reverse=reverso) if orden else Vinoteca.bodegas
        return bodegas

    @staticmethod
    def obtenerCepas(orden=None, reverso=False):
        cepas = sorted(Vinoteca.cepas, key=lambda c: getattr(c, orden), reverse=reverso) if orden else Vinoteca.cepas
        return cepas

    @staticmethod
    def obtenerVinos(anio=None, orden=None, reverso=False):
        vinos = [vino for vino in Vinoteca.vinos if anio in vino.partidas] if anio else Vinoteca.vinos
        vinos = sorted(vinos, key=lambda v: getattr(v, orden), reverse=reverso) if orden else vinos
        return vinos

    @staticmethod
    def buscarBodega(id):
        for bodega in Vinoteca.bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None

    @staticmethod
    def buscarCepa(id):
        for cepa in Vinoteca.cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

    @staticmethod
    def buscarVino(id):
        for vino in Vinoteca.vinos:
            if vino.obtenerId() == id:
                return vino
        return None

    @staticmethod
    def __parsearArchivoDeDatos():
        with open(Vinoteca.archivoDeDatos, 'r') as archivo:
            datos = json.load(archivo)
        return datos

    @staticmethod
    def __convertirJsonAListas(datos):
        for bodega in datos['bodegas']:
            Vinoteca.bodegas.append(Bodega(**bodega))
        for cepa in datos['cepas']:
            Vinoteca.cepas.append(Cepa(**cepa))
        for vino in datos['vinos']:
            Vinoteca.vinos.append(Vino(**vino))

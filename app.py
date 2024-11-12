from flask import Flask, jsonify
from flask_restful import Api, Resource
from vinoteca import Vinoteca

app = Flask(__name__)
api = Api(app)

class BodegaResource(Resource):
    def get(self, id=None):
        if id:
            bodega = Vinoteca.buscarBodega(id)
            if bodega:
                return jsonify(bodega.convertirAJSONFull())
            return {}, 404
        else:
            return jsonify([bodega.convertirAJSON() for bodega in Vinoteca.obtenerBodegas()])

class CepaResource(Resource):
    def get(self, id=None):
        if id:
            cepa = Vinoteca.buscarCepa(id)
            if cepa:
                return jsonify(cepa.convertirAJSONFull())
            return {}, 404
        else:
            return jsonify([cepa.convertirAJSON() for cepa in Vinoteca.obtenerCepas()])

class VinoResource(Resource):
    def get(self, id=None):
        if id:
            vino = Vinoteca.buscarVino(id)
            if vino:
                return jsonify(vino.convertirAJSONFull())
            return {}, 404
        else:
            return jsonify([vino.convertirAJSON() for vino in Vinoteca.obtenerVinos()])

api.add_resource(BodegaResource, '/api/bodegas', '/api/bodegas/<string:id>')
api.add_resource(CepaResource, '/api/cepas', '/api/cepas/<string:id>')
api.add_resource(VinoResource, '/api/vinos', '/api/vinos/<string:id>')

if __name__ == '__main__':
    Vinoteca.inicializar()
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS
import json
from Clusterizador import Clusterizador
class ClusterAPI:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.clusterizador = Clusterizador()

        self.app.add_url_rule('/train', 'train', self.train, methods=['POST'])
        self.app.add_url_rule('/predict', 'predict', self.predict, methods=['POST'])

    def train(self):
        data = request.json
        try:
            self.clusterizador.train(data)
            return jsonify({"message": "Modelo treinado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def predict(self):
        data = request.json
        try:
            processed_input = self.clusterizador.preprocess_input(data)
            usuarios_favoraveis = self.clusterizador.predict(processed_input)
            return jsonify({"usuarios_favoraveis": usuarios_favoraveis}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def run(self, debug=False):
        self.app.run(debug=debug)

# Inicialização do servidor
if __name__ == "__main__":
    api = ClusterAPI()
    api.clusterizador.initialize_from_file(r"C:\Users\Pichau\Documents\python_estudo\classificador\dados_cluster.json")
    api.run(debug=True)
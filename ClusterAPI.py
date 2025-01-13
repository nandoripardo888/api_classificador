from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS
import json
import os
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
            response = jsonify({"message": "Modelo treinado com sucesso!"})
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response, 200
        except Exception as e:
            response = jsonify({"error": str(e)})
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response, 500

    def predict(self):
        data = request.json
        try:
            processed_input = self.clusterizador.preprocess_input(data)
            usuarios_favoraveis = self.clusterizador.predict(processed_input)
            response = jsonify({"usuarios_favoraveis": usuarios_favoraveis})
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response, 200
        except ValueError as e:
            response = jsonify({"error": str(e)})
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response, 400
        except Exception as e:
            response = jsonify({"error": str(e)})
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response, 500

# Criar uma instância da API e expor o objeto `app` para o Gunicorn
api = ClusterAPI()

#api.clusterizador.initialize_from_file(r"C:\Users\Pichau\Documents\python_estudo\classificador\dados_cluster.json")
# Caminho relativo para o arquivo
file_path = os.path.join(os.path.dirname(__file__), "dados_cluster.json")

# Inicialização
api.clusterizador.initialize_from_file(file_path)

app = api.app

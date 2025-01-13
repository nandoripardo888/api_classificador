import requests

# URL base da API
BASE_URL = "http://127.0.0.1:5000"

# Dados para treinamento
train_data = [
    {
        "nome": "Regina",
        "habilidades": ["médica", "salva-vidas"],
        "urgencia": "alta",
        "disponibilidade": ["manhã", "noite"],
        "recursos": ["kit primeiro socorros", "agua potável"]
    },
    {
        "nome": "Carlos",
        "habilidades": ["engenheiro", "carpinteiro"],
        "urgencia": "média",
        "disponibilidade": ["tarde"],
        "recursos": ["ferramentas", "madeira"]
    },
    {
        "nome": "Ana",
        "habilidades": ["enfermeira", "socorrista"],
        "urgencia": "baixa",
        "disponibilidade": ["manhã"],
        "recursos": ["medicamentos", "luvas"]
    }
]

# Dados para predição
predict_data = {
    "habilidades": ["Desenhista", "Navegação e Orientação"],
    "urgencia": "alta",
    "disponibilidade": ["tarde"],
    "recursos": ["Água Potável"]
}

# Função para testar o endpoint /train
def test_train():
    print("Testando o endpoint /train...")
    try:
        response = requests.post(f"{BASE_URL}/train", json=train_data)
        if response.status_code == 200:
            print("Treinamento realizado com sucesso!")
        else:
            print(f"Erro no treinamento: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Erro ao conectar ao endpoint /train: {e}")

# Função para testar o endpoint /predict
def test_predict():
    print("Testando o endpoint /predict...")
    try:
        response = requests.post(f"{BASE_URL}/predict", json=predict_data)
        if response.status_code == 200:
            print("Predição realizada com sucesso!")
            print("Usuários mais favoráveis:", response.json().get("usuarios_favoraveis", []))
        else:
            print(f"Erro na predição: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Erro ao conectar ao endpoint /predict: {e}")

# Executando os testes
if __name__ == "__main__":
    #test_train()
    test_predict()

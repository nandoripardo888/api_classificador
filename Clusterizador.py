import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.cluster import KMeans
import json

class Clusterizador:
    def __init__(self, n_clusters=10):
        self.n_clusters = n_clusters
        self.kmeans = None
        self.scaler = None
        self.mlb_habilidades = None
        self.mlb_disponibilidade = None
        self.mlb_recursos = None
        self.urgencia_mapping = {"alta": 3, "media": 2, "baixa": 1}
        self.df_original = None

    def preprocess_training_data(self, data):
        df = pd.DataFrame(data)

        # Tratar valores ausentes para colunas específicas
        df['habilidades'] = df['habilidades'].apply(lambda x: x if isinstance(x, list) else [])
        df['disponibilidade'] = df['disponibilidade'].apply(lambda x: x if isinstance(x, list) else [])
        df['recursos'] = df['recursos'].apply(lambda x: x if isinstance(x, list) else [])
        df['urgencia'] = df['urgencia'].fillna('baixa')  # Valor padrão para urgência

        # One-hot encoding
        self.mlb_habilidades = MultiLabelBinarizer()
        habilidades_encoded = pd.DataFrame(self.mlb_habilidades.fit_transform(df['habilidades']), columns=self.mlb_habilidades.classes_)

        self.mlb_disponibilidade = MultiLabelBinarizer()
        disponibilidade_encoded = pd.DataFrame(self.mlb_disponibilidade.fit_transform(df['disponibilidade']), columns=self.mlb_disponibilidade.classes_)

        self.mlb_recursos = MultiLabelBinarizer()
        recursos_encoded = pd.DataFrame(self.mlb_recursos.fit_transform(df['recursos']), columns=self.mlb_recursos.classes_)

        # Codificar urgência
        df['urgencia_encoded'] = df['urgencia'].map(self.urgencia_mapping)

        # Concatenar dados codificados
        final_df = pd.concat([habilidades_encoded, disponibilidade_encoded, recursos_encoded, df['urgencia_encoded']], axis=1)

        # Preencher valores ausentes no DataFrame final com 0
        final_df = final_df.fillna(0)

        # Normalizar os dados
        self.scaler = StandardScaler()
        normalized_data = self.scaler.fit_transform(final_df)

        return df, final_df, normalized_data


    def train(self, data):
        self.df_original, final_df, normalized_data = self.preprocess_training_data(data)
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=42)
        self.kmeans.fit(normalized_data)
        self.df_original['cluster'] = self.kmeans.labels_

    def preprocess_input(self, data):
        habilidades_encoded = pd.DataFrame(self.mlb_habilidades.transform([data['habilidades']]), columns=self.mlb_habilidades.classes_)
        disponibilidade_encoded = pd.DataFrame(self.mlb_disponibilidade.transform([data['disponibilidade']]), columns=self.mlb_disponibilidade.classes_)
        recursos_encoded = pd.DataFrame(self.mlb_recursos.transform([data['recursos']]), columns=self.mlb_recursos.classes_)

        urgencia_encoded = pd.DataFrame([self.urgencia_mapping[data['urgencia']]], columns=['urgencia_encoded'])
        processed_data = pd.concat([habilidades_encoded, disponibilidade_encoded, recursos_encoded, urgencia_encoded], axis=1)

        for col in self.scaler.feature_names_in_:
            if col not in processed_data:
                processed_data[col] = 0

        normalized_data = self.scaler.transform(processed_data)
        return normalized_data

    def predict(self, input_data):
        if self.kmeans is None:
            raise ValueError("Modelo não treinado.")
        predicted_cluster = self.kmeans.predict(input_data)[0]
        return self.df_original[self.df_original['cluster'] == predicted_cluster]['nome'].tolist()

    def initialize_from_file(self, file_path):
        """
        Inicializa e treina o modelo a partir de um arquivo JSON local.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.train(data)
            print("Modelo treinado com sucesso a partir do arquivo:", file_path)
            print(self.df_original)
        except Exception as e:
            print(f"Erro ao inicializar o modelo do arquivo {file_path}: {e}")

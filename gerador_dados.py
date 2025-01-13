import random
import json

# Configurações dos dados
HABILIDADES = [
    "Primeiros Socorros", "Suporte Básico de Vida (BLS)", "Gestão de Emergências", "Comunicação Eficaz",
    "Trabalho em Equipe", "Logística e Distribuição", "Navegação e Orientação", "Resgate em Áreas Urbanas",
    "Resgate Aquático", "Operação de Equipamentos de Resgate", "Gestão de Abrigos Temporários", "Apoio Psicológico",
    "Prevenção de Infecções", "Conhecimento de Riscos Naturais", "Planejamento de Evacuação", 
    "Operação de Rádios e Comunicações", "Noções de Construção Temporária", "Gestão de Água e Saneamento", 
    "Distribuição de Alimentos", "Identificação de Perigos", "Coordenação com Autoridades", 
    "Uso de Equipamentos de Proteção Individual (EPI)", "Conhecimento de Protocolos de Emergência", 
    "Habilidades Básicas de Carpintaria", "Adaptabilidade e Resiliência"
]
URGENCIA = ["baixa", "media", "alta"]
DISPONIBILIDADE = ["manhã", "tarde", "noite"]
RECURSOS = [
    "Kits de Primeiros Socorros", "Desfibriladores Externos Automáticos (DEA)", 
    "Equipamentos de Resgate (cordas, capacetes, ferramentas)", "Barracas e Abrigos Temporários", "Água Potável",
    "Alimentos Não Perecíveis", "Roupas de Proteção e EPIs", "Rádios de Comunicação", "Geradores de Energia", 
    "Lanternas e Pilhas", "Medicamentos Básicos", "Cobertores e Sacos de Dormir", 
    "Veículos de Resgate (ambulâncias, barcos)", "Equipamentos de Purificação de Água", "Kits de Higiene Pessoal",
    "Mapas e GPS", "Materiais de Construção Temporária (lonas, madeira)", "Extintores de Incêndio",
    "Sistemas de Saneamento Básico (banheiros químicos)", "Equipamentos de Sinalização (cones, fitas)",
    "Computadores e Tablets para Gestão de Dados", "Kits de Ferramentas Multiuso",
    "Equipamentos de Proteção contra Intempéries (capas, botas)", 
    "Materiais Educativos (guias de primeiros socorros, manuais)", "Recursos Financeiros para Emergências"
]

NOMES = ["Ana", "João", "Maria", "Pedro", "Carla", "Lucas", "Sofia", "Miguel", "Laura", "Gabriel", "Beatriz", "Rafael", "Isabel", "Daniel", "Luiza", "Felipe", "Camila", "André", "Mariana", "Thiago", "Julia", "Leonardo", "Amanda", "Bruno", "Larissa", "Marcos", "Fernanda", "Ricardo", "Patrícia", "Eduardo", "Adriana", "Gustavo", "Tatiana", "Roberto", "Vanessa", "Alexandre", "Priscila", "Diego", "Aline", "Fábio", "Renata", "Marcelo", "Juliana", "Vinícius", "Carolina", "Ronaldo", "Débora", "César", "Natália", "Samuel"]
SOBRENOMES = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Araújo", "Melo", "Barbosa", "Rocha", "Nascimento", "Cunha", "Moreira", "Cardoso", "Cavalcanti", "Dias", "Correia", "Teixeira", "Monteiro", "Lopes", "Batista", "Freitas", "Guimarães", "Macedo", "Pires", "Ramos", "Duarte", "Neves", "Marques", "Andrade", "Bezerra", "Brito", "Siqueira", "Tavares", "Rezende", "Farias", "Peixoto", "Xavier", "Barros", "Franco", "Dantas", "Viana"]

# Função para gerar dados aleatórios
def gerar_dados(qtd: int):
    dados = []
    for i in range(1, qtd + 1):
        pessoa = {
            "nome": random.sample(NOMES, random.randint(1,1))[0] + " " + random.sample(SOBRENOMES, random.randint(1,1))[0], #f"Pessoa{i}",
            "habilidades": random.sample(HABILIDADES, random.randint(3, 6)),
            "urgencia": random.choice(URGENCIA),
            "disponibilidade": random.sample(DISPONIBILIDADE, random.randint(1, 2)),
            "recursos": random.sample(RECURSOS, random.randint(4, 7))
        }
        dados.append(pessoa)
    return dados

# Função para salvar os dados em JSON
def salvar_dados_em_json(dados, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")


def salvar_dados_em_json(dados, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")


# Configuração principal
if __name__ == "__main__":
    quantidade_pessoas = 40  # Alterar para o número desejado de pessoas
    arquivo_saida = "dados_cluster.json"  # Nome do arquivo de saída

    # Gerar e salvar os dados
    dados_gerados = gerar_dados(quantidade_pessoas)
    salvar_dados_em_json(dados_gerados, arquivo_saida)

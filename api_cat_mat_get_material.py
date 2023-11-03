# -*- coding: utf-8 -*-

import requests
import os
import json
import pandas as pd

# Função para baixar dados
def download_data(url, filepath, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        response = requests.get(url)
        with open(filepath, 'w') as file:
            json.dump(response.json(), file)

        # Verifica o tamanho do arquivo
        if os.path.getsize(filepath) > 0:
            return True
        attempts += 1
    print(f"Falha ao baixar dados de {url} após {max_attempts} tentativas.")
    return False

# Função para combinar arquivos CSV
def combine_csv_files(output_filename, csv_files):
    dfs = [pd.read_csv(file, sep=';') for file in csv_files]
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv(output_filename, sep=';', index=False)

# Criação da pasta 'dados_temporarios' se ela não existir
if not os.path.exists('dados_temporarios'):
    os.mkdir('dados_temporarios')

BASE_URL = "https://api-comprasv2.dth.nuvem.gov.br/modulo-material/4_consultarItemMaterial?pagina="
# Obtém o número total de páginas
response = requests.get(BASE_URL + '1')
data = response.json()
total_paginas = data['totalPaginas']

# Página inicial configurável pelo usuário (por exemplo, para retomar a partir da página 500)
pagina_inicial = 500

# Extrai e salva os dados de cada página a partir da página inicial
all_data = []

for pagina in range(pagina_inicial, total_paginas + 1):
    print(f"Analisando página {pagina} de {total_paginas}...")
    file_path = f'dados_temporarios/dados_pagina_{pagina}.json'
    success = download_data(BASE_URL + str(pagina), file_path)

    if success:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Adicionando os dados à lista all_data
            all_data.extend(data.get('resultado', []))
        print(f"{len(all_data)} itens baixados.")

# Converte os dados para um DataFrame do pandas
df = pd.DataFrame(all_data)

# Exporta os dados para o formato CSV
output_csv_filename = 'dados_extraidos_catmat_item.csv'
df.to_csv(output_csv_filename, sep=';', index=False)
print(f"Todos os dados extraídos foram salvos em {output_csv_filename}.")

# Exclui os arquivos temporários e a pasta
for pagina in range(pagina_inicial, total_paginas + 1):
    os.remove(f'dados_temporarios/dados_pagina_{pagina}.json')
os.rmdir('dados_temporarios')

# Solicita ao usuário para combinar os arquivos CSV
combine_option = input("Deseja combinar os arquivos CSV baixados em um único conjunto de dados? (S/N): ")
if combine_option.lower() == 's':
    csv_files = [f'dados_temporarios/dados_pagina_{pagina}.csv' for pagina in range(1, total_paginas + 1)]
    combine_csv_files('dados_combinados.csv', csv_files)
    print("Arquivos CSV combinados com sucesso em 'dados_combinados.csv'.")

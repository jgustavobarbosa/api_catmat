## README.md: Extração de Dados da API do Catálogo de Materiais (CATMAT)

Este script Python automatiza a extração de dados da API do Catálogo de Materiais (CATMAT) do Governo Federal. Ele baixa as informações de cada página da API, salva os dados em arquivos JSON temporários e, em seguida, os combina em um único arquivo CSV.

### Funcionalidades

* **Download Paginado:** O script realiza o download dos dados em lotes, respeitando a paginação da API.
* **Reinício Inteligente:** Permite configurar a página inicial para retomar o processo caso seja interrompido.
* **Combinação de Arquivos CSV:** Oferece a opção de combinar os arquivos CSV baixados em um único arquivo.
* **Tratamento de Erros:** Implementa um mecanismo para lidar com falhas no download dos dados.

### Pré-requisitos

* Python 3.x
* Bibliotecas `requests`, `json`, `pandas`, `os` (instaladas via `pip install requests pandas`)

### Como Usar

1. **Configurar a Página Inicial (Opcional):**
   - Modifique a variável `pagina_inicial` no script para definir a partir de qual página você deseja iniciar a extração. Por padrão, começa na página 1.

2. **Executar o Script:**
   - Abra um terminal ou prompt de comando.
   - Navegue até o diretório onde o script está salvo.
   - Execute o comando: `python catmat_data_extraction.py` (substitua "catmat_data_extraction.py" pelo nome real do seu arquivo).

3. **Opção de Combinar Arquivos:**
   - Ao final da execução, o script perguntará se você deseja combinar os arquivos CSV baixados em um único arquivo. Responda com "S" para sim ou "N" para não.

### Estrutura do Código

1. **Função `download_data`:**
   - Recebe a URL da página, o caminho do arquivo de destino e o número máximo de tentativas.
   - Tenta baixar os dados da URL e salvá-los em formato JSON.
   - Retorna `True` se o download for bem-sucedido, `False` caso contrário.

2. **Função `combine_csv_files`:**
   - Recebe o nome do arquivo de saída e uma lista de arquivos CSV.
   - Lê os arquivos CSV, concatena-os em um único DataFrame do pandas e salva em um novo arquivo CSV.

3. **Fluxo Principal:**
   - Define a URL base da API do CATMAT.
   - Obtém o número total de páginas da API.
   - Cria a pasta `dados_temporarios` para armazenar os arquivos JSON temporários.
   - Itera pelas páginas da API, a partir da `pagina_inicial`:
     - Baixa os dados de cada página usando a função `download_data`.
     - Adiciona os dados baixados à lista `all_data`.
   - Converte a lista `all_data` em um DataFrame do pandas.
   - Salva o DataFrame em um arquivo CSV chamado `dados_extraidos_catmat_item.csv`.
   - Exclui os arquivos temporários e a pasta `dados_temporarios`.
   - Pergunta ao usuário se deseja combinar os arquivos CSV em um único arquivo.
   - Se o usuário responder "S", chama a função `combine_csv_files` para realizar a combinação.

### Personalização

- **URL Base da API:** Modifique a variável `BASE_URL` se a API do CATMAT mudar.
- **Página Inicial:** Ajuste a variável `pagina_inicial` para começar a extração a partir de uma página específica.
- **Nome do Arquivo de Saída:** Altere a variável `output_csv_filename` para personalizar o nome do arquivo CSV final.
- **Máximo de Tentativas:** Ajuste o parâmetro `max_attempts` na função `download_data` para controlar o número de tentativas em caso de falha no download.

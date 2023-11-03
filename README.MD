Extração e Análise de Dados do CATMAT

Este repositório contém o código para extração dos dados abertos do Catálogo de Materiais (CATMAT) do ComprasNet e um exemplo de análise dos dados para ratificação dos elementos baixados.
Na extração dos dados, o script baixa todos os elementos dos catálogos de materiais PDM

O script extracao_catmat.py realiza a extração paginada da API do CATMAT, salvando os dados em formato JSON e CSV.

Para executá-lo:

python extracao_catmat.py

Isso irá:
	•	Fazer requisições paginadas para a API do CATMAT
	•	Salvar os dados JSON temporários na pasta dados_temporarios/
	•	Exportar os dados para dados_extraidos_catmat_item.csv
	•	Excluir os arquivos temporários
	•	Perguntar se deseja combinar todos os CSVs


Análise de dados

O notebook Jupyter analise.ipynb contém um exemplo de leitura e análise exploratória dos dados extraídos.


É possível visualizá-lo online via GitHub Pages.


Dados
	•	dados_extraidos_catmat_item.csv: dados extraídos da API em formato tabular
	•	dados_combinados.csv: todos os CSVs combinados (opcional)


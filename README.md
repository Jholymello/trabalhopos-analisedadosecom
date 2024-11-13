# E-commerce Data Analysis Project
Este projeto utiliza o Streamlit para criar uma aplicação web interativa que permite a análise de dados de um e-commerce. A aplicação carrega e processa dados de vendas, permitindo a visualização de tendências e insights interativos. O objetivo é demonstrar a criação de visualizações e funcionalidades úteis para análises rápidas.

## Funcionalidades
Carregar e processar dados de um arquivo específico.
Utilizar widgets interativos para selecionar e filtrar informações.
Exibir análises de dados e visualizações para auxiliar na tomada de decisão.
Executar uma API local para fornecer dados e interações.

## Estrutura do Projeto
kotlin
Copiar código
├── ecom_data_project2
│   ├── data_loader.py       # Script de carregamento e pré-processamento dos dados
│   ├── data_analysis.py     # Script de análise de dados com funções para visualização
│   ├── api.py               # Script da API para fornecer endpoints de dados
│   ├── app.py               # Script principal que executa a aplicação Streamlit
│   ├── requirements.txt     # Arquivo com as dependências do projeto
│   └── README.md            # Documento explicativo do projeto

## Instalação

## Clone o repositório:
Copiar código
git clone <URL_DO_REPOSITORIO>
cd ecom_data_project2

## Crie um ambiente virtual e ative-o:
Copiar código
python -m venv venv
.\venv\Scripts\Activate

## Instale as dependências:
Copiar código
pip install -r requirements.txt
Executando a Aplicação
# Certifique-se de que os dados necessários estão disponíveis no diretório apropriado.

### Requirements
- Python 3.8+
- Pandas
- Flask
- Streamlit
- Matplotlib

## Para executar o aplicativo Streamlit:
Copiar código
streamlit run app.py  
# verifique o diretorio onde está o seu arquivo.py
# Acesse a aplicação no navegador através do endereço indicado pelo Streamlit (geralmente Streamlit interface at http://localhost:8501 e API http://localhost:5000.)

## Exemplo de Uso
A aplicação apresenta uma interface para análise dos dados de e-commerce, permitindo a filtragem e seleção de métricas específicas. Ao escolher uma métrica, a aplicação gera visualizações interativas que facilitam o entendimento dos dados.
No arquivo exemplo temos as seguintes colunas no csv: ['order_id', 'order_date', 'customer_id', 'customer_name', 'category', 'subcategory', 'product_id', 'product_name', 'quantity', 'price', 'discount', 'profit', 'region']
Gerando gráficos: ['Total de venda por data de compra', 'genero e faixa etária dos compradores', 'ticket médio por período de compra']

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade!



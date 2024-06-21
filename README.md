# Avaliação das Sprints 4 e 5 - Programa de Bolsas Compass UOL e AWS - UFES/UFLA abril/2024

Avaliação da quarta e quinta sprints do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

## 🌐 Sobre o Projeto!

Este projeto consiste na criação de um serviço de machine learning para classificação de preços de reserva em hotéis, utilizando o Hotel Reservations Dataset. O modelo foi treinado com o SageMaker da AWS, rodando localmente e a inferência foi feita por meio de uma API desenvolvida em Python. 

***

# Construção do Modelo

O Hotel Reservations Dataset contém informações sobre reservas em hotéis e será utilizado para classificar os dados por faixa de preços. A equipe criou uma nova coluna chamada `label_avg_price_per_room` para categorizar as reservas em três faixas de preço:

1. `1` para `avg_price_per_room` ≤ 85
2. `2` para 85 < `avg_price_per_room` < 115
3. `3` para `avg_price_per_room` ≥ 115

O dataset original e o processado foram armazenados no AWS RDS e o modelo treinado foi salvo no S3.

## 📂 Estrutura do Repositório

- `assets/`: Diretório para armazenar imagens usadas no README.
    - `sprint4-5.jpg`
      
- `src/`: Diretório que armazena o código-fonte do projeto.
    - `api/`: Código do serviço de inferência em Python.
        - `app.py`: Arquivo principal da aplicação.
        - `docker-compose.yml`: Arquivo de configuração do Docker Compose.
        - `dockerfile`: Define a imagem Docker para o serviço de inferência.
        - `requirements.txt`: Lista de dependências Python do projeto.
    - `python/`: Scripts Python utilizados no projeto.
        - `sagemaker/`: Scripts para treinamento do modelo no SageMaker.
            - `TesteKMeans.ipynb`
            - `TesteLinearLearner.ipynb`
            - `TesteRandomCutForest.ipynb`
            - `TesteRandomForest.ipynb`
        - `scripts/`: Scripts para manipulação de dados.
            - `csv_to_rds.ipynb`
            - `mysql_to_csv.ipynb`

- `.dockerignore`: Lista de arquivos e diretórios que serão ignorados pelo Docker ao construir a imagem.
- `.gitignore`: Lista de arquivos e diretórios que serão ignorados pelo Git.
- `README.md`: Documentação do projeto.

***


## 🔧 Pré-requisitos

`Python 3.8+`, `AWS CLI`, `Jupyter Notebook` e `Docker`

***


## 🚀 Como Usar

1. Clone o Repositório:
    ```bash
    git clone https://github.com/Compass-pb-aws-2024-ABRIL/sprints-4-5-pb-aws-abril.git
    ```
2. Navegue até o diretório do projeto e altere para a branch "grupo-1":
    ```bash
    cd sprints-4-5-pb-aws-abril
    git checkout grupo-1
    ```

### Usando Python

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a API:
    ```bash
    python src/api/app.py
    ```
    
5. Acesse a API:
   ```bash
   http://localhost:8000
    ```

### Usando Docker

3. Construa a Imagem Docker:
    ```bash
    docker build -t nome-da-imagem .
    ```

4. Execute o Container Docker:
    ```bash
    docker run -d -p 8000:8000 nome-da-imagem
    ```
    
5. Acesse a API:
   ```bash
   http://localhost:8000
    ```

***


## Diagrama de Arquitetura AWS

Diagrama de arquitetura da aplicação na AWS.

![AWS API Architecture]("assets/sprint4-5.jpg")

***


## ✅ Tecnologias utilizadas

- `AWS - Sagemaker`
- `AWS - EC2`
- `AWS - S3`
- `AWS - RDS`
- `FastAPI`
- `Anaconda`
- `Jupyter`
- `Python`

***


## ❌ Dificuldades

- Lidar com a integração entre SageMaker, S3 e RDS.
- Realizar o deploy da aplicação na AWS.

***


## 👨‍💻 Autores

- [José Acerbi Almeida Neto](https://github.com/JoseJaan)
- [Luiz Fillipe Oliveira Morais](https://github.com/LuizFillipe1)
- [Gustavo Henrique Vago Brunetti](https://github.com/GustavoBrunetti)
- [Rafael Alves Silva Rezende](https://github.com/rafa-rez)

***



# LPED_ProjetoFinal

Projeto final da disciplina de **Linguagens de Programação para Engenharia de Dados**, desenvolvido em Python.
O objetivo é construir uma pipeline de processamento de dados utilizando boas práticas de organização e versionamento.

## Estrutura de Diretórios
LPED_ProjetoFinal/
├── data/
│ ├── input.csv
│ ├── output.csv
│ └── stage.csv
├── dvc-storage/
├── logs/
│ └── execucao.log
├── src/
│ ├── tasks/
│ └── utils/
│ ├── init.py
│ ├── main.py
│ ├── pipeline.py
│ └── task.py
├── .gitignore
├── .pre-commit-config.yaml
├── dvc.yaml
├── requirements.txt
└── README.md

## Instalação

- Linux / Mac
```bash
python -m venv venv # Cria o virtual env
source venv/bin/activate # Inicia o virtual env
python3 -m pip install -r requirements.txt
mkdir dvc-storage
dvc remote add -d localstore ./dvc-storagemkdir -p data
dvc push
touch data/input.csv data/output.csv data/stage.csh
```
- Windows (CMD)
```bash
python -m venv venv # Cria o virtual env
venv\Scripts\activate # Inicia o virtual env
python3 -m pip install -r requirements.txt
mkdir dvc-storage
dvc remote add -d localstore ./dvc-storage
dvc push
mkdir data
type nul > data\input.csv
type nul > data\output.csv
type nul > data\stage.csh
```

## Execução
```bash
python3 main.py
```

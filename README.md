# Parseador de arquivos txt
Projeto de uma interface web que aceita upload do arquivo CNAB cpm formato .txt, normaliza os dados e armazena-os em um banco de dados relacional e exibe essas informações em tela.

## Tecnologias Utilizadas
  - Python
  - Django
  - SQLite3


## Rodando o projeto localmente

#### Clone o projeto:

```bash
  git clone git@github.com:KamilaMattos/BackEnd-Python-upload-file-cnab.git
```

#### Entre no diretório do projeto:

```bash
  cd cnab-txt-py
```

#### Ative o ambiente virtual:

```bash
  python -m venv venv
```

#### Inicie o ambiente virtual:

- Powershell
```bash
  .\venv\Scripts\activate
```

- Bash
```bash
  source venv/Scripts/activate
```

- Linux
```bash
  source venv/bin/activate
```

#### Instale as dependências:
```bash
  pip install -r requirements.txt
```

#### Rode as migrations:
```bash
  python manage.py migrate
```

#### Inicie o server localmente:
```bash
  python manage.py runserver
```


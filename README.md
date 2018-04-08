# wpchildmaker
Gera arquivos de tema filho para o Divi no Wordpress

[![Build Status](https://travis-ci.org/tiagocordeiro/wpchildmaker.svg?branch=master)](https://travis-ci.org/tiagocordeiro/wpchildmaker)
[![Updates](https://pyup.io/repos/github/tiagocordeiro/wpchildmaker/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/wpchildmaker/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/wpchildmaker/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/wpchildmaker/)


## Como usar

Clone o repositório.

`git clone https://github.com/tiagocordeiro/wpchildmaker.git`

Acesse o diretório.

`cd wpchildmaker`

Crie um ambiente virtual.

`python -m venv venv`

Ative o ambiente.

`source venv/bin/activate`

Instale as dependências do projeto.

`pip install -r requirements.txt`

Acesse o diretório e rode o script com os argumentos.

```
cd wpchildmaker
python wpchildmaker.py --theme_name "MeuTema" --customer_name "Meu Cliente" --customer_site "https://www.mulhergorila.com"
```

Ou, simplesmente:

```
python wpchildmaker.py
```

Pronto, o seu tema filho foi criado no diretório `wpchildmaker/mychilds`

# wpchildmaker
Gera arquivos de tema filho para o Divi no Wordpress


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
python wpchildmaker.py "MeuTema" "Meu Cliente" "https://www.mulhergorila.com"
```

Pronto, o seu tema filho foi criado no diretório `wpchildmaker/mychilds`

# Módulo Introdutório > Desenvolvimento Backend > Aula 2

## Ambiente Python para desenvolvimento

- Após o download, dentro do [Visual Studio Code](https://code.visualstudio.com/), execute o comando para criar e utilizar o ambiente Python

Comando para criar o ambiente de desenvolvimento:

```
docker-compose build
```

Comando para utilizar o ambiente de desenvolvimento criado:

```
docker-compose up -d
```

## Visual Studio Code

> Caso já tenha o Visual Studio Code instalado em seu sistema operacional, não é necessário seguir os passos abaixo

Aqui estão as instruções para instalar o Visual Studio Code (VSCode) em diferentes sistemas operacionais.

### Windows

1. Acesse o site oficial do VSCode em [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Clique no botão de download para Windows.
3. Execute o instalador que foi baixado (geralmente chamado VSCodeSetup.exe).
4. Siga as instruções do instalador, aceitando os padrões recomendados, como associação de arquivos, a menos que você tenha preferências específicas.
5. Após a instalação, inicie o Visual Studio Code a partir do menu Iniciar ou do ícone na área de trabalho.

### macOS

1. Acesse o site oficial do VSCode em [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Clique no botão de download para macOS.
3. Uma vez que o arquivo .dmg for baixado, abra-o.
4. Arraste o ícone do Visual Studio Code para a pasta de "Aplicativos" no seu Mac.
5. Abra o VSCode a partir da pasta de "Aplicativos" ou da Dock.

### linux

1. A forma mais simples de instalar o Visual Studio Code em distribuições Debian/Ubuntu é baixar e instalar o pacote .deb (64 bits)
   [Debian ou Ubunto](https://code.visualstudio.com/download). Caso utilize outra distribuição, [neste link você encontra a documentação oficial com as explicações e passo a passo da instalação](https://code.visualstudio.com/docs/setup/linux).

## Rodando a API Produtos utilizando o framework Django

Acessar o diretório fastapi-produtos

```
cd /referencial/src/django-produtos
```

Criar o ambiente virtual

```
python -m venv ./venv
```

Para ativar o ambiente virtual

```
source venv/bin/activate
```

Instalar o Django

```
pip install django
```

Criar um arquivo txt com as dependências do projeto

```
pip freeze > requirements.txt
```

Para executar o servidor Django

```
python manage.py runserver 0.0.0.0:8000
```

Para criar um app no Django

```
python  manage.py startapp produto
```

Criar a migração dos modelos Django no banco de dados

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Criar um super usuário para o Django Admin

```
python manage.py createsuperuser
```

## Rodando a API Produtos utilizando o framework FastAPI

Acessar o diretório fastapi-produtos

```
cd /referencial/src/fastapi-produtos
```

Para instalar os pacotes necessários para rodar o servidor FastAPI

```
pip install fastapi uvicorn
```

Para executar o servidor FastAPI

```
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

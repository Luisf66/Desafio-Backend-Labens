# Usa uma imagem oficial do Python
FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia todo o código para dentro do container
COPY . .

# Dá permissão ao entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expõe a porta do Django
EXPOSE 8000

# Usa o entrypoint para iniciar o container
ENTRYPOINT ["/app/entrypoint.sh"]

RUN apt-get update && apt-get install -y netcat-openbsd


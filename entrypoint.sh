#!/bin/sh

echo "Aguardando o banco de dados..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Aplicando migrações..."
python manage.py migrate

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando o servidor..."
exec gunicorn app.wsgi:application --bind 0.0.0.0:8000

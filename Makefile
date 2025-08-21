# Makefile

# Rodar o servidor
run:
	python manage.py runserver

# Criar migrations
migrate:
	python manage.py makemigrations
	python manage.py migrate

# Criar superusuário
superuser:
	python manage.py createsuperuser

# Rodar testes
test:
	python manage.py test

# Instalar dependências
install:
	pip install -r requirements.txt

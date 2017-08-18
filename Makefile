clean:
	find . -name "*.pyc" -exec rm -rf {} \;
run:
	python manage.py runserver 0.0.0.0:8000
migrate:
	python manage.py migrate $(param)
migrations:
	python manage.py makemigrations $(param)
createuser:
	python manage.py createsuperuser
shell:
	python manage.py shell
dbshell:
	python manage.py dbshell
startapp:
	python manage.py startapp $(param)
reset:
	ls $(param)/migrations/0* -exec rm -rf {} \;
	python manage.py migrate --fake $(param) zero
requirements:
	pip freeze > requirements.pip

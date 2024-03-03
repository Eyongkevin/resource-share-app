dev-start:
	python manage.py runserver --settings=config.settings.dev
dev-install:
	pip install -r requirements/dev.txt

dev-migrate:
	python manage.py migrate --settings=config.settings.dev

dev-makemigrations:
	python manage.py makemigrations --settings=config.settings.dev

dev-showmigrations:
	python manage.py showmigrations --settings=config.settings.dev

dev-sqlmigrate:
	python manage.py sqlmigrate $(app) $(m) --settings=config.settings.dev

dev-shell:
	python manage.py shell --settings=config.settings.dev

dev-rollback:
	python manage.py migrate $(app) $(m) --settings=config.settings.dev

dev-test:
	python manage.py test $(k)  --settings=config.settings.dev

prod-local-start:
	sudo gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.prod_local -c config/prod/gunicorn/local.py

prod-local-migrate:
	python manage.py migrate --settings=config.settings.prod_local

prod-local-makemigrations:
	python manage.py makemigrations --settings=config.settings.prod_local

prod-local-shell:
	python manage.py shell --settings=config.settings.prod_local

prod-local-check:
	python manage.py check --deploy --settings=config.settings.prod_local

prod-install:
	pip install -r requirements/prod.txt

prod-collectstatic:
	python manage.py collectstatic --settings=config.settings.prod

prod-migrate:
	python manage.py migrate --settings=config.settings.prod

prod-makemigrations:
	python manage.py makemigrations --settings=config.settings.prod

prod-gunicorn:
	gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.prod -c config/prod/gunicorn/prod.py
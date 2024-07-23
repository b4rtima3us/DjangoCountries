# DjangoCountries_23.07.2024

## Инструкция для развертывания проекта
1. `python3 -m venv django_venv`
2. `source django_venv/bin/activate`
3. `pip install -r requirements.txt`
5. `python manage.py runserver`

## Выполнить миграции
1. `python manage.py migrate`
2. `python manage.py makemigrations`'

### Загрузить данные в БД
`python manage.py loaddata MainApp/fixtures/save_all.json`'

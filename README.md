# Django Sheets
Ссылка на задание: https://unwinddigital.notion.site/unwinddigital/Python-1fdcee22ef5345cf82b058c333818c08

Ссылка на Google sheets: https://docs.google.com/spreadsheets/d/1Exzf45LWUdgM9L3aXexvBesCMQgdAnYlfG9wTnMkowc/edit#gid=0

# Руководство по запуску

Для работы приложения необходим Docker и Postgresql.

1. Необходимо создать и запустить виртульное окружение.
2. В корневой директории, где распологается файл .gitignore и docker-compose.yml создайте файл '.env'.
Содержание файла должно быть следущим:
```
SECRET_KEY='Секретный ключ Django'

POSTGRES_USER='Имя пользователя Postgresql'
POSTGRES_PASSWORD='Пароль Postgresql'
POSTGRES_DB='google_sheets_db'
POSTGRES_HOST='db'
POSTGRES_PORT='5432'
POSTGRES_HOST_AUTH_METHOD=trust`
```
Также возможно придётся создать базу данных с именем google_sheets_db

3.Выполните следующие команды в терминале
```
cd sheets_proj
docker-compose up -d --build
```
4. Перейдите по адресу: http://127.0.0.1:8000/

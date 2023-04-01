# Тестовое задание для UpTrader

### Установка и запуск:

1. Создайте папку для проекта;
2. Склонируйте проект с помощью **git** **clone**;
3. Создайте виртуальное окружение с помощью **venv**;
4. Активируйте виртуальное окружение;
5. Выполните команду **pip** **install** *-r* **requirements.txt** и дождитесь установки необходимых пакетов;
6. Перейдите в папку **tree_menu**;
7. С помощью Python выполните команду **manage.py** **makemigrations**;
8. Выполните команду **manage.py** **migrate** для применения миграций БД;
9. Для заполнения БД используйте команду **manage.py** **loaddata** и файл **data.json**;
10. Запустите тестовый веб-сервер с помощью команды **manage.py** **runserver**;
11. Откройте браузер и перейдите по адресу **http://127.0.0.1:8000/**.
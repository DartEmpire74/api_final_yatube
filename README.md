# api_yatube - Это API предоставляет возможность работы с постами, группами, подписками и комментариями пользователей.

## Установка

1. Клонируйте репозиторий:

    git clone https://github.com/your-username/api_final_yatube.git
    cd api_yatube

2. Создайте и активируйте виртуальное окружение: 

    python -m venv venv

3. Установите зависимости:  

    pip install -r requirements.txt

4. Примените миграции: 

    python manage.py migrate

5. Запустите сервер разработки:

    python manage.py runserver
    
По умолчанию, сайт будет доступен по адресу http://127.0.0.1:8000/.

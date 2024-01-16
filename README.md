## API Yatube 

### Описание проекта.
Этот API предоставляет возможность работы с постами, группами, подписками и комментариями пользователей.

### Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/your-username/api_final_yatube.git
```

```
cd api_final_yatube
```


2. Создайте и активируйте виртуальное окружение: 

```
python -m venv env
```
```
. venv/Scripts/activate
```

3. Установите зависимости:  

```
pip install -r requirements.txt
```

4. Примените миграции: 

```
python3 manage.py migrate
```

5. Запустите сервер разработки:

```
python3 manage.py runserver
```
По умолчанию, сайт будет доступен по адресу http://127.0.0.1:8000/.

### Endpoint-ы
`api/v1/posts/:` Посты.

Пример `GET` запроса: http://yourdomain.com/api/v1/posts/

Ответ: 
```
[
    {
        "id": 1,
        "text": "Текст поста 1",
        "author": "username",
        "pub_date": "2022-01-14T12:34:56Z",
        "group": "Group Name"
        "image": string
    },
    {
        "id": 2,
        "text": "Текст поста 2",
        "author": "username",
        "pub_date": "2022-01-14T13:45:30Z",
        "group": "Group Name"
        "image": string
    },
    ...
]
```

`api/v1/groups/:` Группы.

Пример `GET` запроса: http://yourdomain.com/api/v1/groups/

Ответ: 
```
[
    {
        "id": 1,
        "title": "Group Name",
        "slug": "group-slug"
        "description": "group-description"
    },
    {
        "id": 2,
        "title": "Another Group",
        "slug": "another-group"
        "description": "group-description"
    },
    ...
]
```

`api/v1/follow/:` Подписки.

Пример `GET` запроса: http://yourdomain.com/api/v1/follow/

Ответ: 
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

`api/v1/posts/<post_id>/comments/`: Комментарии к посту.

Пример `GET` запроса: http://yourdomain.com/api/v1/posts/{post_id}/comments/

Ответ: 
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

Для работы с пользователями используются сторонние библиотеки `djoser` и `djoser.urls.jwt`, интегрированные в общие маршруты `v1_urls`.

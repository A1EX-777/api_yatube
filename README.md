# API Yatube

Учебный проект в рамках курса Яндекс Практикум. Реализует REST API для социальной сети Yatube.

## Технологии

- Django
- Django REST Framework
- SQLite3

## Основные эндпоинты

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| POST | `/api/v1/api-token-auth/` | Получение токена |
| GET | `/api/v1/posts/` | Список постов |
| POST | `/api/v1/posts/` | Создать пост |
| GET | `/api/v1/posts/{id}/` | Пост по id |
| PUT/PATCH | `/api/v1/posts/{id}/` | Обновить пост (автор) |
| DELETE | `/api/v1/posts/{id}/` | Удалить пост (автор) |
| GET/POST | `/api/v1/posts/{post_id}/comments/` | Комментарии поста |
| GET/PUT/PATCH/DELETE | `/api/v1/posts/{post_id}/comments/{id}/` | Комментарий |
| GET | `/api/v1/groups/` | Список групп |
| GET | `/api/v1/groups/{id}/` | Группа по id |

## Права доступа

Все эндпоинты требуют авторизации

Редактирование/удаление постов и комментариев - только автору

Группы - только чтение

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <url-репозитория>
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate  # Windows
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:
```
cd yatube_api
```

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```




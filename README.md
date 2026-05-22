# API Yatube

Учебный проект в рамках курса Яндекс Практикум. Реализует REST API для социальной сети Yatube.

## Технологии

- Django
- Django REST Framework
- SQLite3

## Права доступа

Все эндпоинты требуют авторизации (токен)

Редактирование/удаление постов и комментариев - только автору

Группы - только чтение

## Установка

```bash
git clone <url-репозитория>
cd api_yatube
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver




Метод	    Эндпоинт	                        Описание
POST	    /api/v1/api-token-auth/	            Получение токена
GET	        /api/v1/posts/	                    Список постов
POST	    /api/v1/posts/	                    Создать пост
GET         /api/v1/posts/{id}/	                Пост по id
PUT/PATCH	/api/v1/posts/{id}/	                Обновить пост (автор)
DELETE	    /api/v1/posts/{id}/	                Удалить пост (автор)
GET	        /api/v1/groups/	                    Список групп
GET	        /api/v1/groups/{id}/	            Группа по id
GET/POST	/api/v1/posts/{post_id}/comments/	Комментарии поста
GET/PUT/PATCH/DELETE	/api/v1/posts/{post_id}/comments/{id}/	Комментарий

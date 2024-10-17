# Сайт кулинарных рецептов

![example workflow](https://github.com/aeee78/recipes/actions/workflows/main.yml/badge.svg)


Это веб-приложение для обмена рецептами, добавления их в избранное, подписки на авторов и создания списков покупок.

## Основные возможности

- **Аутентификация и регистрация** — Регистрация новых пользователей и вход для зарегистрированных.
- **Просмотр и поиск рецептов** — Сортировка по дате публикации и фильтрация по тегам.
- **Рецепты** — Полные инструкции с ингредиентами и изображениями, возможность добавления в избранное.
- **Профили пользователей** — Просмотр рецептов и подписки на авторов.
- **Избранное** — Сохранение любимых рецептов для быстрого доступа.
- **Список покупок** — Автоматическое создание списка ингредиентов для выбранных рецептов.
- **Создание рецептов** — Пользователи могут добавлять и редактировать собственные рецепты.
- **Административные функции** — (Опционально) Управление пользователями, рецептами и тегами.

## Технологии

- Python
- Django
- Docker
- PostgreSQL
- HTML / CSS
- JavaScript

## Демонстрация проекта

Проект развернут и доступен по следующему адресу: [edafood.ddns.net](http://edafood.ddns.net)

## Установка и запуск

### Локальная установка

1. Клонируйте репозиторий:
2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   ```
3. Активируйте виртуальное окружение:
   - Windows: `source venv\Scripts\activate`
   - Linux/macOS: `source venv/bin/activate`
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Выполните миграции:
   ```bash
   python manage.py migrate
   ```
6. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

### Запуск с Docker

1. Клонируйте репозиторий:
2. Создайте и заполните `.env` файл на основе `.env.example`.
3. Запустите Docker контейнеры:
   ```bash
   docker-compose up -d
   ```
4. Выполните миграции и создайте суперпользователя:
   ```bash
   docker-compose exec backend python manage.py migrate
   docker-compose exec backend python manage.py createsuperuser
   docker-compose exec backend python manage.py collectstatic --no-input
   ```








## Разграничение прав

* **Гость:**  Может просматривать рецепты и профили пользователей.
* **Зарегистрированный пользователь:** Доступ ко всем функциям, кроме административных.
* **Администратор:**  Полный доступ ко всем функциям, включая управление пользователями, тегами и рецептами.



## Примеры API запросов

### Получение списка рецептов

```http
GET /api/recipes/
```

### Получение рецепта по ID

```http
GET /api/recipes/{id}/
```

### Создание рецепта (требуется авторизация)

```http
POST /api/recipes/
```

```json
{
  "ingredients": [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 50}
  ],
  "tags": [1, 2],
  "image": "data:image/png;base64,...",
  "name": "Название рецепта",
  "text": "Описание рецепта",
  "cooking_time": 30
}
```

### Добавление рецепта в избранное (требуется авторизация)

```http
POST /api/recipes/{id}/favorite/
```

### Удаление рецепта из избранного (требуется авторизация)

```http
DELETE /api/recipes/{id}/favorite/
```

### Поиск ингредиентов по имени

```http
GET /api/ingredients/?name=карт
```

Полная документация доступна по  адресу: [edafood.ddns.net/api/docs/](http://edafood.ddns.net/api/docs/)

*Примечание:* Замените `{id}` на фактический ID. Для авторизованных запросов используйте заголовок `Authorization: Token <ваш_токен>`.

# Благотворительный фонд поддержки котиков "QRKot"

Код в данном репозитории представляет собой код API для проекта "QRKot": благотворительного фонда поддержки кошек и котов.

Фонд собирает пожертвования на различные целевые проекты:

- медицинское обслуживание нуждающихся хвостатых,
- обустройство кошачьей колонии в подвале,
- корм оставшимся без попечения кошкам
- и другие цели, связанные с поддержкой кошачьей популяции.

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана, проект закрывается.

Каждый пользователь может сделать пожертвование. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых. Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

## Технологии

Python3.10, FastAPI 0.78, SQLAlchemy 1.4, Alembic 1.7

## Как запустить проект локально

Клонируйте репозиторий:

```git clone https://github.com/tanja-ovc/cat_charity_fund.git```

Убедитесь, что находитесь в директории _cat_charity_fund/_ либо перейдите в неё:

```cd cat_charity_fund/```

Cоздайте виртуальное окружение:

```python3 -m venv venv```

Активируйте виртуальное окружение:

* Для Linux/Mac:
 
    ```source venv/bin/activate```

* Для Windows:

    ```source venv/Scripts/activate```

При необходимости обновите pip:

```pip install --upgrade pip```

Установите зависимости из файла requirements.txt:

```pip install -r requirements.txt```

Создайте в корне проекта файл под названием __.env__ и заполните его по образцу имеющегося в репозитории файла __.env.example__, например, так:

```
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=cats_forever
FIRST_SUPERUSER_EMAIL=superuser@example.com
FIRST_SUPERUSER_PASSWORD=superuser-password
```

Примените миграции:

```alembic upgrade head```

Запустите проект:

```uvicorn app.main:app```

После запуска сервера будет автоматически создан первый суперпользователь (о чём выведется сообщение в терминале). Логин и пароль для такого пользователя вы писали выше в файле __.env__.

## Документация API

Увидеть возможные запросы к API и потестировать их после локального запуска будет удобно здесь: http://127.0.0.1:8000/docs

## Авторы

Автор проекта: Татьяна Овчинникова

Авторы тестов: Яндекс.Практикум

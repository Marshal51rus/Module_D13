# Module_D13

## Использовал:
фреймворк Django

## Установка библиотек:
requirements.txt

## Отправка email осуществляется 2 способами: через django и celery

Для запуска celery:<br>
pip install celery<br>
pip install redis<br>
pip install -U "celery[redis]

## Запускаем docker
Устанавливаем Redis<br>
в коммандной стоке пишем: <br>
docker run -d -p 6379:6379 redis

## Комманды для запуска:
celery -A myproject1 worker -l INFO<br>
celery -A myproject1 beat -l INFO<br>
celery -A proj flower --port=5555

### Внимание для запуска celery из под Windows обязательно ставим:
pip install gevent<br>
celery -A myproject1 worker -l info -P gevent<br>
( c версии 4+ celery не поддерживет Windows)

# Module_D13

## Использовал:
фреймворк Django

## Установка библиотек:
requirements.txt

##Отправка email осуществляется 2 способами: через django и celery

Для запуска celery:
pip install celery
pip install redis
pip install -U "celery[redis]

##Запускаем docker
Устанавливаем Redis
в коммандной стоке пишем: 
docker run -d -p 6379:6379 redis

##Комманды для запуска:
celery -A myproject1 worker -l INFO
celery -A myproject1 beat -l INFO
celery -A proj flower --port=5555

## Внимание для запуска celery из под Windows обязательно ставим:
pip install gevent
celery -A myproject1 worker -l info -P gevent
( c версии 4+ celery не поддерживет Windows)

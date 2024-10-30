# healthz-server
Для корректного запуска сервера необходимо установить Python версии 3.10 и созадать файлик .env с содержимым: 
`PORT=<ваш_порт>`

### Запуск сервера на локальной машине:
```
pip install requirements.txt
python3.10 app.py
```

### Сборка и запуск контейнера с сервером(необходимо выполнять в директории с Dockerfile):
```
docker build -t <название_контейнера> .
docker run --network host <название_контейнера>
```
Для запуска контейнра в фоновом режиме необходимо добавить флаг `-d`:
```
docker run --network host -d <название_контейнера>
```

### Проверка работоспособности 
Перейдите в браузере по адресу: `http://localhost:<ваш_порт>/healthz`
Если ответ сервера OK, то сервер успешно запущен

# Используем официальный базовый образ Python
FROM python:3.9-slim

# Копирование содержимого локальной директории в рабочую директорию внутри контейнера
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска приложения
CMD ["python3", "my_relay.py"]

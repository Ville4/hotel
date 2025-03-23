FROM python:3.13-slim

# Устанавливаем необходимые зависимости для работы с selenium и Chromium
RUN apt-get update && apt-get install -y \
    chromium \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Скачиваем и устанавливаем совместимую версию ChromeDriver для версии Chromium 134
RUN wget https://storage.googleapis.com/chrome-for-testing-public/114.0.5735.90/linux64/chrome-linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Переходим в рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое текущей директории в контейнер
COPY . .

# Устанавливаем переменные окружения для Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Открываем порт для приложения Flask
EXPOSE 5000

# Команда для запуска приложения Flask
CMD ["flask", "run", "--host=0.0.0.0"]

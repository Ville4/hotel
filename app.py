from flask import Flask, render_template, request, send_file
import datetime
import io
from test_main import test_open_ostrovok  # Импортируем твой парсинг-скрипт
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_report', methods=['POST'])
def generate_report():
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    # Преобразуем строки в даты
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return "Некорректный формат дат"

    # Запускаем браузер через selenium
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Запускаем твой парсинг-скрипт и генерируем результат
    data = test_open_ostrovok(driver, start_date, end_date)

    # Сохраняем данные в Excel
    excel_path = 'C:\\Users\\Вилле\\Desktop\\hotel_ex\\отели.xlsx'

    # Закрываем драйвер после выполнения
    driver.quit()

    # Отправляем файл пользователю
    return send_file(excel_path, as_attachment=True, download_name='report.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

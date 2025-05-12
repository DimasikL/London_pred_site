from flask import Flask, request, jsonify, send_from_directory
import util
import os

# Указываем путь до папки с клиентом
CLIENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'client'))

# Указываем путь до папки с артефактами
ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), 'artifacts')

app = Flask(__name__)

@app.route('/')
def index():
    # Отправляем html файл клиенту
    return send_from_directory(CLIENT_DIR, 'app.html')

@app.route('/app.js')
def serve_js():
    # Отправляем js файл клиенту
    return send_from_directory(CLIENT_DIR, 'app.js')

@app.route('/app.css')
def serve_css():
    # Отправляем css файл клиенту
    return send_from_directory(CLIENT_DIR, 'app.css')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    # Обрабатываем запрос на получение списка локаций
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # Получаем параметры из запроса
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bedroom = int(request.form['bedroom'])
    bathroom = int(request.form['bathroom'])
    reception = int(request.form['reception'])

    # Получаем предсказание
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bedroom, bathroom, reception)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")

    # Передаем путь для загрузки артефактов
    util.load_saved_artifacts(ARTIFACTS_DIR)

    app.run()

from flask import Flask, render_template, request, jsonify
import base64
import os
from datetime import datetime

app = Flask(__name__)

# Создание папки snapphoto, если она не существует
if not os.path.exists('snapphoto'):
    os.makedirs('snapphoto')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    img_data = data['image']
    img_data = img_data.split(",")[1]
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.png")  # Генерация уникального имени файла
    file_path = os.path.join('snapphoto', filename)
    with open(file_path, "wb") as fh:
        fh.write(base64.b64decode(img_data))
    return jsonify(success=True, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

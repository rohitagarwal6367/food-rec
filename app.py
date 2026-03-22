import os
import json
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for login session

# Paths
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'food_model.keras')
CLASS_PATH = os.path.join(BASE_DIR, 'model', 'class_names.txt')
FOOD_INFO_PATH = os.path.join(BASE_DIR, 'model', 'food_info.json')
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
model = load_model(MODEL_PATH)
num_classes = model.output_shape[-1]

# Load class labels
with open(CLASS_PATH, 'r') as f:
    labels = [line.strip() for line in f if line.strip()]
if len(labels) != num_classes:
    labels += [f"Unknown_{i}" for i in range(len(labels), num_classes)]
class_labels = labels

# Load food info JSON
food_info = {}
if os.path.exists(FOOD_INFO_PATH):
    with open(FOOD_INFO_PATH, 'r') as f:
        food_info = json.load(f)

# Dummy user store
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Dummy check (replace with actual auth)
        if username == 'admin' and password == 'admin':
            session['user'] = username
            return redirect(next_url or url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials', next=next_url)
    return render_template('login.html', next=next_url)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('register.html', error='Username already exists.')
        users[username] = generate_password_hash(password)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file uploaded", 400
    file = request.files['image']
    if file.filename == '':
        return "No file selected", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224), color_mode='rgb')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    index = np.argmax(prediction)
    predicted_label = class_labels[index]

    info = food_info.get(predicted_label, {
        "calories": "N/A",
        "protein": "N/A",
        "fat": "N/A",
        "carbohydrates": "N/A",
        "fiber": "N/A"
    })

    return render_template('result.html',
                           prediction=predicted_label,
                           image_file=file.filename,
                           nutrients=info,
                           logged_in='username' in session)

@app.route('/download/<filename>')
def download(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
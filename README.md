# 🍔 Food Recognition System (Flask + Machine Learning)

A web-based Food Recognition System that allows users to upload food images and get predictions using a trained Machine Learning model. The application also provides food-related information based on the prediction.

---

## 🚀 Features

* 📸 Upload food images from your device
* 🤖 Predict food category using ML model
* 📊 Display prediction results instantly
* 🍽️ Show food details using JSON data
* 🔐 User Authentication (Login/Register)
* 💻 Responsive and user-friendly UI

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Flask (Python)
* **Machine Learning:** TensorFlow / Keras
* **Database:** SQLite (for user authentication)
* **Other Tools:** JSON (for food info)

---

## 📂 Project Structure

```
food-recognition/
│
├── static/               # CSS, JS, Images
├── templates/           # HTML files
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── result.html
│
├── model/
│   └── food_model.keras # Trained ML model
│
├── uploads/             # Uploaded images
├── food_info.json       # Food details
├── app.py               # Main Flask app
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```
git clone https://github.com/rohitagarwal6367/food-recognition.git
cd food-recognition
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```
python -m venv venv
```

Activate the environment:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📸 How It Works

1. User logs in or registers
2. Uploads a food image
3. Model predicts the food category
4. Result is displayed with food details

---

## 🧠 Machine Learning Model

* Built using TensorFlow/Keras
* Trained on multiple food categories
* Uses image preprocessing before prediction

---

## 📌 Future Improvements

* 🔥 Add more food categories
* 📱 Improve mobile responsiveness
* ☁️ Deploy on cloud (Heroku / Render / AWS)
* 📊 Add calorie estimation feature
* 🎯 Improve model accuracy

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📧 Contact

📌 Gmail: agrwalrohit7877@gmail.com

---

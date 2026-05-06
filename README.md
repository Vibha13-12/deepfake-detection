# 🎭 Deepfake Detection System

A Deep Learning-based web application that detects whether an uploaded image is **Real** or **Fake (Deepfake)** using a trained TensorFlow/Keras model.

Built using:
- Python
- Flask
- TensorFlow / Keras
- HTML, CSS, JavaScript

---

# 🚀 Features

✅ Upload images for detection  
✅ Detects real vs fake faces  
✅ Deep learning model integration  
✅ Drag-and-drop upload UI  
✅ Confidence score prediction  
✅ Responsive modern frontend  
✅ Flask backend integration  

---

# 🧠 Model Information

The model was trained using Convolutional Neural Networks (CNN) on a dataset containing:
- Real images
- AI-generated / manipulated fake images

The trained model:
```python
deepfake_model.h5
```

is loaded into the Flask application for prediction.

---

# 📂 Project Structure

```bash
deepfake-detection/
│
├── app/
│   ├── model/
│   │   └── deepfake_model.h5
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── app.py
│
├── Dataset/
│   ├── Train/
│   ├── Validation/
│   └── Test/
│
├── train.py
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Vibha13-12/deepfake-detection.git
```

---

## 2️⃣ Navigate to project folder

```bash
cd deepfake-detection
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements file, install manually:

```bash
pip install flask tensorflow pillow numpy
```

---

# ▶️ Run the Application

```bash
python app/app.py
```

Then open:

```bash
http://127.0.0.1:5000
```

in your browser.

---

# 🖼️ How It Works

1. User uploads an image
2. Flask backend receives image
3. Image preprocessing is applied
4. TensorFlow model predicts:
   - REAL
   - FAKE
5. Result and confidence score are displayed on screen

---

# 📸 Screenshots

<img width="1280" height="832" alt="Screenshot 2026-05-05 at 5 03 45 PM" src="https://github.com/user-attachments/assets/ccc0cbf3-14af-4fcc-b658-e99b816f0022" />


Example:

```markdown
![Home Page](screenshots/home.png)
```

---

# 🔥 Technologies Used

- Python
- Flask
- TensorFlow
- Keras
- NumPy
- PIL
- HTML
- CSS
- JavaScript

---

# 🎯 Future Improvements

- Video deepfake detection
- Live webcam detection
- Better model accuracy
- User authentication
- Cloud deployment
- Explainable AI visualizations

---

# 👩‍💻 Author

**Vibha Reddy**

GitHub:  
[Vibha13-12 GitHub Profile](https://github.com/Vibha13-12?utm_source=chatgpt.com)

---

# ⭐ Support

If you liked this project:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others

---

# 📜 License

This project is for educational and research purposes.

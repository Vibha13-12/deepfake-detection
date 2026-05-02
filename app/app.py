from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("model/deepfake_model.h5")

def preprocess_image(img):
    img = img.convert("RGB")
    img = img.resize((128, 128))   # MUST match training
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None

    if request.method == "POST":
        file = request.files["file"]

        if file:
            img = Image.open(file)

            processed = preprocess_image(img)
            prediction = model.predict(processed)[0][0]

            print("Prediction value:", prediction)

            # 🔥 IMPORTANT LOGIC
            # Works if {'fake': 0, 'real': 1}
            if prediction > 0.5:
                result = "Real"
                confidence = round(prediction * 100, 2)
            else:
                result = "Fake"
                confidence = round((1 - prediction) * 100, 2)

    return render_template("index.html", result=result, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
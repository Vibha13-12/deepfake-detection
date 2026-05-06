from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
import io

app = Flask(__name__)

# 🔥 Fix 413 error
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Load model
model = tf.keras.models.load_model("model/deepfake_model.h5")

IMG_SIZE = (128, 128)


def preprocess_image(img):
    img = img.convert("RGB")
    img = img.resize(IMG_SIZE)
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None

    if request.method == "POST":
        try:
            img = None

            # 🔹 CAMERA
            camera_image = request.form.get("camera_image")

            if camera_image:
                header, encoded = camera_image.split(",", 1)
                image_bytes = base64.b64decode(encoded)
                img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

            # 🔹 UPLOAD
            elif "file" in request.files:
                file = request.files["file"]

                if file and file.filename != "":
                    img = Image.open(file).convert("RGB")

            if img is None:
                return render_template("index.html", result="No image provided")

            processed = preprocess_image(img)

            prediction = model.predict(processed)[0][0]
            print("Prediction:", prediction)

            if prediction > 0.5:
                result = "Real"
                confidence = round(float(prediction) * 100, 2)
            else:
                result = "Fake"
                confidence = round((1 - float(prediction)) * 100, 2)

        except Exception as e:
            print("Error:", e)
            result = "Error processing image"
            confidence = None

    return render_template("index.html", result=result, confidence=confidence)


if __name__ == "__main__":
    app.run(debug=True, port=5009)
import asyncio
from functools import partial
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("./models/braintumor_model_gpu_1.h5")

@app.route("/", methods=["GET"])
def htmlfile():
    return render_template("index.html")

async def predict_image(file):
    try:
        CLASS_TYPES = ['glioma', 'meningioma', 'notumor', 'pituitary']
        image = Image.open(file)
        image = image.resize((150, 150))
        image_array = np.array(image, dtype=np.float32)
        image_array = np.expand_dims(image_array, axis=0)
        image_array /= 255.0  # Normalize the image

        predictions = model.predict(image_array)
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = CLASS_TYPES[predicted_class_index]

        response = {
            'class_label': predicted_class_label,
            'class_index': predicted_class_index,
            'probabilities': predictions.tolist()[0],
            "condition": CLASS_TYPES[predicted_class_index]
        }
        print(response)
        return f"the condition is {response['condition']}"

    except Exception as e:
        return {'error': str(e)}

@app.route('/predict', methods=['POST'])
def handle_predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    return jsonify(asyncio.run(predict_image(file)))

if __name__ == '__main__':
    app.run(debug=True)

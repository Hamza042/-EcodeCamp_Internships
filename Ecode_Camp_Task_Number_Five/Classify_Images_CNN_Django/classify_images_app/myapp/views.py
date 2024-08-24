from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import os

# Load the model
model_path = os.path.join(settings.BASE_DIR, 'model', 'model.h5')
model = tf.keras.models.load_model(model_path)

def index(request):
    predicted_class = None
    confidence = None
    image_url = None

    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        img = Image.open(image).convert('RGB')

        # Predict the image
        predictions = predict_image(img)
        class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
        predicted_class = class_names[np.argmax(predictions)]
        confidence = np.max(predictions) * 100

        # Save the image to display
        image_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_image.jpg')
        img.save(image_path)
        image_url = default_storage.url('uploaded_image.jpg')

    return render(request, 'myapp/index.html', {
        'image_url': image_url,
        'predicted_class': predicted_class,
        'confidence': confidence,
    })

def preprocess_image(image):
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image.astype('float32') / 255.0
    return image

def predict_image(image):
    image = preprocess_image(image)
    predictions = model.predict(image)
    return predictions

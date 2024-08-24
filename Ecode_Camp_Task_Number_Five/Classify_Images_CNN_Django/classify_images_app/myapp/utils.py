import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from django.conf import settings

# Load the model (assumed to be in the same directory as manage.py)
# model = tf.keras.models.load_model(settings.BASE_DIR / 'model.h5')

# Load the model
model_path = settings.BASE_DIR / 'model' / 'model.h5'
model = tf.keras.models.load_model(model_path)

def preprocess_image(image):
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image.astype('float32') / 255.0
    return image

def predict_image(image):
    image = preprocess_image(image)
    predictions = model.predict(image)
    return predictions

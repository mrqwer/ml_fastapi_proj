import tensorflow as tf
import os
from .helpers import existsImageDirectoryOrCreate, existsAnyFile
from .preprocess import process_images
import glob as glob

SIZE = 224

MODEL_REZNET50 = tf.keras.applications.resnet50.ResNet50()

def get_model_predictions() -> dict:
    image_paths = sorted(glob.glob('./model/imgs/*.png'))
    preprocess_input = tf.keras.applications.resnet50.preprocess_input

    d = process_images(MODEL_REZNET50, image_paths, (SIZE, SIZE), preprocess_input)
    return d
 



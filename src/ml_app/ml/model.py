import tensorflow as tf
from .preprocess import process_images
import glob as glob

SIZE = 224

MODEL_REZNET50 = tf.keras.applications.resnet50.ResNet50()


def get_model_predictions(top: int = 1) -> list:
    image_paths = sorted(glob.glob('imgs/*.png'))
    image_paths = [path.replace('\\', '/') for path in image_paths]
    preprocess_input = tf.keras.applications.resnet50.preprocess_input

    l = process_images(MODEL_REZNET50, image_paths, (SIZE, SIZE), preprocess_input, top)
    return l


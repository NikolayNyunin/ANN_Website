import os

import tensorflow as tf
import tensorflow_hub as tf_hub
import matplotlib.pyplot as plt
import numpy as np
import PIL
from tempfile import NamedTemporaryFile
from django.conf import settings

TEMP_URL = settings.MEDIA_URL[1:] + 'temp/'
TEMP_DIR = os.path.join(settings.MEDIA_ROOT, 'temp')


def nst(input_image, style_image_path):
    content_image = load_image(input_image.read(), path=False)
    style_image = load_image(style_image_path)

    hub_module = tf_hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]

    stylized_image = tensor_to_image(stylized_image)
    with NamedTemporaryFile(delete=False, dir=TEMP_DIR, suffix='.jpg') as file:
        stylized_image.save(file.name, 'JPEG')
        stylized_image_url = TEMP_URL + file.name.split('\\')[-1]

    return stylized_image_url


def load_image(image, path=True):
    max_dim = 1024
    if path:
        image = tf.io.read_file(image)
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)

    shape = tf.cast(tf.shape(image)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    image = tf.image.resize(image, new_shape)
    image = image[tf.newaxis, :]
    return image


def show_image(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    plt.imshow(image)
    if title:
        plt.title(title)
    plt.show()


def tensor_to_image(tensor):
    tensor *= 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)

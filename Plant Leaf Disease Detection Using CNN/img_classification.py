"""Module for classifying plant leaf diseases using a trained CNN model."""

import numpy as np
from PIL import Image, ImageOps
import keras


def teachable_machine_classification(img, weights_file):
    """Classify plant leaf diseases using a trained CNN model.

    Args:
        img: PIL Image object containing the leaf image
        weights_file: Path to the trained model weights

    Returns:
        int: Index of the predicted disease class
    """
    model = keras.models.load_model(weights_file)
    image = img
    size = (200, 200)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image = np.asarray(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255
    prediction = model.predict(image)
    return np.argmax(prediction)

    # Load the model
    # model = keras.models.load_model(weights_file)

    # # Create the array of the right shape to feed into the keras model
    # data = np.ndarray(shape=(1, 128, 128, 3), dtype=np.float32)
    # image = img
    # # image sizing
    # size = (128, 128)
    # image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # # turn the image into a numpy array
    # image_array = np.asarray(image)
    # # Normalize the image
    # normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # # Load the image into the array
    # data[0] = normalized_image_array

    # # run the inference
    # prediction = model.predict(data)
    # return np.argmax(prediction)  # return position of the highest probability

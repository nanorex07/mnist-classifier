from PIL import Image
import numpy as np
import tensorflow as tf


def predict(img):
	image = np.array(Image.open(img).convert("L"))
	image = image.reshape((784,))
	scaled = image/255
	scaled = np.expand_dims(scaled, axis=0)

	model = tf.keras.models.load_model("mnist2.h5")
	return np.argmax(model.predict(scaled))
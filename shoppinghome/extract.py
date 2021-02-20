from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.preprocessing import image
import numpy as np
from numpy.linalg import norm
import tensorflow as tf
from io import BytesIO
from PIL import Image
from urllib.request import Request, urlopen

graph = tf.get_default_graph()


model = ResNet50(weights='imagenet', include_top=False,pooling='avg',
                 input_shape=(224, 224, 3))
def extract_features(URL):   
    input_shape = (224, 224, 3)
    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    res = urlopen(req).read()
    img = Image.open(BytesIO(res)).resize((input_shape[0], input_shape[1]))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    with graph.as_default():
        features = model.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / norm(flattened_features)
    normalized_features = normalized_features.reshape((1,2048))
    return normalized_features

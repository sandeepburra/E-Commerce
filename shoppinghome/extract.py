from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.preprocessing import image
import numpy as np
from numpy.linalg import norm
from pathlib import Path
import os
import tensorflow as tf

graph = tf.get_default_graph()

BASE_DIR = Path(__file__).resolve().parent.parent
pic_dir = os.path.join(BASE_DIR,'pics')
model = ResNet50(weights='imagenet', include_top=False,pooling='avg',
                 input_shape=(224, 224, 3))
def extract_features(img_path):    
    
    img_path = os.path.join(pic_dir,img_path)
    input_shape = (224, 224, 3)
    img = image.load_img(img_path, target_size=(
        input_shape[0], input_shape[1]))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    with graph.as_default():
        features = model.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / norm(flattened_features)
    normalized_features = normalized_features.reshape((1,2048))
    return normalized_features
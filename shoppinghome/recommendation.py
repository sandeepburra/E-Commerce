from .extract import extract_features
from sklearn.metrics import pairwise_distances
import pickle
import numpy as np
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
feature_list_path = os.path.join(BASE_DIR,'mlfiles/features.pickle')
filenames_path = os.path.join(BASE_DIR,'mlfiles/filenames.pickle')

feature_list_cnn = pickle.load(open(feature_list_path, 'rb'))
filenames = pickle.load(open(filenames_path, 'rb'))
def get_similar_products_new(img_path1, num_results):
    fv = extract_features(img_path1)
    pairwise_dist = pairwise_distances(feature_list_cnn, fv)

    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    #pdists  = np.sort(pairwise_dist.flatten())[0:num_results]
    returnlist = []
    for i in range(len(indices)):
        #print('Euclidean Distance from input image:', pdists[i])
        returnlist.append(filenames[indices[i]])
    return returnlist

             
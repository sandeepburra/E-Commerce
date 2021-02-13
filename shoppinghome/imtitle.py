from .extract import extract_features
from sklearn.metrics import pairwise_distances
import pickle
import numpy as np
from pathlib import Path
import os
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
feature_list_path = os.path.join(BASE_DIR,'mlfiles/features.pickle')
filenames_path = os.path.join(BASE_DIR,'mlfiles/filenamesNew.pickle')

feature_list_cnn = pickle.load(open(feature_list_path, 'rb'))
filenames = pickle.load(open(filenames_path, 'rb'))

feature_list_path_tf = os.path.join(BASE_DIR,'mlfiles/tfidf.pickle')
tfidf_vectorizer_path = os.path.join(BASE_DIR,'mlfiles/tfidfvectorizer.pkl')

feature_list_tfidf = pickle.load(open(feature_list_path_tf, 'rb'))
tfidf_vectorizer = joblib.load(tfidf_vectorizer_path)


def get_similar_products_imtitle(img_path1, query,num_results):
   
    fv = extract_features(img_path1)
    pairwise_dist1 = pairwise_distances(feature_list_cnn, fv)

    query_list = []
    query_list.append(query)
    query_vector = tfidf_vectorizer.transform(query_list)
    pairwise_dist2 = pairwise_distances(feature_list_tfidf, query_vector)
    pairwise_dist = pairwise_dist1*20+ pairwise_dist2*5

    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    #pdists  = np.sort(pairwise_dist.flatten())[0:num_results]
    returnlist = []
    for i in range(len(indices)):
        #print('Euclidean Distance from input image:', pdists[i])
        returnlist.append(filenames[indices[i]])
    return returnlist
             
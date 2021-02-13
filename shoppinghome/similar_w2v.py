

from sklearn.metrics import pairwise_distances
import numpy as np
from pathlib import Path
import os
import pickle
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
feature_list_path = os.path.join(BASE_DIR,'mlfiles/tfidf.pickle')
filenames_path = os.path.join(BASE_DIR,'mlfiles/filenames.pickle')
tfidf_vectorizer_path = os.path.join(BASE_DIR,'mlfiles/tfidfvectorizer.pkl')

feature_list_tfidf = pickle.load(open(feature_list_path, 'rb'))
filenames = pickle.load(open(filenames_path, 'rb'))
tfidf_vectorizer = joblib.load(tfidf_vectorizer_path)

def tfidf_model(query):
    
    query_list = []
    query_list.append(query)
    query_vector = tfidf_vectorizer.transform(query_list)
    pairwise_dist = pairwise_distances(feature_list_tfidf, query_vector)

    indices = np.argsort(pairwise_dist.flatten())[0:20]
    #pdists  = np.sort(pairwise_dist.flatten())[0:num_results]
    returnlist = []
    for i in range(len(indices)):
        #print('Euclidean Distance from input image:', pdists[i])
        returnlist.append(filenames[indices[i]])
    return returnlist
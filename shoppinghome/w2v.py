
import pickle
import numpy as np
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
w2vModel = os.path.join(BASE_DIR,'mlfiles\\word2vec_model')



with open(w2vModel, 'rb') as handle:
    model = pickle.load(handle)
vocab = model.keys()
class BuildVector():
    def build_avg_vec(self, sentence, num_features):
        
        featureVec = np.zeros((num_features,), dtype="float32")
        # we will intialize a vector of size 300 with all zeros
        # we add each word2vec(worsdi) to this fetureVec
        nwords = 0
        
        for word in sentence.split():
            nwords += 1
            if word in vocab:
                featureVec = np.add(featureVec, model[word])
        if(nwords>0):
            featureVec = np.divide(featureVec, nwords)
        # returns the avg vector of given sentance, its of shape (1, 300)
        return featureVec
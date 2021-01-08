import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.decomposition import LatentDirichletAllocation
import pickle
sys.path.append('./src')
from countvec_cap2 import *


ly = pd.read_csv('../data/1950_2019_with lyrics.csv')

n_clusters = 5

# LDA

# LDA can only uses raw term counts
# X2 is the CountVectorized matrix

# top_words = X2.toarray().argsort()[:,-1:-(num_top_words+1):-1]


def lda_random_words(df, X, model, column='lyrics'):
    assigned_cluster = lda.transform(tf).argmin(axis=1)

    for i in range(n_clusters):
        cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
        sample_articles = np.random.choice(cluster, 5, replace=False)
        print(f"Topic {i+1}:")
        for song in sample_articles:
            print(f"    {ly.loc[song]['lyrics']}")

def lda_display_topics(num_top_words, model, feature_names=tf_feature_names):

    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-num_top_words - 1:-1]]))


if __name__ == '__main__':




    lda = LatentDirichletAllocation(n_components=n_clusters, 
                                    learning_method='online',
                                    random_state=0)
    lda.fit(X2)
    
    with open('../models/ldatrained.pkl', 'wb') as pickle_file:
        pickle.dump(lda, pickle_file)
    

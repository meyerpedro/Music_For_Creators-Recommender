import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from countvec_cap2 import *

n_clusters = 12

ly = pd.read_csv('../data/1950_2019_with lyrics.csv')

kmeans = KMeans(n_clusters=n_clusters, random_state=0)
kmeans.fit(X2)
prediction = kmeans.predict(X2)    

def display_topics(pred, num_clusters=n_clusters):
    '''
    returns what songs are in which topic/cluster

    input:
        pred = fit_predict(X)
    output:
        list of song indexes devided per cluster/topic
    '''

    l = list(range(num_clusters))
    
    for cluster_idx in l:
        dummy_list = []
        for topic_idx, topic in enumerate(pred):
            if topic == cluster_idx:
                dummy_list.append(topic_idx)

        print("Topic %d:" % (cluster_idx+1))
        print(dummy_list)

def display_top_centroids(num_top_centroids, num_clusters=n_clusters, vec=count_vec, model=kmeans):
    '''
    Returns a list of the n words closest to the cluster's centroid
    '''
    top_centroids = model.cluster_centers_.argsort()[:,-1:-(num_top_centroids+1):-1]
    features = vec.get_feature_names()

    l = list(range(num_clusters))
    
    for cluster, centroid in enumerate(top_centroids):
        dummy_list = []
        for feature_idx in centroid:
            dummy_list.append(features[feature_idx])

        print("Topic %d:" % (cluster+1))
        print(dummy_list)

def kmeans_random_words_topic(df, X, column='lyrics', model=kmeans):

    assigned_cluster = model.transform(X).argmin(axis=1)

    for i in range(n_clusters):
        cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
        sample_articles = np.random.choice(cluster, 5, replace=False)
        print(f"Topic {i+1}:")
        for song in sample_articles:
            print(f"    {df.loc[song][column]}")

print('No Errors on KMeans.py')

# Using TfidfVectorizer

def elbow_method(X,init,final):
    '''
    input:
        X = vectorized feature matrix
        init = initial k value
        final = final k value
    output:
        plot of different K values and model scores
    '''
    fig, ax = plt.subplots(dpi=500)

    ax.set_title('Distortion Score for KMeans Clustering')

    visualizer = KElbowVisualizer(kmeans, k=(10,25), ax=ax)
    visualizer.fit(X)        # Fit the data to the visualizer

    visualizer.show()        # Finalize and render the figure

    # plt.savefig('../images/distortion_scores_kmeans.png')
import matplotlib.pyplot as plt
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation
import pickle
from sklearn.metrics.pairwise import cosine_similarity 


from sklearn.datasets import make_blobs
from yellowbrick.cluster import KElbowVisualizer

sys.path.append('./src')
from clean_df import *
from sort_lyrics_to_genre import *
from countvec_cap2 import *

pd.options.display.max_rows = 200

#database with song, lyrics and atributes

ly = pd.read_csv('../data/1950_2019_with lyrics.csv')
ly.drop('Unnamed: 0', axis=1, inplace=True)

#pickled model to use
with open('../models/ldatrained.pkl' , 'rb') as pickle_file:
    lda = pickle.load(pickle_file)

#subsets per genre
hiphop = sort_by_genre(ly, 'hip hop')
rock = sort_by_genre(ly, 'rock')
country = sort_by_genre(ly, 'country')
blues = sort_by_genre(ly, 'blues')
jazz = sort_by_genre(ly, 'jazz')
reggae = sort_by_genre(ly, 'reggae')
pop = sort_by_genre(ly, 'pop')


#all words per genre
hiphopwords= " ".join(hiphop['lyrics'])
rockwords= " ".join(rock['lyrics'])
blueswords= " ".join(blues['lyrics'])
countrywords= " ".join(country['lyrics'])
reggaewords= " ".join(reggae['lyrics'])
popwords= " ".join(pop['lyrics'])
jazzwords= " ".join(jazz['lyrics'])

# Genre and Lyrics per song
genre_lyrics = pd.concat([ly['genre'], ly['lyrics']], axis=1)

#Panda dataset Genre: all words in all lyrics
rock_lyrics = lyrics_to_genre(sort_by_genre(ly, 'rock'), 'rock')
hiphop_lyrics = lyrics_to_genre(sort_by_genre(ly, 'hip hop'), 'hip hop')
pop_lyrics = lyrics_to_genre(sort_by_genre(ly, 'pop'), 'pop')
reggae_lyrics = lyrics_to_genre(sort_by_genre(ly, 'reggae'), 'reggae')
jazz_lyrics = lyrics_to_genre(sort_by_genre(ly, 'jazz'), 'jazz')
country_lyrics = lyrics_to_genre(sort_by_genre(ly, 'country'), 'country')
blues_lyrics = lyrics_to_genre(sort_by_genre(ly, 'blues'), 'blues')


#top words per song
top_features(ly['lyrics'], tfidf_vec, 15)

#Creating Topic Columns
lda_topic_matrix = pd.DataFrame(lda.transform(X2)+1)
lda_topic_matrix.rename({0:'topic_1',1:'topic_2',2:'topic_3',3:'topic_4',4:'topic_5'}, 
                        axis=1, inplace=True)


pd.set_option('display.max_columns', None)

final_df = pd.concat([ly, lda_topic_matrix], axis=1)
final_df.drop(['len', 'dating','violence','world/life','night/time', 'shake the audience','family/gospel','romantic',
              'communication', 'obscene','music','movement/places','light/visual perceptions','family/spiritual',
               'like/girls', 'topic', 'age'], axis=1, inplace=True)



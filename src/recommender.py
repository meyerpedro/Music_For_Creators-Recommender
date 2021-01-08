import sys
sys.path.append('./src')
from countvec_cap2 import count_vec
from capstone3 import final_df, lda, cosine_similarity
import pandas as pd
import numpy as np

def percentiles(col, df=final_df):
    a = np.percentile(df[col].values, [25,50,75]).tolist()
    end =[round(i , 5) for i in a]
    return end

a = percentiles('sadness')
b = percentiles('danceability')
c = percentiles('acousticness')
d = percentiles('instrumentalness')
e = percentiles('valence')
f = percentiles('energy')

def song_recommender(df=final_df, num=5):
    
    user_words = input('Enter words:')
    print('\n''Input Parameters from 0 to 1:')
    print('4 or more decimal points recommended for precision.')
    print('If Parameter is null, enter 0''\n')

    print('For Parameter Definitions go to:')
    print('https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/''\n')

    print(f'Sadness Average: {round(final_df.sadness.values.mean(),3)}')
    print(f'Sadness Percentiles:{a}')
    sadness = float(input('Sadness:'))
          
    print('\n'f'Average Danceability: {round(final_df.danceability.values.mean(),3)}')
    print(f'Danceability Percentiles: {b}')
    danceability = float(input('Danceability:'))
          
    print('\n'f'Average Acousticness: {round(final_df.acousticness.values.mean(),3)}')
    print(f'Acousticness Percentiles: {c}')
    acousticness = float(input('Acousticness:'))
          
          
    print('\n'f'Average Valence: {round(final_df.valence.values.mean(),3)}')  
    print(f'Valence Percentiles: {e}')
    valence = float(input('Valence:'))
          
    print('\n'f'Average Energy: {round(final_df.energy.values.mean(),3)}')
    print(f'Energy Percentiles: {f}')
    energy = float(input('Energy:'))
            
    
    user_feature_matrix = count_vec.transform(pd.Series(user_words))
    user_topic = lda.transform(user_feature_matrix)
    
    user = [sadness, danceability, acousticness,valence,energy]
    
    user.extend(user_topic[0])
    user = np.array(user).reshape(1,-1)
        
    cosine_similarities = cosine_similarity(user , df.loc[:,['sadness',
                                                                   'danceability',
                                                                   'acousticness',
                                                                  'valence',
                                                                  'energy',
                                                                  'topic_1',
                                                                  'topic_2',
                                                                  'topic_3',
                                                                  'topic_4',
                                                                  'topic_5']])

    similar_indices = cosine_similarities[0].argsort()[:-(num+1):-1] 
    similar_items = [df.iloc[i] for i in similar_indices] 


    recommender=pd.DataFrame(similar_items)
    return recommender.iloc[:,:5]

print(song_recommender())
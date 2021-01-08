import sys
sys.path.append('./src')
from countvec_cap2 import *
from KMeans import *
from lda import *

ly = pd.read_csv('../data/1950_2019_with lyrics.csv')
ly.drop('Unnamed: 0', axis=1, inplace=True)

def score_per_k(model, y1, y2, y3):
    '''
    plots model score for 3 different values of K

    input:
        model = what model is being tested
        y1, y2, y3 = float - different score values for different k. 
            Calculated by model.score(vectorized_matrix)

    output:
        plot K value per model score
    '''

    fig, ax = plt.subplots(figsize=(10,10), dpi=100)

    ax.plot(y1, 'bo', label='K = 10')
    ax.plot(y2, 'ro', label='K = 12')
    ax.plot(y3, 'ko', label='K = 18')
    ax.set_title(f'{model} Score per K Value')
    ax.legend()
    ax.show()

# LDA Score Plots

# Scores

fig, ax = plt.subplots(figsize=(10,6), dpi=500)

y = pd.Series({'6':13865039.19,
                '8':13879343.457206184,
                '10':13881247.966845043,
                '12':13881881.754632398,
                '15':13868745.58349507,
                '5':13834934.496505208,
                '4':13794715.81973467}).sort_values(ascending=False)


ax.bar(y.keys(), y, alpha=0.7)

ax.set_title('LDA LogLikelihood Score vs K Value')

ax.set_xlabel('K Value', fontsize=13)
ax.set_ylabel('LogLikelihood Score', fontsize=13)


ax.set_yscale('log')

ax.legend()
plt.show()

plt.savefig('../images/lda_score.png')




# Perplexity Score
# fig, ax = plt.subplots(figsize=(10,6), dpi=500)

# y = pd.Series({'4':2018.95,
#                 '5':2064.25,
#                 '6':2098.82,
#                 '8':2115.45,
#                 '10':2117.67,
#                 '12':2118.41}).sort_values(ascending=False)


# ax.bar(y.keys(), y, alpha=0.7, color='purple')

# ax.set_title('LDA Perplexity Score vs K Value')

# ax.set_xlabel('K Value', fontsize=13)
# ax.set_ylabel('Perplexity Score', fontsize=13)


# ax.set_yscale('log')

# plt.savefig('../images/lda_perplexity.png')
# plt.show();

# Learning_decay Score

# fig, ax = plt.subplots(figsize=(10,6), dpi=500)

# y = pd.Series({'0.5':2236.7318894976393,
#                 '1.0':2130.2805347555213,
#                 '0.7':2064.253798134296}).sort_values(ascending=False)


# ax.bar(y.keys(), y, alpha=0.7, color='green')

# ax.set_title('LDA Perplexity Score vs Learning Rate Value')

# ax.set_xlabel('Learning Rate Value', fontsize=13)
# ax.set_ylabel('Perplexity Score', fontsize=13)


# ax.set_yscale('log')

# plt.savefig('../images/lda_learningdecay.png')
# plt.show();

# coding: utf-8

# In[24]:


# Import necessary libraries
import boto3
import pandas as pd 
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

client = boto3.client('dynamodb', region_name='us-east-1')

print('Pandas version', pd.__version__)
print('Numpy version', np.__version__)
print('Seaborn version', sns.__version__)


# In[25]:


# Read datasets from CSVs
df = pd.read_csv('./tmp/ratings.csv')
movieTitles = pd.read_csv('./tmp/movies.csv')



df = pd.merge(df, movieTitles, on='movieId')

# We will create a new dataframe which will have rating for title and number of ratings it received.b

# In[57]:


averageRatingsDf = pd.DataFrame(df.groupby('title')['rating'].mean())
averageRatingsDf['numberOfRatings'] = df.groupby('title')['rating'].count()


# In[58]:


averageRatingsDf = averageRatingsDf.sort_values(['numberOfRatings', 'rating'], ascending=False)


# The above scatter plot clarly shows, that avergae rating of movies goes up with more number of ratings.

# In[60]:


# Data engineering
movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')


# Now, we will iterate in dataset

# In[61]:


for movie in movie_matrix:
    movieTitle = movie_matrix[movie]
    similarityCorr = movie_matrix.corrwith(movieTitle)
    corr_movie_title = pd.DataFrame(similarityCorr, columns=['Correlation'])
    corr_movie_title.dropna(inplace=True)
    # corr_movie_title.join(averageRatingsDf['numberOfRatings'])
    corr_movie_title = pd.merge(corr_movie_title, averageRatingsDf, on='title')
    if (corr_movie_title.size > 0):
        movieRec = corr_movie_title[corr_movie_title['numberOfRatings'] > 50 ].sort_values(by='Correlation', ascending=False).head(10)
        print(movie, movieRec.index.tolist())
        client.put_item(
            TableName='what-to-watch-next',
            Item={
                'movieTitle': {
                    'S': movie
                },
                'recommendations': {
                    'SS': movieRec.index.tolist()
                }
            }
        )
        # averageRatingsDf.to_csv('./output/recommendations.csv')
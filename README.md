# what-to-watch-next
An end-to-end Movie Recommender System

# Links

Project Link:
Blog Link: TBD

# Tech Stack

- Recommender System: Python, pandas
- Web service: Nodejs
- Dataset: Movielens
- AWS: S3, DynamoDB

# Setup

Make sure you have installed these:

- Python3
- nodejs
- have aws iam tokens (and setup in ~/.aws/credentials and ~/.aws/config)

## create-recommendation

### Download dataset from s3

This module will fetch dataset from S3 and create recommendation for every movie and save in dynamodb.

- cd in module
- Make sure you have movie lens dataset somewhere in your s3
- run `cp .env.sample .env` and add the necessary values
- Run `python3 fetch-dataset-from-s3.py`
- You should see files in /tmp/ folder if you have not got any error 

### Create recommendations for movie and save in database

- Then to create a csv of recommendation of every title with ratings, run `python3 create-recommendation.py`
- Created recommendation will get saved in database (dynamodb) and in csv file at 'output/recommendation.csv' (tbd)

## web-service

- Run 
```
npm install 
npm start
```

- run `cp .env.sample .env` and add the necessary values

- Run this endpoint in your browser, `localhost:8080/api/1/movie=<movie-name-of-your-choice>`
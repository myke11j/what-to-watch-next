# what-to-watch-next
An end-to-end Movie Recommender System

# Links

Project Link:
Blog Link: TBD

# Tech Stack

- Recommender System: Python, pandas
- ETL and CRON: Python
- Dataset: Movielens
- AWS: S3
- Deployed using Heroku

# Setup

Make sure you have installed these:

- Python
- Node.js
- have aws iam tokens

## create-recommendation

### Download dataset from s3

- cd in module
- Make sure you have movie lens dataset somewhere in your s3
- run `cp .env.sample .env` and add the necessary values
- Run `python3 fetch-dataset-from-s3.py`
- You should see files in /tmp/ folder if you have not got any error 
- Then to create a csv of recommendation of every title with ratings, run `python3 create-recommendation.py`
- Created recommendation will get saved in database (dynamodb) and in csv file at 'output/recommendation.csv' (tbd)

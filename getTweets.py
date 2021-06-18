import api_keys
import tweepy
import pandas as pd
import re

print("Welcome to Twitter Sentiment Analysis Program\n\n")
print("Enter a string to search for ")
query = str(input())

auth = tweepy.OAuthHandler(api_keys.consumerKey, api_keys.consumerKeyPrivate)
auth.set_access_token(api_keys.accessKey, api_keys.accessKeyPrivate)
api = tweepy.API(auth)

posts = api.search(q=query, count=5, lang="en",
                   result_type="popular", tweet_mode="extended")

df = pd.DataFrame([tweet.full_text for tweet in posts], columns=["Tweets"])


def cleanTweet(tweet):
    tweet = re.sub(r'RT[\s]', '', tweet)
    tweet = re.sub(r'https?:\/\/\S+', '', tweet)
    tweet = re.sub(r'@[a-zA-Z0-9:]+', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    tweet = re.sub(r'[\n]', '', tweet)
    return tweet


df['Tweets'] = df['Tweets'].apply(cleanTweet)

df.to_csv(path_or_buf='data.csv', columns=['Tweets'], index=False, mode='w')

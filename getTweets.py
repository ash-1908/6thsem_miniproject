import api_keys
import tweepy
import pandas as pd
import re

print("Welcome to Twitter Sentiment Analysis Program\n\n")
print("Enter a string to search for ")
query = str(input())
print("What type of tweets to search for? (popular/top/mixed)")
type = str(input())
type = type.lower()
if(type != "popular" and type != "top" and type != "mixed"):
    print("Wrong type entered!")
    exit()
print("Entered the number of tweets to fetch")
count = int(input())
if(count <= 0):
    print("Error: count should be greater than 0")
    exit()

auth = tweepy.OAuthHandler(api_keys.consumerKey, api_keys.consumerKeyPrivate)
auth.set_access_token(api_keys.accessKey, api_keys.accessKeyPrivate)
api = tweepy.API(auth)

posts = api.search(q=query, count=count, lang="en",
                   result_type=type, tweet_mode="extended")

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

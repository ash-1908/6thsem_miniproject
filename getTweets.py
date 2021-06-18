import sentimentAnalysis
import api_keys
import tweepy
import pandas as pd
import re

print("Welcome to Twitter Sentiment Analysis Program\n\n")

query = input("Enter a keyword to search for: ")

flag = 0

while(flag == 0):
    if(len(query) > 500):
        print("Query length too long\nQuery should not be greater than 500 characters!")
    elif(query.isspace()):
        print("\nQuery cannot contains only spaces!")
    elif(len(query) == 0):
        print("\nQuery cannot be empty!")
    else:
        flag = 1
    if(flag == 0):
        query = input("Enter a keyword to search for: ")

type = input("What type of tweets to search for? (popular/top/mixed) ")
type = type.lower()
while(type != "popular" and type != "top" and type != "mixed"):
    print("Wrong type entered!")
    print("What type of tweets to search for? (popular/top/mixed)")
    type = input("What type of tweets to search for? (popular/top/mixed) ")
    type = type.lower()

count = int(input("Entered the number of tweets to fetch"))
while(count <= 0):
    print("Error: count should be greater than 0")
    count = int(input("Entered the number of tweets to fetch"))

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

print("\nData stored in CSV file successfully!")
print("\nPress any key to continue")
input()


sentimentAnalysis.main()

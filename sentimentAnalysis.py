from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

df = pd.read_csv('data.csv')

sentiment = SentimentIntensityAnalyzer()


def getScore(tweet):
    sentences = tokenize.sent_tokenize(tweet)
    total_score = 0.0
    for sentence in sentences:
        score = sentiment.polarity_scores(sentence)
        total_score += score["compound"]
    return total_score


df["Score"] = df["Tweets"].apply(getScore)


def labelSentiment(score):
    if(score >= 0.5):
        return "Very Positive"
    elif(score > 0.05):
        return "Positive"
    elif(score > -0.05 and score < 0.05):
        return "Neutral"
    elif(score < -0.05 and score > -0.5):
        return "Negative"
    else:
        return "Very Negative"


df['Sentiment'] = df['Score'].apply(labelSentiment)

print(df.head())

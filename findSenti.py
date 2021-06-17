from nltk.tokenize import sent_tokenize


def sentimentAnalysis(word):
    # Sentiment Analysis library
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    findSenti = SentimentIntensityAnalyzer()

    # Helper library to clean text
    import re

    # Helping Lirary to divide tweets into sentences
    from nltk import tokenize

    # Helping Library to import tweets from CSV file
    import pandas as pd

    #import tweets
    df = pd.read_csv('data.csv')

    #cleaning tweets
    def cleanTweet(tweet):
        tweet = re.sub(r'RT[\s]', '', tweet)
        tweet = re.sub(r'https?:\/\/\S+', '', tweet)
        tweet = re.sub(r'@[a-zA-Z0-9:]+', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        tweet = re.sub(r'[\n]', '', tweet)

    df['Tweets'] = df['Tweets'].apply(cleanTweet)

    # Performing Sentiment Analysis
        
        # Giving each tweet their sentiment score
    def getSenti(tweet):
        sentences = tokenize.sent_tokenize(tweet)
        sentiment_score = 0.0
        for sentence in sentences:
            score = findSenti.polarity_scores(sentence)
            sentiment_score += score['compound']
        return sentiment_score

    df['Sentiment_Score'] = df['Tweets'].apply(getSenti)
    
        # Labeling the sentiment of each tweet
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

    df['Sentiment'] = df['Sentiment_Score'].apply(labelSentiment)

     
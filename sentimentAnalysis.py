def main():
    from nltk import tokenize
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    from textblob import TextBlob
    import pandas as pd


# ---------------Read tweets from CSV file--------------

    compareLibraries = pd.read_csv('data.csv')
# pandas.read_csv(filepath_or_buffer, sep=<object object>, delimiter=None,
# header='infer', names=None, index_col=None, usecols=None, squeeze=False,
# prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
# true_values=None, false_values=None, skipinitialspace=False, skiprows=None,
# skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True,
# verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False,
# keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False,
# chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None,
# quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None,
# dialect=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False,
# low_memory=True, memory_map=False, float_precision=None, storage_options=None)

    sentiment = SentimentIntensityAnalyzer()


# -------------Sentiment Analysis using VADER----------------


    def getScore(tweet):
        sentences = tokenize.sent_tokenize(tweet)
        total_score = 0.0
        for sentence in sentences:
            score = sentiment.polarity_scores(sentence)
            total_score += score["compound"]
        return total_score

    compareLibraries["VaderScore"] = compareLibraries["Tweets"].apply(getScore)


# ----------------Function to label sentiment score--------------------------


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

    compareLibraries['VaderSentiment'] = compareLibraries['VaderScore'].apply(
        labelSentiment)


# --------------Sentiment Analysis using TextBlob------------------------------


    def getPol(tweet):
        sentences = tokenize.sent_tokenize(tweet)
        total_score = 0.0
        for sentence in sentences:
            score = TextBlob(sentence).sentiment.polarity
            total_score += score
        return total_score

    compareLibraries["TB_Polarity"] = compareLibraries["Tweets"].apply(getPol)

    compareLibraries["TB_sentiment"] = compareLibraries["TB_Polarity"].apply(
        labelSentiment)

    print(compareLibraries)


# -----------Dataframe to store conflicting results---------------------

    diff_result = pd.DataFrame(
        columns=["Tweets", "__Vader Sentiment__", "__TextBlob Sentiment__"])

    for tweet, vd, tb in zip(compareLibraries["Tweets"], compareLibraries["VaderSentiment"], compareLibraries["TB_sentiment"]):
        if(vd != tb):
            lst = [tweet, vd, tb]
            row = pd.Series(lst, index=diff_result.columns)
            diff_result = diff_result.append(row, ignore_index=True)

    row_count = diff_result.shape[0]


# --------------Printing our result-------------------------

    print("\n\n***Comparing Sentiment calculated by VADER library and TextBlob library***\n\n")

    check = diff_result.empty
    if(check):
        print("\n\nThere are no conflicting results!!")
    else:
        print(diff_result)
        print("\n\nTotal different results : " + str(row_count) + "\n")

        ans = input("Inspect a tweet manually? (Yes/No) ")
        ans = ans.lower()

        while(ans != "no"):
            num = int(input("Enter the row number of the tweet to display "))
            print(diff_result["Tweets"][num])
            ans = input("Inspect a tweet manually? (Yes/No) ")
            ans = ans.lower()

    input("\n\nThank You!\n")

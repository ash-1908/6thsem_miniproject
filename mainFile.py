# ----------------Function to find sentiment of user input--------------------
def sentiment(user_input):
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    from nltk import tokenize

    obj = SentimentIntensityAnalyzer()

    sentences = tokenize.sent_tokenize(user_input)

    positivity = 0.0
    negativity = 0.0
    neutrality = 0.0
    overall = 0.0

    for sentence in sentences:
        score = obj.polarity_scores(sentence)
        positivity += score["pos"]
        negativity += score["neg"]
        neutrality += score["neu"]
        overall += score["compound"]

    print("\nUser input was: ", user_input)
    print("\n\nPositivity: ", positivity, ",Negativity: ", negativity,
          ",Neutrality: ", neutrality, ",Compound Score: ", overall)

    overallSentiment = ""

    if(overall <= 1.0 and overall >= 0.85):
        overallSentiment = "Very Positive"
    elif(overall > 0.05):
        overallSentiment = "Positive"
    elif(overall <= 0.05 and overall >= -0.05):
        overallSentiment = "Neutral"
    elif(overall < -0.05 and overall > -0.85):
        overallSentiment = "Negative"
    else:
        overallSentiment = "Very Negative"

    print("\n\nSentiment of paragraph: ", overallSentiment)


# ------------Beginning of the program--------------------------
print("Welcome to Twitter Sentiment Analysis Program")

user_choice = int(
    input("\n\n1. Find Sentiment of User Input\n2. Compare TextBlob and VADER libraries\n3. Exit the program\n\n"))

if(user_choice == 3):
    input("\n\nExiting program...")
    exit()

while(user_choice != 3):
    if(user_choice == 1):
        user_input = input("\n\nEnter a paragraph:\n")
        sentiment(user_input)

    elif(user_choice == 2):
        import getTweets
        getTweets.main()

    elif(user_choice == 3):
        input("\n\nExiting program...")
        exit()

    else:
        print("\n\nWrong choice entered!")

    user_choice = int(
        input("\n\nFind Sentiment of:\n1. User Input\n2. Tweets\n3. Exit the program\n\n"))

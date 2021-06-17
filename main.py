from findSenti import sentimentAnalysis

print("----Twitter Sentiment Analysis Program----")
print("Enter a word to search for:")
word = input()
for space in word:
    if(space == ' '):
        print("Input a single word only")
        print("Enter a word to search for:")
        word = input()

sentimentAnalysis(word)
import textblob
import nltk
import os
#nltk.download('movie_reviews')
#nltk.download('vader_lexicon')


from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

for filename in os.listdir('corpus-python'):
    with open (os.path.join('corpus-python', filename) , "r", encoding='utf-8') as f:
        lines = f.read()
        
    
#print(lines)
    print(os.path.join('corpus-python', filename))
    sentiment1 = TextBlob(lines, analyzer=NaiveBayesAnalyzer())
    sentiment2 = TextBlob(lines)
    print(sentiment1.sentiment)
    print(sentiment2.sentiment)


    #Sentiment Analysis with NLTK
    sia = SIA()
    print ("Sentiment NLTK", sia.polarity_scores(lines))
    print()

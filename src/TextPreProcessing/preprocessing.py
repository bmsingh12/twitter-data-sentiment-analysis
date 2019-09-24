import json
from nltk.tokenize import word_tokenize

from src.TextPreProcessing.tokenize import preprocess

with open('/home/infotmt-user/PycharmProjects/twitterSentimentAnalysis/src/CollectionData/python.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        print(tokens)
        # print(json.dumps(tweet, indent=4))



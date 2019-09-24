import operator
import json
import string

from collections import Counter, defaultdict
from nltk.corpus import stopwords
from nltk import bigrams

from src.TextPreProcessing.tokenize import preprocess

fname = '/home/infotmt-user/PycharmProjects/twitterSentimentAnalysis/src/CollectionData/python.json'
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
# search_word = sys.argv[1]  # pass a term as a command-line argument
count_search = Counter()


with open(fname, 'r') as f:
    count_all = Counter()
    com = defaultdict(lambda: defaultdict(int))
    com_max = []


    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        # terms_all = [term for term in preprocess(tweet['text'])]
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]

        # terms_bigram = bigrams(terms_stop)
        # print(terms_bigram)

        terms_single = set(terms_stop)
        # Count hashtags only
        terms_hash = [term for term in preprocess(tweet['text'])
                      if term.startswith('#')]
        # Count terms only (no hashtags, no mentions)
        terms_only = [term for term in preprocess(tweet['text'])
                      if term not in stop and
                      not term.startswith(('#', '@'))]

        # Build co-occurrence matrix
        for i in range(len(terms_only) - 1):
            for j in range(i + 1, len(terms_only)):
                w1, w2 = sorted([terms_only[i], terms_only[j]])
                if w1 != w2:
                    com[w1][w2] += 1

        # Update the counter
        count_all.update(terms_only)

    # For each term, look for the most common co-occurrent terms
    for t1 in com:
        t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
        for t2, t2_count in t1_max_terms:
            com_max.append(((t1, t2), t2_count))
    # Get the most frequent co-occurrences
    terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)

    # Print the first 5 most frequent words
    print(count_all.most_common(8))
    print("Terms MAX: ", terms_max[:5])

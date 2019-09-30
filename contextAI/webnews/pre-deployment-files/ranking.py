from collections import defaultdict, Counter

def getOccurances(dictionary):

    dict_word_count = defaultdict(int)

    for source, articles in dictionary.items():
        for article in articles:
            for word in article:
                dict_word_count[word[0]] += 1

    return dict_word_count

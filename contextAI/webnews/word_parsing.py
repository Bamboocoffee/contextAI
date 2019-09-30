from nltk import word_tokenize, pos_tag

def tokenize(dictionary):
    """ Tokensize the words in each of the titles. Extract the Nouns and Verbs
    """

    for source, articles in dictionary.items():
        token_articles = []
        for i in articles:
            i = word_tokenize(i)
            token_articles.append(i)

        dictionary[source] = token_articles

    return dictionary


def tag_tokens(dictionary):
    """ Compare the returned words. If they match with any of them, increment that article by 1 score.
    Order them by the scoring.
    """
    try:
        for source, articles in dictionary.items():
            tagged_tokens = []
            for i in articles:
                i = [v.lower() for v in i]
                i = pos_tag(i)
                tagged_tokens.append(i)

            dictionary[source] = tagged_tokens

        return dictionary

    except ValueError:
        return "Error in data structure. Please see the input data type and ensure that the dictionary is Source : Articles[]. \
        Then ensure that the values are tokenized"

def getNouns(dictionary):
    """ Remove all tokens that are not Nouns and return the dictionary
    """

    try:
        for source, articles in dictionary.items():
            clean_articles = []
            for tokens in articles:
                nouns = []
                for token in tokens:
                    if token[1] == "NN" or token[1] == "NNS" or token[1] == "VBG":
                        nouns.append(token)

                clean_articles.append(nouns)

            dictionary[source] = clean_articles

        return dictionary

    except:
        return "Error, the nouns could not be identified. Check the articles"

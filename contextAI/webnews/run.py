from irish_sites import irishTimesScrape, irishIndependantScrape, RTEScrape, journalScrape
from word_parsing import tokenize, tag_tokens, getNouns
from ranking import getOccurances

def irishSites():
    top_headlines = dict()
    top_headlines = irishTimesScrape(top_headlines)
    top_headlines = irishIndependantScrape(top_headlines)
    top_headlines = RTEScrape(top_headlines)
    top_headlines = journalScrape(top_headlines)
    tokenize_top_headlines = tokenize(top_headlines)
    tagged_tokens = tag_tokens(tokenize_top_headlines)
    nouns = getNouns(tagged_tokens)
    print(getOccurances(nouns))

irishSites()


# Articles:
# https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386


# Send the stuff to Ankit
# Rank the articles based on occruances
#

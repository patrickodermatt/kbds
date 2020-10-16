import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    open("files/nlp2/IMDB_1.txt", "r").read(),
    open("files/nlp2/IMDB_2.txt", "r").read(),
    open("files/nlp2/IMDB_3.txt", "r").read()
]

document_names = ['Doc {:d}'.format(i) for i in range(len(documents))]


def get_tfidf(docs, ngram_range=(1, 2), index=None):
    vect = TfidfVectorizer(stop_words='english', ngram_range=ngram_range)
    tfidf = vect.fit_transform(docs).todense()
    return pd.DataFrame(tfidf, columns=vect.get_feature_names(), index=index).T


print(get_tfidf(documents, ngram_range=(1, 2), index=document_names))

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from nltk import tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


def tokenizierung(satz):
    return tokenize.word_tokenize(satz)

def stop_word_removal(satz):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(satz)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    print(word_tokens)
    print(filtered_sentence)

def word_stemming_and_lemmatization(satz):

    stemmer = PorterStemmer()
    lemmatiser = WordNetLemmatizer()

    words = word_tokenize(satz)

    for w in words:
        print("Stem %s: %s" % (w, stemmer.stem(w)))
    for w in words:
        print("Lemmatise %s: %s" % (w, lemmatiser.lemmatize(w)))


if __name__ == '__main__':
    satz = "When Alexander Graham Bell invented the telephone he had three missed calls from Chuck Norris."
    word_stemming_and_lemmatization(satz)


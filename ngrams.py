import nltk, re, string
from nltk.corpus import gutenberg

text = gutenberg.raw('shakespeare-macbeth.txt')

# XML Markup
text = re.sub('<.*>', '', text)

# EOArticle
text = re.sub('ENDOFARTICLE.', '', text)

# Satzzeichen
text_no_sz = "[" + re.sub("\.", "", string.punctuation) + "]"
text = re.sub(text_no_sz, "", text)

tokenized = text.split()

listBigrams = nltk.bigrams(tokenized)
listTrigrams = nltk.trigrams(tokenized)

freq_bi = nltk.FreqDist(listBigrams)
freq_tri = nltk.FreqDist(listTrigrams)

# Print Bigrams
for k, v in freq_bi.items():
    print(k, v)

# Print Trigrams
for k, v in freq_tri.items():
    print(k, v)


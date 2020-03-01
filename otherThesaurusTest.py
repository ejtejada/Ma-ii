import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

syns = wordnet.synsets("Liquid")
print(syns)
print("Dog")

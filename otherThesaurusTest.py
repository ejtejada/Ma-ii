import nltk
nltk.download('wordnet')
searchWord = "liquid";
synonyms = []; #Desired set
antonyms = [];
from nltk.corpus import wordnet
for syn in wordnet.synsets(searchWord):
	for l in syn.lemmas():
		if searchWord.lower() not in l.name().lower():
			synonyms.append(l.name());
			#FIXME remove all words not of the same class as searchWord 
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name());
print(set(synonyms));
#print(set(antonyms));

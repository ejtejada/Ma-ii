import nltk
import random
nltk.download('wordnet');
nltk.download('punkt');
#nltk.download('omw');
#This function should print out one synonym for a searchWord pulled from NLTK. We must also pass the searchType, to only map verbs or nouns to synonyms of the same PoS.
def synGen(searchWord, searchType):
	#searchWord = "table";
	#searchType = "NOUN"; 
	posNumber = "00";
	synonyms = []; #Desired set
	antonyms = [];
	#From NLTK documentation, lets verify searchWord is a part of speech we want to use.
	#_pos_numbers = {NOUN: 1, VERB: 2, ADJ: 3, ADV: 4, ADJ_SAT: 5}
	if searchType == "NOUN":
		posNumber = ".n.";
	elif searchType == "VERB":
		posNumber = ".v.";
	else:
		return searchWord;
		
	from nltk.corpus import wordnet
	for syn in wordnet.synsets(searchWord):
		for l in syn.lemmas():
			if searchWord.lower() not in l.name().lower(): #Ignore synonyms that contain the search word
				if posNumber in str(l):
					synonyms.append(l.name());
					#Sanity Check
					#print(str(l))
				#FIXME remove all words not of the same class as searchWord
				#print(str(l))
			if l.antonyms():
				antonyms.append(l.antonyms()[0].name());
	#print(set(synonyms));
	if len(synonyms) < 1:
		return searchWord; #No synonyms found, return the orignal word quietly.
	chosenWord = str(random.sample(set(synonyms),1)[0]);
	return chosenWord;


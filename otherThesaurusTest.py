import nltk
nltk.download('wordnet');
#nltk.download('omw');

searchWord = "liquid";
searchType = "VERB"; 
posNumber = "00";
synonyms = []; #Desired set
antonyms = [];
#From NLTK documentation
#_pos_numbers = {NOUN: 1, VERB: 2, ADJ: 3, ADV: 4, ADJ_SAT: 5}
if searchType == "NOUN":
	posNumber = "01";
elif searchType == "VERB":
	posNumber = "02";


from nltk.corpus import wordnet


for syn in wordnet.synsets(searchWord):
	for l in syn.lemmas():
		if searchWord.lower() not in l.name().lower():
			if posNumber in str(l):
				synonyms.append(l.name());
			#FIXME remove all words not of the same class as searchWord
			#Sanity Check
			print(str(l))
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name());
print(set(synonyms));
#print(set(antonyms));

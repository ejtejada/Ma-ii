#Authors: Jonathan Contreras, Jacob Gilmartin, and Edgar Tejada.

#See install.sh for install dependencies
import spacy
import random
from synGen import synGen
nlp = spacy.load("en_core_web_sm");

#Adds a random delay between actions within human response time
def randoDelay():
	low = 0.15;
	high = 0.5;
	x = random.uniform(low, high);
	from time import sleep;
	sleep(x);


with open("HUCKFIN_500.txt","r") as myFile:
	data_text = myFile.read();
	whole_text = ''.join(data_text);  #(DO NOT add extra whitespaces between all chars)
	#print(whole_text); 
	myFile.close();
doc = nlp(whole_text);

listWords = []; #Stores words to be tokenized
listPOS = []; #Stores the corresponding type of word, say noun, pronoun, verb, etc.
listDEP = []; #Stores synatical type, like AUX or nsubj (Noun Subject), or 
for token in doc:
	#print(token.text, token.pos_, token.dep_);
	listWords.append(token.text);
	listPOS.append(token.pos_);
	listDEP.append(token.dep_);
print("==========BEFORE===========\n")
print(listWords);
#Add an rnged 1.5 to 3 second delay between EVERY call to synGen
#print(synGen("slipped", "VERB")); #Yay this works

#Noun Subject and Propositional Subject Swap 
for i, word  in enumerate(listWords):
	if listPOS[i] == "NOUN" and (listDEP[i] == "nsubj" or listDEP[i] == "pobj" or listDEP[i] == "dobj"):
		randoDelay(); #Don't overwhelm NLTK's system
		passedWord = synGen(word, listPOS[i]);
		listWords[i] = passedWord;
print("==========AFTER===========\n")
print(listWords);

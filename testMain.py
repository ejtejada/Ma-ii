#Authors: Jonathan Contreras, Jacob Gilmartin, and Edgar Tejada.

#See install.sh for install dependencies
import spacy 
from synGen import synGen
nlp = spacy.load("en_core_web_sm");
with open("HUCKFIN_500.txt","r") as myFile:
	data_text = myFile.read();
	whole_text = ''.join(data_text);  #(DO NOT add extra whitespaces between all chars)
	print(whole_text); 
	myFile.close();
doc = nlp(whole_text);

listWords = []; #Stores words to be tokenized
listPOS = []; #Stores the corresponding type of word, say noun, pronoun, verb, etc.
listDEP = []; #Stores synatical type, like AUX or nsubj (Noun Subject), or 
for token in doc:
	print(token.text, token.pos_, token.dep_);
	listWords.append(token.text);
	listPOS.append(token.pos_);
	listDEP.append(token.dep_);

#print
#Add an rnged 1.5 to 3 second delay between EVERY call to synGen
print(synGen("slipped", "VERB")); #Yay this works

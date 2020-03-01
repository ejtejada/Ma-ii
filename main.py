#Authors: Jonathan Contreras, Jacob Gilmartin, and Edgar Tejada.

#See install.sh for install dependencies
import spacy 

nlp = spacy.load("en_core_web_sm");
with open("HUCKFIN_500.txt","r") as myFile:
	data_text = myFile.read();
	whole_text = ''.join(data_text);  #(DO NOT add extra whitespaces between all chars)
	print(whole_text); 
	myFile.close();
doc = nlp(whole_text);
for token in doc:
    print(token.text, token.pos_, token.dep_)

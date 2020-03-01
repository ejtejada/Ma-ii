from oxforddictionaries.words import OxfordDictionaries

o = OxfordDictionaries.Oxford('856c3f2a', '07289ed24c8110e78b86bb3093c1ca0b')

relax = o.get_synonyms("absorb").json()

synonyms = relax['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']

for s in range(10):
    print(synonyms[s]['text'])

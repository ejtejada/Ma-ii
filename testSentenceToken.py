from nltk.tokenize import sent_tokenize, word_tokenize
#import /media/friendlysicoach/T1000/Documents/Project_Ma-ii/paraphraser/build/lib/paraphraser/inference
import paraphraser

	shortenSent = paraphraser()

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
print(sent_tokenize(data))

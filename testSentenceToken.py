from nltk.tokenize import sent_tokenize, word_tokenize
#import /media/friendlysicoach/T1000/Documents/Project_Ma-ii/paraphraser/build/lib/paraphraser/inference
import paraphraser

shortenSent = paraphraser('train-20180325-001253.tar.gz.tar.gz/model-171856');

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
print(sent_tokenize(data))

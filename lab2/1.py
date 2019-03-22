import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.8)#80%
print(size)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]


import os
from nltk.metrics import *

unigram_tagger = nltk.UnigramTagger(train_sents)
unigram_tagger.tag(train_sents)
word_tag_pairs = nltk.bigrams(train_sents)


ref  = train_sents.split()
tagged = test_sents.split()

print("Precision: ",precision(set(ref),set(tagged)))
# print("Recall: ",recall(set(ref),set(tagged)))
# print("F measure: ",f_measure(set(ref),set(tagged)))
# print("Accuracy: ",accuracy(ref,tagged))

#another way, library, whats the difference?
# from sklearn import metrics
# print(metrics.classification_report(ref, tagged))
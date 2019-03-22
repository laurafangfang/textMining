import nltk
sent = "I saw a boy in the park with a telescope."
taggedS = nltk.pos_tag(nltk.word_tokenize(sent))
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(taggedS)
print(result)
result.draw()

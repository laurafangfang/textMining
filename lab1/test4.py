import nltk
sent = "When I use a telescope, I saw a boy in the park."
# sent = "I use a telescope saw a boy in the park."
taggedS = nltk.pos_tag(nltk.word_tokenize(sent))
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(taggedS)
print(result)
result.draw()

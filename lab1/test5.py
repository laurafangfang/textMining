import nltk
sent = "2.	Interpret the output to determine which of the two interpretations the parser parses the sentence."
taggedS = nltk.pos_tag(nltk.word_tokenize(sent))
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(taggedS)
print(result)
result.draw()
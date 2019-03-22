import nltk

filename = 'test7.txt'
pos = []
myList=[]
with open(filename, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline()
    if not lines:
      break
    taggedS = nltk.pos_tag(nltk.word_tokenize(lines))
    grammar="NP:{<DT>?<JJ>*(<NN>|<NNS>|<NNP>|<NNPS>)+}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(taggedS)
    nTimes = 0
    for subT in result.subtrees():
#        if subT == result:
#            continue
        print (subT)
        # print  ("===========")
        # print (lines)
#        for lea in subT.leaves():
#            # print (lea)
#           # print(lea[0])
#            if ((lea[0]=="The" or lea[0] =="the") and lea[1]=="DT"):
#                # print (lea)
#                for lea1 in subT.leaves():
#                  # print (lea1)
#                    if(lea1[1]=="NNS"):
#                        myList.append(lea1[0])
#                        myList.sort(key=lambda x: x.lower(),reverse=False)
print (myList)
# print ("The number of definite nouns is:", len(myList))
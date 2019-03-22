import nltk
# Get all words in txt file
try:
    fileStr = open('test6.txt', 'r')   
    sent = fileStr.read()                   
finally:
    if fileStr:
        fileStr.close()  
taggedS = nltk.pos_tag(nltk.word_tokenize(sent))
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(taggedS)
NounsCount =0 #init NounsCount=0
NounsStr=[]   #init a list for extracted Nouns words
trueO=False #False: DT is not "The" or "the", True: DT is "The" or "the"

#Get all subtrees(with "NP") from result 
for subTrees in result.subtrees():
    if subTrees==result:
        continue
    print(subTrees)
    # Get one records
    for records in subTrees.leaves():
        # Find "the" or "The" with "DT"
        if records[1]=="DT" and (records[0]=="The" or records[0]=="the"):
            trueO=True
            
        # Process all Nouns words under NP and followed by DT "the" or "The"
        else: 
            if trueO==True:
                if "NN" in records[1]:
                    NounsCount=NounsCount+1
                    NounsStr.insert(0,records[0])
                    trueO=False
    # trueO=False
NounsStr.sort() # sorted the Nouns words String
print("Total number of nouns is: ",NounsCount)
print ("The result of all nouns words in ASCII ASC order is: ",NounsStr)

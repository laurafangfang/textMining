################################################################################################
# 1.sing Brown corpus from NLTK split the corpus into 80% training and 20% for testing for all of the following exercises.
import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.8)#80%
print(size)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
################################################################################################
#2. Instantiate the following taggers from NLTK.
# a.	Unigram tagger
# b.	TnT tagger
# c.	Perceptron tagger
# d.	CRF tagger
import os

unigram_tagger = nltk.UnigramTagger(train_sents)

tnT_tagger = nltk.tag.tnt.TnT()
if (os.path.isfile('tnT_tagger.pkl') == False):
     tnT_tagger.train(train_sents)
perceptron_tagger = nltk.tag.perceptron.PerceptronTagger(train_sents)
if(os.path.isfile('perceptron_tagger.pkl') == False):
    perceptron_tagger = nltk.tag.perceptron.PerceptronTagger(train_sents)
crf_tagger = nltk.tag.CRFTagger()
if(os.path.isfile('crf_tagger.pkl') == False):  
    crf_tagger.train(train_sents,'crf_tagger.pkl')

################################################################################################
#3. Train all of the taggers and store the trained models as a pickle file.
#Store them
from pickle import dump
def dump_file(filename,tagger):
    output = open(filename, 'wb')#将训练好的标注器存到ugTagger.pkl中
    dump(tagger, output, -1)
    output.close()

dump_file('ugTagger.pkl',unigram_tagger)
dump_file('tnT_tagger.pkl',tnT_tagger)
dump_file('perceptron_tagger.pkl',perceptron_tagger)
################################################################################################
#4.	Retrieve the pickle file and test them on the testing data.
#Retrieve it from a file
from pickle import load
def input_file(filename):
    input = open(filename, 'rb')#从文中导入
    tagger = load(input)
    input.close()
    return tagger

ugtagger=input_file('ugTagger.pkl')
tntTagger=input_file('tnT_tagger.pkl')
perceptrontagger=input_file('perceptron_tagger.pkl')
crf_tagger.set_model_file('crf_tagger.pkl')# crf retrieve it


################################################################################################
#5.	Tabulate and compare the accuracies and choose the best one out of the lot. 
# # You can base this choice on the F1 value.
ugtaggerA=ugtagger.evaluate(test_sents)
tnttaggerA=tntTagger.evaluate(test_sents)
perceptronA=perceptrontagger.evaluate(test_sents)
ctfA=crf_tagger.evaluate(test_sents)

print('ugtagger Accuracy is : ',ugtaggerA) #用testing数据进行testing
print('tnt Accuracy is: ',tnttaggerA) #用testing数据进行testing
print('per Accuracy is:',perceptronA) #用testing数据进行testing
print('crf_tagger accuracy is :',ctfA) #用testing数据进行testing




if ugtaggerA >=tnttaggerA:
    bestTagger='ugtagger'
    bestTV=ugtaggerA
    if ugtaggerA>=perceptronA:
        if ugtaggerA>=ctfA:
            print('Best tagger is :', bestTagger, 'accuracy is :',bestTV)    
        else:
            bestTagger='ctfA'
            bestTV=ctfA
    else:
        bestTagger='perceptronA'
        bestTV=perceptronA
else:
    bestTagger='tnttaggerA'
    bestTV=tnttaggerA
print('Best tagger is :', bestTagger, 'accuracy is :',bestTV)    

################################################################################################
# 6.	Use the best tagger to do the following.
# a.	Download 10 news articles from 10 different news sites on a dominant topic of the day. 
# b.	By reading the articles determine at least 3 nouns that best represents the chosen topic. Lets call this set Ƭ 
# c.	Your task is to determine the percentage of nouns in the set Ƭ compared to all nouns in the 10 articles under study. 
import nltk
# Get all words in txt file
try:
    fileStr = open('1.txt', 'r')   
    sent = fileStr.read()                   
finally:
    if fileStr:
        fileStr.close()  
text = nltk.Text(nltk.word_tokenize(sent))
# print(text)
crf_tagger = nltk.tag.CRFTagger()
crf_tagger.set_model_file('crf_tagger.pkl')# crf retrieve it
taggedS=crf_tagger.tag(text)
Counts =0 #init NounsCount=0
NounsC=0   #init a list for extracted Nouns words
trueO=False #False: DT is not "The" or "the", True: DT is "The" or "the"

word_tag_pairs = nltk.bigrams(taggedS)
noun_preceders = [a[0] for (a, b) in word_tag_pairs if  a[1]=='NN']
# print(noun_preceders) #a[0] is the word a[1]is the type
print("\n",noun_preceders.__sizeof__())
fdist = nltk.FreqDist(noun_preceders)
# print(len(fdist))

print('top three frequent noun words are :',fdist.most_common()[0],fdist.most_common()[2],fdist.most_common()[3])
topOne= fdist.most_common()[0][0]
topTwo= fdist.most_common()[1][0]
topThree= fdist.most_common()[2][0]

total_T_noun = int(fdist.most_common()[0][1])+int(fdist.most_common()[1][1])+int(fdist.most_common()[2][1])
# print(total_T_noun)
for i in range(len(fdist)):
    NounsC = NounsC+int(fdist.most_common()[i][1])
print('T set words count is :',total_T_noun,'\nTotally Noun words is : ',NounsC,'\nPercentage of the top 3 noun word of the total words is :',total_T_noun/NounsC)


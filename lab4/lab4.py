import os, sys
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk

#get root path
cPath = sys.path[0]
# list all files in root path
files_in_data = os.listdir(cPath)
#Variable define
person_list =[]
others_list=[]
sentence_number=0
article_number=0
#get "data" path
for data_folder in files_in_data:
    if data_folder == 'data':
        path_data_foler = cPath + '/' + data_folder

print ('1.Current data folder path is :',path_data_foler)
#list txt files
txt_files = os.listdir(path_data_foler)

print ('txt file list : %s' % txt_files)

# get each path for each txt file
files_path = [os.path.join (path_data_foler, txt_file)for txt_file in txt_files]
print (files_path)



def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    print(chunked)

    # extraction of name entities
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity) #continuous_chunk is the set of the named
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk


#read line from txt file
for file_path in files_path:
    if '.txt' in file_path:
        article_number += 1
        files = open(file_path)
        print(files)
        file_text_record = ''.join(file_path)
        while 1:
            line = files.readline()
            # print('line is :', line)
            print (get_continuous_chunks(line))
            sentence_number += 1
            for sent in nltk.sent_tokenize(line):
                for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                    if hasattr(chunk, 'label'):
                        print(chunk.label(), ' '.join(c[0] for c in chunk))
                        if chunk.label() == 'PERSON' or chunk.label() == 'GPE':
                            person_list.append([chunk.label(),' '.join(c[0] for c in chunk),sentence_number,article_number,file_path])
                        else:
                            others_list.append([chunk.label(),' '.join(c[0] for c in chunk),sentence_number,article_number,file_path])     
            if not line:
                sentence_number = 0
                break
    
print ("the loaction and person list : %s" %person_list)
print ("the others chunks : %s" %others_list)
# #############################################################################################################################
# #precision and recall for preson and loation
# the loaction and person list : [['GPE', 'Phillipstown', 1, 1], 
# ['PERSON', 'Ombudsman Peter Boshier', 7, 1]]
# the others chunks : [['ORGANIZATION', 'NZ Herald', 3, 1], ['ORGANIZATION', 'Newcastle St', 3, 1], 
# ['ORGANIZATION', 'Hawke', 5, 1], ['ORGANIZATION', 'Bay Regional Prison', 5, 1], 
# ['ORGANIZATION', 'CCTV', 11, 1], ['ORGANIZATION', 'Mount Eden', 13, 1], 
# ['ORGANIZATION', 'Department', 13, 1],
#  ['ORGANIZATION', 'Corrections', 13, 1], ['ORGANIZATION', 'CCTV', 15, 1]]
#                                 true 
#                         positive    nagetive
# prediction  positive        2           4
#             nagitive        0           5
# Recall = 2/(2+4) = 0.333
# Precision = 2/(2+0) = 1
# F-value = 2 *(Precision * Recall)/(recall + precision) = 2*0.333*1/1.333 = 0.25



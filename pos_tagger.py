def noun_verb (filepath):
    '''given a path of a text file, it returns the pairs of Noun-Phrase+Verb in the text'''
    import nltk
    text = open(filepath, encoding='utf-8').read()
    noun_verb_pairs=[]
    noun_tag =('NN','NNS', 'NNP','NNPS','PRP')
    verb_tag =('VB','VBD','VBG','VBN','VBP','VBZ')
    tokens = nltk.word_tokenize(text)
    tag=nltk.pos_tag(tokens)
    pairs = [(x,y) for x,y in zip(tag[:-1], tag[1:])]
    for x,y in pairs:
        if x[1] in noun_tag and y[1] in verb_tag:
            noun_verb_pairs.append(str(x[0])+' ' +str(y[0]))
    
    return noun_verb_pairs

def adj(filepath):
    '''given a path to a text file it returns the adjectives'''
    import nltk
    from string import punctuation

    adjectives= []
    text = open(filepath, encoding='utf-8').read()
    tokens = nltk.word_tokenize(text)
    tag=nltk.pos_tag(tokens)
    for x,y in tag:
        if y == 'JJ' and x not in punctuation:
            adjectives.append(x)
    return adjectives

def verbs(filepath):
    import nltk
    from string import punctuation

    verbs= []
    verb_tag =('VB','VBD','VBG','VBN','VBP','VBZ')
    
    text = open(filepath, encoding='utf-8').read()
    tokens = nltk.word_tokenize(text)
    tag=nltk.pos_tag(tokens)
    for x,y in tag:
        if y in verb_tag and x not in punctuation:
            verbs.append(x)
    return verbs
def extract_roots(list_):
    '''given a list of words, it returns the words' stems'''
    from nltk.stem import PorterStemmer
    ps = PorterStemmer()

    stems= []
    for w in list_:
        stems.append( ps.stem(w))

    return stems


def distribution(list_, filepath):
    '''given a list of strings, it returns the frequency (in percentage) of each string in the list'''
    import csv
    freq = {}
    for item in list_:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
            
    percentages = [(item, freq[item] / len(list_)) for item in freq]
    #text_1= open(r'C:\Users\user\Desktop\output_perc.txt', 'w', encoding='utf-8')
    with open(filepath, 'w+', newline ='', encoding='utf-8') as f: 
        write = csv.writer(f)
        write.writerows(percentages) 
    #for x,y in percentages:
     #   text_1.write(x +' : '+ str(y) + '\n')

    return percentages [:10]

def spearman_corr(filepath1, filepath2, filepath3):
    import csv
    import scipy
    from scipy import stats
    input_=[]
    output=[]
    fin={}
    fin1={}
    f1 = csv.reader(open(filepath1, encoding='utf-8'))
    f2 = csv.reader(open(filepath2, encoding='utf-8'))


    for row1 in f1:
        input_.append(row1[0])
    for row2 in f2:
        output.append(row2[0])
    print(output[:10])
    print(input_[:10])


    intersection = list(set(input_).intersection(output))
    print(len(intersection))
    #total= input_ + output
    #print(len(total))
    text_1= open(filepath3, 'w', encoding='utf-8')
    for elem in intersection:
        text_1.write(elem + '\n')


    import pandas as pd

    dict1 = {row[0] : row[1] for _,row in pd.read_csv(filepath1, header=None).iterrows()}
    dict2 = {row[0] : row[1] for _, row in pd.read_csv(filepath2, header=None).iterrows()}

    for elem in intersection:
        if elem in dict1:
            fin[elem]=(dict1[elem])
        else:
            fin[elem] = 0

    for elem in intersection:
        if elem in dict2:
            fin1[elem]=(dict2[elem])
        else:
            fin1[elem]=0


    import numpy as np
    an_array = np.array(list(fin.values()))
    another_arr=np.array(list(fin1.values()))
    a= scipy.stats.spearmanr(an_array, another_arr)
    return a
            


    


    



    
    

                
     

    


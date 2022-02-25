def random_changes(filepath, filepath_1, number):
    import random
    from string import ascii_lowercase
    text = open(filepath, encoding='utf-8').read()
    
    inds = [i for i,c in enumerate(text) if not c.isspace() if not c.isnumeric()]
    sam = random.sample(inds, len(text)//number)

    lst = list(text)
    for ind in sam:
        lst[ind] = random.choice(ascii_lowercase)
    rand_modified =  "".join(lst)
    text_1= open(filepath_1, 'w', encoding='utf-8')
    text_1.write(rand_modified)
    return rand_modified

def random_drop(filepath, filepath_1, number):
    import random
    text = open(filepath, encoding='utf-8').read()
    print(len(text))
    inds = [i for i,c in enumerate(text) if not c.isspace() if not c.isnumeric()]
    sam = random.sample(inds, len(text)//number)

    lst = list(text)
    for ind in sam:
        lst[ind] = ''
    rand_modified =  "".join(lst)
    text_1= open(filepath_1, 'w', encoding='utf-8')
    
    text_1.write(rand_modified)
    return rand_modified [:100]

        
def rand_consonant_changes(filepath, filepath_1, number):
    import random
    from string import ascii_lowercase
    text = open(filepath, encoding='utf-8').read()
    vowel_counts = {}
    for vowel in 'aeiouAEIOU':
        count= text.count(vowel)
        vowel_counts[vowel] = count
    print(vowel_counts)
        
    
    inds = [i for i,c in enumerate(text) if not c.isspace() if not c.isnumeric() if c not in 'aeiouAEIOU']
    sam = random.sample(inds, len(text)//number)
    
    consonants_lowercase = ''.join([letter for letter in ascii_lowercase if letter not in 'aeiou'])
    print(consonants_lowercase)
    lst = list(text)
    for ind in sam:
        lst[ind] = random.choice(consonants_lowercase)
    rand_modified =  "".join(lst)
    text_1= open(filepath_1, 'w', encoding='utf-8')
    text_1.write(rand_modified)
    vowel_counts1 = {}
    for vowel in 'aeiouAEIOU':
        count= rand_modified.count(vowel)
        vowel_counts1[vowel] = count
    print(vowel_counts1)
    return rand_modified

def rand_vowels_changes(filepath, filepath_1, number):
    import random
    from string import ascii_lowercase
    text = open(filepath, encoding='utf-8').read()
    cons_counts = {}
    consonants_lowercase = ''.join([letter for letter in ascii_lowercase if letter not in 'aeiou'])
    for cons in consonants_lowercase:
        count= text.count(cons)
        cons_counts[cons] = count
    print(cons_counts)
        
    
    inds = [i for i,c in enumerate(text) if not c.isspace() if not c.isnumeric() if c not in consonants_lowercase]
    sam = random.sample(inds, len(text)//number)
    
    vowel_lowercase = 'aeiou'
    
    
    lst = list(text)
    for ind in sam:
        lst[ind] = random.choice(vowel_lowercase)
    rand_modified =  "".join(lst)
    text_1= open(filepath_1, 'w', encoding='utf-8')
    text_1.write(rand_modified)
    cons_counts1 = {}
    for cons in consonants_lowercase:
        count= rand_modified.count(cons)
        cons_counts1[cons] = count
    print(cons_counts1)
    return rand_modified

def s_drop(filepath, filepath_1, number):
    import nltk
    import random
    from string import ascii_lowercase
    text = open(filepath, encoding='utf-8').read()
    verb_tag =('VB','VBD','VBG','VBN','VBP','VBZ')    
    tokens = nltk.word_tokenize(text)
    tag=nltk.pos_tag(tokens)
    index=-1
    inds=0
    ind=0
    words=[]
    for w, t in tag:
        index+=1
        if t in verb_tag:
            list_= list(w)
            if list_[-1]=='s':
                ind+=1
                if random.random()>number:
                    list_[-1]=''
                    a=''.join(list_)
                    inds+=1
                    tag[index]=(a, t)
    #print(tag[:20])            
    for w,t in tag:
        words.append(w)
    mod_txt= ' '.join(words)
    print(type(mod_txt))
    text_1= open(filepath_1, 'w', encoding='utf-8')
    text_1.write(mod_txt)

    return inds, ind

def s_rand_change(filepath, filepath_1, number):
    import nltk
    import random
    from string import ascii_lowercase
    text = open(filepath, encoding='utf-8').read()
    verb_tag =('VB','VBD','VBG','VBN','VBP','VBZ')    
    tokens = nltk.word_tokenize(text)
    tag=nltk.pos_tag(tokens)
    mod_word=[]
    index=0
    for w, t in tag:
        index += 1
        if t in verb_tag:
            list_= list(w)
            if list_[-1]=='s':
                list_[-1]=random.choice(ascii_lowercase)
                w=''.join(list_)
                tag[index]=w
    #for w,t in tag:
     #   mod_txt=''.join(w)
    #text_1= open(filepath_1, 'w', encoding='utf-8')
    #text_1.write(mod_txt)
                
    return tag 




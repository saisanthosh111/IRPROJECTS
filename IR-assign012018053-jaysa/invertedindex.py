import os
import re
import string
import time
import sys
start = time.time()

def vowel_or_consonant(word,i):
    if word[i] in ["a","e","i","o","u"]:
        return True
    if i-1>0:
        if ((word[i]=="y") and (word[i-1] not in ["a","e","i","o","u"])):
             return True
    return False

def double_consonants(word):
    if len(word)>2:
        if not ((vowel_or_consonant(word,-1) or (vowel_or_consonant(word,-2)))):
                  return True
    return False

def o_form(word):
    if len(word)>=3:
        if ((not (vowel_or_consonant(word,-1) or (vowel_or_consonant(word,-3)))) and(vowel_or_consonant(word,-2))):
            if word[-1] not in ["w","x","y"]:
                  return True
    return False

def check_vc(word):
    required_string=""
    list_vc = []
    for i in range(len(word)):
        if vowel_or_consonant(word,i):
            if i!=0:
                previous = list_vc[-1]
                if previous!='V':
                    list_vc.append('V')
            else:
                list_vc.append('V')
        else:
            if i!=0:
                previous = list_vc[-1]
                if previous !="C":
                    list_vc.append("C")
            else:
                list_vc.append("V")

    for j in list_vc:
        required_string+=j
    return required_string

def word_vowel_check(word):
    for i in range(len(word)):
        if vowel_or_consonant(word,i):
            return True
    return False

def check_mvalue(word):
    vc = check_vc(word)
    return vc.count("VC")

def check_m_0_replace(word,remain,attach):
    x = word.rfind(remain)
    if check_mvalue(word[0:x])>0:
        return word[0:x]+attach
    else:
        return word

def check_m_1_replace(word,remain,attach):
    x = word.rfind(remain)
    if check_mvalue(word[0:x])>1:
        return word[0:x]+attach
    else:
        return word


def step1a(word):
    if word.endswith('sses'):
        word = word.replace('sses','ss')
    elif word.endswith('ies'):
        word = word.replace('ies','i')
    elif word.endswith('ss'):
         word = word.replace('ss','ss')
    elif word.endswith('s'):
        word = word.replace('s', "")
    return word

def step1b(word):
    flag = False

    if word.endswith("eed"):
        if check_mvalue(word[0:-3])>0:
            word = word[0:-3]+"ee"
    elif word.endswith('ed'):
        if word_vowel_check(word[0:-2]):
            word = word[0:-2]
            flag = True
    elif word.endswith("ing"):
        if word_vowel_check(word[0:-3]):
            word = word[0:-3]
            flag = True

    if flag==True:
        if (word.endswith('at') or word.endswith('bl') or word.endswith('iz')):
            word = word + "e"
        elif double_consonants(word) and not word.endswith('l') and not word.endswith('s') and not word.endswith('z'):
            word = word[:-1]
        elif check_mvalue(word)==1 and o_form(word):
            word = word + "e"
    return word

def step1c(word):
    if word.endswith("y"):
        if word_vowel_check(word[0:-1]):
            word = word[0:-1]+"i"
    return word

def step2(word):
    if word.endswith("ational"):
        word = check_m_0_replace(word,"ational","ate")
    elif word.endswith("tional"):
        word = check_m_0_replace(word,"tional","tion")
    elif word.endswith("enci"):
        word = check_m_0_replace(word,"enci","ence")
    elif word.endswith("anci"):
        word = check_m_0_replace(word,"anci","ance")
    elif word.endswith("izer"):
        word = check_m_0_replace(word,"izer","ize")
    elif word.endswith("abli"):
        word = check_m_0_replace(word,"abli","able")
    elif word.endswith("alli"):
        word = check_m_0_replace(word,"alli","al")
    elif word.endswith("entli"):
        word = check_m_0_replace(word,"entli","ent")
    elif word.endswith("eli"):
        word = check_m_0_replace(word,"eli","e")
    elif word.endswith("ousli"):
        word = check_m_0_replace(word,"ousli","ous")
    elif word.endswith("ization"):
        word = check_m_0_replace(word,"ization","ize")
    elif word.endswith("ation"):
        word = check_m_0_replace(word,"ation","ate")
    elif word.endswith("ator"):
        word = check_m_0_replace(word,"ator","ate")
    elif word.endswith("alism"):
        word = check_m_0_replace(word,"alism","al")
    elif word.endswith("iveness"):
        word = check_m_0_replace(word,"iveness","ive")
    elif word.endswith("fulness"):
        word = check_m_0_replace(word,"fulness","ful")
    elif word.endswith("ousness"):
        word = check_m_0_replace(word,"ousness","ous")
    elif word.endswith("aliti"):
        word = check_m_0_replace(word,"aliti","al")
    elif word.endswith("iviti"):
        word = check_m_0_replace(word,"iviti","ive")
    elif word.endswith("biliti"):
        word = check_m_0_replace(word,"biliti","ble")

    return word

def step3(word):
    if word.endswith("icate"):
        word = check_m_0_replace(word,"icate","ic")
    elif word.endswith("ative"):
        word = check_m_0_replace(word,"ative","")
    elif word.endswith("alize"):
        word = check_m_0_replace(word,"alize","al")
    elif word.endswith("iciti"):
        word = check_m_0_replace(word,"iciti","ic")
    elif word.endswith("ful"):
        word = check_m_0_replace(word,"ful","")
    elif word.endswith("ness"):
        word = check_m_0_replace(word,"ness","")
    elif word.endswith("ical"):
        word = check_m_0_replace(word,"ical","ic")
    return word

def step4(word):
    if word.endswith("al"):
        word = check_m_1_replace(word,"al","")
    elif word.endswith("ance"):
        word = check_m_1_replace(word,"ance","")
    elif word.endswith("ence"):
        word = check_m_1_replace(word,"ence","")
    elif word.endswith("er"):
        word = check_m_1_replace(word,"er","")
    elif word.endswith("ic"):
        word = check_m_1_replace(word,"ic","")
    elif word.endswith("able"):
        word = check_m_1_replace(word,"able","")
    elif word.endswith("ible"):
        word = check_m_1_replace(word,"ible","")
    elif word.endswith("ant"):
        word = check_m_1_replace(word,"ant","")
    elif word.endswith("ement"):
        word = check_m_1_replace(word,"ement","")
    elif word.endswith("ment"):
        word = check_m_1_replace(word,"ment","")
    elif word.endswith("ent"):
        word = check_m_1_replace(word,"ent","")
    elif word.endswith("ou"):
        word = check_m_1_replace(word,"ou","")
    elif word.endswith("ism"):
        word = check_m_1_replace(word,"ism","")
    elif word.endswith("ate"):
        word = check_m_1_replace(word,"ate","")
    elif word.endswith("iti"):
        word = check_m_1_replace(word,"iti","")
    elif word.endswith("ous"):
        word = check_m_1_replace(word,"ous","")
    elif word.endswith("ive"):
        word = check_m_1_replace(word,"ive","")
    elif word.endswith("ize"):
        word = check_m_1_replace(word,"ize","")
    elif word.endswith("ion"):
        if check_mvalue(word[0:-3])>1 and ((word[0:-3]).endswith("s") or (word[0:-3]).endswith("t")):
            word = word[0:-3]
    return word

def step5a(word):
    if word.endswith("e"):
        if check_mvalue(word[0:-1])>1:
            word = word[0:-1]
        elif check_mvalue(word[0:-1])==1 and not o_form(word[0:-1]):
            word = word[0:-1]
    return word

def step5b(word):
    if check_mvalue(word)>1 and double_consonants(word) and word.endswith("l"):
        word = word[0:-1]
    return word

def stemming(word):
        word = step1a(word)
        word = step1b(word)
        word = step1c(word)
        word = step2(word)
        word = step3(word)
        word = step4(word)
        word = step5a(word)
        word = step5b(word)
        return word

def frequency_count(tokens):
    frequency_dictionary={}
    for token in tokens:
        if token not in frequency_dictionary:
            frequency_dictionary[token]=0
        frequency_dictionary[token]+=1
    return frequency_dictionary

def frequency_words(data):
    tokens = []
    for token_list in data.values():
        tokens = tokens + token_list
#     print(len(tokens))
    fdist = frequency_count(tokens)
#     for i in fdist.items():
#         print(i)
#     print(len(fdist.values()))
    return list(fdist.keys())


def inverted_index(preprocessed_data):
    words = frequency_words(preprocessed_data)
    index = {}
    for word in words:
        for doc, tokens in preprocessed_data.items():
            if word in tokens :
                if word in index.keys():
                    index[word].append(doc)
                else:
                    index[word] = [doc]
    return index

def stemmed_tokens(token_filter):
#     creating stemming without using nltk
    stemmed_words = [stemming(token) for token in token_filter]
    return stemmed_words

def rem_stop_words(tokens):
#     remoing the stop words
    stop_words=['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there',
                'about','once','during','out','very','having','with', 'they', 'own',
                'an', 'be', 'some', 'for', 'do', 'its','yours','such','into','of','most',
                'itself','other','off','is','s','am','or','who','as','from','him','each',
                'the','themselves','until','below','are','we','these','your','his','through',
                'don','nor','me','were','her','more','himself','this', 'down','should',
                'our','their','while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she',
                'all','no','when','at','any','before','them','same','and','been','have',
                'in','will','on','does','yourselves','then','that','because','what','over',
                'why', 'so','can','did', 'not','now', 'under','he','you','herself','has',
                'just','where','too','only','myself','which','those','i','after', 'few',
                'whom', 't', 'being','if', 'theirs', 'my','against','a','by','doing', 'it',
                'how', 'further', 'was', 'here', 'than']
    token_filter = [token for token in tokens if token not in stop_words and len(token) > 2]
    return token_filter


def tokenise(content):
#     tokenisation like removing punchuation and other etc.
    remove_punctuation = str.maketrans("","",string.punctuation)
    modified_data = content.translate(remove_punctuation)
    modified_data = modified_data.replace('”',"")
    modified_data = modified_data.replace('“',"")
    modified_data = modified_data.replace('’',"")
    modified_data = modified_data.replace('‘',"")
    modified_data = ''.join([i for i in modified_data if not i.isdigit()])
    x=modified_data.strip()
    z=x.split()
#     print(y)

#     if "cannot" in modified_data:
#         print("hii")
#     for i in y:
#         if i not in z:
#             print(i)

    return z

def read_data(path):
    contents = []
    for file_name in os.listdir(path):
        data = open(path+'\\'+file_name,encoding="utf8").read()
#         getting the doc id if any text is there removed
        data=data.lower()
        file_name = re.sub('\D',"",file_name)
#         creating a docid and data dicionary and it takes complexity of o(m) for rading all the files in the directory
        contents.append((int(file_name),data))
    return contents

def preprocess_data(data):
    term_dictionary = {}
    for content in data:
        tokens = tokenise(content[1])
        token_filter = rem_stop_words(tokens)
#         print(token_filter)
        stemmed_words = stemmed_tokens(token_filter)
        token_filter1 = rem_stop_words(stemmed_words)
        term_dictionary[content[0]]=token_filter1
    return term_dictionary

if __name__=="__main__":
#     path to the corpus directory
    path = "D:\\Downloads\\th-dataset"
#     reading the data
    data = read_data(path)
#     preprocessing the data
    preprocessed_data = preprocess_data(data)
#     generating an inverted index
    invertedindex = inverted_index(preprocessed_data)

#     It is taking an O(n)complexity where n is number of different words for printing
#       i am uing a dictionary here

    orig_stdout = sys.stdout
    f = open('output.txt', 'a', encoding='utf-8')
    sys.stdout = f
    for i in invertedindex:
        x=[]
        invertedindex[i].sort()
        for j in invertedindex[i]:
            p = str(j)
            q = preprocessed_data[j].count(i)
            x.append(p+"="+str(q))
        print("{0} ({1})==> {2}".format(i,str(len(invertedindex[i])),x))
    sys.stdout = orig_stdout
    f.close()
end = time.time()
print(f"Runtime of the program is {end - start}")

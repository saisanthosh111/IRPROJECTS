import re
from itertools import product

class SpellChecker(object):
    def Counter(self,words):
            x = {}
            for word in words:
                if word not in x:
                    x[word]=0
                else:
                    x[word]+=1
            return x

    def __init__(self,path):
         with open(path,"r",encoding="utf8") as f:
                lines = f.readlines()
                words = []
                for line in lines:
                    words+=re.findall(r'\w+',line.lower())
                self.vocabulary = set(words)
                self.word_count = self.Counter(words)
                total_words_count = float(sum(self.word_count.values()))
                self.word_probs= {word:self.word_count[word]/total_words_count for word in self.word_count.keys()}
                
    def numberofduplicates(self,string, index):
            initial = index
            last = string[index]
            while index+1 < len(string) and string[index+1] == last:
                index += 1
            return index-initial

    def reductions(self,word):
        word = list(word)
        for index,i in enumerate(word):
            n = self.numberofduplicates(word, index)
            if n>1:
                flat_list = [i*(r+1) for r in range(n+1)][:3]
                for j in range(n):
                    word.pop(index+1)
                word[index] = flat_list
        for p in product(*word):
            yield ''.join(p)
            
    def list_reductions(self,word):
        x=[]
        for j in self.reductions(word):
            x.append(j)
        return x
    
    def vowelinsertion(self,word):
        vowels = ["a","e","i","o","u"]
        word = list(word)
        for idx, l in enumerate(word):
            if type(l) == list:
                pass                
            elif l in vowels:
                word[idx] = list(vowels)
        for p in product(*word):
                yield ''.join(p)
    
    def list_voweladded(self,word):
        x=[]
        for j in self.vowelinsertion(word):
            x.append(j)
        return x
    
    def both_reduction_vowel(self,word):
        x=[]
        for j in self.both(word):
            x.append(j)
        return x
    
    def both(self,word):
        for reduction in self.reductions(word):
            for variant in self.vowelinsertion(reduction):
                yield variant
#     edit distance one using peter norvigs algorithm
    def edit_distance_one(self,word):
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        split  = [(word[:i],word[i:]) for i in range(len(word)+1)]
        delete = [a+b[1:] for a,b in split if b]
        insert = [a + c + b for a,b in split for c in letters]
        replace = [a + c + b[1:] for a,b in split if b for c in letters]
        swap = [a + b[1] + b[0] + b[2:] for a,b in split if len(b)>1]
        return set(delete+swap+replace+insert)
    
    def edit_distance_two(self,word):
        return set(e2 for e1 in self.edit_distance_one(word) for e2 in self.edit_distance_one(word))
    
    def check(self,word):
        a=self.list_voweladded(word)
        b=self.list_reductions(word)
        c=self.edit_distance_one(word)
        d=self.edit_distance_two(word)
        e=[word] 
        f=self.both_reduction_vowel(word)
        suggestion = set(a)|set(b)|set(c)|set(d)|set(e)|set(f)
        suggest = list(suggestion)
        best_guesses = [w for w in suggest if w in self.vocabulary]
        return sorted([(c,self.word_probs[c]) for c in best_guesses],key=lambda tup: tup[1],reverse = True)
    
if __name__=="__main__":
    #path to the file which is used as a vocabulary
    path = "C:\\Users\\Santhosh\\Desktop\\pdfs1\\big1.txt"
    checker = SpellChecker(path)
    word = input("Enter the mistaken word to know the correct words\n")
#     checking the entered word in the vocabulary
    if word in checker.vocabulary:
        print("The entered word {} is the correct word".format(word))
    else:
#         checking for the correct word
        words = checker.check(word)
        if len(words)==0:
#             if no word exixts in the library
            print("The given word {} is not found in the vocabulary".format(word))
        else:
#             the correct word with maximum probability
            print("The correct word of given word in the vocabulary is {}".format(words[0][0]))
    
    print("-----------------------------TestCases-----------------------------------------------------")
    words = ["peson","lve","jon","acces","evironment","prty","scientist","pocorn","hppy","tor","empre","sigt","fligt","contor","sessin","phne","brd","frind","grl","wrng","bat","belive"]
    for i in words:
        x = checker.check(i)
        if len(x)>0:
            print("{}---predicted---{}".format(i,x[0][0]))
       
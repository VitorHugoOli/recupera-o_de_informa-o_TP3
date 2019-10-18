import nltk
import string
nltk.download('stopwords')
nltk.download('punkt')

class InvertedIndex:
    def __init__(self):
        self.indexInv = {}
        self.raiz = []
    
    def __preprocess__(self, message, lang):
        stop_words = nltk.corpus.stopwords.words(lang)
        stemmer = nltk.stem.PorterStemmer()
        message = [char for char in message if char not in string.punctuation]
        message = ''.join(message)
        message = message.lower()
        tokens = nltk.tokenize.word_tokenize(message)
        tokens = [token for token in tokens if len(token)>2]
        tokens = [token for token in tokens if token not in stop_words]
        tokens = [stemmer.stem(token) for token in tokens]
        return tokens
    
    def insert(self, doc):
        if doc not in self.raiz:
            self.parse(len(self.raiz),doc)
            self.raiz.append(doc)
            return True
        else:
            print("Texto já foi inserido anteriomente")
            return False
    
    def parse(self, idoc, doc):
        words = self.__preprocess__(doc, 'portuguese')
        for w in words:
            if w in self.indexInv:
                if idoc in self.indexInv[w]:
                    self.indexInv[w][idoc] = self.indexInv[w][idoc] + 1
                else:
                    self.indexInv[w][idoc] = 1
                    
            else:
                self.indexInv[w] = {}
                self.indexInv[w][idoc] = 1
                
    def search(self, word):
        if word in self.indexInv:
            return self. indexInv[word]
        else:
            return []
    
    def multisearch(self, phrase, sortedByRelevance=True):
        words = self.__preprocess__(phrase, 'portuguese')
        for i in range(len(words)):
            if i == 0:
                group = self.search(words[i])
            else:
                groupAux = {}
                group2 = self.search(words[i])
                for g in group:
                    if g in group2:
                        if  type(group[g]) is int:
                            groupAux[g] = [group[g]]
                            groupAux[g].append(group2[g])
                        else:
                            groupAux[g] = group[g]
                            groupAux[g].append(group2[g])
                group = groupAux
        relevance = self.__relevancecalc__(group)
        print(group, relevance)
        sortedByRel = self.__sortedByRelevance__(group, relevance)
        if sortedByRelevance == True:
            return sortedByRel, relevance
        else: return group, relevance
    
    def __relevancecalc__(self, dic):
        rel = {}
        for d in dic:
            calc = 0
            if type(dic[d]) is list:
                for i in range(len(dic[d])):
                    calc = calc + pow(dic[d][i], len(dic[d])-i)
                calc = pow(calc, 1/len(dic[d]))   
                
            else:
                calc = dic[d]
            rel[d] = calc
        return rel
    
    def __sortedByRelevance__(self, group, relevance):
        sortedDic = {}
        for item in sorted(group, key = relevance.get, reverse=True):
            sortedDic[item] = group[item]
        return sortedDic
    
    def printd(self):
        print(self.indexInv)
    
    
'''
arq = open('teste', 'r')
texto1 = [arq.read()]
arq = open('teste2', 'r')
texto2 = arq.read()
arq = open('teste3', 'r')
texto3 = arq.read()
#print(texto)

index = IndiceInvertido()
index.insert(texto1)
index.insert(texto2)
index.insert(texto3)
group, relevance = index.multisearch("cadeira filho colegas")
print(group, relevance)


#index.printd()

'''
import datetime

import nltk
import string

from treatmentFile.models.models import Texto, indexInv, DictWord
from django.core.exceptions import ObjectDoesNotExist

nltk.download('stopwords')
nltk.download('punkt')

class InvertedIndex:
    def __init__(self):
        self.dictRepTexo = {}
        # self.raiz = []

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

    def insert(self, doc,title):
        # if doc not in self.raiz:
        if Texto.objects.filter(texto=doc).exists():
            print("Texto já foi inserido anteriomente")
            return False
        else:
            id = Texto.objects.create(texto=doc, titulo=title)
            self.parse(id.id, doc,title)
            return True

    def parse(self, idoc, doc,title):
        words = self.__preprocess__(doc, 'portuguese')
        # indexinvertido = indexInv.objects.filter()
        #Carregando lista de palavras já existentes no banco para otimização da função
        # wordsBD = []
        # for i in indexinvertido:
        #     wordsBD.append(i.word)
        # print(wordsBD)

        print("Step 1 - Create dynamic wordBD")
        print("Amounts of words: " + str(len(words)))
        words.append(title.split(".")[0])
        print(words)
        print("------Start Time: " + str(datetime.datetime.now().time()))

        for w in words:
            try:
                indexinvertido = indexInv.objects.get(word=w)

                try:
                    dicionario = DictWord.objects.get(indexInv=indexinvertido, idTexto=idoc)
                    dicionario.repeticoes= dicionario.repeticoes + 1
                    dicionario.save()

                except ObjectDoesNotExist:
                    DictWord.objects.create(indexInv=indexinvertido, idTexto=idoc, repeticoes=1)


            except ObjectDoesNotExist:
                index = indexInv.objects.create(word=w)
                DictWord.objects.create(indexInv=index, idTexto=idoc, repeticoes=1)

        print("------End Time: " + str(datetime.datetime.now().time()))
        print("\nStep 2 - All words were inclued")

    def search(self, word):
        # if word in self.indexInv:
        if indexInv.objects.filter(word=word).exists():
            dicTextRepetition = {}
            palavra = indexInv.objects.get(word=word)
            dicPalavras = DictWord.objects.filter(indexInv=palavra)
            for i in dicPalavras:
                dicTextRepetition[i.idTexto] = i.repeticoes
            return dicTextRepetition
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

    # def printd(self):
    #     print(self.indexInv)

    def retornaText(self,i):
        return Texto.objects.get(id=i)
    
    
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
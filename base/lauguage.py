# coding: utf-8

from nltk.probability import FreqDist
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

import re
import os

wordsSaveDir = os.getcwd() + "/words/"
allWordsFile = "__all.txt"

def getStopWords():
    sw = stopwords.words('english')
    file = open(os.getcwd() + "/stopWords.txt", "r")
    words = file.read().split("\n")
    file.close()
    sw.extend(words)
    return sw

class Language:

    tokens = None
    
    def __init__(self, content):
        self.text = self.rawContent = content
        # self.text = re.sub(r'[^a-zA-Z0-9\s]','', string= self.rawContent)

    def wordFrequancyToFile(self, moduleName, spiderName):
        file = open(wordsSaveDir + moduleName + "_" + spiderName + ".txt", "w")
        
        words = self.wordFrequancy()
        for word in words:
            file.write(str(word[0]))
            file.write("\t")
            file.write(str(word[1]))
            file.write("\n")
        file.close()
        
    def wordFrequancy(self):
        return self.fdist().most_common()

    def getTaggedSent(self):
        tokens = word_tokenize(self.text)
        return pos_tag(tokens)

    def fdist(self):

        # 词性还原
        wnl = WordNetLemmatizer()
        lemmas_sent = []
        for tag in self.getTaggedSent():
            wordnet_pos = self.get_wordnet_pos(tag[1]) or wordnet.NOUN
            lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))

        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(' '.join(lemmas_sent))

        fd = FreqDist()
        StopWords = getStopWords()
        for word in tokens:
            if re.match("\d+", word):
                continue
            lowerWord = word.lower()
            if lowerWord not in StopWords and len(lowerWord) > 1:
                fd[lowerWord] += 1

        return fd

    # 词性
    def get_wordnet_pos(self, tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

def mergeAllFile():
    files = os.listdir(wordsSaveDir)

    vocabulary = {}
    StopWords = getStopWords()

    for fileName in files:
        if not fileName.endswith(".txt") or fileName == allWordsFile:
            continue

        file = open(wordsSaveDir + fileName, "r")
        content = file.read()
        content = content.strip().split("\n")

        for line in content:
            tmp = line.split("\t")
            if len(tmp) < 2:
                continue
            if not vocabulary.__contains__(tmp[0]):
                vocabulary[tmp[0]] = 0
            vocabulary[tmp[0]] += int(tmp[1])

    file = open(wordsSaveDir + allWordsFile, "w")
    
    vocabulary = sorted(vocabulary.items(),  key=lambda w: w[1], reverse=True)
    for word in vocabulary:
        if word[0] in StopWords:
            continue
        file.write(str(word[0]))
        file.write("\t")
        file.write(str(word[1]))
        file.write("\n")
    file.close()
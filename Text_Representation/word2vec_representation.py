

 
# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import gensim
from gensim.models import Word2Vec


sample = open("C:\\Users\\Admin\\Desktop\\alice.txt", "utf8")
s = sample.read()
 
f = s.replace("\n", " ")
 
data = []
 
for i in sent_tokenize(f):
    temp = []
    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower())
 
    data.append(temp)

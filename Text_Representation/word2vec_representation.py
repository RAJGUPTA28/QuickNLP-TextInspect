

 
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


model1 = gensim.models.Word2Vec(data, min_count = 1, 
                              vector_size = 100, window = 5)




# Other Method

import gensim
w2v_model = gensim.models.Word2Vec(min_count=1, window=2, size=300, sample=6e-5, alpha=0.03, min_alpha=0.0007, negative=20)
w2v_model.build_vocab(input_data)
w2v_model.train(input_data, total_examples=w2v_model.corpus_count, epochs=50)
w2v_model.wv.most_similar(positive=["Robert"])


# Applications of Word Embedding :

>> Sentiment Analysis
>> Speech Recognition
>> Information Retrieval
>> Question Answering

# Techniques Used
------

- Bag of words Represensation
- TF -IDF Representation
- Bi-Gram
- Tri-Gram
- n-Gram
- Word2vec
- BERT
- Sentence Transformer (Hugging Face)


# BOW 
  - Read the dataset
  - Create the subset of 50 records
  - Extract the text from the dataset
  - Convert the extracted texts into list of texts
  - Apply Pre process function to lowercase and stopwords removal
  - Crating bag of words model using count vectorizer
  - Apply fit and transform on list of processed texts obtained on step 5
  - Convert the bag of words matrix to pandas dataframe by assigning all the vocabs as the column of the dataframe
 ![IMG](https://github.com/RAJGUPTA28/QuickNLP-TextInspect/blob/main/Text_Representation/img/bow.png)

# WORD2VEC
Word2Vec creates vectors of the words that are distributed numerical representations of word features – these word features could comprise of words that represent the context of the individual words present in our vocabulary. Word embeddings eventually help in establishing the association of a word with another similar meaning word through the created vectors.
word2vec is not a singular algorithm, rather, it is a family of model architectures and optimizations that can be used to learn word embeddings from large datasets. Embeddings learned through word2vec have proven to be successful on a variety of downstream natural language processing tasks.
These vectors capture information about the meaning of the word and their usage in context. The word2vec algorithm estimates these representations by modeling text in a large corpus.

# TF IDF
TF-IDF stands for Term Frequency Inverse Document Frequency of records. It can be defined as the calculation of how relevant a word in a series or corpus is to a text. The meaning increases proportionally to the number of times in the text a word appears but is compensated by the word frequency in the corpus (data-set).

- **Term Frequency**: In document d, the frequency represents the number of instances of a given word t. Therefore, we can see that it becomes more relevant when a word appears in the text, which is rational. Since the ordering of terms is not significant, we can use a vector to describe the text in the bag of term models. For each specific term in the paper, there is an entry with the value being the term frequency.

- **Inverse Document Frequency**: Mainly, it tests how relevant the word is. The key aim of the search is to locate the appropriate records that fit the demand. Since tf considers all terms equally significant, it is therefore not only possible to use the term frequencies to measure the weight of the term in the paper.

 ![IMG](https://github.com/RAJGUPTA28/QuickNLP-TextInspect/blob/main/Text_Representation/img/tfidf.webp)

 # SENTENCE TRANSFORMERS
 Pretrained Model converts Text to Embeddings
  - **All Models**
 ![img](https://github.com/RAJGUPTA28/QuickNLP-TextInspect/blob/main/Text_Representation/img/SENT_MODEL.png)


# N-Gram Representation

N-grams are continuous sequences of words or symbols, or tokens in a document. In technical terms, they can be defined as the neighboring sequences of items in a document. They come into play when we deal with text data in NLP (Natural Language Processing) tasks. They have a wide range of applications, like language models, semantic features, spelling correction, machine translation, text mining, etc.

- n	Term
- 1	Unigram
- 2	Bigram
- 3	Trigram
- n	n-gram


“I reside in Bengaluru”.

| SL.No.|	Type of n-gram	 |   Generated n-grams|
| 1	| Unigram |	[“I”,”reside”,”in”,”Bengaluru”]|
| 2	| Bigram	| [“I reside”,”reside in”,”in Bengaluru”]|
| 3	| Trigram	| [“I reside in”, “reside in Bengaluru”]|

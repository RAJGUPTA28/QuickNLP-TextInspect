# importing all necessary libraries
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
#setting max width to show all columns in dataframe
pd.set_option('max_colwidth', 100)

# building bag of words model on three sentences
documents = ["Machine learning uses historical data to predict output values.", 
             "It is seen as a part of artificial intelligence.",
             "Machine learning programs can perform tasks without being explicitly programmed to do so."]
print(documents)

def preprocess(document):
   #changes document to lower case and removes stopwords'

    # change sentence to lower case
    document = document.lower()

    # tokenize into words
    words = word_tokenize(document)

    # remove stop words
    words = [word for word in words if word not in stopwords.words("english")]

    # join back words to make sentence
    document = " ".join(words)
    
    return document

documents = [preprocess(document) for document in documents]
print(documents)


vectorizer = CountVectorizer()
bow_model = vectorizer.fit_transform(documents)
print(bow_model)  # returns the rows and column number of cells which have 1 as value

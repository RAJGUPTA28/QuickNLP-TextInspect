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

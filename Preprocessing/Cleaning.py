#import required packages
#basics
import pandas as pd 
import numpy as np

import nltk
nltk.download('averaged_perceptron_tagger')

#viz
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud ,STOPWORDS
from PIL import Image


#nlp
import string
import re    #for regex
import nltk

from nltk.tokenize import word_tokenize



import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Clean Text
def clean_text(text):
#replace the html characters with " "
    text=re.sub('<.*?>', ' ', text)  
    
#remove the punctuations
    text = text.translate(str.maketrans(' ',' ',string.punctuation))
    
#consider only alphabets and numerics
    text = re.sub('[^a-zA-Z]',' ',text)  
    
#replace newline with space
    text = re.sub("\n"," ",text)
    
#convert to lower case
    text = text.lower()
    
#split and join the words
    text=' '.join(text.split())
    return text

def lemmatize_words(text):
    words = text.split()
    words = [lemmatizer.lemmatize(word,pos='v') for word in words]
    return ' '.join(words)







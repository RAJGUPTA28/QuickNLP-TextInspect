
from sklearn.feature_extraction.text import TfidfVectorizer

d1 = 'Geeks'
d2 = 'r2j'

string = [d0, d1]


tfidf = TfidfVectorizer()
result = tfidf.fit_transform(string)

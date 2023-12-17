
from sklearn.feature_extraction.text import TfidfVectorizer

d1 = 'Geeks'
d2 = 'r2j'

string = [d0, d1]


tfidf = TfidfVectorizer()
result = tfidf.fit_transform(string)

print('\nidf values:')
for ele1, ele2 in zip(tfidf.get_feature_names(), tfidf.idf_):
	print(ele1, ':', ele2)

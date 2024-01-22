# 1. Number of Characters
def count_chars(text):
    return len(text)

# 2. Number of words
def count_words(text):
    return len(text.split())

# 3. Count Capital Letter
def count_capital_chars(text):
    count=0
    for i in text:
        if i.isupper():
            count+=1
    return count


# 5.Count Numberr of Puncuation
def count_punctuations(text):
    punctuations='!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
    d=dict()
    for i in punctuations:
        d[str(i)+' count']=text.count(i)
    return d 

# 6.Number of Sentences
def count_sent(text):
    return len(nltk.sent_tokenize(text))

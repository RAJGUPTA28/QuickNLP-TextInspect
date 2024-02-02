# Part of speech Tagging
import nltk
from nltk.tokenize import word_tokenize

text = word_tokenize("Shakespeare was born and raised in Stratford-upon-Avon, Warwickshire. At the age of 18, he married Anne Hathaway, with whom he had three children: Susanna and twins Hamnet and Judith.")
nltk.pos_tag(text)
# part of speech

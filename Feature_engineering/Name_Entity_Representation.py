import spacy
from spacy import displacy

doc = nlp('Shakespeare was born and raised in Stratford-upon-Avon, Warwickshire. At the age of 18, he married Anne Hathaway, with whom he had three children: Susanna and twins Hamnet and Judith.')

displacy.render(doc, jupyter=True, style='ent')

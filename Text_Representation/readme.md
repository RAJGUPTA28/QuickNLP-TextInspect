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
Extract the text from the dataset
Convert the extracted texts into list of texts
Apply Pre process function to lowercase and stopwords removal
Crating bag of words model using count vectorizer
Apply fit and transform on list of processed texts obtained on step 5
Convert the bag of words matrix to pandas dataframe by assigning all the vocabs as the column of the dataframe

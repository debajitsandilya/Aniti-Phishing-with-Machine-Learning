#! C:/Users/Piyush's PC/AppData/Local/Programs/Python/Python36/python.exe


from sklearn.externals import joblib
import pickle
import sys

import re,math
from collections import Counter
import nltk, string, numpy
nltk.download('punkt') # first-time use only
stemmer = nltk.stem.porter.PorterStemmer()

url_fetched = sys.argv[2]

print("\t"+"the url is %s" % url_fetched )

text_read_good = sys.argv[3]

text_read_bad = sys.argv[4]

file_1= "pickel_model.pkl"

with open(file_1, 'rb') as f1:  
   
    logistic_regression = joblib.load(f1)
    
f1.close()

file_1 = "pickel_vector.pkl"

# tokenization method for the URL
def sanitization(web):                      
    web = web.lower()
    token = []
    dot_token_slash = []
    raw_slash = str(web).split('/')
    for i in raw_slash:
        raw1 = str(i).split('-')            # removing slash to get token
        slash_token = []
        for j in range(0,len(raw1)):
            raw2 = str(raw1[j]).split('.')  # removing dot to get the tokens
            slash_token = slash_token + raw2
        dot_token_slash = dot_token_slash + raw1 + slash_token # all tokens
    token = list(set(dot_token_slash))      # to remove same words  
    if 'com' in token:
        token.remove('com')                 # remove com
    return token


with open(file_1, 'rb') as f2:  
    
    vectorizer = joblib.load(f2)

f2.close()

vectorizer = vectorizer
url_list= []
url_list.append(url_fetched)
x = vectorizer.transform(url_list)

y_predict = logistic_regression.predict(x)
print("identified as %s" % y_predict)
print("\n")

#append all words to list
documents= [text_read_good, text_read_bad]

#word processing and tokenization
def StemTokens(tokens):
     return [stemmer.stem(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def StemNormalize(text):
     return StemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
     
nltk.download('wordnet') 
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
     return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

from sklearn.feature_extraction.text import CountVectorizer
LemVectorizer = CountVectorizer(tokenizer=LemNormalize, stop_words='english')

LemVectorizer.fit_transform(documents)
tf_matrix = LemVectorizer.transform(documents).toarray()

from sklearn.feature_extraction.text import TfidfTransformer
tfidfTran = TfidfTransformer(norm="l2")
tfidfTran.fit(tf_matrix)


import math
def idf(n,df):
    result = math.log((n+1.0)/(df+1.0)) + 1
    return result

tfidf_matrix = tfidfTran.transform(tf_matrix)

print(tfidf_matrix.toarray())
import numpy as np

cos_similarity_matrix = (tfidf_matrix * tfidf_matrix.T).toarray()

print(cos_similarity_matrix)
#importing tfidvectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
def cos_similarity(textlist):
    tfidf = TfidfVec.fit_transform(textlist)
    return (tfidf * tfidf.T).toarray()


cos_similarity_matrix= cos_similarity(documents)
print("cosine similarity")
print(cos_similarity_matrix)



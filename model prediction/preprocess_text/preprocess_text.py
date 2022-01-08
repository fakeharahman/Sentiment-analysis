import re
from nltk.stem.snowball import SnowballStemmer
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import pickle
snow_stemmer = SnowballStemmer(language='english')
from tensorflow.keras.preprocessing.text import Tokenizer
import os
import pathlib

def clean_text(text):
    text=re.sub(r'@[A-Za-z0-9]+', "", text) #removes mentions
    text=re.sub(r'https?://[A-Za-z0-9./]+', "", text) #removes links
    text=re.sub("[^a-zA-Z]", " ", text) # removes #
    text = re.sub('\n', '', text) # removes new line
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # remove punctuation marks
    text=re.sub(' +', ' ', text) # remove more than on espace
    text= text.lower()
    text=[word for word in text.split(" ") if word not in stopwords.words('english') ] #removes stopwrds
    text=" ".join(text)
    text=[snow_stemmer.stem(word) for word in text.split(" ")] # gets root of word
    text=" ".join(text)
    print(text)
    return text

def tokenize_text(text):
    tokenizer=Tokenizer(num_words=50000)
    abspath = pathlib.Path("tokenizer.pickle").absolute()
    print(abspath)
    with open('C:\\Users\Fakeha Rahman\Desktop\Sentiment Analysis\model prediction\preprocess_text\\tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    sequence=tokenizer.texts_to_sequences([text])
    return sequence
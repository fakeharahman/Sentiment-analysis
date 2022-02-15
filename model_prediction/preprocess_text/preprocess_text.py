from asyncio.windows_events import NULL
import re
from nltk.stem.snowball import SnowballStemmer
import string
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
# python -m nltk.downloader stopwords
import pickle
snow_stemmer = SnowballStemmer(language='english')
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
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
    # print(text)
    return text

tokenizer=NULL
def tokenize_text(text):
    max_words=50000 #No of distinct words allowed
    max_len=300 #max len of tweet
    tokenizer=Tokenizer(num_words=max_words)
    # abspath = pathlib.Path("tokenizer.pickle").absolute()
    # print(abspath)
    #change here to absolute path
    #read about packaging python projects
    
    with open('C:\\Users\Fakeha Rahman\Desktop\Sentiment Analysis\model_prediction\preprocess_text\\tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    sequences=tokenizer.texts_to_sequences([text])
    sequences=sequence.pad_sequences(sequences, maxlen=max_len)
    return sequences
import numpy as np
import pickle
import tensorflow as tf
from keras.utils import pad_sequences
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
import re
import string

model1 = tf.keras.models.load_model('./model_training/model1.h5')
model2 = tf.keras.models.load_model('./model_training/model2.h5')
token = pickle.load(open('model_training/token.pickle','rb'))


def remove_stopwords(text):
    tokens = []
    for token in text.split():
        if token not in stop:
            tokens.append(token)
    return " ".join(tokens)


def remove_URL(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', text)


def remove_html(text):
    html = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    return re.sub(html, '', text)


def remove_punct(text):
    table = str.maketrans('', '', string.punctuation)
    return text.translate(table)


def predict(x):
    remove_stopwords(x)
    remove_URL(x)
    remove_html(x)
    remove_punct(x)
    x=token.texts_to_sequences([x])
    x=pad_sequences(x,maxlen=200,padding='pre')
    result = model2.predict(x)[0]
    index = np.argmax(result,axis=0)
    cat = ['LIFESTYLE AND WELLNESS','POLITICS','PARENTING AND EDUCATION','SPORTS AND ENTERTAINMENT','TRAVEL-TOURISM & ART-CULTURE','EMPOWERED VOICES','BUSINESS-MONEY','WORLDNEWS','ENVIRONMENT','SCIENCE AND TECH','GENERAL','MISC']
    return (cat[index],model1.predict(x)>0.5)
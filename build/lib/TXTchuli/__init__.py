

__version__ = '0.1'
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pyttsx3
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from collections import Counter
from gtts import gTTS
import jieba
import pseg
import jieba.posseg as pseg
from collections import defaultdict
import vaderSentiment
import wordcloud
import vaderSentiment
__all__ = '__version__', 'nltk', 'pyttsx3', 'matplotlib', 'collection', 'gtts', 'jieba', 'pseg', 'collections','wordcloud','vaderSentiment'

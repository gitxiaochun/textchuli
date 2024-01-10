from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pyttsx3
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from collections import Counter
from gtts import gTTS
import jieba.posseg as pseg
import jieba
import vaderSentiment
class yuyin:
    def yuyinbofang(file_name):
        # 读取本地文本文件
        engine = pyttsx3.init()  # 初始化语音合成引擎
        txt = file_name
        with open(txt , "r", encoding="utf-8") as file:
            text = file.read()        
        # 要说出的文本内容
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(text)
        engine = pyttsx3.init()  # 初始化语音合成引擎
        if sentiment_scores['compound'] > 0.05:
            speed = 150
        elif sentiment_scores['compound'] < -0.05:
            speed = 60
        else:
            speed = 120
            # 初始化语音引擎
        engine = pyttsx3.init()
            # 设置发音速度
        engine.setProperty('rate', speed)
            # 设置没有口音的语音包为默认语音
        voices = engine.getProperty('voices')   
        engine.say(text)  # 让引擎说出文本内容
        engine.runAndWait()  # 等待引擎完成当前任务并停止执行后续代码
    def yuyinluzhi(file_name,savefill):
        # 读取本地文本文件
        txt = file_name
        with open(txt, "r", encoding="utf-8") as file:
            text = file.read()
        # 要说出的文本内容
        tts = gTTS(text,lang='zh-cn')
        tts.save(savefill+".mp3")
  
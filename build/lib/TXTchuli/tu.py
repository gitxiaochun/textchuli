from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from collections import Counter
import vaderSentiment
class tu:
    def fenxitu(file_name):
        txt = file_name
        # 读取本地文本文件
        with open(txt, "r", encoding="utf-8") as file:
            text = file.read()
        # 初始化情感分析器
        sia = SentimentIntensityAnalyzer()
        # 分析文本情感
        sentiment_scores = sia.polarity_scores(text)
        plt.bar(['Positive', 'Neutral', 'Negative'], [sentiment_scores['pos'], sentiment_scores['neu'], sentiment_scores['neg']])
        plt.xlabel('Sentiment')
        plt.ylabel('Score')
        plt.title('Sentiment Analysis of Text')
        plt.show()
    def ciyuntuzi(file_name):
        # 读取本地文本文件
        txt = file_name  
        with open(txt, "r", encoding="utf-8") as file:
            text = file.read()
        # 计算词频
        word_freq = Counter(text)
        # 创建词云对象
        wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", width=800, height=600).generate_from_frequencies(word_freq)
        # 显示词云图               渲染
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
    def ciyuntuci(file_name):
        # 读取本地文本文件
        txt = file_name  
        with open(txt, "r", encoding="utf-8") as file:
            text = file.read()
        # 创建词云对象
        wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", width=800, height=600).generate(text)
        # 显示词云图               渲染
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()


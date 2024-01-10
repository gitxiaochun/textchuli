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
class fengcichuli:
    def fengci(file_name,fencileixing,fuhao):
        # 读取本地文本文件
        txt = file_name
        with open(txt, "r", encoding="utf-8") as file:
            text = file.read()
        # 判断语句进行分词分词
        if fencileixing=='nltk':
            fencileixing = word_tokenize(text)
            print('分词结果',fencileixing)
        elif fencileixing=='jieba(精确)':
            fencileixing = jieba.cut(text,cut_all=False)
            print("精确模式：", fuhao.join(fencileixing))
        elif fencileixing=='jieba(全)':
            fencileixing = jieba.cut(text,cut_all=True)
            print("全模式：", fuhao.join(fencileixing))
        elif fencileixing=='jieba(搜索)':
            fencileixing = jieba.cut_for_search(text)
            print("搜索引擎模式：", fuhao.join(fencileixing))
        else:
            print('暂无该分词模式,重新输入')
fengcichuli.fengci('text.txt','nltk',None)
class tingyongci:
    def yingwen(file_name,yesorno,savefile):
        # 读取本地文本文件
        txt = file_name
        with open(txt, "r", encoding="utf-8") as file:
            text = file.read()
        # 定义一个包含常见停用词的列表
        stop_words = set(stopwords.words('english'))
        # 分词
        word_tokens = word_tokenize(text)
        # 过滤停用词
        filtered_text = [word for word in word_tokens if word.lower() not in stop_words]        
        print("去除停用词后的文本："+" ".join(filtered_text))
        if yesorno=='yes':
            with open(savefile, "w") as file:
                file.write(filtered_text)    
    def zhongwen(file_name,yesorno,savefile):
        # 读取本地文本文件
        txt = file_name
        # 加载停用词列表
        stop_words = set(["的", "地", "得", "和"])
        with open(txt, "r", encoding="utf-8") as file:
            text = file.read()
        # 分割文本为单词列表
        # words = text.split()
        # 使用jieba进行分词
        seg_list = jieba.cut(text)
        # 去除停用词
        filtered_words = [word for word in seg_list if word not in stop_words]
        # 将处理后的单词列表重新组合成文本内容
        filtered_text = " ".join(filtered_words)
        print('去除停用词以后的文本:'+(filtered_text))
        if yesorno=='yes':
            # 写入到新文件中
            with open(savefile, "w") as file:
                file.write(filtered_text)
class cixingbiaozhu:
    def yingwen(file_name):
        # 读取本地文本文件
        txt = file_name
        with open(txt , "r", encoding="utf-8") as file:
            text = file.read()        
        # NLTK进行英文词性标注
        tokenized = word_tokenize(text)
        tagged = nltk.pos_tag(tokenized)
        print(tagged) 

    def zhongwen(file_name):
        # 读取本地文本文件
        txt = file_name
        with open(txt, "r", encoding="utf-8") as file:
            text = file.read()
        words = pseg.cut(text)
        pos_count = defaultdict(int)
        for word, flag in words:
            pos_count[flag] += 1
            print('%s %s' % (word, flag))
        print(pos_count)
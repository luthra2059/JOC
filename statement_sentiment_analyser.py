# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:56:25 2019

@author: om8007 (https://github.com/om8007)
"""


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()
statement = input("Enter statement: ")

ss = sid.polarity_scores(statement)

for k in ss:
    print(k,ss[k])

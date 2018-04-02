# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 18:58:50 2018 by Meena Sirisha"""

import urllib.request
import re

url = "https://www.sec.gov/Archives/edgar/data/3662/0000889812-99-003241.txt"

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
respData
theText = respData.decode()
theText

r = re.findall("\nITEM \d+\. MANAGEMENT'S DISCUSSION AND ANALYSIS .*?(?:\nITEM|\nPART)", theText,re.S)
r

import nltk

from nltk.tokenize import word_tokenize
w1=word_tokenize(r)
len(w1)

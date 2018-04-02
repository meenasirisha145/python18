# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 11:42:36 2018 by Meena Sirisha"""

import requests #used for calling url
import csv
from bs4 import BeautifulSoup  #converts the text into structured form

page=requests.get("https://www.sec.gov/Archives/edgar/data/3662/0000889812-99-003241.txt")
type(page)
data=str(page.content)
type(data)

import re
r = re.findall("\nITEM \d+\. MANAGEMENT'S DISCUSSION AND ANALYSIS .*?(?:\nITEM|\nPART)", data,re.S)
r
data.find("ITEM 7")
data1=data[10000:]
data1.find("ITEM 7")
data1.find("ITEM 8")
data1

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:22:54 2018 by Meena Sirisha"""
import numpy as np
import pandas as pd
import math
import requests #used for calling url
import csv
from bs4 import BeautifulSoup  #converts the text into structured form

data=pd.read_csv('F:\pywork\pyWork\pyProjects\pythonbasic\Assignment\cik_list.csv')
data
data.columns.values

urls=data.SECFNAME.tolist()
urls
type(urls)

from urllib.parse import urlencode

url1="https://www.sec.gov/Archives/"

type(url1)
links=[]
for url in urls:
    links.append(url1+url)

links

pages=[]
for link in links:
    page=requests.get(link)
    pages.append(page)


pages[0]
pages[0].content

soups=[]
for pag in pages:
    soup = BeautifulSoup(pag.text,'html.parser')
    soups.append(soup)


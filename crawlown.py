# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:20:37 2018 by Meena Sirisha"""

import requests #used for calling url
import csv
from bs4 import BeautifulSoup  #converts the text into structured form

page=requests.get("https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2017")
page
soup = BeautifulSoup(page.text,'html.parser')
soup

tables=soup.find_all("table")


for table in tables:
    print(table.get("id"))
    if(table.get("id")=="data"):
        for row in table.find_all("tr"):
            for col in row.find_all("td"):
                print(col.contents[0],end=" ")

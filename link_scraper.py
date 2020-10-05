#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:10:53 2020

@author: tapli
"""

from requests import get
url = input('Website link:')
response = get(url)


from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
a_tag = html_soup.findAll('a')

links = []
for c in a_tag:
    link = c.get('href')
    links.append(link)
        

import pandas as pd
df = pd.DataFrame({'links': links})
print(df)
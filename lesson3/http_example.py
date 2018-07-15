# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:39:55 2018

"""
import urllib.request
from bs4 import BeautifulSoup

html_doc = urllib.request.urlopen("http://www.google.com").read()

print(html_doc)

soup = BeautifulSoup(html_doc)

print(soup.title)
print(soup.title.name)
print(soup.title.string)

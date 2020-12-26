# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 18:50:26 2020

@author: Giannela HC
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("./driver/chromedriver.exe")

titulo_comic = []

driver.get("https://xkcd.com/archive/")

content = driver.page_source

soup = BeautifulSoup(content,'html.parser')

titulos = soup.find('div',id='middleContainer').find_all('a')
for t in titulos:
    titulo_comic.append(t.text.strip())
    
archivo = pd.DataFrame({'TituloComic':titulo_comic})
archivo.to_csv('comic.csv', index = False)
print(archivo)
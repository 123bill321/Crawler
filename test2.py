import sys
import requests
import re
import urllib2
import shutil
from bs4 import BeautifulSoup
link = "https://apkpure.com/art_and_design"

def Get_apk_information(temps):
    #temps = soup.find_all("div", attrs={"class": "category-template-title"})
    for i in temps:
        temp = i.find_all(href=True)
        temp_2 = temp[0]['href']
        temp_2 = "https://apkpure.com" + temp_2

        res2 = requests.get(temp_2)
        soup2 = BeautifulSoup(res2.text,"html.parser")
        temps_2 = soup2.find_all('ul', {'class': 'version-ul'})
        temp = temps_2[0].find_all('p')
        print temp[3].text,' ',temp[5].text,' '

        temps_3 = soup2.find_all('span', {'class': 'fsize'})
        temp = temps_3[0].text
        temp = temp.replace('(','')
        temp = temp.replace(')','')
        print temp,'\n'

res = requests.get(link)
soup = BeautifulSoup(res.text,"html.parser")#parser the page
temps = soup.find_all("div", attrs={"class": "category-template-title"})
Get_apk_information(temps)

import sys
import requests
import re
import urllib2
import shutil
from bs4 import BeautifulSoup


res = requests.get("https://apkpure.com/kinemaster-%E2%80%93-pro-video-editor/com.nexstreaming.app.kinemasterfree")
soup = BeautifulSoup(res.text,"html.parser")
temps = soup.find_all('ul', {'class': 'version-ul'})
temp = temps[0].find_all('p')
print temp[3].text,'\n',temp[5].text#Latest Version,Publish Date:
temps = soup.find_all('span', {'class': 'fsize'})
temp2 = temps[0].text
temp2 = temp2.replace('(','')
temp2 = temp2.replace(')','')
print temp2#Latest Version,Publish Date:

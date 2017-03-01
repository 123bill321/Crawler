# -*- coding: UTF-8 -*-
import sys
import os
import requests
import re
import urllib2
import shutil
from bs4 import BeautifulSoup

dictObj ={'vt_scan': 'null','submit_date':'null','source':'apkpure.com','title':'null',
'sub_title':'null','name':'null','rank':'null','pgname':'null','version':'null',
'size':'null','upload_date':'null','apkdata':'null','normal_permission':'null','danger_permission':'null',
'sha1':'null','sha256':'null','ssdeep':'null','md5':'null'}

#download file by link and rename
def Download_link(link, file_name,rank):
    dictObj['name'] = file_name
    dictObj['rank'] = rank+1
    file_name = file_name + ".apk"#add the filename extesion after the file_name
    res = requests.get(link)#Connect to the apk download page
    soup = BeautifulSoup(res.text,"html.parser")#parser the apk download link
    temps_name = soup.find_all("a", attrs={"class": "ga"})
    for i in temps_name:#key = r
        #print i['href']
        r = requests.get(i['href'], stream=True)#get url and download through https
        dictObj['apkdata'] = r
        if r.status_code == 200:
            with open(file_name, 'wb') as f:#rename apk file
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

def Get_apk_information(temps_name):
    for i in temps_name:
        temp = i.find_all(href=True)
        temp_2 = temp[0]['href']
        temp_2 = "https://apkpure.com" + temp_2

        res2 = requests.get(temp_2)
        soup2 = BeautifulSoup(res2.text,"html.parser")
        temps_2 = soup2.find_all('ul', {'class': 'version-ul'})
        temp = temps_2[0].find_all('p')
        dictObj['version'] = temp[3].text
        dictObj['upload_date'] = temp[5].text
        temps_3 = soup2.find_all('span', {'class': 'fsize'})
        temp = temps_3[0].text
        temp = temp.replace('(','')
        temp = temp.replace(')','')
        dictObj['size'] = temp
#---------------------------------------------------------------

#get apk name
def Get_apk_name_and_link(apk_topic):
    dictObj['title'] = apk_topic
    apk_topic = "https://apkpure.com"+ apk_topic #Connect to the apk page
    res = requests.get(apk_topic)
    soup = BeautifulSoup(res.text,"html.parser")#parser the page
    temps_name = soup.find_all("div", attrs={"class": "category-template-title"})
    Get_apk_information(temps_name)

    #print dictObj
    #find all apk's informations in this page


    app_name = []#store the apk's name
    for i in temps_name:
        temp = i.find_all(title=True)
        temp_2 = temp[0]['title']
        temp_2 = temp_2.replace(" ","_")#replace the space to underline
        app_name.append(temp_2)

    #get apk download link
    app_downlink = []#store the apk's link
    temps = soup.find_all("div", attrs={"class": "category-template-down"})
    for i in temps:
        temp = i.find_all(href=True)
        temp2 = "https://apkpure.com" + temp[0]['href']
        #add a header in front of the href
        app_downlink.append(temp2)

    for i in range(len(app_name)):
        Download_link(app_downlink[i],app_name[i],i)


if __name__ == '__main__':
    res = requests.get("https://apkpure.com/app")
    soup = BeautifulSoup(res.text,"html.parser")
    temps = soup.find_all('ul', {'class': 'index-category cicon'})
    # get apk category
    apk_category = []
    for i in temps[1].find_all('li'):
        temp = i.find_all(href=True)
        Get_apk_name_and_link(temp[0]['href'])

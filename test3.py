import sys
import requests
import re
import urllib2
import shutil
from bs4 import BeautifulSoup
import tempfile
import os
d = {'file':""}
# temp = "https://apkpure.com/vidmate-hd-video-downloader-live-tv/com.nemo.vidmate"
# temp = temp.split("/")
# print temp[4]

r = requests.get("https://download.apkpure.com/b/apk/Y29tLmFwa3B1cmUuYWVnb25fODg1X2NkYTJlYTM2?_fn=QVBLUHVyZV92MS4yLjdfYXBrcHVyZS5jb20uYXBr&k=6b4760655d80fc619a4367a82036f64b58ba1fcf&as=3ec5904925577686209d76c42194a6f658b77d47&_p=Y29tLmFwa3B1cmUuYWVnb24%3D&c=1%7CTOOLS", stream=True)#get url and download through https
if r.status_code == 200:
    with open("123.apk", 'wb') as f:#rename apk file
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
f = open('123.apk', 'r')
d['file'] = f.read()
print type(d['file']),'   ',len(d['file'])

if os.path.exists("123.apk"):
    try:
         os.remove("123.apk")
    except OSError, e:
        print ("Error: %s - %s." % (e.filename,e.strerror))
else:
    print "file not found!"

import sys
import requests
import re
import urllib2
import shutil
from bs4 import BeautifulSoup
d = {'a':'0'}
f = open('Textgram - write on photos APK.2.2.apk', 'r')
d['a'] = f.read()

print type(d['a'])

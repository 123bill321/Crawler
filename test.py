import sys
import requests
import re
import urllib2
import shutil
from bs4 import BeautifulSoup
import hashlib
import ssdeep
f = open('test2.py', 'r')
temp = f.read()
#hash1 = ssdeep.hash(temp)
#m = hashlib.sha256()
m = hashlib.sha1()
m.update(temp)
print m.hexdigest()
# m = hashlib.md5()
# f = open('test2.py', 'r')
# temp = f.read()
# m.update(temp)
# print m.hexdigest()
# print m.digest()

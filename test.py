import os
import sys
import re
from URL_and_IP_check import *

# temp = "xmlns:stEvt=\"http://ns.adobe.com/xap/1.0/sType/ResourceEvent"
file_name = "Textgram\ write\ on\ photos_v3.0.10_apkpure.com.apk"
temp = []
pattern = r'http.*'
# temp = Find_URL("ColourGo_-_Coloring_book_APK.apk")
# match = re.search(pattern,temp)
# print match.group()
#-------------------------------------------------------------
# cmd = r'strings -a %s | grep -i "http"' %file_name
# temp = subprocess.check_output(cmd,shell=True)
# temp_string = ''
# for i in temp:
#     if i == ' ':
#         match = re.search(pattern,temp_string)
#         if match:
#             print match.group()
#         temp_string = ''
#     else:
#         temp_string += i


l1 = ['b','c','d','b','c','a','a']
l1 = list(set(l1))
print l1

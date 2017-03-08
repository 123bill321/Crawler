import os
import sys
import subprocess
import re
# file_name = "virus.apk"

def Find_URL(file_name):
    URL_list = []#store URL set
    cmd = r'strings -a %s | grep -i "http"' %file_name
    pattern = r'http.*'
    #use cmd to find the raw which including "http"
    try:
        temp = subprocess.check_output(cmd,shell=True)
        #received the result from the cmd
    except subprocess.CalledProcessError as e:
        # raise except if cmd don't found any raw which including the keyword
        return URL_list #return empty list
    # put the string into list
    temp_string = ''
    for i in temp:
        if i == ' ':
            match = re.search(pattern,temp_string)
            if match:
                URL_list.append(match.group())
            temp_string = ''
        else:
            temp_string += i
    URL_list = list(set(URL_list))
    return URL_list

def Find_IP_address(file_name):
    cmd = r'strings -a %s | grep "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}"' %file_name
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    IP_list = []
    try:
        temp = subprocess.check_output(cmd,shell=True)
    except subprocess.CalledProcessError as e:
        # URL_list.append("NULL")
        return IP_list

    temp_string = ''
    for i in temp:
        if i == '\n':
            #filter IP
            match = re.search(pattern,temp_string)
            if match :
                IP_list.append(match.group())
            temp_string = ''
        else:
            temp_string += i

    IP_list = list(set(IP_list))
    return IP_list
def main():
    # file_name = "virus.apk"
    temp = Find_IP_address("virus.apk")
    print temp
    temp = Find_URL("virus.apk")
    print temp
if __name__ == '__main__':
    main()

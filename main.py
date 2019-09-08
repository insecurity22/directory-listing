# -*- coding: utf-8 -*-
import sys
import re
import requests
from bs4 import BeautifulSoup # beautifulsoup4

def help(usage): # sys.argv[0], argv
    print('Usage: ./' + usage)
    sys.exit(1)

# ex) http://demo.testfire.net/login/login.jsp
def get_urldirectorypath(url):
    current_pagep = '\/[a-zA-Z0-9]*\.[a-zA-Z0-9]*$'  # ex) /login.php
    path = re.sub(current_pagep, "", url)  # ex) domain/login
    print("Path = " + path)
    return path

def return_souporhtml(url, str):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    if(str=="soup"):
        return soup
    elif(str=="html"):
        return soup.text

def regex_search(regex, str):
    p = re.compile(regex)
    s = p.search(str)
    return s

if __name__ == '__main__':
    if(len(sys.argv)!=2):
        usage = "main url"
        help(usage)

    url = str(sys.argv[1])
    path = get_urldirectorypath(url)

    html = return_souporhtml(path, "html")
    s = regex_search('Index of /', html)
    if s == None:
        print("\n***** This website is \"SAFE\" from Directory listing")
    else:
        print("\n***** This website is \"RISK\" from Directory listing")

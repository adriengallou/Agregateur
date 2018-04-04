#!/usr/bin/python
#encoding = "utf-8"

from pattern.web import DuckDuckGo, SEARCH, plaintext

engine = DuckDuckGo(license=None,throttle=0.5, language='en')

query = raw_input("Mot clef:")

for result in engine.search(query, type=SEARCH, start=1):
    print ("URL:"+result.url)
    print ("TITLE:"+result.title)
    print ("TEXT:"+result.text)
    print ("LANGUAGE:"+result.language)
    print ("AUTHOR:"+result.author)
    print ("DATE:"+result.date)
    print (" ")

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:32:37 2020

@author: Hanna Szczepanek
"""


from lxml  import html
import requests



def transcription():
    words = input('Type or paste your sentence(s) below:\n')
    words_list = words.split()
    print("getting your transcription ready, please wait")
    
    for word in words_list:
        page = requests.get('https://dictionary.cambridge.org/dictionary/english/' + str(word))
        tree = html.fromstring(page.content)
        Words = tree.xpath('//span[@class="ipa dipa lpr-2 lpl-1"]/text()')
        word1 = Words[0]
        print(word1)
transcription()

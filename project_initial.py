# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:32:37 2020

@author: Hanna Szczepanek
"""
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from multiprocessing import Pool

def ipa(sentences):
    print('Getting your transcription ...')

    dic_url='https://dictionary.cambridge.org/dictionary/english/ist'
    dic_content = get_content(dic_url)
    
    links = dic_content.find_all('a')    

    urls = []

    for link in links:
        if len(link.get_text()) > 1:
            base_url = 'https://dictionary.cambridge.org'
            url= urllib.parse.urljoin(base_url, link['href'])
            encoded_url = fix_encoding(url)
            urls.append(encoded_url)
    
    print('Your transcription: ')    
    
def transcription():
    sentences = input('Type or paste your sentence(s) below:\n')
    ipa(sentences)

def fix_encoding(url):
    components = urllib.parse.urlsplit(url)
    components = list(components)
    components[2] = urllib.parse.quote(components[2])
    return urllib.parse.urlunsplit(components)
 
def get_content(url):
    response = urllib.request.urlopen(url)
    data= response.read()
    doc = BeautifulSoup(data, 'html.parser')
    return doc.find(id = 'tresc_wlasciwa')    

transcription()
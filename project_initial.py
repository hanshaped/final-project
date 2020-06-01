# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:32:37 2020

@author: black
"""
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from multiprocessing import Pool

def transcription():
    sentences = input('Type or paste your sentence(s) below:\n')
    print(sentences)
    
transcription()
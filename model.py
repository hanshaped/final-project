# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:42:49 2020

@author: black
"""

from lxml  import html
import requests

class Model:
    def __init__(self, controller):
        self.controller = controller
        
    def transcribe(self, words):
        transcription = self.get_transcription(words)
        self.controller.handle_transcription(transcription)
        
        
    def get_transcription(self, words):
        # words = input('Type or paste your sentence(s) below:\n')
        words_list = words.split()
        print("Getting your transcription ready, please wait")
        transcribed_words = ""
    
        for word in words_list:
            page = requests.get('https://dictionary.cambridge.org/dictionary/english/' + str(word))
            tree = html.fromstring(page.content)
            Words = tree.xpath('//span[@class="ipa dipa lpr-2 lpl-1"]/text()')
            word1 = Words[1]
            transcribed_words = transcribed_words + " " + word1
        
        return(transcribed_words)
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:42:49 2020

@author: black
"""

class Model:
    def __init__(self, controller):
        self.controller = controller
        
    def transcribe(self, words):
        transcription = self.get_transcription(words)
        self.controller.handle_translation(translation)
        
        
    def get_transcription(self, words):
        words = input('Type or paste your sentence(s) below:\n')
        words_list = words.split()
        print("Getting your transcription ready, please wait")
    
        for word in words_list:
            page = requests.get('https://dictionary.cambridge.org/dictionary/english/' + str(word))
            tree = html.fromstring(page.content)
            Words = tree.xpath('//span[@class="ipa dipa lpr-2 lpl-1"]/text()')
            word1 = Words[1]
            print(word1)
        
        return(word1)
        
model = Model(None)
print(model.get_transcription("apple tree"))
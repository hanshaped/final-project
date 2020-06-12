# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:42:49 2020

@author: black
"""

from lxml  import html
import requests
import re

class Model:
    def __init__(self, controller):
        self.controller = controller
        
    def transcribe(self, words):
        transcription = self.get_transcription(words)
        self.controller.handle_transcription(transcription)
        
        
    def get_transcription(self, words):
        words_list = words.split()
        print("Getting your transcription ready, please wait")
        transcribed_words = ""
        
        for word in words_list:
            page = requests.get('https://dictionary.cambridge.org/dictionary/english/' + str(word))
            tree = html.fromstring(page.content)
            Words = tree.xpath('//span[@class="ipa dipa lpr-2 lpl-1"]/text()')
            word1 = Words[1]
            #pattern1 = '\b.+(aæɑəeɛɜɪɔɒouʊʌiː)s\b'
            #Word_class = tree.xpath('//span[@class="pos dpos"]/text()')
            #if Word_class[1] == 'noun':
                #plural = ''
                #isitplural = 0
                #result1 = re.match(pattern1, word1)
                #if result1 == 'None':
                    #return isitplural
                #else:
                    #isitplural = 1
                    #if isitplural == 1:
                        #plural == 'ɪz'
                    #else:
                        #plural == ''
                #return plural
            #else:
                #pass
            transcribed_words = transcribed_words + " " + word1 #+ plural
        
        return(transcribed_words)
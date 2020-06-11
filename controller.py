# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:44:19 2020

@author: black
"""

from model import Model
from view import View

class Controller:
    def __init__(self, root):
        self.model = Model(self)
        self.view = View(root, self)
        
    def handle_transcription(self, transcription):
        self.view.display_transcription(transcription)
    
    def words_entered(self, words):
        self.model.transcribe(words)
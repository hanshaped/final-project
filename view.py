# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:19:56 2020

@author: Hanna Szczepanek
"""

from tkinter import Tk, Label, 

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        
        self.info_label = tk.Label(root, text='Welcome to TransSCRIBE!')
        self.info_label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.button = tk.Button(root, text="", command=self.get_word)
        self.button.pack()
        
        self.transcription_label = tk.Label(root)
        self.transcription_label.pack()
        
    def get_word(self):
        word = self.entry.get()
        print(word)
        
    def display_transcription(self, transcription):
        self.transcription_label.configure(text="Transcribtion:/n" + transcription)
        
root = tk.Tk()
view = view(root, None)
root.mainloop()
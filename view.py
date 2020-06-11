# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:19:56 2020

@author: Hanna Szczepanek
"""

import tkinter as tk

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        
        self.info_label1 = tk.Label(root,
                                    text='Welcome to TransSCRIBE!',
                                    fg='#00244d')
        self.info_label1.pack()
        
        self.info_label2 = tk.Label(root, text='TransSCRIBE allows for the basic transciption of a list of words or sentences into the phonetic alphabet.')
        self.info_label2.pack()
        
        self.info_label3 = tk.Label(root, text='In short, you can see how to pronounce them!')
        self.info_label3.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.button = tk.Button(root, text="TransSCRIBE!", command=self.get_word)
        self.button.pack()
        
        self.transcription_label = tk.Label(root)
        self.transcription_label.pack()
        
    def get_word(self):
        word = self.entry.get()
        self.controller.word_entered(word)
        
    def display_transcription(self, transcription):
        self.transcription_label.configure(text="Transcribtion:/n" + transcription)
        
root = tk.Tk()
view = View(root, None)
root.mainloop()
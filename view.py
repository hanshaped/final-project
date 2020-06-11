# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:19:56 2020

@author: Hanna Szczepanek
"""

import tkinter as tk
from tkinter import BOTH, TOP, RIGHT, N, LEFT, CENTER

class View:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("TransSCRIBE – Check How To Pronounce!")
        self.controller = controller
        
        self.frame = tk.Frame(root, bg='#cceeff')
        self.frame.pack()
        
        self.info_label1 = tk.Label(root,
                                    text='Welcome to TransSCRIBE!',
                                    padx=10,
                                    pady=10,
                                    fg='#cceeff',
                                    bg='#004466',
                                    font=('times',22,'bold','italic'))
        self.info_label1.pack(expand=True, fill=BOTH, side=TOP)
        
        self.info_label2 = tk.Label(root,
                                    text='TransSCRIBE allows for the basic transciption of a list of words or sentences into the phonetic alphabet.',
                                    padx=15,
                                    pady=15,
                                    justify=CENTER,
                                    wraplength=500,
                                    fg='#004466',
                                    bg='#cceeff',
                                    font=('times',12))
        self.info_label2.pack(expand=True, fill=BOTH, side=TOP)
        
        self.info_label3 = tk.Label(root,
                                    text='In short, you can see how to pronounce them!',
                                    padx=15,
                                    pady=15,
                                    anchor=N,
                                    justify=CENTER,
                                    wraplength=500,
                                    fg='#004466',
                                    bg='#cceeff',
                                    font=('times',12,'bold'))
        self.info_label3.pack(expand=True, fill=BOTH, side=TOP)
        
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
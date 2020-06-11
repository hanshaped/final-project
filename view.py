# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:19:56 2020

@author: Hanna Szczepanek
"""

import tkinter as tk
from tkinter import BOTH, TOP, RIGHT, N, LEFT, CENTER, filedialog

class View:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("TransSCRIBE – Check How To Pronounce!")
        self.root.geometry("600x400")
        self.controller = controller
        
        # s = Style()
        # s.configure('My.TFrame', background='#cceeff')
        
        self.frame = tk.Frame(root)
        self.frame.config(background='#e6f7ff')
        self.frame.pack(fill='both', expand=True)
        
        self.info_label1 = tk.Label(root,
                                    text='Welcome to TransSCRIBE!',
                                    padx=10,
                                    pady=10,
                                    fg='#e6f7ff',
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
                                    bg='#e6f7ff',
                                    font=('times',12))
        self.info_label2.pack(expand=True, fill=BOTH, side=TOP)
        
        self.info_label3 = tk.Label(root,
                                    text='In short, you can see how to pronounce them!',
                                    padx=15,
                                    pady=15,
                                    justify=CENTER,
                                    wraplength=500,
                                    fg='#004466',
                                    bg='#e6f7ff',
                                    font=('times',12,'bold'))
        self.info_label3.pack(expand=True, fill=BOTH, side=TOP)
        
        self.entry = tk.Entry(root)
        self.entry.pack(expand=True, fill=BOTH, side=TOP, padx=15, pady=15)
        
        self.button = tk.Button(root,
                                text="TransSCRIBE!", 
                                command=self.get_word, 
                                fg='#e6f7ff', 
                                bg='#004466',
                                font=('times',11,'bold'))
        self.button.pack(expand=True, side=TOP)
        
        self.info_label4 = tk.Label(root,
                                    text='Your transription:',
                                    padx=15,
                                    pady=15,
                                    justify=CENTER,
                                    wraplength=500,
                                    fg='#004466',
                                    bg='#e6f7ff',
                                    font=('times',13,'bold'))
        self.info_label4.pack(expand=True, fill=BOTH, side=TOP)
        
        self.transcription_label = tk.Label(root,
                                            padx=15,
                                            pady=15,
                                            justify=CENTER,
                                            wraplength=500,
                                            fg='#00aeff',
                                            bg='#e6f7ff',
                                            font=('times',12))
        self.transcription_label.pack(expand=True, fill=BOTH, side=TOP)
        
        self.button_save = tk.Button(root,
                                     text="Save your transcription",
                                     padx=15,
                                     pady=15,
                                     command=self.save_transcription, 
                                     fg='#e6f7ff', 
                                     bg='#004466',
                                     font=('times',11,'bold'))
        self.button_save.pack(expand=True, side=TOP)
        
    def get_word(self):
        word = self.entry.get()
        self.controller.word_entered(word)
        
    def display_transcription(self, transcription):
        self.transcription_label.configure(text="Transcribtion:/n" + transcription)
    
    def save_transcription(self, transcription):
        self.filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
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
        self.root.title("TransSCRIBE – Simple Transcription!")
        self.root.geometry("600x400")
        self.root.iconphoto(False, tk.PhotoImage(file='graphics/chat.png'))
        self.controller = controller
        
        self.frame = tk.Frame(root)
        self.frame.config(background='#e6f7ff')
        self.frame.pack(fill='both', expand=True)
        
        def donothing():
            x = 0
        
        self.menubar = tk.Menu(root)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="About the app", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="TransSCRIBE", menu=filemenu)
        
        helpmenu = tk.Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        self.menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=self.menubar)
        
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
        
        self.info_label4 = tk.Label(root,
                                    text='Simply type or paste your sentence below:',
                                    padx=15,
                                    pady=15,
                                    justify=CENTER,
                                    wraplength=500,
                                    fg='#004466',
                                    bg='#e6f7ff',
                                    font=('times',12))
        self.info_label4.pack(expand=True, fill=BOTH, side=TOP)
        
        self.entry = tk.Entry(root, fg='#004466', font=('times',12))
        self.entry.pack(expand=False, fill=BOTH, side=TOP, padx=15, pady=15)
        
        self.button = tk.Button(root,
                                text="TransSCRIBE!", 
                                command=self.get_words, 
                                fg='#e6f7ff', 
                                bg='#004466',
                                activebackground='#33cccc',
                                activeforeground='#ebfafa',
                                font=('times',11,'bold'))
        self.button.pack(expand=True, side=TOP)
        
        self.info_label5 = tk.Label(root,
                                    text='Your transcription:',
                                    padx=15,
                                    pady=15,
                                    justify=CENTER,
                                    wraplength=500,
                                    fg='#004466',
                                    bg='#e6f7ff',
                                    font=('times',13,'bold'))
        self.info_label5.pack(expand=True, fill=BOTH, side=TOP)
        
        self.transcription_label = tk.Label(root,
                                            padx=15,
                                            pady=15,
                                            justify=CENTER,
                                            wraplength=500,
                                            fg='#00aeff',
                                            bg='#e6f7ff',
                                            font=('times',12))
        self.transcription_label.pack(expand=True, fill=BOTH, side=TOP)
        
    def get_words(self):
        words = self.entry.get()
        self.controller.words_entered(words)
        
    def display_transcription(self, transcription):
        self.transcription_label.configure(text=transcription)
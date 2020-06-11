# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:46:11 2020

@author: black
"""

import tkinter as tk
from controller import Controller

if __name__ == '__main__':
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
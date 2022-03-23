import tkinter.filedialog
from tkinter import *
def openfile():
    global filepath
    filepath=tkinter.filedialog.askopenfilename(filetypes=[("*.exe,*.com,*.pea","exe")])
    #f = open(filepath,mode='r',encoding='utf-8')
    return filepath

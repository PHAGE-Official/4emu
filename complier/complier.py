import tkinter.filedialog
from tkinter import *
def open_file():
    filepath=tkinter.filedialog.askopenfilename(filetypes=[("*.exe,*.com","exe")])
    #f = open(filepath,mode='r',encoding='utf-8')
    print(filepath)

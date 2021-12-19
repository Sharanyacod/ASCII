# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 08:59:01 2021

@author: Lighthouse
"""
from tkinter import *
root=Tk()
root.title("ASCII")
root.geometry("400x400")
label_series=Label(root,text="Name In ASCII:    ",bg="red",fg="black")
enter_word=Entry(root)
def ASCIIConverter():
    input_word=enter_word.get()
    for letter in input_word:
        label_series["text"]+=str(ord(letter))+" "
        


btn=Button(root,text="Show",command=ASCIIConverter,bg="gold",fg="black")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label_series.place(relx=0.5,rely=0.6,anchor=CENTER)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()






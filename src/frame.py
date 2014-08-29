#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use the grid
manager to create a more complicated
layout.

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

from Tkinter import *


class MainFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Windows")
        # self.style = Style()
        # self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(3, pad=7)
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Osztályok")
        lbl.grid(sticky=W, pady=4, padx=5)

        # area = Text(self)
        # area.grid(row=1, column=0, columnspan=2, rowspan=4,
        #     padx=5, sticky=E+W+S+N)


    def createClassButton(self, name, x, y):
        btn = Button(self, text=name)
        btn.grid(sticky=W+N, row=x, column=y)

def main():

    root = Tk()
    root.geometry("350x300+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
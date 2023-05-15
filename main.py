import subprocess
#import pandas
from tkinter import *
from tkinter import ttk
import json
import re
#import numpy as np
clicks = 0

def pdf_opener_at():
    path = 'Атлант расправил плечи часть 1.pdf'
    subprocess.Popen([path], shell=True)

def pdf_opener(path):
    #path = 'Атлант расправил плечи часть 1.pdf'
    subprocess.Popen([path], shell=True)

class Ui:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap("EMGP.ico")
        self.root.title("Experiment Material Protocol ")
        self.root.geometry("500x300")
        self.frame_tree = Frame(self.root, width=1050)
        self.treeview = ttk.Treeview(self.frame_tree)
        # main branch
        self.treeview.insert('', '0', 'mechanics', text='Механика')
        #secondary branch
        self.treeview.insert('mechanics', '0', 'stretch', text='Металл')
        self.treeview.insert('stretch', '0', '14H2GMP', text='14Х2ГМР')
        self.treeview.insert('14H2GMP', '2', 'SKRN0', text='СКРН')  #
        self.treeview.insert('14H2GMP', '2', 'OK0', text='Общая коррозия')
        self.treeview.insert('14H2GMP', '2', 'Protocol', text='Протоколы')
        self.treeview.insert('Protocol', '3', 'Protocol1', text='раствор А, 80%')
        self.treeview.insert('Protocol', '3', 'Protocol2', text='раствор А, 70%')
        self.treeview.insert('Protocol', '3', 'Protocol3', text='раствор А, 90%')
        self.treeview.insert('stretch', '1', 'steel20', text='Сталь 20')
        self.treeview.insert('steel20', '2', 'SKRN1', text='СКРН')  #
        self.treeview.insert('steel20', '2', 'OK1', text='Общая коррозия') #
        self.treeview.insert('stretch', '1', '06GFBM', text='06ГФБМ')
        self.treeview.insert('06GFBM', '2', 'SKRN2', text='СКРН')  #
        self.treeview.insert('06GFBM', '2', 'OK2', text='Общая коррозия')
        self.treeview.insert('stretch', '1', '26HMFBR', text='26ХМФБР')
        self.treeview.insert('26HMFBR', '2', 'SKRN3', text='СКРН')  #
        self.treeview.insert('26HMFBR', '2', 'OK3', text='Общая коррозия')
        self.treeview.insert('stretch', '1', '25HGMA', text='25ХГМА')
        self.treeview.insert('25HGMA', '2', 'SKRN4', text='СКРН')  #
        self.treeview.insert('25HGMA', '2', 'OK4', text='Общая коррозия')
        self.treeview.insert('mechanics', '1', 'compression', text='Композит')
        self.treeview.insert('compression', '0', 'concrete', text='Бетон')
        self.treeview.bind('<Double-1>', self.work_window)
        self.frame_tree.pack(padx=10, pady=10, side='left', fill='x')
        self.btn_atlant()
        self.treeview.pack()
        self.root.mainloop()

    def work_window(self,event):
        item = self.treeview.identify('item', event.x, event.y)
        if self.treeview.item(item, "text") == 'Металл':
            print("you clicked on", self.treeview.item(item, "text"))
            frame = Frame(self.root, width=250, height=220)
            with open("info.txt") as file:
                l = [str(line) for line in file]
                s = ''.join(map(str, l))
            lab = Label(frame, text=(s), font="Arial 14", bg='white', justify='left')
            frame.pack(padx=10, pady=10, side='right')
            lab.pack()
        elif self.treeview.item(item, "text") == 'Протоколы':
            path = 'АО «НИИтурбокомпрессор им. В.Б. Шнеппа» - 14Х2ГМР -основной (СРКН-А, раствор А, 80%).pdf'
            subprocess.Popen([path], shell=True)

        else:
            print('Lack of Data')

    def btn_atlant(self):
        btn = Button(text="Atlant", command=pdf_opener_at)
        btn.pack(padx=10, pady=10, side = 'bottom' )

    def click_button(self):
        root.title("Clicks {}".format(clicks))


if __name__ == '__main__':
    # self.root = Tk()
    # self.root.iconbitmap("EMGP.ico")
    # self.root.title("Experiment Material Protocol ")
    # self.root.geometry("400x300")
    # Ui.btn_atlant()
    # Ui.main_tree()
    # #work_window()
    # root.mainloop()
    ui = Ui()






#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *

from tkinter.filedialog import * 

from readtle import CatalogTLE

from calcsigma import drawShort_R
from calcsigma import drawShort_3
from calcsigma import drawShort_ephem

from calcsigma import drawLong_R
from calcsigma import drawLong_3
from calcsigma import drawLong_ephem

global catalog

global sat_name


def btn_open_clicked():
    ''' диалоговое окно открытия файла
    '''
    global catalog

    file_open = askopenfilename()

    catalog = CatalogTLE()
    
    catalog.readFullTLE(file_open)
    
    label_sat1['text'] = catalog.name[1], '    [', str(len(catalog.name)), ']'
    label_sat2['text'] = 'период:', catalog.JD[-1] - catalog.JD[1], 'суток'

    scale_numsat['from_'] = 0
    scale_numsat['to'] = len(catalog.name) - 1


def btnShort_R_clicked():           # короткие интервалы!
    global catalog
    drawShort_R(catalog)


def btnShort_3_clicked():
    '''
    '''
    global catalog
    drawShort_3(catalog)


def btnShort_ephem_clicked():
    '''
    '''
    ephem = list_ephem.curselection()
    
    if  ephem[0] == 0:
        eph = 'a'
    elif ephem[0] == 1:
        eph = 'e'
    elif ephem[0] == 2:
        eph = 'i'        
    elif ephem[0] == 3:
        eph = 'd'
    elif ephem[0] == 4:
        eph = 'w'
    elif ephem[0] == 5:
        eph = 'm'
    else:
        print('Косяк с выбором эфемериды!!! ')  
        return  
    
    drawShort_ephem(catalog, eph)

    
def btnLong_R_clicked():            # длинные интервалы
    global catalog
    drawLong_R(catalog, scale_numsat.get())


def btnLong_3_clicked():
    '''
    '''
    global catalog
    drawLong_3(catalog, scale_numsat.get())


def btnLong_ephem_clicked():
    '''
    '''
    ephem = list_ephem.curselection()
    drawLong_ephem(catalog, ephem[0], scale_numsat.get())


def close():
    root.destroy()
    root.quit()


root = Tk()
root.title("Sattelarium!")
#root.geometry('400x200')
# выключаем возможность изменять окно
root.resizable(width=False, height=False)


label_main = Label(root, text="Sattelarium ver 0.2.9   (test gui)", font='GentiumAlt 24', fg="blue")

textbox = Text(root, font='Arial 12', wrap='word', width=25, height=10)

label_sat1 = Label(root, text=" -- ", font='arial 10')
label_sat2 = Label(root, text=" -- ", font='arial 10')

list_ephem = Listbox(root, height=6, width=10, selectmode=SINGLE)
list1=["a", "e", "i", "draco", "omega", "M_0"]
for i in list1:
    list_ephem.insert(END,i)
list_ephem.activate(0)

btn_open = Button(root)
btn_open['text'] = 'выбрать каталог'
btn_open['command'] = btn_open_clicked


# -------------------------------   короткие интервалы   ---------------------
labelShort = Label(root, text="Короткие.", font='arial 12')

btnShort_R = Button(root)
btnShort_R['text'] = 'Граф. (R)'
btnShort_R['command'] = btnShort_R_clicked

btnShort_3 = Button(root)
btnShort_3['text'] = 'Граф.  (3)'
btnShort_3['command'] = btnShort_3_clicked

btnShort_a = Button(root)
btnShort_a['text'] = 'Граф.'
btnShort_a['command'] = btnShort_ephem_clicked


# -------------------------------   длинные интервалы   ---------------------

labelLong = Label(root, text="Длинные:", font='arial 12')

scale_numsat = Scale(root,orient=VERTICAL,length=250,from_=0,to=1,tickinterval=10,
               resolution=1)

btnLong_R = Button(root)
btnLong_R['text'] = 'Граф. (R)'
btnLong_R['command'] = btnLong_R_clicked

btnLong_3 = Button(root)
btnLong_3['text'] = 'Граф. (3)'
btnLong_3['command'] = btnLong_3_clicked

btnLong_a = Button(root)
btnLong_a['text'] = 'Граф.'
btnLong_a['command'] = btnLong_ephem_clicked


# ------------------------------   РАСПОЛОЖЕНИЕ   --------------------------
label_main.grid(  row=0,      column=0, columnspan=5)

textbox.grid(     row=1,      column=0, rowspan=5)

label_sat1.grid(  row=1,      column=1)
label_sat2.grid(  row=2,      column=1)
btn_open.grid(    row=3,      column=1)
list_ephem.grid(  row=4,      column=1)

labelShort.grid(  row=1,      column=2)
btnShort_R.grid(  row=2,      column=2)
btnShort_3.grid(  row=3,      column=2)
btnShort_a.grid(  row=4,      column=2)

scale_numsat.grid(row=1,      column=3, rowspan=5)

labelLong.grid(   row=1,      column=4)
btnLong_R.grid(   row=2,      column=4)
btnLong_3.grid(   row=3,      column=4)
btnLong_a.grid(   row=4,      column=4)


root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()



# ========================  та супер--утилитка: ===============================
#
# quickly create ubuntu-application foo
# quickly edit
# quickly design
# quickly run
# quickly add help-guide <имя руководства>
# quickly add dialog <имя диалога>
#
# Где подключать сигналы к функциям.
#
# def on_button1_clicked(self, widget, data=None):
#    //Тут ваш код
#
# Как обращаться к виджетам из python кода.
# self.builder.get_object("object_name")
# self.builder.get_object("text").set_text("Text") 
# Или
# text = self.builder.get_object("text")
# text.set_text("Text")


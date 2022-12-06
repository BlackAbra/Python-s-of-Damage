from tkinter import * 
import random

def kare():
    sayi = float(txSayi.get())
    lbkare['text']=str(sayi*sayi)
pencere =Tk()
pencere.geometry('300x200+150+150')
lbSayi=Label(text='Sayi :')
lbSayi.grid(row=0,column=0,padx=10,pady=10)
txSayi = Entry()
txSayi.grid(row=0,column=1,padx=10,pady=10)
btHesaplama = Button(text='Hesapla',command=kare)
btHesaplama.grid(row=1,column=0)
lbkare =Label()
lbkare.grid(row=1,column=1)
mainloop()
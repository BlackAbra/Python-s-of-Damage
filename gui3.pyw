from tkinter import * 
import random
pencere = Tk()
pencere.geometry('300x200+150+150')
def rasgele():
    r = random.randint(0,100)
    sayi.delete(0,END)
    sayi.insert(0,r)

sayi = Entry()
sayi.pack() 
buton = Button(text='Yaz',command=rasgele)
buton.pack()
mainloop()

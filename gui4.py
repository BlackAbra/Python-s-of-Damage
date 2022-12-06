from tkinter import * 
def yaz():
    metin=txAd.get()
    lbYaz['text'] = metin
pencere = Tk()
pencere.geometry('300x200+150+150')
lbAD=Label(text='Ad')
lbAD.grid(row=0,column=0,padx=10,pady=10)
txAd =Entry()
txAd.grid(row=0,column=1,padx=10,pady=10)
btYaz = Button(text='Yaz ',command=yaz)
btYaz.grid(row=1,column=0)
lbYaz =Label()
lbYaz.grid(row=1,column=1)
mainloop()
from tkinter import * 
window = Tk()
window.title('BFG -- 9000')
window.geometry('400x300+200+100')
window.resizable(width=1,height=1)

enAD = Entry()
enAD.pack()
btSil = Button(text='Kapat',command=window.quit())
btSil.pack()
window.mainloop()

btdosyaolustu = Button(text='Dosya Olustur',command=dosyaOlustur)
btdosyaolustu.pack()

btsil = Button(text='Metni Sil',command=sil)
btsil.pack()

def dosyaOlustur():
    dosya =open('dosyaolustur.txt','w')

def sil():
    enAD.delete(0,END)


btdosyaolustu = Button(text='Dosya Olustur',command=dosyaOlustur)
btdosyaolustu.pack()

btsil = Button(text='Metni Sil',command=sil)
btsil.pack()
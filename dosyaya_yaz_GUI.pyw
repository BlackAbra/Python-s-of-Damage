from tkinter import * 
pencere = Tk()
pencere.title('Dosyaya Yaz')
pencere.geometry('800x300+200+200')
pencere.resizable(width=0,height=0)


def yaz():
    dosya = open('dosya20.txt','w')
    dosya.write(enMetin.get())
    dosya.close()



enMetin =Entry()
enMetin.pack()

btYaz = Button(text='Metni dosyaya yaz',command=yaz)
btYaz.pack()

mainloop()



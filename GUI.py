from tkinter import * 
# window = Tk()
# window.title('BFG -- 9000')
# window.geometry('400x300+200+100')
# window.resizable(width=1,height=1)
# # istediginiz kodlari yazin \

# # lbAD =Label(text='Merhaba Python ',fg='red',bg='yellow')#For ground back ground
# lbAD = Label(text='Adiniz')
# lbAD.pack()

# 1 satirlik metin kutusu 
enAD = Entry()
enAD.pack()

# # Dugme / Buton 

# btSil = Button(text='Kapat',command=window.quit())
# btSil.pack()

# window.mainloop()


window = Tk()
def dosyaOlustur():
    dosya =open('dosyaolustur.txt','w')

def sil():
    enAD.delete(0,END)


window.geometry('800x300+150+150')

btdosyaolustu = Button(text='Dosya Olustur',command=dosyaOlustur)
btdosyaolustu.pack()

btsil = Button(text='Metni Sil',command=sil)
btsil.pack()
window.mainloop()

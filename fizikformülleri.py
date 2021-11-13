import tkinter as tk
from tkinter import *
import math

x = ""
def main():
    r = tk.Tk()
    r.geometry('600x600')  
    r.title('Ana Pencere')
    r.configure(background='blue')
    button1 = tk.Button(r, text='RL-R DEVRELERI', height = 5, width=20, command=altPencere_1)
    button1.place(relx = 0.4, rely = 0.2)
    button2 = tk.Button(r, text='R-C DEVRELERİ', height = 5, width=20, command=altPencere_2)
    button2.place(relx = 0.4, rely = 0.4)
    button3 = tk.Button(r, text='R-L-C DEVRELERİ', height = 5, width=20, command=altPencere_3)
    button3.place(relx = 0.4, rely = 0.6)
    r.mainloop()

def altPencere_1():

    
    def xlhesapla():
        result = 2*math.pi*int(str(f.get()))*int(str(l.get()))
        global x 
        x = "XL = " + str(result) + "\n"
        print(result)
    def URhesapla():
        result = int(str(ı.get()))*int(str(r.get()))
        x = "UR = " + str(result) + "\n"
        print(result)
    def ULhesapla():
        result = int(str(ı.get()))*int(str(xl.get()))
        x = "UL = " + str(result) + "\n"
        print(result)
    def IRhesapla():
        result = int(str(v.get()))/int(str(r.get()))
        x = "IR = " + str(result) + "\n"
        print(result)
    def IThesapla():
        result = math.sqrt(math.pow(int(str(il.get())),2)+math.pow(int(str(ir.get())),2))
        x = "IT = " + str(result) + "\n"
        print(result)
    def Zhesapla():
        result = int(str(v.get()))/int(str(it.get()))
        x = "Z = " + str(result) + "\n"
        print(result)

    def writefunction():
        with open('values.txt', 'w') as f:
            f.write(x)


    altPencere1 = tk.Tk()
    tk.Label(altPencere1, text = "RL-R DEVRELERİNİN SERİ VE PARALEL BAĞLANMASI").place(x=20,y=0)
    tk.Label(altPencere1, text="F").place(x=20,y=40)
    tk.Label(altPencere1, text="L").place(x=20,y=60)
    tk.Label(altPencere1, text="I").place(x=20,y=80)
    tk.Label(altPencere1, text="R").place(x=20,y=100)
    tk.Label(altPencere1, text="XL").place(x=20,y=120)
    tk.Label(altPencere1, text="V").place(x=20,y=140)
    tk.Label(altPencere1, text="Z").place(x=20,y=160)
    tk.Label(altPencere1, text="IT").place(x=20,y=180)
    tk.Label(altPencere1, text="IR").place(x=20,y=200)
    tk.Label(altPencere1, text="IL").place(x=20,y=220)
    f = Entry(altPencere1, width = 10, bg = "light yellow")
    f.place(x=100,y=40)
    l = Entry(altPencere1, width = 10, bg = "light yellow")
    l.place(x=100,y=60)
    ı = Entry(altPencere1, width=10, bg = "light yellow")
    ı.place(x=100, y=80)
    r = Entry(altPencere1, width = 10, bg = "light yellow")
    r.place(x=100,y=100)
    xl = Entry(altPencere1, width = 10, bg = "light yellow")
    xl.place(x=100,y=120)
    v = Entry(altPencere1, width = 10, bg = "light yellow")
    v.place(x=100,y=140)
    z = Entry(altPencere1, width = 10, bg = "light yellow")
    z.place(x=100,y=160)
    it = Entry(altPencere1, width = 10, bg = "light yellow")
    it.place(x=100,y=180)
    ir = Entry(altPencere1, width = 10, bg = "light yellow")
    ir.place(x=100,y=200)
    il = Entry(altPencere1, width = 10, bg = "light yellow")
    il.place(x=100,y=220)
    
    tk.Label(altPencere1, text="SERİ BAĞLI").place(relx=0.7, rely =0.01)
    tk.Label(altPencere1, text="PARALEL BAĞLI").place(relx=0.7, rely =0.4)
    
    altPencere1.geometry('600x600')  
    altPencere1.title('Alt Pencere 1')
    altPencere1.configure(background='blue')
    save = tk.Button(altPencere1, text='SAVE',  height = 5, width=20, command = lambda:writefunction())
    save.place(relx = 0.35, rely = 0.8)
    xlcalculate = tk.Button(altPencere1, text='XL Hesapla',  height = 2, width=10, command = lambda:xlhesapla())
    xlcalculate.place(relx = 0.70, rely = 0.1)
    xlcalculate = tk.Button(altPencere1, text='XL Hesapla',  height = 2, width=10, command = lambda:xlhesapla())
    xlcalculate.place(relx = 0.70, rely = 0.5)
    ur = tk.Button(altPencere1, text='UR Hesapla',  height = 2, width=10, command = lambda:URhesapla())
    ur.place(relx = 0.70, rely = 0.2)
    ul = tk.Button(altPencere1, text='UL Hesapla',  height = 2, width=10, command = lambda:ULhesapla())
    ul.place(relx = 0.70, rely = 0.3)
    ircalculate = tk.Button(altPencere1, text='IR Hesapla',  height = 2, width=10, command = lambda:IRhesapla())
    ircalculate.place(relx = 0.70, rely = 0.6)
    zcalculate = tk.Button(altPencere1, text='Z Hesapla',  height = 2, width=10, command = lambda:Zhesapla())
    zcalculate.place(relx = 0.70, rely = 0.7)
    itcalculate = tk.Button(altPencere1, text='IT Hesapla',  height = 2, width=10, command = lambda:IThesapla())
    itcalculate.place(relx = 0.70, rely = 0.8)


def altPencere_2():

    def Xchesapla():
        result = 1/(2*math.pi*int(str(f.get()))*int(str(c.get())))
        global x 
        x = "Xc = " + str(result) + "\n"
        print(result)
    def Zhesapla():
        global x 
        result = math.pow(int(str(r.get())),2) + int(str(a.get()))*math.pow(int(str(c.get())),2)
        x = "Z = " + str(result) + "\n"
        print(result)
    def Cshesapla():
        result = int(str(c.get()))
        global x 
        x = "Xc = " + str(result) + "\n"
        print(result)
    def Cphesapla():
        global x 
        result = 1/int(str(c.get()))
        x = "Z = " + str(result) + "\n"
        print(result)
    
    def writefunction():
        with open('values.txt', 'w') as f:
            f.write(x)


    altPencere2 = tk.Tk()
    altPencere2.geometry('600x600')  
    altPencere2.title('Alt Pencere 2')
    altPencere2.configure(background='blue')
    tk.Label(altPencere2, text="F").place(x=20,y=40)
    tk.Label(altPencere2, text="C").place(x=20,y=60)
    tk.Label(altPencere2, text="Z").place(x=20,y=80)
    tk.Label(altPencere2, text="R").place(x=20,y=100)
    tk.Label(altPencere2, text="X").place(x=20,y=120)
    tk.Label(altPencere2, text="C").place(x=20,y=140)
    tk.Label(altPencere2, text="EMPEDANS:").place(relx = 0.70,rely = 0.25)
    tk.Label(altPencere2, text="SERİ KONDANSATÖR:").place(relx = 0.70,rely = 0.4)
    tk.Label(altPencere2, text="PARALEL KONDANSATÖR:").place(relx = 0.70,rely = 0.55)

    f = Entry(altPencere2, width = 10, bg = "light yellow")
    f.place(x=100,y=40)
    c = Entry(altPencere2, width = 10, bg = "light yellow")
    c.place(x=100,y=60)
    z = Entry(altPencere2, width=10, bg = "light yellow")
    z.place(x=100, y=80)
    r = Entry(altPencere2, width = 10, bg = "light yellow")
    r.place(x=100,y=100)
    a = Entry(altPencere2, width = 10, bg = "light yellow")
    a.place(x=100,y=120)
    c = Entry(altPencere2, width = 10, bg = "light yellow")
    c.place(x=100,y=140)

    xccalculate = tk.Button(altPencere2, text='Xc Hesapla',  height = 2, width=10, command = lambda:Xchesapla())
    xccalculate.place(relx = 0.70, rely = 0.15)
    zcalculate = tk.Button(altPencere2, text='Z Hesapla',  height = 2, width=10, command = lambda:Zhesapla())
    zcalculate.place(relx = 0.70, rely = 0.3)
    cscalculate = tk.Button(altPencere2, text='Cs Hesapla',  height = 2, width=10, command = lambda:Cshesapla())
    cscalculate.place(relx = 0.70, rely = 0.45)
    cpcalculate = tk.Button(altPencere2, text='Cp Hesapla',  height = 2, width=10, command = lambda:Cphesapla())
    cpcalculate.place(relx = 0.70, rely = 0.6)       

    save = tk.Button(altPencere2, text='SAVE',  height = 5, width=20, command=altPencere2.destroy)
    save.place(relx = 0.35, rely = 0.8)


def altPencere_3():

    def xchesapla():
        result1 = 1/(2*math.pi*int(str(f.get()))*int(str(c1.get())))
        result2 = 1/(2*math.pi*int(str(f.get()))*int(str(c2.get())))
        result3 = 2*math.pi*int(str(f.get()))*int(str(l.get()))
        global x 
        x = "Xc = " + str(result1) + "\n" + str(result2) + " " + str(result3)
        print("Xc1 = " + str(result1) + " Xc2 = " + str(result2) + " XL = " + str(result3))
    def xlhesapla():
        result1 = 2*math.pi*int(str(f.get()))*int(str(l.get()))
        result2 = 1/(2*math.pi*int(str(f.get()))*int(str(c1.get())))
        global x 
        x = "Xc = " + str(result1) + "\n" + str(result2)
        print("XL = " + str(result1) + " Xc = " + str(result2))

    def paralelrlchesapla():
        print("DEVRE PARALEL OLDUĞU İÇİN BÜTÜN GERİLİM DEĞERLERİ AYNIDIR")


    def writefunction():
        with open('values.txt', 'w') as f:
            f.write(x)

    altPencere3 = tk.Tk()
    altPencere3.geometry('600x600')  
    altPencere3.title('Alt Pencere 3')
    altPencere3.configure(background='blue')

    tk.Label(altPencere3, text="F").place(x=20,y=40)
    tk.Label(altPencere3, text="C").place(x=20,y=60)
    tk.Label(altPencere3, text="C2").place(x=20,y=80)
    tk.Label(altPencere3, text="L").place(x=20,y=100)

    tk.Label(altPencere3, text="SERİ PARALEL RLC DEVRESİ:").place(relx = 0.70,rely = 0.25)
    tk.Label(altPencere3, text="SERİ RLC DEVRESİ:").place(relx = 0.70,rely = 0.4)
    tk.Label(altPencere3, text="PARALEL RLC DEVRELERİ:").place(relx = 0.70,rely = 0.55)

    f = Entry(altPencere3, width = 10, bg = "light yellow")
    f.place(x=100,y=40)
    c1 = Entry(altPencere3, width = 10, bg = "light yellow")
    c1.place(x=100,y=60)
    c2 = Entry(altPencere3, width = 10, bg = "light yellow")
    c2.place(x=100,y=80)
    l = Entry(altPencere3, width = 10, bg = "light yellow")
    l.place(x=100,y=100)

    seriparalelrlc = tk.Button(altPencere3, text='Xc ve XL Hesapla',  height = 2, width=10, command = lambda:xchesapla())
    seriparalelrlc.place(relx = 0.70, rely = 0.3)
    serirlc = tk.Button(altPencere3, text='UR Hesapla',  height = 2, width=10, command = lambda:xlhesapla())
    serirlc.place(relx = 0.70, rely = 0.45)
    paralelrlc = tk.Button(altPencere3, text='PARALEL RLC HESAPLA',  height = 2, width=10, command = lambda:paralelrlchesapla())
    paralelrlc.place(relx = 0.70, rely = 0.6)

    save = tk.Button(altPencere3, text='SAVE',  height = 5, width=20, command=altPencere3.destroy)
    save.place(relx = 0.35, rely = 0.8)





main()
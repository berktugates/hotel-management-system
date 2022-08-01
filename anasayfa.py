from cProfile import label
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as ttk  
import mysql.connector
from musteri import Musteri
from odarezervasyon import OdaRezervasyon
from oda import Oda


class AnaSayfa:
    def __init__(self,root):
        self.root=root
        self.root.title("ATEŞ Otel Yönetim Sistemi")
        self.root.geometry("1550x800+0+0")

#En Üstteki Otel Resmi
        resim1=Image.open(r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\otelfotograf.png")
        resim1=resim1.resize((1920,140),Image.ANTIALIAS)
        self.photoresim1=ImageTk.PhotoImage(resim1)

        lblresim1=Label(self.root,image=self.photoresim1,bd=4,relief=RIDGE)
        lblresim1.place(x=0,y=0,width=1920,height=140)

#Sol Üst Köşe Logo
        resim2=Image.open(r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\ateshotellogo.png")
        resim2=resim2.resize((230,140),Image.ANTIALIAS)
        self.photoresim2=ImageTk.PhotoImage(resim2)

        lblresim2=Label(self.root,image=self.photoresim2,bd=4,relief=RIDGE)
        lblresim2.place(x=0,y=0,width=230,height=140)


#Başlık
        lblbaslik=Label(self.root,text="ATEŞ OTEL YÖNETİM SİSTEMİ",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lblbaslik.place(x=0,y=140,width=1570,height=55)


#Başlık Yazısının Çerçevesi
        baslikyazisicerceve=Frame(self.root,bd=4,relief=RIDGE)
        baslikyazisicerceve.place(x=0,y=190,width=1920,height=620)


#Menü Kutucuğu
        menukutucugu=Label(baslikyazisicerceve,text="Menü",font=("times new roman",20,"bold") ,bg="black", fg="gold" ,bd=0,relief=RIDGE)
        menukutucugu.place(x=0,y=0,width=230)

#Butonlar için Çerçeve
        btnCerceve=Frame(baslikyazisicerceve,bd=4,relief=RIDGE)
        btnCerceve.place(x=0,y=35,width=228,height=155)

        btnMusteri=Button(btnCerceve,command=self.MusteriSayfasiniAc,text="Müşteri İşlemleri",width=22, font=("times new roman",14,"bold") ,bg="black", fg="gold" ,bd=0,cursor="hand2")
        btnMusteri.grid(row=0,column=0,pady=1)

        btnRezervasyon=Button(btnCerceve,command=self.RezervasyonSayfasiniAc,text="Rezervasyon İşlemleri",width=22, font=("times new roman",14,"bold") ,bg="black", fg="gold" ,bd=0,cursor="hand2")
        btnRezervasyon.grid(row=1,column=0,pady=1)

        btnOda=Button(btnCerceve,command=self.OdaSayfasiniAc,text="Oda İşlemleri",width=22, font=("times new roman",14,"bold") ,bg="black", fg="gold" ,bd=0,cursor="hand2")
        btnOda.grid(row=2,column=0,pady=1)

        btnCikisYap=Button(btnCerceve,command=self.CikisYap,text="Çıkış Yap",width=22, font=("times new roman",14,"bold") ,bg="black", fg="gold" ,bd=0,cursor="hand2")
        btnCikisYap.grid(row=4,column=0,pady=1)


#Sağ Tarafa Koyulacak Resim
        resim3=Image.open(r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\Resepsiyon-resmi.jpg")
        resim3=resim3.resize((1340,607),Image.ANTIALIAS)
        self.photoresim3=ImageTk.PhotoImage(resim3)

        lblresim3=Label(baslikyazisicerceve,image=self.photoresim3,bd=0,relief=RIDGE)
        lblresim3.place(x=225,y=0,width=1340,height=607)


#Sol Alta Koyulacak Fotoğraflar
        resim4=Image.open(r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\otel-bar.jpg")
        resim4=resim4.resize((225,220),Image.ANTIALIAS)
        self.photoresim4=ImageTk.PhotoImage(resim4)


        lblresim4=Label(baslikyazisicerceve,image=self.photoresim4,bd=0.5,relief=RIDGE)
        lblresim4.place(x=0,y=190,width=225,height=220)


        resim5=Image.open(r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\otel-sauna.jpg")
        resim5=resim5.resize((225,220),Image.ANTIALIAS)
        self.photoresim5=ImageTk.PhotoImage(resim5)

        lblresim5=Label(baslikyazisicerceve,image=self.photoresim5,bd=0.5,relief=RIDGE)
        lblresim5.place(x=0,y=390,width=225,height=220)


    def MusteriSayfasiniAc(self):
        self.yenipencere=Toplevel(self.root)
        self.app=Musteri(self.yenipencere)
    


    def RezervasyonSayfasiniAc(self):
        self.yenipencere=Toplevel(self.root)
        self.app=OdaRezervasyon(self.yenipencere)


    def OdaSayfasiniAc(self):
        self.yenipencere=Toplevel(self.root)
        self.app=Oda(self.yenipencere)

    def CikisYap(self):
        self.root.destroy()   





if __name__ == "__main__":   
    root=Tk()
    root.resizable(0,0)
    nsn=AnaSayfa(root)
    root.mainloop()    

 
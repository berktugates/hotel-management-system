
from cProfile import label
from tkinter import *
from tkinter import messagebox
from turtle import left, width
from PIL import Image,ImageTk
import tkinter as ttk  
import mysql.connector

    
        


class UyeOlPenceresi:
    def __init__(self,root):
        self.root=root
        self.root.title("Üye Ol")
        self.root.geometry("1600x900+0+0")


        self.KullaniciIsmi=StringVar()
        self.KullaniciSoyadi=StringVar()
        self.KullaniciTelefonNo=StringVar()
        self.KullaniciEPosta=StringVar()
        
        self.KullaniciGuvenlikCevabi=StringVar()
        self.KullaniciParola=StringVar()
        self.KullaniciOnaylanmisParola=StringVar()
        

#Arka plan resmi koyuldu.       
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\otelfotograf.png")

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


#Sol Taraf Marka Logo Resmi
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\ateshotellogo.png")
        sol_lbl=Label(self.root,image=self.bg1)
        sol_lbl.place(x=50,y=300,width=470,height=310)

       
       
#Sağ Taraftaki Çerçeve       
        cerceve=Frame(self.root,bg="#F3EFEF")
        cerceve.place(x=620,y=170,width=800,height=550)


        uyeol_lbl=Label(cerceve,text="Üye Ol",font=("times new roman",20,"bold"),fg="darkgreen")
        uyeol_lbl.place(x=350,y=40)


#Kaydolma Bilgileri Satır 1

        isim=Label(cerceve,text="Adınız",font=("times new roman",15,"bold"))
        isim.place(x=80,y=100)

        isim_girisi=ttk.Entry(cerceve,textvariable=self.KullaniciIsmi,font=("times new roman",15,"bold"))
        isim_girisi.place(x=80,y=130,width=250)

        soyad=Label(cerceve,text="Soyadınız",font=("times new roman",15,"bold"))
        soyad.place(x=400,y=100)

        self.txt_Soyad=ttk.Entry(cerceve,textvariable=self.KullaniciSoyadi,font=("times new roman",15,"bold"))
        self.txt_Soyad.place(x=400,y=130,width=250)


#Kaydolma Bilgileri Satır 2

        telno=Label(cerceve,text="Telefon No",font=("times new roman",15,"bold"))
        telno.place(x=80,y=170)

        self.txt_TelNo=ttk.Entry(cerceve,textvariable=self.KullaniciTelefonNo,font=("times new roman",15,"bold"))
        self.txt_TelNo.place(x=80,y=200,width=250)


        eposta=Label(cerceve,text="E-Posta",font=("times new roman",15,"bold"))
        eposta.place(x=400,y=170)

        self.txt_ePosta=ttk.Entry(cerceve,textvariable=self.KullaniciEPosta,font=("times new roman",15,"bold"))
        self.txt_ePosta.place(x=400,y=200,width=250)


#Kaydolma Bilgileri Satır 3

        guvenliksorusu=Label(cerceve,text="Güvenlik Sorusu",font=("times new roman",15,"bold"))
        guvenliksorusu.place(x=80,y=240)

        # self.combo_guvenliksorusu=ttk.Combobox(cerceve,font=("times new roman",15,"bold"),state="readonly")
        # self.combo_guvenliksorusu["values"]=("Seçiniz","İlkokul Öğretmeninizin Adı","Tuttuğunuz Takım","En Sevdiğiniz Hayvan","En Yakın Arkadaşınız")
        # self.combo_guvenliksorusu.place(x=50,y=270,width=250)
        # self.combo_guvenliksorusu.current(0)

        self.BelirlenmisGuvenlikSorusu = StringVar()
        self.BelirlenmisGuvenlikSorusu.set('İlkokul Öğretmeninizin Adı')
        
        self.txt_GuvenlikSorusu=ttk.Entry(cerceve,textvariable=self.BelirlenmisGuvenlikSorusu,font=("times new roman",15,"bold"),state=DISABLED)
        self.txt_GuvenlikSorusu.place(x=80,y=270,width=250)

        guvenlikcevabi=Label(cerceve,text="Güvenlik Cevabınız",font=("times new roman",15,"bold"))
        guvenlikcevabi.place(x=400,y=240)   

        self.txt_GuvenlikCevabi=ttk.Entry(cerceve,textvariable=self.KullaniciGuvenlikCevabi,font=("times new roman",15,"bold"))
        self.txt_GuvenlikCevabi.place(x=400,y=270,width=250)




#Kaydolma Bilgileri Satır 4

        sifre=Label(cerceve,text="Şifre",font=("times new roman",15,"bold"))
        sifre.place(x=80,y=310)

        self.txt_Sifre=ttk.Entry(cerceve,textvariable=self.KullaniciParola,font=("times new roman",15,"bold"))
        self.txt_Sifre.place(x=80,y=340,width=250)


        sifreonayi=Label(cerceve,text="Şifrenizi Yeniden Girin",font=("times new roman",15,"bold"))
        sifreonayi.place(x=400,y=310)

        self.txt_SifreOnayi=ttk.Entry(cerceve,textvariable=self.KullaniciOnaylanmisParola,font=("times new roman",15,"bold"))
        self.txt_SifreOnayi.place(x=400,y=340,width=250)



#Kayıt Butonu

        btnUyeOl=Button(cerceve,command=self.KullaniciKaydet,text="Üye Ol",borderwidth=0,font=("times new roman",15,"bold"),bd=3,fg="white",bg="green",activeforeground="black",activebackground="white")
        btnUyeOl.place(x=140,y=420,width=150)


#giriş yap butonu
        btnGirisYap=Button(cerceve,text="Giriş Yap",font=("times new roman",15,"bold"),bd=3,fg="white",bg="green",activeforeground="black",activebackground="white")
        btnGirisYap.place(x=450,y=420,width=150)



    def KullaniciKaydet(self):        
        
    
        if self.KullaniciIsmi.get()=="" or self.KullaniciEPosta.get()=="" or self.KullaniciSoyadi.get()=="" or self.KullaniciTelefonNo.get()=="" or self.KullaniciGuvenlikCevabi.get()=="" or self.KullaniciParola.get()=="" or self.KullaniciOnaylanmisParola.get()=="":
                 messagebox.showerror("Hata","Lütfen tüm alanları doldurunuz.")
        elif self.KullaniciParola.get()!=self.KullaniciOnaylanmisParola.get():
                messagebox.showerror("Hata","Parolalarınız birbiriyle uyuşmuyor.")
        else:
                baglanti=mysql.connector.connect(host="localhost", user="root", password="Test123456",database="otelveritabani")
                imlecim=baglanti.cursor()
                query=("select * from kullanici where eposta=%s")
                deger=(self.KullaniciEPosta.get(),)
                imlecim.execute(query,deger)
                satir=imlecim.fetchone()

        if satir!=None:
                        messagebox.showerror("Hata","Kullanıcı zaten mevcut, lütfen başka e-posta adresi giriniz.")

        else:
                        imlecim.execute("insert into kullanici values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                 self.KullaniciIsmi.get(),
                                                                                                 self.KullaniciSoyadi.get(),
                                                                                                 self.KullaniciTelefonNo.get(),
                                                                                                 self.KullaniciEPosta.get(),
                                                                                                 self.BelirlenmisGuvenlikSorusu.get(),
                                                                                                 self.KullaniciGuvenlikCevabi.get(),
                                                                                                 self.KullaniciParola.get()


                                                                                            ))
        baglanti.commit()
        baglanti.close()
        messagebox.showinfo("Başarılı","Üyelik işleminiz başarıyla tamamlandı.")                                                                                    
        self.KullaniciBilgileriniSifirla()
        
       
    def KullaniciBilgileriniSifirla(self):

        self.KullaniciIsmi.set("")
        self.KullaniciSoyadi.set("")
        self.KullaniciTelefonNo.set("")
        self.KullaniciEPosta.set("")
        self.KullaniciGuvenlikCevabi.set("")
        self.KullaniciParola.set("")
        self.KullaniciOnaylanmisParola.set("")


        




if __name__ == "__main__":
        root=Tk()
        root.resizable(0,0)
        nsn=UyeOlPenceresi(root)
        root.mainloop()
      
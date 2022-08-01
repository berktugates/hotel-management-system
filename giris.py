from cProfile import label
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as ttk  
import mysql.connector
from anasayfa import AnaSayfa

from musteri import Musteri
from oda import Oda
from odarezervasyon import OdaRezervasyon
 


def main():
    win=Tk()
    win.resizable(0,0)
    app=Giris_Penceresi(win)
    win.mainloop()



class Giris_Penceresi:
    def __init__(self,root):
        self.root=root
        self.root.title("Giris Yap")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("ateshotelicon.ico")



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\otelfotograf.png")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        cerceve=Frame(self.root,bg="white")
        cerceve.place(x=610,y=170,width=340,height=450)

        resim1=Image.open(r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\ateshotellogo.png")
        resim1=resim1.resize((300,200),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(resim1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)


        #Kullanıcıdan giriş bilgileri istendi.

        girisYap=Label(cerceve,text="Giriş Yap",font=("times new roman",20,"bold"),fg="black",bg="white")
        girisYap.place(x=110,y=100)


        ePosta=lbl=Label(cerceve,text="E-Posta",font=("times new roman",15,"bold"),fg="black",bg="white")
        ePosta.place(x=70,y=155)

        self.txtePosta=ttk.Entry(cerceve,font=("times new roman",15,"bold"))
        self.txtePosta.place(x=40,y=180,width=270)
       


        parola=lbl=Label(cerceve,text="Şifre",font=("times new roman",15,"bold"),fg="black",bg="white")
        parola.place(x=70,y=225)

        self.txtParola=ttk.Entry(cerceve,font=("times new roman",15,"bold"))
        self.txtParola.place(x=40,y=250,width=270)


        #İkonlar


        #e-posta ikonu
        resim2=Image.open(r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\epostaIcon.png")
        resim2=resim2.resize((20,20),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(resim2)
        lblresim1=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblresim1.place(x=650,y=325,width=25,height=25)


        #parola ikonu
        resim3=Image.open(r"C:\Users\berktug\Desktop\OtelYonetimSistemi\resimler\sifreIcon.png")
        resim3=resim3.resize((20,20),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(resim3)
        lblresim2=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblresim2.place(x=650,y=397,width=25,height=25)


        #giriş yap butonu
        btnGirisYap=Button(cerceve,command=self.giris,text="Giriş Yap",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="black",activebackground="white")
        btnGirisYap.place(x=110,y=300,width=120,height=35)
        
          

        #üye ol butonu
        btnUyeOl=Button(cerceve,text="Üye Ol",command=self.kaydolpenceresiniac,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="green",activebackground="white",activeforeground="black")
        btnUyeOl.place(x=25,y=380,width=140)


        #şifremi unuttum butonu
        btnSifremiUnuttum=Button(cerceve,command=self.sifremiunuttumpenceresiniac,text="Şifremi Unuttum",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="green",activebackground="white",activeforeground="black")
        btnSifremiUnuttum.place(x=180,y=380,width=140)





    def kaydolpenceresiniac(self):
        self.yeni_pencere=Toplevel(self.root)
        self.app=UyeOlPenceresi(self.yeni_pencere)


    def giris(self):
            if self.txtePosta.get()=="" or self.txtParola.get()=="":
                messagebox.showerror("Hata","Tüm alanları doldurunuz")

            # elif  self.txtePosta.get()=="berke" and self.txtParola.get()=="ates":
            # messagebox.showinfo("Başarılı","Ateş Otel Yönetim Sistemine Hoş Geldiniz!") 

            else:
                baglanti2=mysql.connector.connect(host="localhost",user="root",password="Test123456",database="otelveritabani")
                imlecim2=baglanti2.cursor()
                imlecim2.execute("select * from kullanici where eposta=%s and sifre=%s", (
                                                                                        self.txtePosta.get(),
                                                                                        self.txtParola.get()
                
                
                                                                                ))     
                satir2=imlecim2.fetchone()
                if satir2==None:
                    messagebox.showerror("Hata","E-posta adresiniz veya şifreniz hatalıdır.")
                else:
                    self.root.withdraw()
                    self.yeni_pencere=Toplevel(self.root)
                    self.app=AnaSayfa(self.yeni_pencere)
                    

                baglanti2.commit()                   
                baglanti2.close()



    def sifresifirla(self):
        if self.txt_GuvenlikCevabi.get()=="":
            messagebox.showerror("Hata","Lütfen güvenlik cevabınızı giriniz.",parent=self.root2)
        elif self.txtYeniParola.get()=="":
            messagebox.showerror("Hata","Lütfen yeni parolanızı giriniz.",parent=self.root2)
        else:
            baglanti4=mysql.connector.connect(host="localhost",user="root",password="Test123456",database="otelveritabani")
            imlecim4=baglanti4.cursor()
            sorgu2=("select * from kullanici where eposta=%s and guvenlikcevabi=%s and guvenliksorusu=%s")
            value2=(self.txtePosta.get(),self.txt_GuvenlikCevabi.get(),self.txt_GuvenlikSorusu.get(),)
            imlecim4.execute(sorgu2,value2)
            row2=imlecim4.fetchone()
            if row2==None:
                messagebox.showerror("Hata","Güvenlik cevabınız yanlıştır.",parent=self.root2)
            else:
                sorgu3=("update kullanici set sifre=%s where eposta=%s")
                deger3=(self.txtYeniParola.get(),self.txtePosta.get())
                imlecim4.execute(sorgu3,deger3)


                baglanti4.commit()
                baglanti4.close()
                messagebox.showinfo("Bilgi","Şifreniz başarıyla sıfırlandı.Yeni şifrenizle giriş yapabilirsiniz.",parent=self.root2)
                self.root2.destroy()


# Şifremi Unuttum Penceresi İçin
    def sifremiunuttumpenceresiniac(self):
        if self.txtePosta.get()=="":
            messagebox.showerror("Hata","Şifrenizi sıfırlamak için lütfen e-posta adresinizi giriniz.")
        else:
            baglanti3=mysql.connector.connect(host="localhost",user="root",password="Test123456",database="otelveritabani")
            imlecim3=baglanti3.cursor()
            sorgu=("select * from kullanici where eposta=%s")
            value=(self.txtePosta.get(),)
            imlecim3.execute(sorgu,value)
            row=imlecim3.fetchone()
            
            if row ==None:
                messagebox.showerror("Hata","Lütfen geçerli bir e-posta adresi giriniz.")
            else:
                baglanti3.close()
                self.root2=Toplevel()
                self.root2.title("Şifremi Unuttum")
                self.root2.geometry("340x450+610+170")
                self.root2.resizable(0,0)

                l=Label(self.root2,text="Şifremi Unuttum",font=("times new roman",20,"bold"),fg="red",bg="black")
                l.place(x=0,y=10,relwidth=1)

                #Kaydolma Bilgileri Satır 3

                guvenliksorusu=Label(self.root2,text="Güvenlik Sorusu",font=("times new roman",15,"bold"))
                guvenliksorusu.place(x=50,y=80)

        # self.combo_guvenliksorusu=ttk.Combobox(cerceve,font=("times new roman",15,"bold"),state="readonly")
        # self.combo_guvenliksorusu["values"]=("Seçiniz","İlkokul Öğretmeninizin Adı","Tuttuğunuz Takım","En Sevdiğiniz Hayvan","En Yakın Arkadaşınız")
        # self.combo_guvenliksorusu.place(x=50,y=270,width=250)
        # self.combo_guvenliksorusu.current(0)

                self.BelirlenmisGuvenlikSorusu = StringVar()
                self.BelirlenmisGuvenlikSorusu.set('İlkokul Öğretmeninizin Adı')
        
                self.txt_GuvenlikSorusu=ttk.Entry(self.root2,textvariable=self.BelirlenmisGuvenlikSorusu,font=("times new roman",15,"bold"),state=DISABLED)
                self.txt_GuvenlikSorusu.place(x=50,y=110,width=250)

                guvenlikcevabi=Label(self.root2,text="Güvenlik Cevabınız",font=("times new roman",15,"bold"))
                guvenlikcevabi.place(x=50,y=150)   

                self.txt_GuvenlikCevabi=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_GuvenlikCevabi.place(x=50,y=180,width=250)

                yeni_parola=Label(self.root2,text="Yeni Parola",font=("times new roman",15,"bold"),fg="black")
                yeni_parola.place(x=50,y=220)

                self.txtYeniParola=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txtYeniParola.place(x=50,y=250,width=250)

                btnSifreSifirla=Button(self.root2,command=self.sifresifirla,text="Şifre Sıfırla",font=("times new roman",15,"bold"),fg="red",bg="black")
                btnSifreSifirla.place(x=100,y=290)





class UyeOlPenceresi:
    def __init__(self,root):
        self.root=root
        self.root.title("Üye Ol")
        self.root.geometry("1600x900+0+0")
        root.resizable(0,0)

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
        # self.combo_guvenliksorusu["value"]=("Seçiniz","İlkokul Öğretmeninizin Adı","Tuttuğunuz Takım","En Sevdiğiniz Hayvan","En Yakın Arkadaşınız")
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
        btnGirisYap=Button(cerceve,command=self.girisidondur,text="Giriş Yap",font=("times new roman",15,"bold"),bd=3,fg="white",bg="green",activeforeground="black",activebackground="white")
        btnGirisYap.place(x=450,y=420,width=150)



    def KullaniciKaydet(self):        
        
    
        if self.KullaniciIsmi.get()=="" or self.KullaniciEPosta.get()=="" or self.KullaniciSoyadi.get()=="" or self.KullaniciTelefonNo.get()=="" or self.KullaniciGuvenlikCevabi.get()=="" or self.KullaniciParola.get()=="" or self.KullaniciOnaylanmisParola.get()=="":
                 messagebox.showerror("Hata","Lütfen tüm alanları doldurunuz.",parent=self.root)
        elif self.KullaniciParola.get()!=self.KullaniciOnaylanmisParola.get():
                messagebox.showerror("Hata","Parolalarınız birbiriyle uyuşmuyor.",parent=self.root)
        else:
                baglanti=mysql.connector.connect(host="localhost", user="root", password="Test123456",database="otelveritabani")
                imlecim=baglanti.cursor()
                query=("select * from kullanici where eposta=%s")
                deger=(self.KullaniciEPosta.get(),)
                imlecim.execute(query,deger)
                satir=imlecim.fetchone()

        if satir!=None:
                        messagebox.showerror("Hata","Kullanıcı zaten mevcut, lütfen başka e-posta adresi giriniz.",parent=self.root)

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
        messagebox.showinfo("Başarılı","Üyelik işleminiz başarıyla tamamlandı.",parent=self.root) 

    def girisidondur(self):
        self.root.destroy()
       

class AnaSayfa:
    def __init__(self,root):
        self.root=root
        self.root.title("ATEŞ Otel Yönetim Sistemi")
        self.root.geometry("1550x800+0+0")
        root.resizable(0,0)

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
    main()



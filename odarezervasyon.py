from cProfile import label
from logging import root  # Kendi eklenmiş programı bozmaması için ellemiyorum.
from multiprocessing import parent_process  # Kendi eklenmiş programı bozmaması için ellemiyorum.
from tkinter import *
from tkinter import messagebox
from webbrowser import get  # Kendi eklenmiş programı bozmaması için ellemiyorum.
from PIL import Image,ImageTk
import tkinter as ttk  
import mysql.connector
from tkinter import ttk
from mysqlx import Column  # Kendi eklenmiş programı bozmaması için ellemiyorum.
from time import strftime
from datetime import datetime





class OdaRezervasyon:
    def __init__(self,root):
        self.root=root
        self.root.title("Oda Rezervasyon İşlemleri")
        self.root.geometry("1295x550+230+220")


        self.MusteriKimlikNo=StringVar()
        self.RezervasyonGirisTarihi=StringVar()
        self.RezervasyonCikisTarihi=StringVar()
        self.RezervasyonOdaTipi=StringVar()
        self.RezervasyonOdaNo=StringVar()
        self.RezervasyonGunSayisi=StringVar()
        self.RezervasyonVergiTutari=StringVar()
        self.RezervasyonKonaklamaUcreti=StringVar()
        self.RezervasyonToplamTutar=StringVar()



        # self.MusteriKimlikNumarasi=self.MusteriKimlikNo.get()
        # self.RezGirisTarihi=self.RezervasyonGirisTarihi.get()
        # self.RezCikisTarihi=self.RezervasyonCikisTarihi.get()
        # self.RezOdaTipi=self.RezervasyonOdaTipi.get()
        # self.RezOdaNo=self.RezervasyonOdaNo.get()
        # self.RezGunSayisi=self.RezervasyonGunSayisi.get()
        # self.RezVergiTutari=self.RezervasyonVergiTutari.get()
        # self.RezKonaklamaUcreti=self.RezervasyonKonaklamaUcreti.get()
        # self.RezToplamTutar=self.RezervasyonToplamTutar.get()
        


#Başlık        
        lblBaslik=Label(self.root,text="Oda Rezervasyon Bilgileri",font=("times new roman",18,"bold"),bg="black",fg="gold") 
        lblBaslik.place(x=0,y=0,width=1295,height=50)

#Sol Label Çerçevesi
        labelcercevesol=LabelFrame(self.root,bd=2,relief=RIDGE,text="Oda Rezervasyon Detayları",font=("arial",12,"bold"),padx=2,pady=4)
        labelcercevesol.place(x=5,y=50,width=425,height=490)
        

#Müşteri Kimlik No 
        lblMusteriKimlikNo=Label(labelcercevesol,text="Müşteri Kimlik No",font=("times new roman",14,"bold"))
        lblMusteriKimlikNo.grid(row=0,column=0,sticky=W)

        txtMusteriKimlikNo=ttk.Entry(labelcercevesol,textvariable=self.MusteriKimlikNo,font=("times new roman",13,"bold"),width=24)
        txtMusteriKimlikNo.grid(row=0,column=1,sticky=W) 


#Rezervasyon İçin Bİlgileri Getir Butonu
        btnRezicinKisiBilGetir=Button(labelcercevesol,command=self.RezIcinMusteriBİlgileriGetir,text="Rez. için Kişi Bilgisi Getir",font=("arial",11,"bold"),bg="black",fg="gold",width=24)   
        btnRezicinKisiBilGetir.place(x=200,y=344,width=200,height=36) 
       
#Giriş Tarihi 
        lblGirisTarihi=Label(labelcercevesol,text="Giriş Tarihi",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblGirisTarihi.grid(row=1,column=0,sticky=W)

        txtGirisTarihi=ttk.Entry(labelcercevesol,textvariable=self.RezervasyonGirisTarihi,font=("times new roman",13,"bold"),width=24)
        txtGirisTarihi.grid(row=1,column=1)


#Çıkış Tarihi 
        lblCikisTarihi=Label(labelcercevesol,text="Çıkış Tarihi",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblCikisTarihi.grid(row=2,column=0,sticky=W)

        txtCikisTarihi=ttk.Entry(labelcercevesol,textvariable=self.RezervasyonCikisTarihi,font=("times new roman",13,"bold"),width=24)
        txtCikisTarihi.grid(row=2,column=1)

#Oda Tipi
        lblOdaTipi=Label(labelcercevesol,text="Oda Tipi",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblOdaTipi.grid(row=3,column=0,sticky=W)

        baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
        imlec=baglanti.cursor()
        imlec.execute("select distinct OdaTipi from oda")
        satirlar=imlec.fetchall()


        comboOdaTipi=ttk.Combobox(labelcercevesol,textvariable=self.RezervasyonOdaTipi,font=("times new roman",13,"bold"),width=22,state="readonly")
        comboOdaTipi["value"]=satirlar
        comboOdaTipi.grid(row=3,column=1)

#Oda No
        lblOdaNo=Label(labelcercevesol,text="Oda No",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblOdaNo.grid(row=4,column=0,sticky=W)

        baglantimizz=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
        imlecimizz=baglantimizz.cursor()
        # imlecimizz.execute("select distinct OdaNo from oda where OdaDurumu='Boş' and OdaTipi=%s",(self.RezOdaTipi,))
        # imlecimizz.execute("select OdaNo from oda")

        
        imlecimizz.execute("select distinct OdaNo from oda ")
        # degerr=(self.RezervasyonOdaTipi.get(),)
        # imlecimizz.execute(sorguu,degerr)
        
        # degerimizz=(self.RezOdaTipi,)
        # imlecimizz.execute(sorgumuzz,degerimizz)
        tumsatirlar=imlecimizz.fetchall()
        
        comboOdaNo=ttk.Combobox(labelcercevesol,textvariable=self.RezervasyonOdaNo,font=("times new roman",13,"bold"),width=22,state="readonly")
        comboOdaNo["value"]=tumsatirlar
        comboOdaNo.grid(row=4,column=1)


#Kaç Gün Kalacağını Gösteren Label
        lblGunSayisi=Label(labelcercevesol,text="Kalınacak Gün Sayısı",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblGunSayisi.grid(row=5,column=0,sticky=W)

        txtGunSayisi=ttk.Entry(labelcercevesol,textvariable=self.RezervasyonGunSayisi,font=("times new roman",13,"bold"),width=24)
        txtGunSayisi.grid(row=5,column=1)

#Vergi Tutarı
        lblVergiTutari=Label(labelcercevesol,text="Vergi Tutarı",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblVergiTutari.grid(row=6,column=0,sticky=W)
            
        txtVergiTutari=ttk.Entry(labelcercevesol,textvariable=self.RezervasyonVergiTutari,font=("times new roman",13,"bold"),width=24)
        txtVergiTutari.grid(row=6,column=1)

#Konaklama Ücreti
        lblKonaklamaUcreti=Label(labelcercevesol,text="Konaklama Ücreti",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblKonaklamaUcreti.grid(row=7,column=0,sticky=W)
            
        txtKonaklamaUcreti=ttk.Entry(labelcercevesol,textvariable=self.RezervasyonKonaklamaUcreti,font=("times new roman",13,"bold"),width=24)
        txtKonaklamaUcreti.grid(row=7,column=1) 

#Toplam Tutar
        lblToplamTutar=Label(labelcercevesol,text="Toplam Tutar",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblToplamTutar.grid(row=8,column=0,sticky=W)
            
        txtToplamTutar=ttk.Entry(labelcercevesol,textvariable=self.RezervasyonToplamTutar,font=("times new roman",13,"bold"),width=24)
        txtToplamTutar.grid(row=8,column=1)

#Hesapla Butonu
        btnHesapla=Button(labelcercevesol,command=self.TutarHesapla,text="Hesapla",font=("arial",11,"bold"),bg="black",fg="gold",width=10)     
        btnHesapla.place(x=10,y=344,width=160,height=36)               

# Butonlar İçin Çerçeve
        btnCerceve=Frame(labelcercevesol,bd=0,relief=RIDGE)
        btnCerceve.place(x=45,y=400,width=320,height=40)



#Butonlar
        btnOdaRezEkle=Button(btnCerceve,text="Ekle",command=self.RezEkle,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnOdaRezEkle.grid(row=0,column=0,padx=1)

        btnOdaRezGuncelle=Button(btnCerceve,command=self.RezGuncelle,text="Güncelle",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnOdaRezGuncelle.grid(row=0,column=1,padx=1)

        btnOdaRezSil=Button(btnCerceve,command=self.RezSil,text="Sil",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnOdaRezSil.grid(row=0,column=2,padx=1)


#Sağ Label Çerçevesi
        saglabelcercevesi=LabelFrame(self.root,bd=2,relief=RIDGE,text="Arama Sonuçları ve Detayları Görüntüleme",font=("arial",12,"bold"))
        saglabelcercevesi.place(x=435,y=280,width=860,height=260)

        lblAramaFiltresi=Label(saglabelcercevesi,font=("arial",12,"bold"),text="Filtrele",bg="black",fg="gold")
        lblAramaFiltresi.grid(row=0,column=0,sticky=W,padx=2)

        self.SecilenFiltre=StringVar()
        comboAramaFiltre=ttk.Combobox(saglabelcercevesi,textvariable=self.SecilenFiltre,font=("arial",12,"bold"),width=24,state="readonly")
        comboAramaFiltre["value"]=("OdaTipi","OdaNo")
        comboAramaFiltre.grid(row=0,column=1,padx=2)

        self.txtArananKelime=StringVar()
        txtAranan=ttk.Entry(saglabelcercevesi,textvariable=self.txtArananKelime,font=("arial",13,"bold"),width=24)
        txtAranan.grid(row=0,column=2,padx=2)

        btnAra=Button(saglabelcercevesi,command=self.RezAra,text="Ara",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAra.grid(row=0,column=3,padx=1)

        btnTumunuGoster=Button(saglabelcercevesi,command=self.RezListele,text="Tümünü Göster",font=("arial",11,"bold"),bg="black",fg="gold",width=15)
        btnTumunuGoster.grid(row=0,column=4,padx=1)


#Rezervasyon Veri Tablosu Çerçevesi
        VeriTablosuCercevesi=Frame(saglabelcercevesi,bd=2,relief=RIDGE)
        VeriTablosuCercevesi.place(x=0,y=50,width=860,height=180)


        scrollX=ttk.Scrollbar(VeriTablosuCercevesi,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(VeriTablosuCercevesi,orient=VERTICAL)

        
        self.RezervasyonVeriTablosu=ttk.Treeview(VeriTablosuCercevesi,column=("OdaNo","musterikimlikno","giristarihi","cikistarihi","OdaTipi","gunsayisi"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command=self.RezervasyonVeriTablosu.xview)
        scrollY.config(command=self.RezervasyonVeriTablosu.yview)

        self.RezervasyonVeriTablosu.heading("OdaNo",text="Oda No")
        self.RezervasyonVeriTablosu.heading("musterikimlikno",text="Müşteri Kimlik No")
        self.RezervasyonVeriTablosu.heading("giristarihi",text="Giriş Tarihi")
        self.RezervasyonVeriTablosu.heading("cikistarihi",text="Çıkış Tarihi")
        self.RezervasyonVeriTablosu.heading("OdaTipi",text="Oda Tipi")
        
        self.RezervasyonVeriTablosu.heading("gunsayisi",text="Gün Sayısı")


        self.RezervasyonVeriTablosu["show"]="headings"

        self.RezervasyonVeriTablosu.column("OdaNo",width=100)
        self.RezervasyonVeriTablosu.column("musterikimlikno",width=100)
        self.RezervasyonVeriTablosu.column("giristarihi",width=100)
        self.RezervasyonVeriTablosu.column("cikistarihi",width=100)
        self.RezervasyonVeriTablosu.column("OdaTipi",width=100)
        
        self.RezervasyonVeriTablosu.column("gunsayisi",width=100)
        self.RezervasyonVeriTablosu.pack(fill=BOTH,expand=1) #Satırı ve sütunu tamamen doldurmak için kullanılır.
        self.RezervasyonVeriTablosu.bind("<ButtonRelease-1>",self.SeciliMRezervasyonBilgileriniGetir)        
        self.RezListele()




#Rezervasyon İçin Müşteri Bilgilerini Getir


    def RezIcinMusteriBİlgileriGetir(self):
        if self.MusteriKimlikNo.get()=="":
                messagebox.showerror("Hata","Lütfen Müşteri Kimlik Numarasını Giriniz.",parent=self.root)
        else:                
                baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                imlec=baglanti.cursor()
                sorgu=("select isim from musteri where kimlikno=%s")
                deger=(self.MusteriKimlikNo.get(),)
                imlec.execute(sorgu,deger)
                satir=imlec.fetchone()

                if satir==None:
                        messagebox.showerror("Hata","Girdiğiniz kimlik no bulunamadı",parent=self.root)
                else:
                        baglanti.commit()
                        baglanti.close()

                        KimlikNoBilgiCercevesi=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                        KimlikNoBilgiCercevesi.place(x=455,y=55,width=300,height=180)

#Veritabanından çekilen isim bilgisi
                        lblIsim=Label(KimlikNoBilgiCercevesi,text="İsim",font=("arial",12,"bold"))
                        lblIsim.place(x=0,y=0)

                        lbl=Label(KimlikNoBilgiCercevesi,text=satir,font=("arial",12,"bold"))
                        lbl.place(x=90,y=0)


#Veritabanından çekilen soyisim bilgisi
                        baglanti2=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                        imlec2=baglanti2.cursor()
                        sorgu2=("select soyisim from musteri where kimlikno=%s")
                        deger2= (self.MusteriKimlikNo.get(),)
                        imlec2.execute(sorgu2,deger2)
                        satir2=imlec2.fetchone()


                        lblSoyisim=Label(KimlikNoBilgiCercevesi,text="Soyad",font=("arial",12,"bold"))
                        lblSoyisim.place(x=0,y=30)

                        lbl2=Label(KimlikNoBilgiCercevesi,text=satir2,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=30)


#Veritabanından çekilen cinsiyet bilgisi
                        baglanti3=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                        imlec3=baglanti3.cursor()
                        sorgu3=("select cinsiyet from musteri where kimlikno=%s")
                        deger3= (self.MusteriKimlikNo.get(),)
                        imlec3.execute(sorgu3,deger3)
                        satir3=imlec3.fetchone()


                        lblCinsiyet=Label(KimlikNoBilgiCercevesi,text="Cinsiyet",font=("arial",12,"bold"))
                        lblCinsiyet.place(x=0,y=60)

                        lbl3=Label(KimlikNoBilgiCercevesi,text=satir3,font=("arial",12,"bold"))
                        lbl3.place(x=90,y=60)
        
 

#Veritabanından çekilen uyruk bilgisi
                        baglanti4=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                        imlec4=baglanti4.cursor()
                        sorgu4=("select uyruk from musteri where kimlikno=%s")
                        deger4= (self.MusteriKimlikNo.get(),)
                        imlec4.execute(sorgu4,deger4)
                        satir4=imlec4.fetchone()


                        lblUyruk=Label(KimlikNoBilgiCercevesi,text="Uyruk",font=("arial",12,"bold"))
                        lblUyruk.place(x=0,y=90)

                        lbl4=Label(KimlikNoBilgiCercevesi,text=satir4,font=("arial",12,"bold"))
                        lbl4.place(x=90,y=90)


#Veritabanından çekilen e-posta bilgisi
                        baglanti5=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                        imlec5=baglanti5.cursor()
                        sorgu5=("select eposta from musteri where kimlikno=%s")
                        deger5= (self.MusteriKimlikNo.get(),)
                        imlec5.execute(sorgu5,deger5)
                        satir5=imlec5.fetchone()


                        lblEposta=Label(KimlikNoBilgiCercevesi,text="E-posta",font=("arial",12,"bold"))
                        lblEposta.place(x=0,y=120)

                        lbl5=Label(KimlikNoBilgiCercevesi,text=satir5,font=("arial",12,"bold"))
                        lbl5.place(x=90,y=120)





#Rezervasyon ekleme fonksiyonu

    def RezEkle(self):
            if self.RezervasyonOdaNo.get()=="" or self.MusteriKimlikNo.get()=="" or self.RezervasyonGirisTarihi.get()=="" or self.RezervasyonCikisTarihi.get()=="" or self.RezervasyonOdaTipi.get()=="" or self.RezervasyonGunSayisi.get()=="" or self.RezervasyonVergiTutari.get()=="" or self.RezervasyonKonaklamaUcreti.get()=="" or self.RezervasyonToplamTutar.get()=="":
                messagebox.showerror("Hata","Tüm alanların doldurulması zorunludur.",parent=self.root)
            else:
                try:
                        baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                        imlec=baglanti.cursor()
                        imlec.execute("insert into odarezervasyon values(%s,%s,%s,%s,%s,%s)",(
    
                                                                        self.RezervasyonOdaNo.get(),
                                                                        self.MusteriKimlikNo.get(),
                                                                        self.RezervasyonGirisTarihi.get(),
                                                                        self.RezervasyonCikisTarihi.get(),
                                                                        self.RezervasyonOdaTipi.get(),
                                                                        
                                                                        self.RezervasyonGunSayisi.get()
                                                                        



                                                                                        ))                        
    
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        



                                                                                       

                        # seciliodayidoluyapmasorgusu=("update oda o inner join odarezervasyon odarez on o.OdaNo = odarez.OdaNo set OdaDurumu='Dolu' where odarez.OdaNo=%s")
                        # seciliodadegeri=(self.RezervasyonOdaNo.get())
                        # imlec.execute(seciliodayidoluyapmasorgusu,seciliodadegeri)                                                                        


                        baglanti.commit()
                        self.RezListele()
                        baglanti.close()
                        messagebox.showinfo("Başarılı","Rezervasyon eklendi.",parent=self.root)
                        self.RezervasyonBilgileriniSifirla()
                except Exception as es:
                        messagebox.showwarning("Uyarı","Rezervasyon eklenemedi.",parent=self.root)


    def RezListele(self):
                 baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                 imlec=baglanti.cursor()
                 imlec.execute("select * from odarezervasyon")
                 tumsatirlar=imlec.fetchall()

                 if len(tumsatirlar)!=0:
                     self.RezervasyonVeriTablosu.delete(*self.RezervasyonVeriTablosu.get_children())
                     for i in tumsatirlar:
                         self.RezervasyonVeriTablosu.insert("",END,values=i)
                     baglanti.commit()
                     baglanti.close()            


    def RezervasyonBilgileriniSifirla(self):
        self.MusteriKimlikNo.set("")
        self.RezervasyonGirisTarihi.set("")
        self.RezervasyonCikisTarihi.set("")
        self.RezervasyonOdaTipi.set("")
        self.RezervasyonOdaNo.set("")
        self.RezervasyonGunSayisi.set("")
        self.RezervasyonVergiTutari.set("")
        self.RezervasyonKonaklamaUcreti.set("")
        self.RezervasyonToplamTutar.set("")
        
    def SeciliMRezervasyonBilgileriniGetir(self,event=""):
        satirimleci=self.RezervasyonVeriTablosu.focus()
        icerik=self.RezervasyonVeriTablosu.item(satirimleci)
        satir=icerik["values"]

        self.RezervasyonOdaNo.set(satir[0])
        self.MusteriKimlikNo.set(satir[1])
        self.RezervasyonGirisTarihi.set(satir[2])
        self.RezervasyonCikisTarihi.set(satir[3])
        self.RezervasyonOdaTipi.set(satir[4])
        self.RezervasyonGunSayisi.set(satir[5])
        


    def RezGuncelle(self):
        if self.RezervasyonOdaNo.get()=="" or self.MusteriKimlikNo.get()=="" or self.RezervasyonGirisTarihi.get()=="" or self.RezervasyonCikisTarihi.get()=="" or self.RezervasyonOdaTipi.get()=="" or self.RezervasyonGunSayisi.get()=="" or self.RezervasyonVergiTutari.get()=="" or self.RezervasyonKonaklamaUcreti.get()=="" or self.RezervasyonToplamTutar.get()=="":
            messagebox.showerror("Hata","Tüm alanların doldurulması zorunludur.",parent=self.root)

        else:
            baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
            imlec=baglanti.cursor()
        #     rezguncellemesorgusu=("update odarezervasyon set giristarihi=%s,cikistarihi=%s,OdaTipi=%s,gunsayisi=%s where musterikimlikno=%s")
            imlec.execute("update odarezervasyon set OdaNo=%s,giristarihi=%s,cikistarihi=%s,OdaTipi=%s,gunsayisi=%s where musterikimlikno=%s",(

                                                                                                                                             self.RezervasyonOdaNo.get(),
                                                                                                                                             self.RezervasyonGirisTarihi.get(),
                                                                                                                                             self.RezervasyonCikisTarihi.get(),                                                       
                                                                                                                                             self.RezervasyonOdaTipi.get(),
                                                                                                                                             
                                                                                                                                             self.RezervasyonGunSayisi.get(),
                                                                                                                                             self.MusteriKimlikNo.get()

                                                                                                                                                        ))

                                                                                                                                             
                                                                                                                                                                                                    
                                                                                                                                             
                                                                                                                                             
                                                                                                                                             
                                                                                                                                             

        #     digersorgu=("select * from odarezervasyon where musterikimlikno=%s")
        #     degerimiz=(self.MusteriKimlikNumarasi,)                                                                                                                                          
        #     imlec.execute(digersorgu,degerimiz)
        #     VeritabanindanOkunanSatir=imlec.fetchone()
        #     VeritabanindanOkunanOdaNo=VeritabanindanOkunanSatir[5]

        #     if VeritabanindanOkunanOdaNo != self.RezOdaNo:
        #         sayac = 0
        #         while (sayac < 2):
        #                 GuncellemeSorusu=messagebox.askyesno("Soru","Bu rezervasyonun oda numarasını güncellemek istediğinizden emin misiniz?",parent=self.root)
        #                 if GuncellemeSorusu>0:
        #                         aynirezicinsecilmisodalar=list()
        #                         digersorgu2=("select * from odarezervasyon where musterikimlikno=%s")
        #                         degerimiz2=(self.MusteriKimlikNumarasi,)
        #                         imlec.execute(digersorgu2,degerimiz2)
        #                         okunansatir=imlec.fetchone()
        #                         uye=okunansatir[5]
        #                         uye=aynirezicinsecilmisodalar[sayac]
                                

        #                         digersorgu3=("update oda o inner join odarezervasyon odarez on o.OdaNo = odarez.OdaNo set OdaDurumu='Boş' where odarez.OdaNo=%s ")
        #                         degerimiz3=(uye,)
        #                         imlec.execute(digersorgu3,degerimiz3)

        #                         digersorgu4=("update odarezervasyon set OdaNo=%s where musterikimlikno=%s")
        #                         degerimiz4=(self.RezOdaNo,self.MusteriKimlikNumarasi)
        #                         imlec.execute(digersorgu4,degerimiz4)

        #                         digersorgu5=("update oda o inner join odarezervasyon odarez on o.OdaNo=odarez.OdaNo set OdaDurumu='Dolu' where odarez.OdaNo=%s")
        #                         degerimiz5=(self.RezOdaNo,)
        #                         imlec.execute(digersorgu5,degerimiz5)

        #                         sayac=sayac+1


                                
             
            
                                                                        
                    


                



            baglanti.commit()
            self.RezListele()
            baglanti.close()
            messagebox.showinfo("Başarılı","Rezervasyon bilgileri başarıyla güncellendi.",parent=self.root)
            self.TutarHesapla()
            self.RezervasyonBilgileriniSifirla()





    def RezSil(self):
        SilmeSorusu=messagebox.askyesno("Soru","İlgili kaydı silmek istediğinizden emin misiniz?",parent=self.root)
        if SilmeSorusu>0:
            baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
            imlec=baglanti.cursor()

        #     imlec.execute("select * from odarezervasyon where musterikimlikno=%s",(self.MusteriKimlikNumarasi))
        #     OkunanSatir=imlec.fetchone()
        #     silinecekOdaNo=OkunanSatir[5]

        #     imlec.execute("update oda o inner join odarezervasyon odarez on o.OdaNo = odarez.OdaNo set OdaDurumu='Boş' where odarez.OdaNo=%s",(silinecekOdaNo))

            sorgu="delete from odarezervasyon where musterikimlikno=%s"
            deger=(self.MusteriKimlikNo.get(),)
            imlec.execute(sorgu,deger)

        else:
            if not SilmeSorusu:
                return 

        baglanti.commit()
        self.RezListele()
        baglanti.close()
        self.RezervasyonBilgileriniSifirla()

 

    def TutarHesapla(self):
        girist=self.RezervasyonGirisTarihi.get()
        cikist=self.RezervasyonCikisTarihi.get()
        girist=datetime.strptime(girist,"%d/%m/%Y")
        cikist=datetime.strptime(cikist,"%d/%m/%Y")
        self.RezervasyonGunSayisi.set(abs(cikist-girist).days)

        if(self.RezervasyonOdaTipi.get()=="{Tek Kişilik Oda}"):
           tekkisilikkonaklamaucretibirimfiyat=10000
           tekkisilikgunsayisi=int(self.RezervasyonGunSayisi.get())
           tekkisilikkonaklamaucreti=tekkisilikkonaklamaucretibirimfiyat*tekkisilikgunsayisi
           tekkisilikvergitutari=tekkisilikkonaklamaucreti*0.18
           tekkisiliktoplamtutar=tekkisilikkonaklamaucreti+tekkisilikvergitutari

           self.RezervasyonVergiTutari.set(tekkisilikvergitutari)
           self.RezervasyonKonaklamaUcreti.set(tekkisilikkonaklamaucreti)
           self.RezervasyonToplamTutar.set(tekkisiliktoplamtutar)



        elif(self.RezervasyonOdaTipi.get()=="{Çift Kişilik Oda}"):
           ciftkisilikkonaklamaucretibirimfiyat=18000
           ciftkisilikgunsayisi=int(self.RezervasyonGunSayisi.get())
           ciftkisilikkonaklamaucreti=ciftkisilikkonaklamaucretibirimfiyat*ciftkisilikgunsayisi
           ciftkisilikvergitutari=ciftkisilikkonaklamaucreti*0.18
           ciftkisiliktoplamtutar=ciftkisilikkonaklamaucreti+ciftkisilikvergitutari

           self.RezervasyonVergiTutari.set(ciftkisilikvergitutari)
           self.RezervasyonKonaklamaUcreti.set(ciftkisilikkonaklamaucreti)
           self.RezervasyonToplamTutar.set(ciftkisiliktoplamtutar)

           
                   

        elif(self.RezervasyonOdaTipi.get()=="{Tek Kişilik Kral Odası}"):
           tekkisilikkralodasikonaklamaucretibirimfiyat=15000
           tekkisilikkralodasigunsayisi=int(self.RezervasyonGunSayisi.get())
           tekkisilikkralodasikonaklamaucreti=tekkisilikkralodasikonaklamaucretibirimfiyat*tekkisilikkralodasigunsayisi
           tekkisilikkralodasivergitutari=tekkisilikkralodasikonaklamaucreti*0.18
           tekkisilikkralodasitoplamtutar=tekkisilikkralodasikonaklamaucreti+tekkisilikkralodasivergitutari

           self.RezervasyonVergiTutari.set(tekkisilikkralodasivergitutari)
           self.RezervasyonKonaklamaUcreti.set(tekkisilikkralodasikonaklamaucreti)
           self.RezervasyonToplamTutar.set(tekkisilikkralodasitoplamtutar)



        elif(self.RezervasyonOdaTipi.get()=="{Çift Kişilik Kral Odası}"):
           ciftkisilikkralodasikonaklamaucretibirimfiyat=25000
           ciftkisilikkralodasigunsayisi=int(self.RezervasyonGunSayisi.get())
           ciftkisilikkralodasikonaklamaucreti=ciftkisilikkralodasikonaklamaucretibirimfiyat*ciftkisilikkralodasigunsayisi
           ciftkisilikkralodasivergitutari=ciftkisilikkralodasikonaklamaucreti*0.18
           ciftkisilikkralodasitoplamtutar=ciftkisilikkralodasikonaklamaucreti+ciftkisilikkralodasivergitutari

           self.RezervasyonVergiTutari.set(ciftkisilikkralodasivergitutari)
           self.RezervasyonKonaklamaUcreti.set(ciftkisilikkralodasikonaklamaucreti)
           self.RezervasyonToplamTutar.set(ciftkisilikkralodasitoplamtutar)







    def RezAra(self):
        baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
        imlec=baglanti.cursor()

        imlec.execute("select * from odarezervasyon where "+str(self.SecilenFiltre.get())+" LIKE '%"+str(self.txtArananKelime.get())+"%'")
        
        
        


        satirlar=imlec.fetchall()
        if len(satirlar)!=0:
            self.RezervasyonVeriTablosu.delete(*self.RezervasyonVeriTablosu.get_children())
            for i in satirlar:
                self.RezervasyonVeriTablosu.insert("",END,values=i)
            baglanti.commit()
            baglanti.close()










if __name__=="__main__":
    root=Tk()
    root.resizable(0,0)
    nsn=OdaRezervasyon(root)
    root.mainloop()
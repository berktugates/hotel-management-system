from cProfile import label
from tkinter import *
from tkinter import messagebox
from webbrowser import get   # Kendi eklenmiş programı bozmaması için ellemiyorum.
from PIL import Image,ImageTk
import tkinter as ttk  
import mysql.connector
from tkinter import ttk
from mysqlx import Column  # Kendi eklenmiş programı bozmaması için ellemiyorum.
from setuptools import Command  # Kendi eklenmiş programı bozmaması için ellemiyorum.




class Musteri:
    def __init__(self,root):
        self.root=root
        self.root.title("Müşteri İşlemleri")
        self.root.geometry("1295x550+230+220")


        self.MusteriAdi=StringVar()
        self.MusteriSoyadi=StringVar()
        self.MusteriCinsiyeti=StringVar()
        self.MusteriTelefonNo=StringVar()
        self.MusteriEPosta=StringVar()
        self.MusteriUyruk=StringVar()
        self.MusteriKimlikTipi=StringVar()
        self.MusteriKimlikNo=StringVar()


#Başlık        
        lblBaslik=Label(self.root,text="Müşteri Bilgileri",font=("times new roman",18,"bold"),bg="black",fg="gold") 
        lblBaslik.place(x=0,y=0,width=1295,height=50)

#Label Çerçevesi
        labelcercevesol=LabelFrame(self.root,bd=2,relief=RIDGE,text="Müşteri Detayları",font=("arial",12,"bold"),padx=2)
        labelcercevesol.place(x=5,y=50,width=425,height=490)

# Labellar ve kullanıcı girişleri

    # Müşteri isim 
        lblMusteriIsim=Label(labelcercevesol,font=("arial",12,"bold"),text="İsim:",padx=2,pady=6)
        lblMusteriIsim.grid(row=0,column=0,sticky=W)
        txtMusteriIsim=ttk.Entry(labelcercevesol,textvariable=self.MusteriAdi,font=("arial",13,"bold"),width=29)
        txtMusteriIsim.grid(row=0,column=1)

    # Müşteri Soyisim
        lblMusteriSoyad=Label(labelcercevesol,font=("arial",12,"bold"),text="Soyad:",padx=2,pady=6)
        lblMusteriSoyad.grid(row=1,column=0,sticky=W)
        txtMusteriSoyad=ttk.Entry(labelcercevesol,textvariable=self.MusteriSoyadi,font=("arial",13,"bold"),width=29)
        txtMusteriSoyad.grid(row=1,column=1)

    # Cinsiyet Combo Box
        lblCinsiyet=Label(labelcercevesol,font=("arial",12,"bold"),text="Cinsiyet:",padx=2,pady=6)
        lblCinsiyet.grid(row=2,column=0,sticky=W)

        comboMusteriCinsiyet=ttk.Combobox(labelcercevesol,textvariable=self.MusteriCinsiyeti,font=("arial",12,"bold"),width=27,state="readonly")
        comboMusteriCinsiyet["value"]=("Erkek","Kadın","Diğer")
        comboMusteriCinsiyet.grid(row=2,column=1)

    # Telefon Numarası
        lblMusteriTelefonNo=Label(labelcercevesol,font=("arial",12,"bold"),text="Telefon Numarası:",padx=2,pady=6)
        lblMusteriTelefonNo.grid(row=3,column=0,sticky=W)

        txtMusteriTelefonNo=ttk.Entry(labelcercevesol,textvariable=self.MusteriTelefonNo,font=("arial",12,"bold"),width=29)
        txtMusteriTelefonNo.grid(row=3,column=1)

    # E-Posta
        lblMusteriEposta=Label(labelcercevesol,font=("arial",12,"bold"),text="E-Posta:",padx=2,pady=6)
        lblMusteriEposta.grid(row=4,column=0,sticky=W)

        txtMusteriEposta=ttk.Entry(labelcercevesol,textvariable=self.MusteriEPosta,font=("arial",12,"bold"),width=29)
        txtMusteriEposta.grid(row=4,column=1)

    # Uyruk
        lblMusteriUyruk=Label(labelcercevesol,font=("arial",12,"bold"),text="Uyruk:",padx=2,pady=6)
        lblMusteriUyruk.grid(row=5,column=0,sticky=W)
        txtMusteriUyruk=ttk.Entry(labelcercevesol,textvariable=self.MusteriUyruk,font=("arial",13,"bold"),width=29)
        txtMusteriUyruk.grid(row=5,column=1)    

    # Kimlik Tipi Combo Box
        lblMusteriKimlikTipi=Label(labelcercevesol,font=("arial",12,"bold"),text="Kimlik Tipi:",padx=2,pady=6)
        lblMusteriKimlikTipi.grid(row=6,column=0,sticky=W)

        comboMusteriKimlikTipi=ttk.Combobox(labelcercevesol,textvariable=self.MusteriKimlikTipi,font=("arial",12,"bold"),width=27,state="readonly")
        comboMusteriKimlikTipi["value"]=("TC Kimlik","Pasaport","Ehliyet")
        comboMusteriKimlikTipi.grid(row=6,column=1)

    # Kimlik Tipi No
        lblMusteriKimlikNo=Label(labelcercevesol,font=("arial",12,"bold"),text="Kimlik No:",padx=2,pady=6)
        lblMusteriKimlikNo.grid(row=7,column=0,sticky=W)
        txtMusteriKimlikNo=ttk.Entry(labelcercevesol,textvariable=self.MusteriKimlikNo,font=("arial",13,"bold"),width=29)
        txtMusteriKimlikNo.grid(row=7,column=1)



#Butonlar
        #Müşteri Kaydet
        btnMusteriKaydet=Button(labelcercevesol,command=self.MusteriEkle,text="Kaydet",font=("arial",11,"bold"),bg="black",fg="gold",width=10)        
        btnMusteriKaydet.place(x=45,y=320)

        #Müşteri Güncelle
        btnMusteriGuncelle=Button(labelcercevesol,command=self.MusteriGuncelle,text="Güncelle",font=("arial",11,"bold"),bg="black",fg="gold",width=10)       
        btnMusteriGuncelle.place(x=155,y=320)

        #Müşteri Sil
        btnMusteriSil=Button(labelcercevesol,text="Sil",command=self.MusteriSil,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnMusteriSil.place(x=265,y=320)


#MySQL Veri Tablo Çerçevesi
        TabloCercevesi=LabelFrame(self.root,bd=2,relief=RIDGE,text="Detayları Görüntüleme ve Arama",font=("arial",12,"bold"),padx=2)
        TabloCercevesi.place(x=435,y=50,width=860,height=490)


        lblAramaFiltresi=Label(TabloCercevesi,font=("arial",12,"bold"),text="Filtrele:",bg="black",fg="gold")
        lblAramaFiltresi.grid(row=0,column=0,sticky=W,padx=2)

        self.SecilenAramaFiltresi=StringVar()
        comboFiltrele=ttk.Combobox(TabloCercevesi,textvariable=self.SecilenAramaFiltresi,font=("arial",12,"bold"),width=24,state="readonly")
        comboFiltrele["value"]=("İsim","Uyruk","Cinsiyet","EPosta")
        comboFiltrele.grid(row=0,column=1,padx=2)

        self.ArananIfade=StringVar()
        txtArama=ttk.Entry(TabloCercevesi,textvariable=self.ArananIfade,font=("arial",13,"bold"),width=24)
        txtArama.grid(row=0,column=2,padx=2)

        btnAra=Button(TabloCercevesi,command=self.MusteriAra,text="Ara",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAra.grid(row=0,column=3,padx=20)

        btnHepsiniListele=Button(TabloCercevesi,command=self.MusteriListele,text="Tümünü Listele",font=("arial",11,"bold"),bg="black",fg="gold",width=15)
        btnHepsiniListele.grid(row=0,column=4,padx=1)



#Müşteri Veri Tablosu Çerçevesi
        VeriTablosuCercevesi=Frame(TabloCercevesi,bd=2,relief=RIDGE)
        VeriTablosuCercevesi.place(x=0,y=50,width=860,height=350)


        scrollX=ttk.Scrollbar(VeriTablosuCercevesi,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(VeriTablosuCercevesi,orient=VERTICAL)

        
        self.MusteriVeriTablosu=ttk.Treeview(VeriTablosuCercevesi,column=("isim","soyisim","cinsiyet","telefonno","eposta","uyruk","kimliktipi","kimlikno"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command=self.MusteriVeriTablosu.xview)
        scrollY.config(command=self.MusteriVeriTablosu.yview)

        self.MusteriVeriTablosu.heading("isim",text="İsim")
        self.MusteriVeriTablosu.heading("soyisim",text="Soyad")
        self.MusteriVeriTablosu.heading("cinsiyet",text="Cinsiyet")
        self.MusteriVeriTablosu.heading("telefonno",text="Telefon No")
        self.MusteriVeriTablosu.heading("eposta",text="E-Posta")
        self.MusteriVeriTablosu.heading("uyruk",text="Uyruk")
        self.MusteriVeriTablosu.heading("kimliktipi",text="Kimlik Tipi")
        self.MusteriVeriTablosu.heading("kimlikno",text="Kimlik No")

        self.MusteriVeriTablosu["show"]="headings"

        self.MusteriVeriTablosu.column("isim",width=100)
        self.MusteriVeriTablosu.column("soyisim",width=100)
        self.MusteriVeriTablosu.column("cinsiyet",width=100)
        self.MusteriVeriTablosu.column("telefonno",width=100)
        self.MusteriVeriTablosu.column("eposta",width=100)
        self.MusteriVeriTablosu.column("uyruk",width=100)
        self.MusteriVeriTablosu.column("kimliktipi",width=100)
        self.MusteriVeriTablosu.column("kimlikno",width=100)
        
       



        self.MusteriVeriTablosu.pack(fill=BOTH,expand=1)
        self.MusteriVeriTablosu.bind("<ButtonRelease-1>",self.SeciliMusteriBilgileriniGetir)
        self.MusteriListele()



    def MusteriEkle(self):
        if self.MusteriAdi.get()=="" or self.MusteriSoyadi.get()=="" or self.MusteriCinsiyeti.get()=="" or self.MusteriTelefonNo.get()=="" or self.MusteriEPosta.get()=="" or self.MusteriUyruk.get()=="" or self.MusteriKimlikTipi.get()=="" or self.MusteriKimlikNo.get()=="":
            messagebox.showerror("Hata","Tüm alanların doldurulması zorunludur.",parent=self.root)
        else:
            try:
                baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                imlec=baglanti.cursor()
                imlec.execute("insert into musteri values(%s,%s,%s,%s,%s,%s,%s,%s)",(
    
                                                                        self.MusteriAdi.get(),
                                                                        self.MusteriSoyadi.get(),
                                                                        self.MusteriCinsiyeti.get(),
                                                                        self.MusteriTelefonNo.get(),
                                                                        self.MusteriEPosta.get(),
                                                                        self.MusteriUyruk.get(),
                                                                        self.MusteriKimlikTipi.get(),
                                                                        self.MusteriKimlikNo.get()



                                                                                        ))        


                baglanti.commit()
                self.MusteriListele()
                baglanti.close()
                messagebox.showinfo("Başarılı","Müşteri sisteme eklendi.",parent=self.root)
                self.MusteriBilgileriniSifirla()
            except Exception as es:
                messagebox.showwarning("Uyarı","Bir şeyler ters gitti. Lütfen yeniden deneyiniz:{str(es)}",parent=self.root)



    def MusteriListele(self):
                 baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                 imlec=baglanti.cursor()
                 imlec.execute("select * from musteri")
                 tumsatirlar=imlec.fetchall()

                 if len(tumsatirlar)!=0:
                     self.MusteriVeriTablosu.delete(*self.MusteriVeriTablosu.get_children())
                     for sayac in tumsatirlar:

                         self.MusteriVeriTablosu.insert("",END,values=sayac)
                     baglanti.commit()
                     baglanti.close() 


    def SeciliMusteriBilgileriniGetir(self,event=""):
        satirimleci=self.MusteriVeriTablosu.focus()
        icerik=self.MusteriVeriTablosu.item(satirimleci)
        satir=icerik["values"]

        self.MusteriAdi.set(satir[0])
        self.MusteriSoyadi.set(satir[1])
        self.MusteriCinsiyeti.set(satir[2])
        self.MusteriTelefonNo.set(satir[3])
        self.MusteriEPosta.set(satir[4])
        self.MusteriUyruk.set(satir[5])
        self.MusteriKimlikTipi.set(satir[6])
        self.MusteriKimlikNo.set(satir[7])
        

    def MusteriGuncelle(self):

        if self.MusteriAdi.get()=="" or self.MusteriSoyadi.get()=="" or self.MusteriCinsiyeti.get()=="" or self.MusteriTelefonNo.get()=="" or self.MusteriEPosta.get()=="" or self.MusteriUyruk.get()=="" or self.MusteriKimlikTipi.get()=="" or self.MusteriKimlikNo.get()=="":
            messagebox.showerror("Hata","Tüm alanların doldurulması zorunludur.",parent=self.root)
            

        else:
            baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
            imlec=baglanti.cursor()

            
            imlec.execute("update musteri set isim=%s,soyisim=%s,cinsiyet=%s,telefonno=%s,eposta=%s,uyruk=%s,kimliktipi=%s,kimlikno=%s where eposta=%s",(

                                                                                                                                             self.MusteriAdi.get(),
                                                                                                                                             self.MusteriSoyadi.get(),                                                       
                                                                                                                                             self.MusteriCinsiyeti.get(),
                                                                                                                                             self.MusteriTelefonNo.get(),
                                                                                                                                             self.MusteriEPosta.get(),
                                                                                                                                             self.MusteriUyruk.get(),
                                                                                                                                             self.MusteriKimlikTipi.get(),
                                                                                                                                             self.MusteriKimlikNo.get(),
                                                                                                                                             self.MusteriEPosta.get()
                                                                                                                                        
                                                                                                                                                        ))


        
            baglanti.commit()
            self.MusteriListele()
            baglanti.close()
            messagebox.showinfo("Başarılı","Müşteri bilgileri başarıyla güncellendi.",parent=self.root)
            self.MusteriBilgileriniSifirla()
        

    def MusteriSil(self):
        SilmeSorusu=messagebox.askyesno("Soru","İlgili kaydı silmek istediğinizden emin misiniz?",parent=self.root)
        if SilmeSorusu>0:
            baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
            imlec=baglanti.cursor()
            sorgu="delete from musteri where eposta=%s"
            deger=(self.MusteriEPosta.get(),)
            imlec.execute(sorgu,deger)

        else:
            if not SilmeSorusu:
                return 

        baglanti.commit()
        self.MusteriListele()
        baglanti.close()
        self.MusteriBilgileriniSifirla()


    def MusteriBilgileriniSifirla(self):
        self.MusteriAdi.set("")
        self.MusteriSoyadi.set("")
        self.MusteriCinsiyeti.set("")
        self.MusteriTelefonNo.set("")
        self.MusteriEPosta.set("")
        self.MusteriUyruk.set("")
        self.MusteriKimlikTipi.set("")
        self.MusteriKimlikNo.set("")

    def MusteriAra(self):
        baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
        imlec=baglanti.cursor()

        imlec.execute("select * from musteri where "+str(self.SecilenAramaFiltresi.get())+" LIKE '%"+str(self.ArananIfade.get())+"%'")
        
        
        
        satirlar=imlec.fetchall()
        if len(satirlar)!=0:
            self.MusteriVeriTablosu.delete(*self.MusteriVeriTablosu.get_children())
            for i in satirlar:
                self.MusteriVeriTablosu.insert("",END,values=i)


        else:
            messagebox.showerror("Hata","Girdiğiniz terimlere uygun sonuç bulunamamıştır.")

            baglanti.commit()
            baglanti.close()




if __name__ == "__main__":     
    root=Tk()
    root.resizable(0,0) #Ekranın büyütme seçeneği devre dışı bırakıldı.
    nsn=Musteri(root)
    root.mainloop()















    
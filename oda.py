from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random  # Kendi eklenmiş programı bozmaması için ellemiyorum.
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox 
from pyparsing import col  # Kendi eklenmiş programı bozmaması için ellemiyorum.



class Oda:
    def __init__(self,root):
        self.root=root
        self.root.title("Oda İşlemleri")
        self.root.geometry("1295x550+230+220")

        self.OdaKatNo=StringVar()
        self.OdaNo=StringVar()
        self.OdaTipi=StringVar()



#Başlık        
        lblBaslik=Label(self.root,text="Oda Bilgileri",font=("times new roman",18,"bold"),bg="black",fg="gold") 
        lblBaslik.place(x=0,y=0,width=1295,height=50)

#Sol Label Çerçevesi
        labelcercevesol=LabelFrame(self.root,bd=2,relief=RIDGE,text="Oda Detayları",font=("arial",12,"bold"),padx=2,pady=4)
        labelcercevesol.place(x=5,y=50,width=425,height=490)


#Oda No
        lblOdaNo=Label(labelcercevesol,text="Oda No",font=("arial",12,"bold"),padx=2,pady=6)
        lblOdaNo.grid(row=0,column=0,sticky=W,padx=20)

        txtOdaNo=ttk.Entry(labelcercevesol,textvariable=self.OdaNo,font=("arial",13,"bold"),width=20)
        txtOdaNo.grid(row=0,column=1,sticky=W)




#Odanın katı
        lblKat=Label(labelcercevesol,text="Kat",font=("arial",12,"bold"),padx=2,pady=6)
        lblKat.grid(row=1,column=0,sticky=W,padx=20)

        txtKat=ttk.Entry(labelcercevesol,textvariable=self.OdaKatNo,font=("arial",13,"bold"),width=20)
        txtKat.grid(row=1,column=1,sticky=W)



#Oda Tipi
        lblOdaTipi=Label(labelcercevesol,text="Oda Tipi",font=("arial",12,"bold"),padx=2,pady=6)
        lblOdaTipi.grid(row=2,column=0,sticky=W,padx=20)

        txtOdaTipi=ttk.Entry(labelcercevesol,textvariable=self.OdaTipi,font=("arial",13,"bold"),width=20)
        txtOdaTipi.grid(row=2,column=1,sticky=W)



#Butonlar için Çerçeve
        btnCerceve=Frame(labelcercevesol,bd=0,relief=RIDGE)
        btnCerceve.place(x=0,y=200,width=412,height=40)



#Butonlar
        btnOdaEkle=Button(btnCerceve,command=self.OdaEkle,text="Ekle",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnOdaEkle.grid(row=0,column=0,padx=1)

        btnOdaGuncelle=Button(btnCerceve,command=self.OdaGuncelle,text="Güncelle",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnOdaGuncelle.grid(row=0,column=1,padx=1)


        btnOdaSil=Button(btnCerceve,command=self.OdaSil,text="Sil",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnOdaSil.grid(row=0,column=2,padx=1)


#Sağ Tablo Çerçevesi

        SagTabloCercevesi=LabelFrame(self.root,bd=2,relief=RIDGE,text="Oda Detaylarını Görüntüleme",font=("arial",12,"bold"))
        SagTabloCercevesi.place(x=440,y=55,width=850,height=490)

        scrollX=ttk.Scrollbar(SagTabloCercevesi,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(SagTabloCercevesi,orient=VERTICAL)
        self.OdaVeriTablosu=ttk.Treeview(SagTabloCercevesi,column=("OdaNo","kat","OdaTipi"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command=self.OdaVeriTablosu.xview)
        scrollY.config(command=self.OdaVeriTablosu.yview)      

        

        self.OdaVeriTablosu.heading("OdaNo",text="OdaNo")
        self.OdaVeriTablosu.heading("kat",text="Kat")
        self.OdaVeriTablosu.heading("OdaTipi",text="OdaTipi")
        self.OdaVeriTablosu["show"]="headings"



        self.OdaVeriTablosu.column("OdaNo",width=100)
        self.OdaVeriTablosu.column("kat",width=100)
        self.OdaVeriTablosu.column("OdaTipi",width=100)
        self.OdaVeriTablosu.pack(fill=BOTH,expand=1)
        self.OdaVeriTablosu.bind("<ButtonRelease-1>",self.SeciliOdaBilgileriniGetir)
        self.OdaListele()




#Oda ekleme fonksiyonu

    def OdaEkle(self):
            if self.OdaKatNo.get()=="" or self.OdaNo.get()=="" or self.OdaTipi.get()=="" :
                messagebox.showerror("Hata","Tüm alanların doldurulması zorunludur.",parent=self.root)
            else:
                try:
                        baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                        imlec=baglanti.cursor()
                        imlec.execute("insert into oda(OdaNo,kat,OdaTipi) values(%s,%s,%s)",(
    
                                                                        self.OdaNo.get(),
                                                                        self.OdaKatNo.get(),
                                                                        self.OdaTipi.get()
                                                                        
                                                                        



                                                                        ))        


                        baglanti.commit()
                        self.OdaListele()
                        baglanti.close()
                        messagebox.showinfo("Başarılı","Oda eklendi.",parent=self.root)
                        self.OdaBilgileriniSifirla()
                        
                except Exception as es:
                        messagebox.showwarning("Uyarı","Oda eklenemedi.Lütfen tekrar deneyiniz.",parent=self.root)


    def OdaListele(self):
                 baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
                 imlec=baglanti.cursor()
                 imlec.execute("select * from oda")
                 tumsatirlar=imlec.fetchall()

                 if len(tumsatirlar)!=0:
                     self.OdaVeriTablosu.delete(*self.OdaVeriTablosu.get_children())
                     for i in tumsatirlar:
                         self.OdaVeriTablosu.insert("",END,values=i)
                     baglanti.commit()
                     baglanti.close()


    def SeciliOdaBilgileriniGetir(self,event=""):
        satirimleci=self.OdaVeriTablosu.focus()
        icerik=self.OdaVeriTablosu.item(satirimleci)
        satir=icerik["values"]

        self.OdaNo.set(satir[0])
        self.OdaKatNo.set(satir[1])
        self.OdaTipi.set(satir[2])
        
    def OdaGuncelle(self):
        if self.OdaKatNo.get()=="" or self.OdaNo.get()=="" or self.OdaTipi.get()=="" :
            messagebox.showerror("Hata","Tüm alanların doldurulması zorunludur.",parent=self.root)

        else:
            messagebox.showerror("Uyarı","Oda No alanı güncellenememektedir.")    
            baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
            imlec=baglanti.cursor()








            imlec.execute("update oda set kat=%s,OdaTipi=%s where OdaNo=%s",(

                                                                                self.OdaKatNo.get(),                                                      
                                                                                self.OdaTipi.get(),
                                                                                self.OdaNo.get()
                                                                                

                                                                                ))


        
            baglanti.commit()
            self.OdaListele()
            baglanti.close()
            messagebox.showinfo("Başarılı","Oda bilgileri başarıyla güncellendi.",parent=self.root)
            self.OdaBilgileriniSifirla()


    def OdaSil(self):
        SilmeSorusu=messagebox.askyesno("Soru","İlgili kaydı silmek istediğinizden emin misiniz?",parent=self.root)
        if SilmeSorusu>0:
            baglanti=mysql.connector.connect(host="localhost",username="root",password="Test123456",database="otelveritabani")
            imlec=baglanti.cursor()
            sorgu="delete from oda where OdaNo=%s"
            deger=(self.OdaNo.get(),)
            imlec.execute(sorgu,deger)

        else:
            if not SilmeSorusu:
                return 

        baglanti.commit()
        self.OdaListele()
        baglanti.close()
        self.OdaBilgileriniSifirla()
        



    def OdaBilgileriniSifirla(self):
        self.OdaKatNo.set("")
        self.OdaNo.set("")
        self.OdaTipi.set("")
                

if __name__=="__main__":
    root=Tk()
    root.resizable(0,0)
    nsn=Oda(root)
    root.mainloop()        
from tkinter import *
from tkinter import  messagebox
import sqlite3


if "kütüphane.db":
    print("Bağlantı Başarılıdır.")
else:
    print("Bağlantı Başarısız")



con = sqlite3.connect("kütüphane.db")
imlec = con.cursor()


win = Tk()
win.title("Giriş Ekranı")
win.geometry("450x450")

win.iconbitmap("kütüphane.ico")

sistemKullaniciAdi="kütüphane"
sistemKullaniciSifre="kütüphane"

#Ekranda ki yazılı yazılar(Yönlendiriciler)
adLabel= Label(win,text=" Kullanıcı Adınızı Giriniz ")
adLabel.grid(row=2,column=0,sticky=W)

sifreeLabel= Label(win,text=" Kullanıcı Şifrenizi Giriniz")
sifreeLabel.grid(row=3,column=0,sticky=W)

kontrolLabel= Label(win,text="")
kontrolLabel.grid(row=5,column=2,sticky=E)

def girisKontrol():

    if (sistemKullaniciAdi == kAdiEntry.get()) and (sistemKullaniciSifre==sifreEntry.get()):
        win.destroy()


        pencere = Tk()
        pencere.title("Kitap İşlem")
        pencere.geometry("750x350")
        pencere.iconbitmap("kütüphane2.ico")

        baslik = Label(text="Kişi Bilgisi", font=("Calibri", 15))
        baslik.place(x=1, y=1)

        kLLıdEntry = Entry(pencere, fg="black", bg="white")
        kLLıdEntry.insert(0, "İşlem No :")
        kLLıdEntry.grid(row=4, column=1)

        kLLadEntry = Entry(pencere, fg="black", bg="white")
        kLLadEntry.insert(0, "Kullanıcı Adı:")
        kLLadEntry.grid(row=4, column=3)

        kLLsydEntry = Entry(pencere, fg="black", bg="white")
        kLLsydEntry.insert(0, "Kullanıcı Soyad:")
        kLLsydEntry.grid(row=4, column=5)

        kLLtlfEntry = Entry(pencere, fg="black", bg="white")
        kLLtlfEntry.insert(0, "Kullanıcı Telefon No")
        kLLtlfEntry.grid(row=4, column=6)

        ktpIDEntry = Entry(pencere, fg="black", bg="white")
        ktpIDEntry.insert(0, "Kitap ID:")
        ktpIDEntry.grid(row=8, column=1)

        ktpADEntry = Entry(pencere, fg="black", bg="white")
        ktpADEntry.insert(0, "Kitap Adı:")
        ktpADEntry.grid(row=8, column=3)

        ktpSYFEntry = Entry(pencere, fg="black", bg="white")
        ktpSYFEntry.insert(0, "Kitabın Sayfa Sayısı: ")
        ktpSYFEntry.grid(row=8, column=5)

        ktpYZREntry = Entry(pencere, fg="black", bg="white")
        ktpYZREntry.insert(0, "Kitabın Yazarı: : ")
        ktpYZREntry.grid(row=8, column=6)

        islemTRHEntry = Entry(pencere, fg="black", bg="white")
        islemTRHEntry.insert(0, "İşlem Tarihi: ")
        islemTRHEntry.grid(row=12, column=1)

        islemTuruEntry = Entry(pencere, fg="black", bg="white")
        islemTuruEntry.insert(0, "İşlem Türü Aldı\Verdi: ")
        islemTuruEntry.grid(row=12, column=3)




        liste = Listbox(width=90)
        liste.place(x=150, y=150)

        def degerekle():
            ID = kLLıdEntry.get()
            ad = kLLadEntry.get()
            soyad = kLLsydEntry.get()
            telefonno = kLLtlfEntry.get()
            kitapID = ktpIDEntry.get()
            kitapad = ktpADEntry.get()
            kitapsayfasys = ktpSYFEntry.get()
            kitapyazar = ktpYZREntry.get()
            islemtarihi = islemTRHEntry.get()
            islemtürü = islemTuruEntry.get()

            liste.insert(END, (
            ID, ad, soyad, telefonno, kitapID, kitapad, kitapsayfasys, kitapyazar, islemtarihi, islemtürü))

            def kayitekle():
                imlec.execute("""INSERT INTO bilgi VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                              [ID, ad, soyad, telefonno, kitapID, kitapad, kitapsayfasys, kitapyazar, islemtarihi,
                               islemtürü])
                con.commit()

            kayitekle()


        def degersil():
            sil = kLLadEntry.get()
            liste.delete(ACTIVE)

            def kayitsil():
                imlec.execute("""DELETE FROM bilgi WHERE kullanici_adi = ?""", [sil])
                con.commit()

            kayitsil()
        def islenenKitaplar():
            messagebox.showinfo("Kayıt Kuralı", """  'İşlem No'  kısmına İşlemi yaptığınız zamanı esas alarak Tarih Saat Dakika Saniye olarak bitişik bir şekilde yazmanız gerekmektedir.
            Örn:17122022223940
             Ayrıca Kayıt Sil Butonu sadece son eklediğiniz kaydı silmeye yarar.
             """)

        def Kitaplar():

            from tkinter import ttk


            pen = Tk()
            pen.title("Tavsiye Edilebilecek Kitaplar")


            tablo = ttk.Treeview(pen)
            tablo["columns"] = ("A","B")
            tablo.column("#0",width = 250)
            tablo.column("A", width=250)
            tablo.column("B", width=250)




            tablo.heading("#0",text = "Kitap ID")
            tablo.heading("A",text = "Kitap Adi")
            tablo.heading("B",text = "Kitap Yazarı")




            tablo.insert("","end",text="001", values=("NUTUK","MUSTAFA KEMAL ATATÜRK"))
            tablo.insert("","end",text="002", values=("KUTADGU BİLİG DEN SEÇMELER","ANONİM"))
            tablo.insert("","end",text="003", values=("DEDE KORKUT HİKAYELERİ","ANONİM"))
            tablo.insert("","end",text="004", values=("YUNUS EMRE DİVANINDAN SEÇMELER","ANONİM"))
            tablo.insert("","end",text="005", values=("MESNEVİ DEN SEÇMELER","MEVLANA"))
            tablo.insert("","end",text="006", values=("NASRETTİN HOCA DAN SEÇMELER","ANONİM"))
            tablo.insert("","end",text="007", values=("DİVAN ŞİİRİNDEN SEÇMELER","ANONİM"))
            tablo.insert("","end",text="008", values=("HALK ŞİİRİNDEN SEÇMELER","ANONİM"))
            tablo.insert("","end",text="009", values=("SEYAHATNAMESİNDEN SEÇMELER","EVLİYA ÇELEBİ"))
            tablo.insert("","end",text="010", values=("KEREM İLE ASLI","ANONİM"))
            tablo.insert("","end",text="011", values=("SERGÜZEŞT","SAMİ PAŞAZADE SEZAİ"))
            tablo.insert("","end",text="012", values=("MAİ VE SİYAH","HALİT ZİYA UŞAKLIGİL"))
            tablo.insert("","end",text="013", values=("ŞEHİR","AHMET RASİM"))
            tablo.insert("","end",text="014", values=("ÇİLE","NECİP FAZIL KISAKÜREK"))
            tablo.insert("","end",text="015", values=("KUYUCAKLI YUSUF","SABAHATTİN ALİ"))
            tablo.insert("","end",text="016", values=("DOSTLAR BEN HATIRLASIN","AŞIK VEYSEL"))
            tablo.insert("","end",text="017", values=("SOKRATESİN SAVUNMASI","PLATON"))
            tablo.insert("","end",text="018", values=("ÖLÜ CANLILAR","GOGOL"))
            tablo.insert("","end",text="019", values=("FAUST","GOETHE"))
            tablo.insert("","end",text="020", values=("SAVAŞ VE BARIŞ","TOLSTOY"))
            tablo.insert("","end",text="021", values=("SUÇ VE CEZA","DOSTOYEVSKİ"))
            tablo.insert("","end",text="022", values=("VADİDEKİ ZAMBAK","BALZAC"))
            tablo.insert("","end",text="023", values=("SEFİLLER","VİCTOR HUGO"))
            tablo.insert("","end",text="024", values=("BEYAZ DİŞ","JACK LONDON"))
            tablo.insert("","end",text="025", values=("SES VE ÖFKE","WİLLİAM FAULKNER"))
            tablo.insert("","end",text="026", values=("FARELER VE İNSANLAR","JOHN STEİNBECK"))
            tablo.insert("","end",text="027", values=("DON KİŞOT","CERVANTES"))
            tablo.insert("","end",text="028", values=("DEVLET","EFLATUN"))
            tablo.insert("","end",text="029", values=("GÜLİSTAN","SADİ"))
            tablo.insert("","end",text="030", values=("İKİ ŞEHRİN HİKAYESİ","CHARLES DİCKENS"))


            tablo.pack()
            pen.mainloop()


#Menü kodları
        myMenu = Menu(pencere)
        pencere.config(menu=myMenu)

        def HesapMakinesi():


            root = Tk()
            root.title('Hesap Makinesi')
            root.geometry('260x300')
            root.resizable(FALSE, FALSE)
            root.configure(bg='black')
            root.iconbitmap("Hesapmak.ico")

            entry = Entry(root, width=30, borderwidth=5)
            entry.grid(row=0, column=0, columnspan=4)

            def tiklanan_buton(sayi):
                entry.insert(END, sayi)

            def toplama():
                global sayi1
                global islem
                islem = "toplama"
                sayi1 = int(entry.get())
                entry.delete(0, END)

            def cikarma():
                global sayi1
                global islem
                islem = "cikarma"
                sayi1 = int(entry.get())
                entry.delete(0, END)

            def carpma():
                global sayi1
                global islem
                islem = "carpma"
                sayi1 = int(entry.get())
                entry.delete(0, END)

            def bolme():
                global sayi1
                global islem
                islem = "bolme"
                sayi1 = int(entry.get())
                entry.delete(0, END)

            def esittir():
                sayi2 = int(entry.get())
                entry.delete(0, END)

                if islem == "toplama":
                    entry.insert(0, sayi1 + sayi2)

                if islem == "cikarma":
                    entry.insert(0, sayi1 - sayi2)

                if islem == "bolme":
                    entry.insert(0, sayi1 / sayi2)

                if islem == "carpma":
                    entry.insert(0, sayi1 * sayi2)

            def temizle():
                entry.delete(0, END)

            buton_1 = Button(root, text='1', font="times 14 ", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(1))

            buton_2 = Button(root, text='2', font="times 14", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(2))

            buton_3 = Button(root, text='3', font="times 14", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(3))

            buton_4 = Button(root, text='4', font="times 14 ", bg='grey',
                             fg='white', activebackground='yellow',
                             command=lambda: tiklanan_buton(4))

            buton_5 = Button(root, text='5', font="times 14", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(5))

            buton_6 = Button(root, text='6', font="times 14", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(6))

            buton_7 = Button(root, text='7', font="times 14 ", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(7))

            buton_8 = Button(root, text='8', font="times 14", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(8))

            buton_9 = Button(root, text='9', font="times 14", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(9))

            buton_0 = Button(root, text='0', font="times 14", bg='grey',
                             fg='white', activebackground='yellow',
                             relief=RAISED,
                             command=lambda: tiklanan_buton(0))

            buton_topla = Button(root, text='+', font="times 14", bg='grey',
                                 fg='white', activebackground='yellow',
                                 relief=RAISED,
                                 command=toplama)

            buton_cikar = Button(root, text='-', font="times 14", bg='grey',
                                 fg='white', activebackground='yellow',
                                 relief=RAISED,
                                 command=cikarma)

            buton_bol = Button(root, text='/', font="times 14", bg='grey',
                               fg='white', activebackground='yellow',
                               relief=RAISED,
                               command=bolme)

            buton_carp = Button(root, text='*', font="times 14", bg='grey',
                                fg='white', activebackground='yellow',
                                relief=RAISED,
                                command=carpma)

            buton_esittir = Button(root, text='=', font="times 14", bg='grey',
                                   fg='white', activebackground='yellow',
                                   relief=RAISED,
                                   command=esittir)

            # en sontanimla
            buton_temizle = Button(root, text='Temizle', font="times 14", bg='grey',
                                   fg='white', activebackground='yellow',
                                   relief=RAISED,
                                   command=temizle)

            buton_1.grid(row=1, column=0, padx=4, pady=4, ipadx=26)
            buton_2.grid(row=1, column=1, padx=4, pady=4, ipadx=26)
            buton_3.grid(row=1, column=2, padx=4, pady=4, ipadx=26)
            buton_4.grid(row=2, column=0, padx=4, pady=4, ipadx=26)
            buton_5.grid(row=2, column=1, padx=4, pady=4, ipadx=26)
            buton_6.grid(row=2, column=2, padx=4, pady=4, ipadx=26)
            buton_7.grid(row=3, column=0, padx=4, pady=4, ipadx=26)
            buton_8.grid(row=3, column=1, padx=4, pady=4, ipadx=26)
            buton_9.grid(row=3, column=2, padx=4, pady=4, ipadx=26)
            buton_0.grid(row=4, column=0, padx=4, pady=4, ipadx=26)
            buton_topla.grid(row=4, column=1, padx=4, pady=4, ipadx=26)
            buton_cikar.grid(row=4, column=2, padx=4, pady=4, ipadx=26)
            buton_carp.grid(row=5, column=0, padx=4, pady=4, ipadx=26)
            buton_bol.grid(row=5, column=1, padx=4, pady=4, ipadx=29)
            buton_esittir.grid(row=5, column=2, padx=4, pady=4, ipadx=24)
            buton_temizle.grid(row=6, column=0, columnspan=3)
            root.mainloop()

        def bki():
            root = Tk()
            root.title("BKİ Hesaplama")
            root.geometry("300x300")
            root.iconbitmap("Bki.ico")

            boyLabel = Label(root, text=" Boy Giriniz ")
            boyLabel.grid(row=2, column=4)

            kiloLabel = Label(root, text=" Kilo  Giriniz ")
            kiloLabel.grid(row=4, column=4)

            boyEntry = Entry(root)
            boyEntry.grid(row=2, column=2)

            kiloEntry = Entry(root)
            kiloEntry.grid(row=4, column=2)

            def girisKontrol():
                boy = float(boyEntry.get())
                kilo = float(kiloEntry.get())
                bki = kilo / (boy * boy)
                messagebox.showinfo("BKİ Değeriniz", "BKİ Değeriniz" + str(bki))

            girisButton = Button(root, text="giriş yap", command=girisKontrol)
            girisButton.grid(row=6, column=2, sticky=E)

            root.mainloop()



        fileMenu = Menu(myMenu)
        myMenu.add_cascade(label="Tavsiye Edilebilecek Kitaplar", menu=fileMenu)
        myMenu.add_cascade(label="Bki Hesapla", command=bki)
        myMenu.add_cascade(label="Hesap Makinesi", command=HesapMakinesi)




        fileMenu.add_command(label="Kitap Listesi",command=Kitaplar)
        fileMenu.add_separator()
        fileMenu.add_command(label="Pencereyi Kapat", command=pencere.destroy)
        fileMenu.add_separator()






        kaydetbuton = Button(text=("Kaydet"), fg=("Black"), bg=("Yellow"), width=15, command=degerekle)
        kaydetbuton.place(x=10, y=150)

        kitapgösterbuton = Button(text=(" Kayıt Kuralları."), fg=("Black"), bg=("Yellow"), width=15,command=islenenKitaplar)
        kitapgösterbuton.place(x=10, y=180)

        kayitsilbuton = Button(text=("Kayıt Sil"), fg=("Black"), bg=("Yellow"), width=15, command=degersil)
        kayitsilbuton.place(x=10, y=210)

        cikisbuton = Button(text=("Çıkış"), fg=("Black"), bg=("Yellow"), width=15, command=exit)
        cikisbuton.place(x=10, y=240)

        pencere.mainloop()


        # girişin yanlış veya doğru olup olmadığı ile ilgili if elif kodları
    elif sistemKullaniciAdi != kAdiEntry.get() and sistemKullaniciSifre == sifreEntry.get():
        kontrolLabel["text"] = "kullanıcı adı hatalıdır"
    elif sistemKullaniciAdi == kAdiEntry.get() and sistemKullaniciSifre != sifreEntry.get():
        kontrolLabel["text"] = "şifre  hatalıdır"
    elif sistemKullaniciAdi != kAdiEntry.get() and sistemKullaniciSifre != sifreEntry.get():
        kontrolLabel["text"] = "kullanıcı adı ve şifre hatalıdır"

# giriş ekranı kodları

kAdiEntry = Entry(win, fg="black", bg="white")
kAdiEntry.insert(0, "Kullanıcı Adı")
kAdiEntry.grid(row=2, column=2)

sifreEntry = Entry(win, fg="black", bg="white", show="*")
sifreEntry.insert(0, "Şifre")
sifreEntry.grid(row=3, column=2)

girisButton = Button(win, text="giriş yap", command=girisKontrol)
girisButton.grid(row=4, column=2, sticky=E)






win.mainloop()
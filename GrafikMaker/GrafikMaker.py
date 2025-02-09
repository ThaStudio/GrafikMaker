

"""

Grafik Maker [1.0.5 PRE-ALPHA] open soruce codes.

!!!!!Please read the license before using the codes!!!!!

Do not use this app for any commercial or malware purposes.

License : Apache License 2.0

"""

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk
from tkinter import PhotoImage
import webbrowser
import os
import time
import sys

from image_reads import dosya_bul

def ProgramStart():

    def kapan():
        yuklenme.destroy()
        time.sleep(0.8)

    yuklenme = tk.Tk()
    yuklenme.geometry("815x485+250+260")
    yuklenme.resizable(False, False)
    yuklenme.overrideredirect(True)
    yuklenme.attributes("-topmost", True)
    yuklenme.focus()

    yol_2 = dosya_bul("GrafikMaker_Yuklenme.png")

    yuklenme_resim = PhotoImage(file=yol_2)
    resim = tk.Label(image=yuklenme_resim)
    resim.pack()

    yuklenme.after(8000, kapan)

    yuklenme.mainloop()

    def baslat_kod():
        if grafik_type.get() == "":
            messagebox.showerror("Grafik Maker","Lütfen Grafik Türünü Seçiniz!!!")
        else:

            if grafik_type.get() == "Çizgi":

                def olsutur_cizgi():
                    try:
                        if x_duzlem_1.get().strip() == "":
                            x_duzlem_1.insert(0, 5)

                        if x_duzlem_2.get().strip() == "":
                            x_duzlem_2.insert(0, 10)

                        if x_duzlem_3.get().strip() == "":
                            x_duzlem_3.insert(0, 15)

                        if x_duzlem_4.get().strip() == "":
                            x_duzlem_4.insert(0, 20)

                        if y_duzlem_1.get().strip() == "":
                            y_duzlem_1.insert(0, 5)

                        if y_duzlem_2.get().strip() == "":
                            y_duzlem_2.insert(0, 10)

                        if y_duzlem_3.get().strip() == "":
                            y_duzlem_3.insert(0, 15)

                        if y_duzlem_4.get().strip() == "":
                            y_duzlem_4.insert(0, 20)

                        xpoints = np.array([int(x_duzlem_1.get()), int(x_duzlem_2.get()), int(y_duzlem_3.get()), int(y_duzlem_4.get())])
                        ypoints = np.array([int(y_duzlem_1.get()), int(y_duzlem_2.get()), int(y_duzlem_3.get()), int(y_duzlem_4.get())])

                        plt.title(cizgi_title_adlandir.get())
                        plt.xlabel(cizgi_x_adlandir.get())
                        plt.ylabel(cizgi_y_adlandir.get())

                        plt.plot(xpoints, ypoints, marker = ".")
                        plt.grid()
                        plt.show()

                    except:
                        messagebox.showerror("Grafik Maker","Lütfen girişleri boş bırakmayın ve, uygun değerleri giriniz!")

                def resetle_cizgi():
                    sor_cizgi = messagebox.askyesno("Grafik Maker","Tüm verileri silmek istediğinizden emin misiniz?")
                    if sor_cizgi == True:
                        cizgi_x_adlandir.delete(0, tk.END)
                        cizgi_y_adlandir.delete(0, tk.END)
                        cizgi_title_adlandir.delete(0, tk.END)
                        x_duzlem_1.delete(0, tk.END)
                        x_duzlem_2.delete(0, tk.END)
                        x_duzlem_3.delete(0, tk.END)
                        x_duzlem_4.delete(0, tk.END)
                        y_duzlem_1.delete(0, tk.END)
                        y_duzlem_2.delete(0, tk.END)
                        y_duzlem_3.delete(0, tk.END)
                        y_duzlem_4.delete(0, tk.END)

                def close_cizgi():
                    close_cizgi_uyari = messagebox.askyesno("Grafik Maker",f"{proje_adi.get()} Adındaki grafiği kapatmak istediğinizden emin misiniz?")

                    if close_cizgi_uyari == True:
                        cizgi_pencere.destroy()

                cizgi_pencere = tk.Toplevel()

                if proje_adi.get().strip() == "":
                    cizgi_pencere.title("Grafik Maker (Çizgi)")
                    proje_adi.insert(0, "Grafik Maker (Çizgi)")
                else:
                    cizgi_pencere.title(proje_adi.get())

                cizgi_pencere.resizable(False, False)
                cizgi_pencere.geometry("500x270+500+500")
                yol_3 = dosya_bul("gm_logo_.png")
                cizgi_icon = PhotoImage(file=yol_3)
                cizgi_pencere.iconphoto(False, cizgi_icon)
                cizgi_pencere.protocol("WM_DELETE_WINDOW", close_cizgi)

                baslik_cizgi = tk.Label(cizgi_pencere, text="ÇİZGİ GRAFİK", fg="blue", font="Aria 17 bold")
                baslik_cizgi.pack()

                x_cizgi_arrow = tk.Label(cizgi_pencere, text="X DÜZLEM", fg="red", font="Aria 14 bold")
                x_cizgi_arrow.pack()
                x_cizgi_arrow.place(x="10",y="35")

                x_duzlem_1 = ttk.Entry(cizgi_pencere, width=10)
                x_duzlem_1.pack()
                x_duzlem_1.place(x="20",y="65")

                x_duzlem_2 = ttk.Entry(cizgi_pencere, width=10)
                x_duzlem_2.pack()
                x_duzlem_2.place(x="20",y="85")

                x_duzlem_3 = ttk.Entry(cizgi_pencere, width=10)
                x_duzlem_3.pack()
                x_duzlem_3.place(x="20",y="105")

                x_duzlem_4 = ttk.Entry(cizgi_pencere, width=10)
                x_duzlem_4.pack()
                x_duzlem_4.place(x="20",y="125")

                x_duzlem_numara = tk.Label(cizgi_pencere, text="1\n2\n3\n4", fg="red", font="Aria 11 bold")
                x_duzlem_numara.pack()
                x_duzlem_numara.place(x="0", y="65")

                y_duzlem_numara = tk.Label(cizgi_pencere, text="1\n2\n3\n4", fg="red", font="Aria 11 bold")
                y_duzlem_numara.pack()
                y_duzlem_numara.place(x="120", y="65")

                y_cizgi_arrow = tk.Label(cizgi_pencere, text="Y DÜZLEM", fg="red", font="Aria 14 bold")
                y_cizgi_arrow.pack()
                y_cizgi_arrow.place(x="130",y="35")

                y_duzlem_1 = ttk.Entry(cizgi_pencere, width=10)
                y_duzlem_1.pack()
                y_duzlem_1.place(x="140",y="65")

                y_duzlem_2 = ttk.Entry(cizgi_pencere, width=10)
                y_duzlem_2.pack()
                y_duzlem_2.place(x="140",y="85")

                y_duzlem_3 = ttk.Entry(cizgi_pencere, width=10)
                y_duzlem_3.pack()
                y_duzlem_3.place(x="140",y="105")

                y_duzlem_4 = ttk.Entry(cizgi_pencere, width=10)
                y_duzlem_4.pack()
                y_duzlem_4.place(x="140",y="125")

                cizgi_adlandirma = tk.Label(cizgi_pencere, text="ADLANDIR", fg="red", font="Aria 14 bold")
                cizgi_adlandirma.pack()
                cizgi_adlandirma.place(x="290", y="35")

                cizgi_y_adlandir = ttk.Entry(cizgi_pencere)
                cizgi_y_adlandir.pack()
                cizgi_y_adlandir.place(x="300",y="65")

                cizgi_x_adlandir = ttk.Entry(cizgi_pencere)
                cizgi_x_adlandir.pack()
                cizgi_x_adlandir.place(x="300",y="95")

                cizgi_title_adlandir = ttk.Entry(cizgi_pencere)
                cizgi_title_adlandir.pack()
                cizgi_title_adlandir.place(x="300",y="125")

                cizgi_adlandir_y_label = tk.Label(cizgi_pencere, text="Y :", fg="red", font="Aria 13 bold")
                cizgi_adlandir_y_label.pack()
                cizgi_adlandir_y_label.place(x="270",y="65")

                cizgi_adlandir_x_label = tk.Label(cizgi_pencere, text="X :", fg="red", font="Aria 13 bold")
                cizgi_adlandir_x_label.pack()
                cizgi_adlandir_x_label.place(x="270",y="95")

                cizgi_adlandir_title_label = tk.Label(cizgi_pencere, text="BAŞLIK :", fg="red", font="Aria 13 bold")
                cizgi_adlandir_title_label.pack()
                cizgi_adlandir_title_label.place(x="220",y="125")

                cizgi_olustur = tk.Button(cizgi_pencere, text="Oluştur", fg="red", bg="white", font="Aria 15 bold",command=olsutur_cizgi)
                cizgi_olustur.pack()
                cizgi_olustur.place(x="150",y="200")

                reset_cizgi = tk.Button(cizgi_pencere, text="Reset",fg="orange", bg="white", font="Aria 15 bold",command=resetle_cizgi)
                reset_cizgi.pack()
                reset_cizgi.place(x="250", y="200")

                cizgi_menu = tk.Menu(cizgi_pencere)
                cizgi_pencere.config(menu=cizgi_menu)

                olusturma = tk.Menu(cizgi_pencere, tearoff=0)

                cizgi_menu.add_cascade(label="Grafik Oluştur", menu=olusturma)
                olusturma.add_command(label="Oluştur", command=olsutur_cizgi)
                olusturma.add_command(label="Resetle", command=resetle_cizgi)
                cizgi_menu.add_command(label="Kapat", command=close_cizgi)

                cizgi_pencere.mainloop()

            if grafik_type.get() == "Daire":
                def daire_grafik_olustur():
                    try:
                        if daire_adlandir_1.get().strip() == "":
                            daire_adlandir_1.insert(0, "A")

                        if daire_adlandir_2.get().strip() == "":
                            daire_adlandir_2.insert(0, "B")

                        if daire_adlandir_3.get().strip() == "":
                            daire_adlandir_3.insert(0, "C")

                        if daire_adlandir_4.get().strip() == "":
                            daire_adlandir_4.insert(0, "D")

                        if daire_adlandir_5.get().strip() == "":
                            daire_adlandir_5.insert(0, "E")

                        if daire_adlandir_6.get().strip() == "":
                            daire_adlandir_6.insert(0, "F")

                        if daire_renklendir_1.get().strip() == "":
                            daire_renklendir_1.insert(0, "red")

                        if daire_renklendir_2.get().strip() == "":
                            daire_renklendir_2.insert(0, "green")

                        if daire_renklendir_3.get().strip() == "":
                            daire_renklendir_3.insert(0, "blue")

                        if daire_renklendir_4.get().strip() == "":
                            daire_renklendir_4.insert(0, "orange")

                        if daire_renklendir_5.get().strip() == "":
                            daire_renklendir_5.insert(0, "pink")

                        if daire_renklendir_6.get().strip() == "":
                            daire_renklendir_6.insert(0, "yellow")

                        degerler_daire = [int(daire_deger_1.get()),int(daire_deger_2.get()),int(daire_deger_3.get()),int(daire_deger_4.get()),int(daire_deger_5.get()),int(daire_deger_6.get())]
                        deger_adlandirma_daire = [f"{daire_adlandir_1.get()} ({daire_deger_1.get()})",f"{daire_adlandir_2.get()} ({daire_deger_2.get()})",f"{daire_adlandir_3.get()} ({daire_deger_3.get()})",f"{daire_adlandir_4.get()} ({daire_deger_4.get()})",f"{daire_adlandir_5.get()} ({daire_deger_5.get()})",f"{daire_adlandir_6.get()} ({daire_deger_6.get()})"]
                        grafik_renklendirme_daire = [daire_renklendir_1.get().strip().lower(), daire_renklendir_2.get().strip().lower(),daire_renklendir_3.get().strip().lower(),daire_renklendir_4.get().strip().lower(),daire_renklendir_5.get().strip().lower(),daire_renklendir_6.get().strip().lower()]

                        plt.pie(degerler_daire, labels=deger_adlandirma_daire, colors=grafik_renklendirme_daire)
                        plt.legend(title = daire_liste.get())
                        plt.title(daire_title_giris.get())
                        plt.show()
                    except Exception as e:
                        print(e)
                        messagebox.showerror("Grafik Maker", "Lütfen girişleri boş bırakmayın ve, uygun değerleri giriniz!")

                def daire_resetleme():
                    reset_emin = messagebox.askyesno("Grafik Maker","Tüm verileri silmek istediğinizden emin misiniz?")

                    if reset_emin == True:
                        daire_adlandir_1.delete(0, tk.END)
                        daire_adlandir_2.delete(0, tk.END)
                        daire_adlandir_3.delete(0, tk.END)
                        daire_adlandir_4.delete(0, tk.END)
                        daire_adlandir_5.delete(0, tk.END)
                        daire_adlandir_6.delete(0, tk.END)
                        daire_deger_1.delete(0, tk.END)
                        daire_deger_2.delete(0, tk.END)
                        daire_deger_3.delete(0, tk.END)
                        daire_deger_4.delete(0, tk.END)
                        daire_deger_5.delete(0, tk.END)
                        daire_deger_6.delete(0, tk.END)
                        daire_renklendir_1.delete(0, tk.END)
                        daire_renklendir_2.delete(0, tk.END)
                        daire_renklendir_3.delete(0, tk.END)
                        daire_renklendir_4.delete(0, tk.END)
                        daire_renklendir_5.delete(0, tk.END)
                        daire_renklendir_6.delete(0, tk.END)
                        daire_title_giris.delete(0, tk.END)
                        daire_liste.delete(0, tk.END)

                def close_daire():
                    daire_close_uyari = messagebox.askyesno("Grafik Maker",f"{proje_adi.get()} Adındaki grafiği kapatmak istediğinizden emin misiniz?")

                    if daire_close_uyari == True:
                        daire_grafik.destroy()
                
                daire_grafik = tk.Toplevel()

                if proje_adi.get().strip()== "":
                    daire_grafik.title("Grafik Maker (Daire)")
                    proje_adi.insert(0, "Grafik Maker (Daire)")
                else:
                    daire_grafik.title(proje_adi.get())

                daire_grafik.geometry("600x280+500+500")
                daire_grafik.resizable(False, False)
                yol_4 = dosya_bul("gm_logo_.png")
                daire_icon = PhotoImage(file=yol_4)
                daire_grafik.iconphoto(False, daire_icon)
                daire_grafik.protocol("WM_DELETE_WINDOW", close_daire)

                daire_baslik = tk.Label(daire_grafik, text="DAİRE GRAFİK", fg="blue", font="Aria 17 bold")
                daire_baslik.pack()

                daire_deger_baslik = tk.Label(daire_grafik,text="DEĞER", fg="red" ,font="Aria 15 bold")
                daire_deger_baslik.pack()
                daire_deger_baslik.place(x="20", y="40")

                daire_deger_numara = tk.Label(daire_grafik, text="1\n2\n3\n4\n5\n6", fg="red", font="Aria 13 bold")
                daire_deger_numara.pack()
                daire_deger_numara.place(x="5", y="80")

                daire_deger_1 = ttk.Entry(daire_grafik)
                daire_deger_1.pack()
                daire_deger_1.place(x="30", y="80")

                daire_deger_2 = ttk.Entry(daire_grafik)
                daire_deger_2.pack()
                daire_deger_2.place(x="30",y="100")

                daire_deger_3 = ttk.Entry(daire_grafik)
                daire_deger_3.pack()
                daire_deger_3.place(x="30", y="120")

                daire_deger_4 = ttk.Entry(daire_grafik)
                daire_deger_4.pack()
                daire_deger_4.place(x="30", y="140")

                daire_deger_5 = ttk.Entry(daire_grafik)
                daire_deger_5.pack()
                daire_deger_5.place(x="30", y="160")

                daire_deger_6 = ttk.Entry(daire_grafik)
                daire_deger_6.pack()
                daire_deger_6.place(x="30", y="180")

                daire_adlandirma = tk.Label(daire_grafik, text="ADLANDIR", fg="red", font="Aria 15 bold")
                daire_adlandirma.pack()
                daire_adlandirma.place(x="190", y="40")
                
                daire_adlandir_numara = tk.Label(daire_grafik, text="1\n2\n3\n4\n5\n6", fg="red", font="Aria 13 bold")
                daire_adlandir_numara.pack()
                daire_adlandir_numara.place(x="180", y="80")

                daire_adlandir_1 = ttk.Entry(daire_grafik)
                daire_adlandir_1.pack()
                daire_adlandir_1.place(x="200", y="80")

                daire_adlandir_2 = ttk.Entry(daire_grafik)
                daire_adlandir_2.pack()
                daire_adlandir_2.place(x="200", y="100")

                daire_adlandir_3 = ttk.Entry(daire_grafik)
                daire_adlandir_3.pack()
                daire_adlandir_3.place(x="200", y="120")

                daire_adlandir_4 = ttk.Entry(daire_grafik)
                daire_adlandir_4.pack()
                daire_adlandir_4.place(x="200", y="140")

                daire_adlandir_5 = ttk.Entry(daire_grafik)
                daire_adlandir_5.pack()
                daire_adlandir_5.place(x="200", y="160")

                daire_adlandir_6 = ttk.Entry(daire_grafik)
                daire_adlandir_6.pack()
                daire_adlandir_6.place(x="200", y="180")

                daire_renklerndir_baslik = tk.Label(daire_grafik, text="RENKLENDİR", fg="red", font="Aria 15 bold")
                daire_renklerndir_baslik.pack()
                daire_renklerndir_baslik.place(x="340", y="40")

                daire_renklendir_numara = tk.Label(daire_grafik, text="1\n2\n3\n4\n5\n6", fg="red", font="Aria 13 bold")
                daire_renklendir_numara.pack()
                daire_renklendir_numara.place(x="330", y="80")

                daire_renklendir_1 = ttk.Entry(daire_grafik)
                daire_renklendir_1.pack()
                daire_renklendir_1.place(x="350", y="80")

                daire_renklendir_2 = ttk.Entry(daire_grafik)
                daire_renklendir_2.pack()
                daire_renklendir_2.place(x="350", y="100")

                daire_renklendir_3 = ttk.Entry(daire_grafik)
                daire_renklendir_3.pack()
                daire_renklendir_3.place(x="350", y="120")

                daire_renklendir_4 = ttk.Entry(daire_grafik)
                daire_renklendir_4.pack()
                daire_renklendir_4.place(x="350", y="140")

                daire_renklendir_5 = ttk.Entry(daire_grafik)
                daire_renklendir_5.pack()
                daire_renklendir_5.place(x="350", y="160")

                daire_renklendir_6 = ttk.Entry(daire_grafik)
                daire_renklendir_6.pack()
                daire_renklendir_6.place(x="350", y="180")

                daire_liste_baslik = tk.Label(daire_grafik, text="LİSTE\nBAŞLIK", fg="red", font="Aria 14 bold")
                daire_liste_baslik.pack()
                daire_liste_baslik.place(x="500", y="40")

                daire_liste = ttk.Entry(daire_grafik, width=15)
                daire_liste.pack()
                daire_liste.place(x="490", y="90") 

                daire_olustur = tk.Button(daire_grafik, text="Oluştur", fg="red", bg="white", font="Aria 15 bold", command=daire_grafik_olustur)
                daire_olustur.pack()
                daire_olustur.place(x="180", y="210")

                daire_reset = tk.Button(daire_grafik,text="Reset" ,fg="orange", bg="white", font="Aria 15 bold", command=daire_resetleme)
                daire_reset.pack()
                daire_reset.place(x="290", y="210")

                daire_title = tk.Label(daire_grafik, text="BAŞLIK", fg="red", font="Aria 15 bold")
                daire_title.pack()
                daire_title.place(x="500", y="120")

                daire_title_giris = ttk.Entry(daire_grafik, width=15)
                daire_title_giris.pack()
                daire_title_giris.place(x="490", y="150")

                daire_menu = tk.Menu(daire_grafik)
                daire_grafik.config(menu=daire_menu)

                daire_olusturma = tk.Menu(daire_grafik, tearoff=0)

                daire_menu.add_cascade(label="Grafik Oluştur", menu=daire_olusturma)
                daire_olusturma.add_command(label="Oluştur", command=daire_grafik_olustur)
                daire_olusturma.add_command(label="Resetle", command=daire_resetleme)
                daire_menu.add_command(label="Kapat", command=close_daire)

                daire_grafik.mainloop()

            if grafik_type.get() == "Bar":

                def bar_olustur_com():
                    try:
                        if bar_renk.get().strip() == "":
                            bar_renk.insert(0, "blue")

                        if bar_adlandirma_1.get().strip() == "":
                            bar_adlandirma_1.insert(0, "A")

                        if bar_adlandirma_2.get().strip() == "":
                            bar_adlandirma_2.insert(0, "B")

                        if bar_adlandirma_3.get().strip() == "":
                            bar_adlandirma_3.insert(0, "C")

                        if bar_adlandirma_4.get().strip() == "":
                            bar_adlandirma_4.insert(0, "D")

                        if bar_adlandirma_5.get().strip() == "":
                            bar_adlandirma_5.insert(0, "E")

                        if bar_adlandirma_6.get().strip() == "":
                            bar_adlandirma_6.insert(0, "F")

                        bar_deger_list = ["0",bar_deger_1.get(), bar_deger_2.get(), bar_deger_3.get(), bar_deger_4.get(), bar_deger_5.get(), bar_deger_6.get()]
                        bar_adlandir_list = ["0",bar_adlandirma_1.get(), bar_adlandirma_2.get(), bar_adlandirma_3.get(), bar_adlandirma_4.get(), bar_adlandirma_5.get(), bar_adlandirma_6.get()]

                        plt.bar(bar_adlandir_list,bar_deger_list , color=bar_renk.get().strip())
                        plt.title(bar_title.get())
                        plt.show()
                    except Exception as e:
                        messagebox.showerror("Grafik Maker",f"HATA! Lütfen girişleri boş bırakmayın ve, uygun değerleri giriniz! {e}")

                def bar_reset_com():
                    bar_sor = messagebox.askyesno("Grafik Maker","Tüme verileri silmek istediğinizden emin misiniz?")

                    if bar_sor == True:
                        bar_deger_1.delete(0, tk.END)
                        bar_deger_2.delete(0, tk.END)
                        bar_deger_3.delete(0, tk.END)
                        bar_deger_4.delete(0, tk.END)
                        bar_deger_5.delete(0, tk.END)
                        bar_deger_6.delete(0, tk.END)
                        bar_adlandirma_1.delete(0, tk.END)
                        bar_adlandirma_2.delete(0, tk.END)
                        bar_adlandirma_3.delete(0, tk.END)
                        bar_adlandirma_4.delete(0, tk.END)
                        bar_adlandirma_5.delete(0, tk.END)
                        bar_adlandirma_6.delete(0, tk.END)
                        bar_renk.delete(0, tk.END)
                        bar_title.delete(0, tk.END)
                    else:
                        pass

                def close_bar():
                    close_bar_uyari = messagebox.askyesno("Grafik Maker",f"{proje_adi.get()} Adındaki grafiği kapatmak istedğinizden emin misiniz?")

                    if close_bar_uyari == True:
                        bar_grafik.destroy()

                bar_grafik = tk.Toplevel()
                bar_grafik.geometry("500x290+500+500")
                bar_grafik.resizable(False, False)
                yol_5 = dosya_bul("gm_logo_.png")
                bar_icon = PhotoImage(file=yol_5)
                bar_grafik.iconphoto(False, bar_icon)
                bar_grafik.protocol("WM_DELETE_WINDOW", close_bar)

                if proje_adi.get().strip() == "":
                    bar_grafik.title("Grafik Maker (Bar)")
                    proje_adi.insert(0, "Grafik Maker (Bar)")
                else:
                    bar_grafik.title(proje_adi.get())

                bar_baslik = tk.Label(bar_grafik, text="BAR GRAFİK", fg="blue", font="Aria 17 bold")
                bar_baslik.pack()

                bar_deger_baslik = tk.Label(bar_grafik, text="DEĞER", fg="red", font="Aria 15 bold")
                bar_deger_baslik.pack()
                bar_deger_baslik.place(x="20", y="40")

                bar_deger_1 = ttk.Entry(bar_grafik)
                bar_deger_1.pack()
                bar_deger_1.place(x="30",y="80")

                bar_deger_2 = ttk.Entry(bar_grafik)
                bar_deger_2.pack()
                bar_deger_2.place(x="30",y="100")

                bar_deger_3 = ttk.Entry(bar_grafik)
                bar_deger_3.pack()
                bar_deger_3.place(x="30",y="120")

                bar_deger_4 = ttk.Entry(bar_grafik)
                bar_deger_4.pack()
                bar_deger_4.place(x="30",y="140")

                bar_deger_5 = ttk.Entry(bar_grafik)
                bar_deger_5.pack()
                bar_deger_5.place(x="30",y="160")

                bar_deger_6 = ttk.Entry(bar_grafik)
                bar_deger_6.pack()
                bar_deger_6.place(x="30",y="180")

                bar_adlandirma_baslik = tk.Label(bar_grafik, text="ADLANDIR", fg="red", font="Aria 15 bold")
                bar_adlandirma_baslik.pack()
                bar_adlandirma_baslik.place(x="190", y="40")

                bar_adlandirma_1 = ttk.Entry(bar_grafik)
                bar_adlandirma_1.pack()
                bar_adlandirma_1.place(x="200", y="80")

                bar_adlandirma_2 = ttk.Entry(bar_grafik)
                bar_adlandirma_2.pack()
                bar_adlandirma_2.place(x="200", y="100")

                bar_adlandirma_3 = ttk.Entry(bar_grafik)
                bar_adlandirma_3.pack()
                bar_adlandirma_3.place(x="200", y="120")

                bar_adlandirma_4 = ttk.Entry(bar_grafik)
                bar_adlandirma_4.pack()
                bar_adlandirma_4.place(x="200", y="140")

                bar_adlandirma_5 = ttk.Entry(bar_grafik)
                bar_adlandirma_5.pack()
                bar_adlandirma_5.place(x="200", y="160")

                bar_adlandirma_6 = ttk.Entry(bar_grafik)
                bar_adlandirma_6.pack()
                bar_adlandirma_6.place(x="200", y="180")

                bar_renk_label = tk.Label(bar_grafik, text="RENK", fg="red", font="Aria 15 bold")
                bar_renk_label.pack()
                bar_renk_label.place(x="370", y="40")

                bar_renk = ttk.Entry(bar_grafik)
                bar_renk.pack()
                bar_renk.place(x="370", y="80")

                bar_title_label = tk.Label(bar_grafik, text="BAŞLIK", fg="red", font="Aria 15 bold")
                bar_title_label.pack()
                bar_title_label.place(x="370", y="120")

                bar_title = ttk.Entry(bar_grafik)
                bar_title.pack()
                bar_title.place(x="370", y="160")

                bar_deger_numara = tk.Label(bar_grafik, text="1\n2\n3\n4\n5\n6", fg="red", font="Aria 11 bold")
                bar_deger_numara.pack()
                bar_deger_numara.place(x="7", y="81")

                bar_adlandir_numara = tk.Label(bar_grafik, text="1\n2\n3\n4\n5\n6", fg="red", font="Aria 12 bold")
                bar_adlandir_numara.pack()
                bar_adlandir_numara.place(x="185", y="81")

                bar_olustur = tk.Button(bar_grafik, text="Oluştur", fg="red", bg="white", font="Aria 15 bold",command=bar_olustur_com)
                bar_olustur.pack()
                bar_olustur.place(x="180", y="210")

                bar_reset = tk.Button(bar_grafik, text="Reset", fg="orange", bg="white", font="Aria 15 bold", command=bar_reset_com)
                bar_reset.pack()
                bar_reset.place(x="290", y="210")

                bar_menu = tk.Menu(bar_grafik)
                bar_grafik.config(menu=bar_menu)

                bar_olusturma = tk.Menu(bar_grafik, tearoff=0)

                bar_menu.add_cascade(label="Grafik Oluştur", menu=bar_olusturma)
                bar_olusturma.add_command(label="Oluştur", command=bar_olustur_com)
                bar_olusturma.add_command(label="Resetle", command=bar_reset_com)
                bar_menu.add_command(label="Kapat", command=close_bar)

                bar_grafik.mainloop()

    def exitt():
        eminmisin = messagebox.askyesno("Grafik Maker", "Çıkmak İstediğinizden Emin Misiniz?")

        if eminmisin == True:
            baslangic.destroy()

    def about():
        global hakkinda_pencere

        hakkinda_pencere = tk.Toplevel()
        hakkinda_pencere.title("Grafik Maker Hakkında")
        hakkinda_pencere.geometry("230x280+400+400")
        yol_6 = dosya_bul("gm_logo_.png")
        hakkinda_icon = PhotoImage(file=yol_6)
        hakkinda_pencere.iconphoto(False, hakkinda_icon)
        hakkinda_pencere.resizable(False, False)

        hakkinda_baslik = tk.Label(hakkinda_pencere, text="Hakkında", fg="red", font="Aria 17 bold")
        hakkinda_baslik.pack()

        hakkinda_yazi = tk.Label(hakkinda_pencere, text=" Grafik Maker\nbasit tabanlı grafik\noluşturmaya yarar.\n\nVersion: 1.0.5 [DEMO]", fg="black", font="Aria 15 bold")
        hakkinda_yazi.pack()
        hakkinda_yazi.place(x="4", y="50")

        hakkinda_web = tk.Label(hakkinda_pencere, text="bit.ly/grafikmaker", fg="red", font="Aria 14 bold")
        hakkinda_web.pack()
        hakkinda_web.place(x="35", y="210")

        hakkinda_pencere.mainloop()

    def updates():
        guncelleme_url="https://thastudio.my.canva.site/grafikmaker#g%C3%BCncelleme"
        webbrowser.open(guncelleme_url)

    def help():
        yardim_url = "https://thastudio.my.canva.site/grafikmaker#kullanma"
        webbrowser.open(yardim_url)

    def iletisim():
        iletisim_url = "https://thastudio.my.canva.site/grafikmaker#i%CC%87leti%C5%9Fim"
        webbrowser.open(iletisim_url)

    def duyurular():
        iletisim_url = "https://thastudio.my.canva.site/grafikmaker#duyurular"
        webbrowser.open(iletisim_url)

    def reset_grafik_data():
        reset_sorgu_data = messagebox.askyesno("Grafik Maker","Grafik oluşturma bilgilerini silmek istediğinizden emin misiniz?")

        if reset_sorgu_data == True:
            grafik_type.delete(0, tk.END)
            proje_adi.delete(0, tk.END)

    def restat_app():
        baslangic.destroy()
        time.sleep(1)
        try:
            python = sys.executable 
            os.execv(python, [python] + sys.argv)
        except:
            os.system("GrafikMaker.exe")

    def console():
        def console_code():
            console_sonuc.yview_moveto(1.0)
            if kodlar.get().strip() == "/console.hi":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                console_sonuc.insert(tk.END, "\n\nMerhaba!")
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/app.info":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                console_sonuc.insert(tk.END, "\n\nName : Grafik Maker\nVersion : 1.0.5 [PRE-ALPHA]\nPublisher : Tha Studio\nDeveloper : Tha Studio")
                console_sonuc.config(state="disabled")
            
            elif kodlar.get().strip()== "/clear":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                console_sonuc.delete("1.0", "end")
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/exit" or kodlar.get() == "/close":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                exitt()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/create.project":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                baslat_kod()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/reset_data":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                reset_grafik_data()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/help":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                console_sonuc.insert(tk.END, "\n\n-/help\n-/create.project\n-/reset_data\n-/exit - /close\n-/app.info\n-/console.hi\n-/clear\n-/app.periodical.id\n-/grafik.info\n-/app.help\n-/app.about\n-/app.announcement\n-/app.updates\n-/app.communication\n-/app.restat\n-/app.version")
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/grafik.info":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                console_sonuc.insert(tk.END, "\n\n Çizgi Grafiği : Basit çizgi grafikleri oluşturur,istediğiniz noktaya doğru çizer.\n\nDaire Grafiği: Basit bir daire grafiğidir istediğiniz değere göre grafik oluşturur.\n\nBar Grafiği: Basit dikey bar grafikleri oluşturur.\n\n3D Grafik : 3D termal-istenilen gibi 3 boyutlu bir grafik oluşturur.\n\nHistogram Grafiği : Basit bir histogram grafiği oluşturur. Fazla sütunlu daha faza değerlidir.")
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/console.hack.theme == True":
                console_sonuc.config(state="normal")
                console_sonuc.configure(fg="green")
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/console.hack.theme == False":
                console_sonuc.config(state="normal")
                console_sonuc.configure(fg="white")
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/app.updates":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                updates()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/app.about":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                about()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/app.announcement":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                duyurular()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/app.communication":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                iletisim()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/app.help":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                help()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/app.restat":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                console_sonuc.insert(tk.END, f"\n\nUygulama yeniden başlatılıyor...")
                time.sleep(0.5)
                restat_app()
                console_sonuc.config(state="disabled")

            elif kodlar.get().strip() == "/app.version":
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                console_sonuc.insert(tk.END, f"\n\nUygulama Versiyonu : 1.0.5 [PRE-ALPHA]")
                console_sonuc.config(state="disabled")

            else:
                console_sonuc.config(state="normal")
                kodlar.delete(0, tk.END)
                console_sonuc.insert(tk.END, f'\n\nError!\n4804 : Tanımlanmayan komut!')
                console_sonuc.config(state="disabled")

        console_pencere = tk.Toplevel()
        console_pencere.geometry("270x300+500+500")
        console_pencere.title("Grafik Maker | Konsol")
        console_pencere.resizable(False, False)
        console_pencere.bind("<Return>", lambda event: console_code())
        yol_7 = dosya_bul("gm_logo_.png")
        icon_console = PhotoImage(file=yol_7)
        console_pencere.iconphoto(False, icon_console)

        console_sonuc = tk.Text(console_pencere, height=13, width=29, bg="black", fg="white", font="Arial 13 bold")
        console_sonuc.pack()
        console_sonuc.insert(tk.END, f'Grafik Maker v1.0.5 Basic Command Console "/help" \n\n')
        console_sonuc.config(state="disabled")

        kodlar = ttk.Entry(console_pencere, width=30)
        kodlar.pack()

        enter_code = ttk.Button(console_pencere, text="Enter", command=console_code)
        enter_code.pack()

        console_pencere.mainloop()

    baslangic = tk.Tk()
    baslangic.title("Grafik Maker")
    baslangic.resizable(False, False)
    baslangic.geometry("320x170+350+350")
    baslangic.configure(bg="#f0f0f0")

    yol_1 = dosya_bul("gm_logo_.png")

    icon = PhotoImage(file=yol_1)
    baslangic.iconphoto(False, icon)
    baslangic.bind("<Return>", lambda event: baslat_kod())
    baslangic.bind("<Escape>", lambda event: baslangic.destroy())

    baslik = tk.Label(text="GRAFIK MAKER", fg="blue", font="Aria 15 bold")
    baslik.pack()
    baslik.place(x="80",y="5")

    grafik_type = Combobox(baslangic, values=("Çizgi","Daire","Bar"))
    grafik_type.pack()
    grafik_type.place(x="110",y="40")

    grafik_yazi_tur = tk.Label(text="Grafik Tür :", fg="red", font="Aria 12 bold")
    grafik_yazi_tur.pack()
    grafik_yazi_tur.place(x="15", y="40")

    proje_adi = ttk.Entry(baslangic)
    proje_adi.pack()
    proje_adi.place(x="120",y="80")

    proje_yazi = tk.Label(text="Proje Ad :", fg="red", font="Aria 12 bold")
    proje_yazi.pack()
    proje_yazi.place(x="20", y="80")

    baslat = ttk.Button(text="Grafik Oluştur", command=baslat_kod) 
    baslat.pack()
    baslat.place(x="123",y="115")

    menu = tk.Menu(baslangic)
    baslangic.config(menu=menu)

    menu_buton = tk.Menu(baslangic, tearoff=0)
    destek = tk.Menu(menu_buton, tearoff=0)
    grafik_olusturma = tk.Menu(menu_buton, tearoff=0)

    menu.add_cascade(label="Menü", menu=menu_buton)
    menu_buton.add_cascade(label="Yardım", menu=destek)
    menu_buton.add_cascade(label="Grafik Oluşturma", menu=grafik_olusturma)
    grafik_olusturma.add_command(label="Grafik Oluştur", command=baslat_kod)
    grafik_olusturma.add_command(label="Bilgileri Sil", command=reset_grafik_data)
    destek.add_command(label="Hakkında", command=about)
    destek.add_command(label="Güncelleme", command=updates)
    destek.add_command(label="İletişim", command=iletisim)
    destek.add_command(label="Duyurular",command=duyurular)
    menu_buton.add_command(label="Console",command=console)
    menu_buton.add_separator()
    menu_buton.add_command(label="Çıkış", command=exitt)
    menu.add_command(label="Yardım",command=help)

    baslangic.mainloop()

if __name__ == "__main__":
    ProgramStart()

import tkinter

my_window = tkinter.Tk()
my_window.minsize(300, 300)
my_window.title("BMI_Calculator")


kilo = tkinter.Label(text="Lütfen Kilo Bilginizi Giriniz").place(x=85, y=0)
kilo_entry = tkinter.Entry(width=10)
kilo_entry.place(x=125, y=20)
kilo_unit = tkinter.Label(text="kg").place(x=195, y=20)


boy = tkinter.Label(text="Lütfen Boy Bilginizi Giriniz").place(x=85, y=100)
boy_entry = tkinter.Entry(width=10)
boy_entry.place(x=125, y=120)
boy_unit = tkinter.Label(text="cm").place(x=195, y=120)

bmi_label = tkinter.Label(text="")
bmi_label.pack(pady=100, side="bottom")
#bmi_label.place(x=100, y=180)

def BMI_Hesaplama():
    kg = kilo_entry.get()
    cm = boy_entry.get()
    try:
        kg_float = float(kg)
        cm_float = float(cm) / 100
        bmi_index = kg_float / (cm_float * cm_float)
        bmi_index = round(bmi_index, 1)
        if bmi_index <= 18.5:
            bmi_label.config(text="Vücut kitle indeksiniz= "+str(bmi_index)+" --> Zayıfsınız")
        elif 18.5 < bmi_index <= 24.9:
            bmi_label.config(text="Vücut kitle indeksiniz= "+str(bmi_index)+" --> Normalsiniz")
        elif 24.9 < bmi_index <= 29.9:
            bmi_label.config(text="Vücut kitle indeksiniz= "+str(bmi_index)+" --> Kilolusunuz")
        elif 29.9 < bmi_index:
            bmi_label.config(text="Vücut kitle indeksiniz= "+str(bmi_index)+" --> Obezsiniz")
    except ValueError:
        if not kg:
            bmi_label.config(text="Lütfen bir kilogram değeri giriniz")
        elif not cm:
            bmi_label.config(text="Lütfen bir boy değeri giriniz")
        else:
            bmi_label.config(text="Lütfen bir sayı giriniz")


bmi = tkinter.Button(text="Hesapla", command=BMI_Hesaplama)
bmi.place(x=130, y=150)
bmi.update()


my_window.mainloop()
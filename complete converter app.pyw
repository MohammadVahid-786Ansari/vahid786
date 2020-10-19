from tkinter import Tk, Button, Label, DoubleVar, Entry ,BooleanVar
window = Tk()
window.title("Feet To Meter and C.M. Converter")
window.configure(background="black")
window.geometry("550x300")
window.resizable(width=False, height=False)


def convert():
    """this function will convert feet to meter and cm"""
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set(round(meter,4))
    cm = value * 30.48
    cm_value.set(round(cm,4))

def convert1():
    value_1 = float(mt_entry.get())
    feet_1 = value_1/0.3048
    ft_value.set(round(feet_1,4))
    cm_1 = value_1*100
    cm_value.set(round(cm_1,4))

def convert2():
    value_2 = float(cm_entry.get())
    feet_2 = value_2 / 30.48
    ft_value.set(round(feet_2,4))
    meter_2= value_2 / 100
    mt_value.set(round(meter_2,4))

def clr():
    ft_value.set("")
    mt_value.set("")
    cm_value.set("")


ft_label = Label(window, text="FEET", bg="white", fg="black", width=20)
ft_label.grid(column=0, row=0, padx=28, pady=20)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=20)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')

mt_label = Label(window, text="METER", bg="white", fg="black", width=20)
mt_label.grid(column=0, row=1, pady=20)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=20)
mt_entry.grid(column=1, row=1)
mt_entry.delete(0, 'end')

cm_label = Label(window, text="C.M.", bg="white", fg="black", width=20)
cm_label.grid(column=0, row=2, pady=20)

cm_value = DoubleVar()
cm_entry = Entry(window, textvariable=cm_value, bg="white", fg="black", width=20)
cm_entry.grid(column=1, row=2)
cm_entry.delete(0, 'end')

convert_btn = Button(window, text="FEET TO ME. AND CM", bg="white", fg="black", width=20, command=convert)
convert_btn.grid(column=0, row=3, pady=15)

convert_btn1 = Button(window, text="ME. TO FEET AND CM", bg="white", fg="black", width=20, command=convert1)
convert_btn1.grid(column=1, row=3, pady=15)

convert_btn2 = Button(window, text="CM TO FEET AND ME.", bg="white", fg="black", width=20, command=convert2)
convert_btn2.grid(column=2, row=3, padx=15,pady=15)

clr_btn = Button(window, text="CLEAR", bg="white", fg="black", width=15, command=clr)
clr_btn.grid(column=1, row=4, padx=15,pady=15)

window.mainloop()


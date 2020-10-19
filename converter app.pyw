from tkinter import Tk,Button,Label,DoubleVar,Entry

window = Tk()
window.title("Feet To Meter and C.M. Converter")
window.configure(background="black")
window.geometry("400x300")
window.resizable(width=False,height=False)


def convert():
    """this function will convert"""
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set(round(meter,4))
    cm = value * 30.48
    cm_value.set(round(cm,4))


def clr():
    """this function will clear"""
    ft_value.set("")
    mt_value.set("")
    cm_value.set("")


ft_label = Label(window,text="FEET",bg="white",fg="black",width=20)
ft_label.grid(column=0,row=0,padx=45,pady=20)

ft_value = DoubleVar()
ft_entry = Entry(window,textvariable=ft_value,width=20)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')


mt_label = Label(window,text="METER",bg="white",fg="black",width=20)
mt_label.grid(column=0,row=1,pady=20)

mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=20)
mt_entry.grid(column=1,row=1)
mt_entry.delete(0,'end')



cm_label = Label(window,text="C.M.",bg="white",fg="black",width=20)
cm_label.grid(column=0,row=2,pady=20)

cm_value = DoubleVar()
cm_entry = Entry(window,textvariable=cm_value,bg="white",fg="black",width=20)
cm_entry.grid(column=1,row=2)
cm_entry.delete(0,'end')


convert_btn = Button(window,text="CONVERT",bg="white",fg="black",width=15,command=convert)
convert_btn.grid(column=0,row=3,pady=15)

clr_btn = Button(window,text="CLEAR",bg="white",fg="black",width=15,command=clr)
clr_btn.grid(column=1,row=3,pady=15)














window.mainloop()





































































































































































































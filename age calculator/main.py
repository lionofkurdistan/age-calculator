
from time import daylight
from tkinter import *
from datetime import date
from unicodedata import name

root = Tk()
root.title("age calculator")
root.geometry("800x600")
root.resizable(False,False)


photo = PhotoImage(file="Agecalculator.png")
myimage = Label(image=photo)
myimage.pack(padx=15,pady=15)


def calculatorAge():
    today = date.today()
    birthDate = date(int(yearEnty.get()),int(monthEnty.get()),int(dayEnty.get()))
    age = today.year - birthDate.year - ((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}",font=30).place(x=300,y=500)

Label(text="Name",font=23).place(x=200,y=250)

Label(text="Year",font=23).place(x=200,y=300)

Label(text="Month",font=23).place(x=200,y=350)

Label(text="Day",font=23).place(x=200,y=400)


nameValue = StringVar()

yearValue = StringVar()

monthValue = StringVar()

dayValue = StringVar()


nameEnty = Entry(root,textvariable=nameValue,width=30,bd=3,font=20)
nameEnty.place(x=300,y=250)

yearEnty = Entry(root,textvariable=yearValue,width=30,bd=3,font=20)
yearEnty.place(x=300,y=300)

monthEnty = Entry(root,textvariable=monthValue,width=30,bd=3,font=20)
monthEnty.place(x=300,y=350)


dayEnty = Entry(root,textvariable=dayValue,width=30,bd=3,font=20)
dayEnty.place(x=300,y=400)


Button(text="calculator",font=20,bg="black",fg="white",width=11,height=2,command=calculatorAge).place(x=300,y=450)











root.mainloop()

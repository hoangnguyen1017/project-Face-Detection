from tkinter import *
from test import *
r = Toplevel()
r.geometry("300x300")
r.title("Face Recognition")
r.resizable(False, False)


def account():
    pass

def Face_recognition():
    pass

lb_manage = Label(r,text="Log in with  account or face recognition",fg="red",font="arial 10")
lb_manage.place(x=40,y=50)

bttn_acc = Button(r,text="Account",fg="black",font="arial 10",width=10,command=account)
bttn_acc.place(x=100, y=90)

bttn_fr = Button(r,text="Face Recognition",fg="black",font="arial 10",width=15,command=manage_window)
bttn_fr.place(x=80, y=130)

r.mainloop()
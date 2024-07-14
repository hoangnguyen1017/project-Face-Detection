from tkinter import *
#from Sign import*
from window import *
from test import *
root = Tk()
root.geometry("550x500")
root.title("Face Recognition")
root.resizable(False,False)

bg = PhotoImage(file=r"C:\Users\nguye\Downloads\Project-FACE\pic4.png")
bg = bg.subsample(4)
lb = Label(root, image=bg)
lb.place(x=-10 ,y=-90, relwidth=1, relheight=1)

def client():
    root.withdraw()
    window_client()
    
def manage():
    root.withdraw()
    manage_window()

lb_wel = Label(root,text="Facial Recognition Program",fg="red",font="arial 30")
lb_wel.place(x=30,y=10)

lb_1 = Label(root,text="Please choose role to continue: ",fg="black",font="arial 10")
lb_1.place(x=170,y=250)

#button Client
bttn_client= Button(root,text="Client",fg="black",font="arial 10",width=10,command=client)
bttn_client.place(x=215, y=280)

#button Manage
bttn_manage= Button(root,text="Manager",fg="black",font="arial 10",width=10,command=manage)
bttn_manage.place(x=215, y=318)



root.mainloop()

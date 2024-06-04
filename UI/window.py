from tkinter import *
from Sign import *
from pass_encrypt import *
from Register import *
from database import *
def window_client():
    r = Tk()
    r.geometry("1400x700")
    r.title("Facial Recognition")
    r.resizable(False,False)

    bg = PhotoImage(file=r"C:\Users\nguye\Downloads\Project-FACE\pic1.png")

    lb = Label(r, image=bg)
    lb.place(x=400 ,y=0, relwidth=1, relheight=1)

    def sign():
        r.withdraw()
        name = input_name.get()
        passw = input_pass.get()
        login_hash_pass = hash_password_salt(passw)
        check_password = check_pass(name,login_hash_pass)
        if check_password is not None:
            print("Logged in successfully")
            lb_2 = Label(r,text="Logged in successfully",fg="red",font="arial 10")
            lb_2.place(x=110,y=290)
            query = "SELECT id_user FROM User WHERE name = ? and password = ?"
            result = fetch_one(query, (name, login_hash_pass))
            if result is not None:
                id_user = result[0] 
                
                check_role(id_user)
        else:
            messagebox.showerror(title="Error", message="Wrong account or password. Please check again")
            print("Error")

    def register():
        r.withdraw()
        register_window()
        

    #window 1
    show_icon = PhotoImage(file='show_icon.png')
    hide_icon = PhotoImage(file='hide_icon.png')
    show_icon= show_icon.subsample(7)
    hide_icon= hide_icon.subsample(7)

    def show_pass():
        if pass_entry['show']== '':
            pass_entry.config(show='*')
            show_hide_bttn1.config(image=hide_icon)
        else:
            pass_entry.config(show='')
            show_hide_bttn1.config(image=show_icon)
            
    show_hide_bttn1 = Button(r, image=hide_icon,bd=0,command=show_pass)
    show_hide_bttn1.place(x=365,y=267)

    lb= Label(r,text="Sign in",font="arial 20", fg="black")
    lb.place(x=150,y=140)

    input_name = StringVar()
    lb_name = Label(r,text="Username: ",font="arial 10")
    lb_name.place(x=30,y=240)

    input_pass = StringVar()
    lb_pass = Label(r,text="Password: ",font="arial 10")
    lb_pass.place(x=30,y=270)

    name_entry = Entry(r,bg= "white",width="35",fg="black",font="arial 10",textvariable=input_name)
    name_entry.place(x= 110, y=240)

    pass_entry = Entry(r,bg= "white",width="35",fg="black",font="arial 10",show="*",textvariable=input_pass)
    pass_entry.place(x= 110, y=270)

    #button sign
    bttn_sign = Button(r,text="SIGN IN",fg="black",font="arial 10",width="10",command=sign)
    bttn_sign.place(x=110,y=320)

    #buttion register
    bttn_register = Button(r,text="REGISTER",fg="black",font="arial 10",width="10",command=register)
    bttn_register.place(x=270,y=320)


    r.mainloop()
window_client()

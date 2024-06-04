from tkinter import *
import sqlite3
root = Tk()
root.geometry("500x500")

def select_role(event):
    lb = Label(root, text= clicked.get().split(',')[0].split('()')).pack()


conn =sqlite3.connect('Face_db.db')
c = conn.cursor()

query = """SELECT role_name FROM role """
c = conn.cursor()
c.execute(query)
rows = c.fetchall()
conn.commit()
print(rows)

clicked = StringVar()
clicked.set(rows[0])

drop = OptionMenu(root,clicked, *rows,command=select_role)
drop.pack(pady= 20)

# bttn_select = Button(root,text="Select",command=select_role)
# bttn_select.pack()
root.mainloop()
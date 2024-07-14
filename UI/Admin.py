from tkinter import *
from tkinter import ttk
import sqlite3
from database import *
def admin_window():
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',values=i)

    def search():
        q2= q.get()
        query = "SELECT id_user,name,role from admin where name LIKE'%"+q2+"%'"
        c.execute(query)
        rows = c.fetchall()
        update(rows)
        
    def clear():
        query = "SELECT id_user,name,role from admin "
        c.execute(query)
        rows = c.fetchall()    
        update(rows)

    def getrow(event):
        item = trv.item(trv.focus())
        t1.set(item['values'][0])
        t2.set(item['values'][1])
        t3.set(item['values'][2])

    def update_user():
        id = t1.get()
        name = t2.get()
        role = t3.get()

        if messagebox.askyesno("Confirm Please", "Are you Sure you want to update this user?"):
            admin_query = "UPDATE admin SET name=  ?, role= ? WHERE id_user= ?"
            c.execute(admin_query,(name,role,id))

            user_query = "UPDATE user SET name=? WHERE id_user=?"
            c.execute(user_query, (name, id))

            user_role_query = "UPDATE user_role SET id_role=(SELECT id_role FROM role WHERE role_name=?) WHERE id_user=?"
            c.execute(user_role_query, (role, id))
            
            conn.commit()
            clear()
        else:
            return True


    def delete_user():
        user_id = t1.get()
        if messagebox.askyesno("Confirm Delete","Are you sure want to delete this user?"):
            query = "DELETE FROM Admin WHERE id = "+user_id
            c.execute(query)
            clear()
        else:
            return True


    conn =sqlite3.connect('Face_db.db')
    c = conn.cursor()

    root = Toplevel()
    q = StringVar()
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()


    box1 = LabelFrame(root,text="User List")
    box2 = LabelFrame(root,text="Search")
    box3 = LabelFrame(root,text="User Data")

    box1.pack(fill="both",expand="yes",padx=20,pady=10)
    box2.pack(fill="both",expand="yes",padx=20,pady=10)
    box3.pack(fill="both",expand="yes",padx=20,pady=10)

    trv = ttk.Treeview(box1,columns=(1,2,3),show="headings",height="6")
    trv.pack()

    trv.heading(1, text="User ID")
    trv.heading(2, text="Name")
    trv.heading(3, text="Role")

    trv.bind_all('<Double 1>',getrow)


    query = 'SELECT * FROM Admin'
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()
    update(rows)



    query1 = """SELECT role_name FROM role """
    c = conn.cursor()
    c.execute(query1)
    rows1 = c.fetchall()
    roles = [role[0] for role in rows1]

    #Label Search
    lb = Label(box2,text="Search")
    lb.pack(side=LEFT, padx=10)
    entry = Entry(box2,textvariable=q)
    entry.pack(side=LEFT, padx=6)
    bttn = Button(box2,text="Search",command=search)
    bttn.pack(side=LEFT,padx=6)
    #Clear
    bttn_clear = Button(box2,text="Clear",command=clear)
    bttn_clear.pack(side=LEFT,padx=6)


    #User data
    lb1 = Label(box3, text="User ID : ")
    lb1.grid(row=0,column=0,padx=5,pady=3)
    entry1 = Entry(box3,textvariable=t1)
    entry1.grid(row=0,column=1,padx=5,pady=3)

    lb2 = Label(box3, text="Name : ")
    lb2.grid(row=1,column=0,padx=5,pady=3)
    entry2 = Entry(box3,textvariable=t2)
    entry2.grid(row=1,column=1,padx=5,pady=3)

    lb3 = Label(box3, text="Role : ")
    lb3.grid(row=2,column=0,padx=5,pady=3)
    t3.set(rows1[0])
    entry3 = OptionMenu(box3,t3,*roles)
    entry3.grid(row=2,column=1,padx=5,pady=3)


    bttn_update = Button(box3,text="Update",command=update_user)
    bttn_delete = Button(box3,text="Delete",command=delete_user)

    bttn_update.grid(row=3,column=0,padx=5,pady=3)
    bttn_delete.grid(row=3,column=4,padx=5,pady=3)






    root.title("Admin")
    root.geometry("700x600")
    root.mainloop()
admin_window()
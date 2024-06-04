# from Register import *
from tkinter import messagebox
import sqlite3

conn =sqlite3.connect('Face_db.db')
c = conn.cursor()


# TABLE User

def addUser(id,name,password):
    view = "select * from User where id_user = ?"
    add = """INSERT INTO User
                                              (id_user,name,password)
                                              VALUES (?, ?, ?);"""
    add_user_role = """INSERT INTO user_role 
                                            (id_user, id_role)
                                            VALUES (?, ?);"""

    if fetch_one(view, (id,)) is not None:
        messagebox.showerror(title="Error",message="Name is available")
        
    elif fetch_one(view, (id,)) is None:
        execute_sql(add, (id,name,password))
        execute_sql(add_user_role, (id,1))
        print("Account successfully created")
    else:
        messagebox.showerror(title="Error",message="Name is available")

def check_pass(name,password):
    view = "select * from User where name = ? and password = ?"
    record = fetch_one(view,(name, password,))
    return record

#TABLE Admin

def admin():
    query = """
    INSERT INTO Admin (ID_user, Name, Role)
    SELECT u.id_user, u.name, r.role_name
    FROM user u
    JOIN user_role ur ON u.id_user = ur.id_user
    JOIN role r ON ur.id_role = r.id_role
    WHERE u.id_user NOT IN (SELECT ID_user FROM Admin);
"""
    execute_sql(query)



# TABLE ROLE

def addRole(id,role_name):
    view = "select * from Role where id_role = ?"
    add = """INSERT INTO Role
                                              (id_role,role_name)
                                              VALUES (?, ?);"""
    
                                                    
    if fetch_one(view, (id,)) is not None:
        messagebox.showerror(title="Error",message="Name is available")
        
    elif fetch_one(view, (id,)) is None:
        execute_sql(add, (id,role_name))

        print("Account successfully created")
    else:
        messagebox.showerror(title="Error",message="Name is available")







# c.execute('''CREATE TABLE IF NOT EXISTS test_password (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT,
#                     password TEXT
#                 )''')

# c.execute("""CREATE TABLE ADMIN (
#           ID_User integer PRIMARY KEY,
#           Name text,
#           Role text
#           )""")

# c.execute("""CREATE TABLE Role (
#           ID_Role integer PRIMARY KEY,
#           Role_Name text
#           )""")

# c.execute("""CREATE TABLE User_Role (
#           ID_User integer PRIMARY KEY,
#           ID_Role integer 
#           )""")

# c.execute("""CREATE TABLE User (
#           ID_User integer PRIMARY KEY,
#           Name integer,
#           Password integer 
#           )""")



def execute_sql(sql, params=()):
   cur = conn.cursor()
   cur.execute(sql, params)
   conn.commit()
   return cur

def fetch_all(sql):
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def fetch_all1(sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchall()

def fetch_one(sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchone()



def executemany_sql(sql, params):
    cur = conn.cursor()
    cur.executemany(sql, params)
    conn.commit()
    return cur



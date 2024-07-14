
from database import *
conn =sqlite3.connect('Face_db.db')
from Admin import *

def validUser(name, password):
    view = "SELECT * FROM User WHERE  name = ? AND password = ?"
    if fetch_one(view, (name,password,)) is None:
        return False
    else:
        return True

def fetch_one(sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchone()



def check_role(id):
    view = "SELECT id_user, name FROM User WHERE id_user = ? "
    user_data = fetch_one(view, (id,)) 
    if user_data is not None:
        user_id, name = user_data
        query = """
            SELECT r.role_name
            FROM user_role ur
            JOIN role r ON ur.id_role = r.id_role
            WHERE ur.id_user = ? ;
        """
        role_data = fetch_one(query, (user_id,))
        if role_data is not None:
            role_name = role_data[0]  
            if role_name == 'Admin':                 
                admin_window()
            else:
                print("Error: User is not an admin")
        else:
            print("Error: User has no role assigned")
    else:
        print("Error: User not found")


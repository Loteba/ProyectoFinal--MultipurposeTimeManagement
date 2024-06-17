import sqlite3

def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, 
                  username TEXT NOT NULL UNIQUE, 
                  password TEXT NOT NULL, 
                  fullname TEXT, 
                  email TEXT, 
                  phone TEXT)''')
    conn.commit()
    conn.close()

def register_user(fullname, email, phone, username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (fullname, email, phone, username, password) VALUES (?, ?, ?, ?, ?)",
                  (fullname, email, phone, username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Username already exists
    conn.close()
    return True

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

create_database()

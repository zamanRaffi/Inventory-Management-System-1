import sqlite3
from utils import hash_password

def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()

    # Create employee table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            eid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            dob TEXT,
            doj TEXT,
            pass TEXT,
            utype TEXT,
            address TEXT,
            salary TEXT
        )
    """)
    con.commit()

    # Create supplier table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS supplier (
            invoice INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            desc TEXT
        )
    """)
    con.commit()

    # Create category table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS category (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)
    con.commit()

    # Create product table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS product (
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            Category TEXT,
            Supplier TEXT,
            name TEXT,
            price TEXT,
            qty TEXT,
            status TEXT
        )
    """)
    con.commit()

    # Create users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    con.commit()

    # Insert default admin user if the users table is empty
    cur.execute("SELECT * FROM users WHERE username = 'admin'")
    if cur.fetchone() is None:
        hashed_password = hash_password('admin123')  # Hash the default password
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', hashed_password))
        con.commit()
    else:
        print("Default user already exists.")

    con.close()
  

# Call the function to create the database and tables
create_db()

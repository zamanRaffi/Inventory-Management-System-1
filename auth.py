# auth.py
from tkinter import *
from tkinter import messagebox
import sqlite3

class AuthClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300+500+250")
        self.root.title("Login")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        self.var_username = StringVar()
        self.var_password = StringVar()

        # Title
        title = Label(self.root, text="Login", font=("goudy old style", 20), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        # Username
        lbl_username = Label(self.root, text="Username", font=("goudy old style", 15), bg="white").place(x=20, y=70)
        txt_username = Entry(self.root, textvariable=self.var_username, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=70, width=200)

        # Password
        lbl_password = Label(self.root, text="Password", font=("goudy old style", 15), bg="white").place(x=20, y=120)
        txt_password = Entry(self.root, textvariable=self.var_password, show='*', font=("goudy old style", 15), bg="lightyellow").place(x=150, y=120, width=200)

        # Login Button
        btn_login = Button(self.root, text="Login", command=self.login, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=150, y=180, width=100, height=40)

    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE username=? AND password=?", (self.var_username.get(), self.var_password.get()))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
            else:
                messagebox.showinfo("Success", "Login Successful", parent=self.root)
                self.root.destroy()  # Close the login window
                import dashboard  # Import dashboard after successful login
                dashboard.launch_dashboard()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = AuthClass(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
import pyodbc  # Assuming you have installed pyodbc for database connectivity

# Establish a database connection
conn = pyodbc.connect('DRIVER={ODBC Driver};SERVER=test;UID=M11MCA20;PWD=M11MCA20;')

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        self.label1 = tk.Label(root, text="Username:")
        self.label1.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.label2 = tk.Label(root, text="Password:")
        self.label2.pack()
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username.lower() == "admin" and password.lower() == "admin":
            self.root.withdraw()  # Hide the login window
            AdminWindow(self.root)
        else:
            messagebox.showerror("Error", "Invalid login credentials")

class AdminWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")

        self.label = tk.Label(root, text="Welcome, Admin!")
        self.label.pack()

        self.logout_button = tk.Button(root, text="Logout", command=self.logout)
        self.logout_button.pack()

    def logout(self):
        self.root.destroy()
        LoginWindow(tk.Tk())

if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()

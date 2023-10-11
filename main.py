import tkinter as tk
from tkinter import Entry, Label, Button, messagebox

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    
    # Insert login logic here
    # For now, it'll just display a message box
    messagebox.showinfo("Login Info", f"Logging in with:\nUsername: {user}\nPassword: {pwd}")

def create_username():
    new_user = create_username_entry.get()
    
    # Insert logic for creating a new user here
    # For now, it'll just display a message box
    messagebox.showinfo("Creation Info", f"Creating user with Username: {new_user}")

# Create the main window
root = tk.Tk()
root.title("Login and Create User")

# Login widgets
username_label = Label(root, text="Username:")
username_label.grid(row=0, column=0)

username_entry = Entry(root)
username_entry.grid(row=0, column=1)

password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0)

password_entry = Entry(root, show='*')
password_entry.grid(row=1, column=1)

login_button = Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

# Create username widgets
create_username_label = Label(root, text="Create Username:")
create_username_label.grid(row=3, column=0)

create_username_entry = Entry(root)
create_username_entry.grid(row=3, column=1)

create_username_button = Button(root, text="Create", command=create_username)
create_username_button.grid(row=4, column=0, columnspan=2)

# Run the main loop
root.mainloop()

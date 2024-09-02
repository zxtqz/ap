import tkinter as tk

window = tk.Tk()

window.title = "My First GUI App"
window.geometry("500x700")

username_var = tk.StringVar(value ="")
password_var = tk.StringVar(value ="")
msg_var = tk.StringVar(value="")
is_active = tk.BooleanVar(value=False)

def submit_login_command():
    
    if username_var.get() == "admin" and password_var.get() == "admin":
       msg_var.set("Entered into ADMIN")
    else:
        print("Incorrect Username or Password",msg_var)

def showpassword_command():
    if is_active.get():
        is_active.set(False)
        password_entry.config(show="*")
    else:
        is_active.se(True)
        password_entry.config(show="")

welcome_label = tk.Label(text="My LoginPage",font=("Helvetice",24,'bold'))

welcome_label.pack(pady=25)

username_label = tk.Label(text="Username: ",font=("Helvetica",18,"bold"))

username_label.pack(pady=10,anchor="nw",padx=25)

username_entry = tk.Entry(font=("Helvetica",18,"bold"),textvariable=username_var)

username_entry.pack(fill="x",padx=25,ipady=5,ipadx=10)

password_label = tk.Label(text="Password: ",font=("Helvetica",18,"bold"))

password_label.pack(pady=10,anchor="nw",padx=25)

password_var = tk.StringVar()

password_entry = tk.Entry(font=("Helvetica",18,"bold"),show="*",textvariable=password_var)

password_entry.pack(fill="x",padx=25,ipady=5)

submit_button = tk.Button(
    command=submit_login_command,
    text="LOGIN",
    bg="#52f24d",
    fg="white",
    activebackground="#64ed60",
    activeforeground="#FEFEFE",
    pady=10,
    padx=15,
    bd=0,
    font=("Helvetica",18,"bold")
    )

submit_button.pack(pady=25,fill="x",padx=50)
error_msg_label = tk.Label(textvariable=msg_var)
error_msg_label.pack()

# def submit_login_command():
#     error_msg_var.set("Incorrect password")
#     if username_var.get() == "admin" and password_var.get() == "admin":
#         print("Sucessfully Entered")
#     else:
#         print("Incorrect Username or Password",error_msg_var)

# def click_me():
#     print("Clicked!")

# my_label = tk.Label(text="Hello, World",
#     bg="#0ceac2",
#     fg="#FFFFFF",
#     width=10,
#     height=10,
#     font=('MS Sans Serif',50))

# my_label.pack()

# mycommand =  click_me

# x = tk.StringVar()

# user_entry = tk.Entry(textvariable=x)

# user_entry.pack()

# test_label = tk.Label(textvariable=x)

# test_label.pack()

# # my_button = tk.Button(text= "Click Me!",width=50,height=30,command=click_me)

# my_cool_button = tk.Button(text="Click Me!",
#     command=mycommand,
#     font=("Helvetica",16,'bold'),
#     bg="#0cb1ea",
#     fg="#FFFFFF",
#     bd = 10,
#     padx = 20,
#     pady=30,
#     activebackground="red",
#     activeforeground="black"
# )

# my_cool_button.pack()

# # my_button.pack()

window.mainloop()
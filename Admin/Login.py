import sqlite3
from tkinter import *
from tkinter import messagebox
import os
import tkinter as tk
root = Tk()
# Tính toán kích thước và vị trí của cửa sổ giữa màn hình
width = 1366
height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.title("Retail Manager(ADMIN)")


user = StringVar()
passwd = StringVar()
class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Quản lý bán hàng (ADMIN)")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/admin_login.png")
        self.img = PhotoImage(file="./Images/admin_login.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.373, rely=0.273, width=374, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        self.entry1.focus()
        self.entry1.configure(textvariable=user)
        new_text = "ADM002"
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, new_text)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.373, rely=0.384, width=374, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passwd)
        new_text = "12345"
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, new_text)


        self.button1 = Button(root)
        self.button1.place(relx=0.366, rely=0.685, width=356, height=43)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#D2463E")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#D2463E")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(command=self.login)

    def login(self, Event=None):
        username = user.get()
        password = passwd.get()

        with sqlite3.connect("./Database/database.db") as db:
            cur = db.cursor()
        find_user = "SELECT * FROM employee WHERE emp_id = ? and password = ?"
        cur.execute(find_user, [username, password])
        results = cur.fetchall()
        if results:
            if results[0][6] == "Admin":
                messagebox.showinfo("Login Page", "The login is successful.")
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)

                root.withdraw()
                os.system("python ./Admin/menuAdmin.py")
                root.deiconify()


            else:
                messagebox.showerror("Oops!!", "You are not an admin.")

        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            page1.entry2.delete(0, END)


    def exit(self):
        sure = messagebox.askyesno("Exit", "Bạn có muốn thoát không?", parent=root)
        if sure == True:
            root.destroy()


page1 = login_page(root)
root.bind("<Return>", login_page.login)
root.mainloop()
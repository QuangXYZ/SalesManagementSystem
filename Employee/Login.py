from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()

root.geometry("1366x768")
root.title("Login")

user = StringVar()
passwd = StringVar()


# "INSERT INTO employee(emp_id, name, contact_num, address, aadhar_num, password, designation) VALUES(?,?,?,?,?,?,?)"
def create_emp():
    conn = sqlite3.connect('./Database/database.db')

    # Tạo bảng trong cơ sở dữ liệu
    conn.execute('''CREATE TABLE employee
                    (emp_id TEXT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    contact_num TEXT NULL,
                    address TEXT NULL,
                    cccd TEXT NULL,                   
                    password TEXT NOT NULL,
                    designation TEXT NULL
                    );''')

    # Thêm dữ liệu vào bảng
    conn.execute(
        "INSERT INTO employee (emp_id, name, contact_num, address, cccd, password, designation) VALUES ('EMP001', 'John Doe', '123456789', 'Hcm', '079202021234', 'bcd', 'abc')")
    conn.execute(
        "INSERT INTO employee (emp_id, name, contact_num, address, cccd, password, designation) VALUES ('EMP002', 'q', '123456789', 'Hcm', '079202021234', '12345', 'abc')")
    conn.commit()
    conn.close()
create_emp()
class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Retail Manager")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/employee_login.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.373, rely=0.273, width=374, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.373, rely=0.384, width=374, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passwd)

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
        self.button1.configure(command=login)


def login(Event=None):
    global username
    username = user.get()
    password = passwd.get()
    print(username)
    print(password)
    with sqlite3.connect("./Database/database.db") as db:
        cur = db.cursor()
    find_user = "SELECT * FROM employee WHERE emp_id = ? and password = ?"
    cur.execute(find_user, [username, password])
    results = cur.fetchall()
    print(results)
    if results:
        messagebox.showinfo("Login Page", "The login is successful")
        # page1.entry1.delete(0, END)
        # page1.entry2.delete(0, END)
        # root.withdraw()
        # global biller
        # global page2
        # biller = Toplevel()
        # page2 = bill_window(biller)
        # page2.time()
        # biller.protocol("WM_DELETE_WINDOW", exitt)
        # biller.mainloop()
        print("Thành công")

    else:
        messagebox.showerror("Error", "Incorrect username or password.")
        # page1.entry2.delete(0, END)
        print("Thất bại")

page1 = login_page(root)
root.mainloop()
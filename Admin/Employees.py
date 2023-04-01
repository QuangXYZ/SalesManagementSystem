import sqlite3
from time import strftime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import string
import random


root = Tk()
width = 1366
height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.title("Retail Manager(ADMIN)")

with sqlite3.connect("./Database/database.db") as db:
    cur = db.cursor()

def random_emp_id(stringLength):
    Digits = string.digits
    strr=''.join(random.choice(Digits) for i in range(stringLength-3))
    return ('EMP'+strr)

def valid_phone(phn):
    if re.match(r"[0]\d{9}$", phn):#[0]: bắt đầu bằng số 0, \d: đại diện ký tự từ 0-9, {9}: bắt buộc có 9 ký tự
        return True
    return False

def valid_identification(aad):
    if aad.isdigit() and len(aad)==12:
        return True
    return False

def checkData(e_add, name, contact, identification, designation, address, password):
    if not name:
        messagebox.showerror("Lỗi!", "Vui lòng nhập tên.", parent=e_add)
        return False
    if valid_phone(contact) is False:
        messagebox.showerror("Lỗi!", "Số điện thoại không hợp lệ.", parent=e_add)
        return False
    if valid_identification(identification) is False:
        messagebox.showerror("Lỗi!", "Số căn cước không hợp lệ.", parent=e_add)
        return False
    if not designation:
        messagebox.showerror("Lỗi!", "Vui lòng nhập quyền.", parent=e_add)
        return False
    if not address:
        messagebox.showerror("Lỗi!", "Vui lòng nhập địa chỉ.", parent=e_add)
        return False
    if not password:
        messagebox.showerror("Lỗi!", "Vui lòng nhập password.", parent=e_add)
        return False
    return True

class Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Employee Management")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/employee2.png")
        self.label1.configure(image=self.img)

        self.message = Label(root)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""Quản trị viên""")
        self.message.configure(anchor="w")

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(root)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Tìm kiếm""")
        self.button1.configure(command=self.search_emp)

        self.button2 = Button(root)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Đăng xuất""")
        # self.button2.configure(command=self.Logout)

        self.button3 = Button(root)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""THÊM NHÂN VIÊN""")
        self.button3.configure(command=self.add_emp)

        self.button4 = Button(root)
        self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""CHỈNH SỬA NHÂN VIÊN""")
        self.button4.configure(command=self.update_emp)

        self.button5 = Button(root)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""XÓA NHÂN VIÊN""")
        self.button5.configure(command=self.delete_emp)

        self.button6 = Button(root)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""THOÁT""")
        # self.button6.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(root, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(root, orient=VERTICAL)
        self.tree = ttk.Treeview(root)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Mã nhân viên",
                "Tên nhân viên",
                "Số điện thoại",
                "Địa chỉ",
                "Căn cước",
                "Mật khẩu",
                "Quyền"
            )
        )

        self.tree.heading("Mã nhân viên", text="Mã nhân viên", anchor=W)
        self.tree.heading("Tên nhân viên", text="Tên nhân viên", anchor=W)
        self.tree.heading("Số điện thoại", text="Số điện thoại", anchor=W)
        self.tree.heading("Địa chỉ", text="Địa chỉ", anchor=W)
        self.tree.heading("Căn cước", text="Căn cước", anchor=W)
        self.tree.heading("Mật khẩu", text="Mật khẩu", anchor=W)
        self.tree.heading("Quyền", text="Quyền", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=198)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)

        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT * FROM employee")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def add_emp(self):
        global e_add
        e_add = Toplevel()
        page6 = add_employee(e_add)
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.mainloop()

    def ex(self):
        e_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()

    def ex2(self):
        e_update.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def update_emp(self):

        if len(self.sel) == 1:
            global e_update
            e_update = Toplevel()
            page3 = Update_Employee(e_update)
            e_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)

            page3.entry1.insert(0, vall[1])
            page3.entry2.insert(0, vall[2])
            page3.entry3.insert(0, vall[4])
            page3.entry4.insert(0, vall[6])
            page3.entry5.insert(0, vall[3])
            page3.entry6.insert(0, vall[5])
            e_update.mainloop()
        elif len(self.sel) == 0:
            messagebox.showerror("Error", "Vui lòng chọn nhân viên để chình sửa.")
        else:
            messagebox.showerror("Error", "Chỉ có thể chọn 1 nhân viên để chỉnh sửa.")

    def delete_emp(self):
        val = []
        to_delete = []

        if len(self.sel) != 0:
            sure = messagebox.askyesno("Confirm", "Bạn có chắc chắn muốn xóa các nhân viên?")
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)

                for j in range(len(val)):
                    if j % 7 == 0:
                        to_delete.append(val[j])

                flag = 1

                for k in to_delete:
                    if k == "ADM002":
                        flag = 0
                        break
                    else:
                        delete = "DELETE FROM employee WHERE emp_id = ?"
                        cur.execute(delete, [k])
                        db.commit()

                if flag == 1:
                    messagebox.showinfo("Success!!", "Nhân viên đã xóa khỏi cơ sở dữ liệu.")
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())
                    self.DisplayData()
                else:
                    messagebox.showerror("Error!!", "Không thể xóa quản trị viên.")
        else:
            messagebox.showerror("Error!!", "Vui lòng chọn nhân viên.")

    def search_emp(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Employee ID: {} tìm thấy.".format(self.entry1.get()))
                break
        else:
            messagebox.showerror("Oops!!", "Employee ID: {} không tìm thấy.".format(self.entry1.get()))

class add_employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Employee")

        self.label1 = Label(e_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/add_employee1.png")
        self.label1.configure(image=self.img)

        self.r1 = e_add.register(self.testint)
        self.r2 = e_add.register(self.testchar)

        self.entry1 = Entry(e_add)
        self.entry1.place(relx=0.132, rely=0.296, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(e_add)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_add)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_add)
        self.entry4.place(relx=0.527, rely=0.296, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry5 = Entry(e_add)
        self.entry5.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_add)
        self.entry6.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        self.button1 = Button(e_add)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ADD""")
        self.button1.configure(command=self.add)

        self.button2 = Button(e_add)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def add(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eidentification = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()
        #def checkData(self, name, contact, identification, designation, address, password):
        if checkData(e_add, ename, econtact, eidentification, edes, eadd, epass):
            emp_id = random_emp_id(7)
            insert = (
                "INSERT INTO employee(emp_id, name, contact_num, address, cccd, password, designation) VALUES(?,?,?,?,?,?,?)"
            )
            cur.execute(insert, [emp_id, ename, econtact, eadd, eidentification, epass, edes])
            db.commit()
            messagebox.showinfo("Success!!", "Employee ID: {} successfully added in database.".format(emp_id),parent=e_add)
            self.clearr()
        else:
            messagebox.showinfo("Lỗi!!", "Xảy ra lỗi.",parent=e_add)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False


class Update_Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Employee")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_employee1.png")
        self.label1.configure(image=self.img)

        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)

        self.entry1 = Entry(e_update)
        self.entry1.place(relx=0.132, rely=0.296, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(e_update)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_update)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_update)
        self.entry4.place(relx=0.527, rely=0.296, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry5 = Entry(e_update)
        self.entry5.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_update)
        self.entry6.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        self.button1 = Button(e_update)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""UPDATE""")
        self.button1.configure(command=self.update)

        self.button2 = Button(e_update)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

    def update(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eidentification = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()
        #def checkData(self, name, contact, identification, designation, address, password):
        if checkData(e_update, ename, econtact, eidentification, edes, eadd, epass):
            emp_id = vall[0]
            update = (
                "UPDATE employee SET name = ?, contact_num = ?, address = ?, cccd = ?, password = ?, designation = ? WHERE emp_id = ?"
            )
            cur.execute(update, [ename, econtact, eadd, eidentification, epass, edes, emp_id])
            db.commit()
            messagebox.showinfo("Success!!", "Employee ID: {} Đã chỉnh sửa dữ liệu.".format(emp_id))
            self.clearr()
    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False


page1 = Employee(root)
root.mainloop()
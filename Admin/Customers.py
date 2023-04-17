import os
import random
import re
import sqlite3
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import cv2

root = Tk()
width = 1366
height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

with sqlite3.connect("./Database/database.db") as db:
    cur = db.cursor()


def create_ctm():
    conn = sqlite3.connect('./Database/database.db')

    # Tạo bảng trong cơ sở dữ liệu
    conn.execute('''CREATE TABLE Customer
                    (ctm_id TEXT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    contact_num TEXT NULL,
                    address TEXT NULL,
                    cccd TEXT NULL,                   
                    img TEXT NULL,
                    discount TEXT NULL,
                    isLoyal BOOLEAN
                    discount TEXT NULL
                    );''')

    # Thêm dữ liệu vào bảng
    conn.execute(
        "INSERT INTO Customer (ctm_id, name, contact_num, address, cccd, img, discount,isLoyal) VALUES ('CTM001', 'John Doe', '123456789', 'Hcm', '079202021234', 'CTM001.png', '10','FALSE')")
    conn.execute(
        "INSERT INTO Customer (ctm_id, name, contact_num, address, cccd, img, discount,isLoyal) VALUES ('CTM002', 'John Doe', '123456789', 'Hcm', '079202021234', 'CTM002.png', '10','FALSE')")
    conn.commit()
    conn.close()


# cur.execute("drop table Customer")
# create_ctm(
# cur.execute("SELECT isLoyal from Customer where ctm_id='CTM001'")
# print(cur.fetchall())    
# conn.execute(
#     "INSERT INTO Customer (ctm_id, name, contact_num, address, cccd, img, discount) VALUES ('CTM002', 'John Doe', '123456789', 'Hcm', '079202021234', 'CTM002.png', '10')")
# conn.commit()
# conn.close()


class Customer:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Quản lý khách hàng")
        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/customer.png")
        self.label1.configure(image=self.img)

        self.message = Label(root)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(root)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

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
        self.button1.configure(text="""Tìm""")
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
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

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
        self.button3.configure(text="""Thêm Khách hàng""")
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
        self.button4.configure(text="""Cập nhật thông tin""")
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
        self.button5.configure(text="""Xóa khách hàng""")
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
        self.button6.configure(text="""Thoát""")
        self.button6.configure(command=self.Exit)

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
                "Customer ID",
                "Customer Name",
                "Contact No.",
                "Address",
                "Cccd",
                "Image",
                "Discount"
            )
        )

        self.tree.heading("Customer ID", text="Mã khách hàng", anchor=W)
        self.tree.heading("Customer Name", text="Tên khách hàng", anchor=W)
        self.tree.heading("Contact No.", text="Số điện thoại", anchor=W)
        self.tree.heading("Address", text="Địa chỉ", anchor=W)
        self.tree.heading("Cccd", text="Số CCCD", anchor=W)
        self.tree.heading("Image", text="Ảnh", anchor=W)
        self.tree.heading("Discount", text="Giảm giá (%)", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=220)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=140)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=180)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)

        self.DisplayData()

    sel = []

    def DisplayData(self):
        cur.execute("SELECT * FROM Customer")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def Exit(self):
        sure = messagebox.askyesno("Exit", "Bạn có chắc muốn thoát ?", parent=root)
        if sure == True:
            root.destroy()

    def add_emp(self):
        global e_add
        global emp_id
        emp_id = random_emp_id(7)
        e_add = Toplevel()
        page2 = add_employee(e_add)
        # page2.time()
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        e_add.mainloop()

    def search_emp(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search == to_search:
                self.tree.selection_set(val[val.index(search) - 1])
                self.tree.focus(val[val.index(search) - 1])
                messagebox.showinfo("Success!!", "Khách hàng ID: {} đã tìm thấy.".format(self.entry1.get()), parent=root)
                break
        else:
            messagebox.showerror("Oops!!", "khách hàng ID: {} không tìm thấy.".format(self.entry1.get()), parent=root)

    def ex(self):  # thoát screen thêm kh
        e_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Bạn có muốn đăng xuất?")
        if sure == True:
            root.destroy()
            os.system("python ./Admin/Login.py")

    def update_emp(self):

        if len(self.sel) == 1:
            global e_update
            e_update = Toplevel()
            page3 = Update_Employee(e_update)
            e_update.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            # page3.time()
            e_update.protocol("WM_DELETE_WINDOW", self.exUpdate)
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
            page3.entry6.configure(state='normal')
            page3.entry6.insert(0, vall[5])
            page3.entry6.configure(state='disabled')
            if (vall[7] == 'TRUE'):
                page3.checkButton.select()
            else:
                page3.checkButton.deselect()

            e_update.mainloop()
        elif len(self.sel) == 0:
            messagebox.showerror("Error", "Hãy chọn khách hàng cần cập nhất.")
        else:
            messagebox.showerror("Error", "Chỉ có thể cập nhật 1 khách hàng mỗi lần .")

    def exUpdate(self):
        sure = messagebox.askyesno("Exit", "Bạn có muốn thoát không?", parent=e_update)
        if sure == True:
            e_update.destroy()

    def delete_emp(self):
        val = []
        to_delete = []

        if len(self.sel) != 0:
            sure = messagebox.askyesno("Confirm", "Bạn có chắc muốn xóa (những) khách hàng này không?", parent=root)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)

                for j in range(len(val)):
                    if j % 7 == 0:
                        to_delete.append(val[j])

                flag = 1

                for k in to_delete:
                    if k == "EMP0000":
                        flag = 0
                        break
                    else:
                        delete = "DELETE FROM Customer WHERE ctm_id = ?"
                        cur.execute(delete, [k])
                        db.commit()

                if flag == 1:
                    messagebox.showinfo("Success!!", "Xóa thành công (những) khách hàng.", parent=root)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())
                    self.DisplayData()
                else:
                    messagebox.showerror("Error!!", "Cannot delete master admin.")
        else:
            messagebox.showerror("Error!!", "Please select an employee.", parent=root)


# màn hình thêm kh
class add_employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Thêm khách hàng")

        self.label1 = Label(e_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/add_customer.png")
        self.label1.configure(image=self.img)

        self.clock = Label(e_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

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
        self.entry4.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry5 = Entry(e_add)
        self.entry5.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_add)
        self.entry6.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(state='disabled')
        self.entry6.configure(relief="flat")

        self.button3 = Button(e_add)
        self.button3.place(relx=0.800, rely=0.529, width=86, height=30)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 14")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""PHOTO""")
        self.button3.configure(command=self.takePhoto)

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
        self.button1.configure(command=self.addCustomer)

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
        self.button2.configure(command=self.clearForm)

    def clearForm(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)

    def addCustomer(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()

        if ename.strip():
            if valid_phone(econtact):
                if valid_cccd(eaddhar):
                    if edes:
                        if eadd:
                            if epass:

                                insert = (
                                    "INSERT INTO Customer(ctm_id, name, contact_num, address, cccd, img, discount) VALUES(?,?,?,?,?,?,?)"
                                )
                                cur.execute(insert, [emp_id, ename, econtact, eadd, eaddhar, epass, edes])
                                db.commit()
                                messagebox.showinfo("Success!!",
                                                    "Khách hàng ID: {} đã thêm thành công.".format(emp_id),
                                                    parent=e_add)
                                self.clearForm()
                            else:
                                messagebox.showerror("Oops!", "Chưa điền mật khẩu.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Chưa điền địa chỉ.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Chưa điền mức giảm giá.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Số căn cước chưa đúng.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Số điện thoại chưa đúng.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Chưa điền tên nhân viên.", parent=e_add)

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

    def takePhoto(self):
        # Initialize camera object
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            # Capture a frame from camera
            ret, frame = cap.read()
            if not ret:
                break
            # Lật ngược chiều dọc
            flip_frame = cv2.flip(frame, 1)
            cv2.imshow('Nhấn Q để chụp ảnh', flip_frame)
            if cv2.waitKey(1) == ord('q'):
                # Save the captured frame to file
                path = "Images/Face_customer/" + emp_id + ".png"
                cv2.imwrite(path, frame)
                self.entry6.configure(state='normal')
                self.entry6.delete(0, "end")
                self.entry6.insert(0, path)
                self.entry6.configure(state='disabled')
                break
        # Release camera object
        cap.release()
        cv2.destroyAllWindows()


# màn hình update khách hàng
class Update_Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Employee")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_customer.png")
        self.label1.configure(image=self.img)

        self.clock = Label(e_update)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

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
        self.entry4.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry5 = Entry(e_update)
        self.entry5.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_update)
        self.entry6.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(state='disabled')
        self.entry6.configure(relief="flat")

        self.button3 = Button(e_update)
        self.button3.place(relx=0.800, rely=0.529, width=86, height=30)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 14")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""PHOTO""")
        self.button3.configure(command=self.takePhoto)

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
        self.button2.configure(text="""XÓA""")
        self.button2.configure(command=self.clearr)

        self.checkButton = Checkbutton(e_update)
        self.stateCheck = BooleanVar()
        self.checkButton.place(relx=0.132, rely=0.6, width=200, height=34)
        self.checkButton.configure(text="Khách hàng thân thiết")
        self.checkButton.configure(offvalue="FALSE")
        self.checkButton.configure(onvalue="TRUE")
        self.checkButton.configure(variable=self.stateCheck)

    def update(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()

        eloyal = self.stateCheck.get()
        if eloyal == True:
            eloyal = "TRUE"
        else:
            eloyal = "FALSE"

        if ename.strip():
            if valid_phone(econtact):
                if valid_cccd(eaddhar):
                    if edes:
                        if eadd:
                            if epass:
                                emp_id = vall[0]
                                update = (

                                    "UPDATE Customer SET name = ?, contact_num = ?, address = ?, cccd = ?, img = ?, discount = ?, isLoyal = ? WHERE ctm_id = ?"
                                )
                                cur.execute(update, [ename, econtact, eadd, eaddhar, epass, edes, eloyal, emp_id])


                                db.commit()
                                messagebox.showinfo("Success!!",
                                                    "Khách hàng ID: {} đã cập nhật thành công.".format(emp_id),
                                                    parent=e_update)
                                vall.clear()
                                page1.tree.delete(*page1.tree.get_children())
                                page1.DisplayData()
                                Customer.sel.clear()
                                e_update.destroy()
                            else:
                                messagebox.showerror("Oops!", "Chưa điền mật khẩu.", parent=e_update)
                        else:
                            messagebox.showerror("Oops!", "Chưa điền địa chỉ.", parent=e_update)
                    else:
                        messagebox.showerror("Oops!", "Chưa điền mức giảm giá.", parent=e_update)
                else:
                    messagebox.showerror("Oops!", "Số căn cước chưa đúng.", parent=e_update)
            else:
                messagebox.showerror("Oops!", "Số điện thoại chưa đúng.", parent=e_update)
        else:
            messagebox.showerror("Oops!", "Chưa điền tên nhân viên.", parent=e_update)

    def takePhoto(self):
        # Initialize camera object
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            # Capture a frame from camera
            ret, frame = cap.read()
            if not ret:
                break
            # Lật ngược chiều dọc
            flip_frame = cv2.flip(frame, 1)
            cv2.imshow('Nhấn Q để chụp ảnh', flip_frame)
            if cv2.waitKey(1) == ord('q'):
                # Save the captured frame to file
                path = "Images/Face_customer/" + vall[0] + ".png"
                cv2.imwrite(path, frame)
                self.entry6.configure(state='normal')
                self.entry6.delete(0, "end")
                self.entry6.insert(0, path)
                self.entry6.configure(state='disabled')
                break
        # Release camera object
        cap.release()
        cv2.destroyAllWindows()

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


def valid_phone(phn):
    if re.match(r"[0]\d{9}$", phn):
        return True
    return False


def valid_cccd(aad):
    if aad.isdigit() and len(aad) == 12:
        return True
    return False


def random_emp_id(stringLength):
    Digits = string.digits
    strr = ''.join(random.choice(Digits) for i in range(stringLength - 3))
    return ('CTM' + strr)


page1 = Customer(root)
root.mainloop()
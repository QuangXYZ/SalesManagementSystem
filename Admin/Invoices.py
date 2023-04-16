# ==================imports===================
import os
import re
import sqlite3
from time import strftime
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext as tkst

# ============================================
root = Tk()

# Tính toán kích thước và vị trí của cửa sổ giữa màn hình
width = 1366
height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.title("Invoices")

with sqlite3.connect("./Database/database.db") as db:
    cur = db.cursor()


def create_ctm():
    conn = sqlite3.connect('./Database/database.db')

    # Tạo bảng trong cơ sở dữ liệu
    conn.execute('''CREATE TABLE bill
                    (bill_no TEXT PRIMARY KEY NOT NULL,
                    date TEXT NOT NULL,
                    customer_name TEXT NULL,
                    customer_no TEXT NULL,
                    bill_details TEXT NULL          
                    );''')

    # Thêm dữ liệu vào bảng
    conn.execute(
        "INSERT INTO bill(bill_no, date, customer_name, customer_no, bill_details) VALUES('BB000001','1/1/2023','Quang','CTM001','Test bill')")
    conn.commit()
    conn.close()


def invoices():
    global invoice
    invoice = Toplevel()
    page7 = Invoice(invoice)
    # page7.time()
    invoice.protocol("WM_DELETE_WINDOW", exit)
    invoice.mainloop()   
    

class Invoice:
    def __init__(self,top) -> None:
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Invoices")
        
        # Add Hinh
        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/invoices.png")
        self.label1.configure(image=self.img)
        # =============================================
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
        # =================================================
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
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_inv)
        # ==================================================
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
        # =====================================
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
        self.button3.configure(text="""DELETE INVOICE""")
        self.button3.configure(command=self.delete_invoice)
        #===================================
        self.button4 = Button(root)
        self.button4.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""EXIT""")
        self.button4.configure(command=self.Exit)
        #=================================================
        self.scrollbarx = Scrollbar(root, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(root, orient=VERTICAL)
        
        # ================================================
        self.tree = ttk.Treeview(root)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=575)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.double_tap)
        
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Số Hóa Đơn",
                "Ngày",
                "Tên Khách Hàng",
                "SDT",
            )
        )
        self.tree.heading("Số Hóa Đơn", text="Số Hóa Đơn", anchor=W)
        self.tree.heading("Ngày", text="Ngày", anchor=W)
        self.tree.heading("Tên Khách Hàng", text="Tên Khách Hàng", anchor=W)
        self.tree.heading("SDT", text="SDT", anchor=W)
        

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=219    )
        self.tree.column("#2", stretch=NO, minwidth=0, width=219)
        self.tree.column("#3", stretch=NO, minwidth=0, width=219)
        self.tree.column("#4", stretch=NO, minwidth=0, width=219)
        

        self.DisplayData()    

    def DisplayData(self):
        cur.execute("SELECT * FROM bill")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))


    sel = []
    def on_tree_select(self, Event):
        
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)
    # Hiển thị chi tiết hóa đơn
    def double_tap(self, Event):
        item = self.tree.identify('item', Event.x, Event.y)
        global bill_num
        bill_num = self.tree.item(item)['values'][0]
        
        global bill
        bill = Toplevel()
        
        
        #mở bill  
        pg = open_bill(bill)
        #bill.protocol("WM_DELETE_WINDOW", exitt)
        bill.mainloop()
    
    def delete_invoice(self):
        val = []
        to_delete = []
        print('hi')
        if len(self.sel)!=0:
            sure = messagebox.askyesno("Xác Nhận", "Bạn có chắc chắn xóa hóa đơn ? ", parent=root)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%5==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    delete = "DELETE FROM bill WHERE bill_no = ?"
                    cur.execute(delete, [k])
                    db.commit()

                messagebox.showinfo("Thành Công!!", "Xóa Hóa Đơn Thành Công", parent=root)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())
                self.DisplayData()
                
        else:
            messagebox.showerror("Lỗi!","Vui Lòng Chọn 1 Hóa Đơn", parent=root)
  
    def search_inv(self):
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
                messagebox.showinfo("Thành Công!!", "Số Hoá Đơn: {} Tồn Tại.".format(self.entry1.get()), parent=root)
                break
        else: 
            messagebox.showerror("LỖI!!", "Số Hoá Đơn: {} Không Tồn Tại.".format(self.entry1.get()), parent=root)
    
    def Logout(self):
        sure = messagebox.askyesno("Đăng Xuất", "Bạn có muốn đăng xuất?")
        if sure == True:
            root.destroy()
            os.system("python ./Admin/Login.py")

    def Exit(self):
        sure = messagebox.askyesno("Thoát","Bạn có chắc chắn muốn thoát không?", parent=root)
        if sure == True:
            root.destroy()
class open_bill:
    def __init__(self, top=None):
        
        top.geometry("765x488")
        top.resizable(0, 0)
        top.title("Bill")

        self.label1 = Label(bill)
        self.label1.place(relx=0, rely=0, width=765, height=488)
        self.img = PhotoImage(file="./images/bill.png")
        self.label1.configure(image=self.img)
        
        self.name_message = Text(bill)
        self.name_message.place(relx=0.178, rely=0.205, width=176, height=30)
        self.name_message.configure(font="-family {Podkova} -size 10")
        self.name_message.configure(borderwidth=0)
        self.name_message.configure(background="#ffffff")

        self.num_message = Text(bill)
        self.num_message.place(relx=0.835, rely=0.215, width=90, height=30)
        self.num_message.configure(font="-family {Podkova} -size 10")
        self.num_message.configure(borderwidth=0)
        self.num_message.configure(background="#ffffff")

        self.bill_message = Text(bill)
        self.bill_message.place(relx=0.150, rely=0.243, width=176, height=26)
        self.bill_message.configure(font="-family {Podkova} -size 10")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(bill)
        self.bill_date_message.place(relx=0.780, rely=0.248, width=90, height=26)
        self.bill_date_message.configure(font="-family {Podkova} -size 10")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")


        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.044, rely=0.41, width=695, height=284)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        find_bill = "SELECT * FROM bill WHERE bill_no = ?"
        cur.execute(find_bill, [bill_num])
        results = cur.fetchall()
        if results:
            self.name_message.insert(END, results[0][2])
            self.name_message.configure(state="disabled")
    
            self.num_message.insert(END, results[0][3])
            self.num_message.configure(state="disabled")
    
            self.bill_message.insert(END, results[0][0])
            self.bill_message.configure(state="disabled")

            self.bill_date_message.insert(END, results[0][1])
            self.bill_date_message.configure(state="disabled")

            self.Scrolledtext1.configure(state="normal")
            self.Scrolledtext1.insert(END, results[0][4])
            self.Scrolledtext1.configure(state="disabled")           
page1 = Invoice(root)
root.mainloop()
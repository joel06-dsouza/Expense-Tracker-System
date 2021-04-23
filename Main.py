from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Expense Tracker System")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="yellow")

#VARIABLES
ITEMTYPE = StringVar()
ITEMNAME = StringVar()
DATEOFPURCHASE = StringVar()
ITEMPRICE = StringVar()


#METHODS

tkMessageBox.showwarning('','Mini-Project Python -> By Joel Dsouza(50), Swastik Sawant(28), Shruti Mahalpure(47)', icon="warning")

def Database():
    conn = sqlite3.connect("python.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, itemtype TEXT, itemname TEXT, dop TEXT, itemprice TEXT)")
    cursor.execute("SELECT * FROM `member` ORDER BY `itemname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  ITEMTYPE.get() == "" or ITEMNAME.get() == "" or DATEOFPURCHASE.get() == "" or ITEMPRICE.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("python.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `member` (itemtype ,itemname, dop, itemprice) VALUES(?, ?, ?, ?)", (str(ITEMTYPE.get()), str(ITEMNAME.get()), str(DATEOFPURCHASE.get()), str(ITEMPRICE.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `itemname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        ITEMTYPE.set("")
        ITEMNAME.set("")
        DATEOFPURCHASE.set("")
        ITEMPRICE.set("")

def UpdateData():
    if DATEOFPURCHASE.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("python.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `member` SET `itemtype` = ?, `itemname` = ?, `dop` =?, `itemprice` = ? WHERE `mem_id` = ?", (str(ITEMTYPE.get()), str(ITEMNAME.get()), str(DATEOFPURCHASE.get()), int(ITEMPRICE.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `itemname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        ITEMTYPE.set("")
        ITEMNAME.set("")
        DATEOFPURCHASE.set("")
        ITEMPRICE.set("")
        
    
def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    ITEMTYPE.set("")
    ITEMNAME.set("")
    DATEOFPURCHASE.set("")
    ITEMPRICE.set("")
    ITEMTYPE.set(selecteditem[1])
    ITEMNAME.set(selecteditem[2])
    DATEOFPURCHASE.set(selecteditem[3])
    ITEMPRICE.set(selecteditem[4])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Expense List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()


    #FRAMES
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
        

    #LABELS
    lbl_title = Label(FormTitle, text="Updating Expense", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_itemtype = Label(ContactForm, text="ITEMTYPE", font=('arial', 14), bd=5)
    lbl_itemtype.grid(row=0, sticky=W)
    lbl_itemname = Label(ContactForm, text="ITEMNAME", font=('arial', 14), bd=5)
    lbl_itemname.grid(row=1, sticky=W)
    lbl_dop = Label(ContactForm, text="PURCHASE DATE", font=('arial', 14), bd=5)
    lbl_dop.grid(row=2, sticky=W)
    lbl_itemprice = Label(ContactForm, text="ITEMPRICE", font=('arial', 14), bd=5)
    lbl_itemprice.grid(row=3, sticky=W)

    #ENTRY
    itemtype = Entry(ContactForm, textvariable=ITEMTYPE, font=('arial', 14))
    itemtype.grid(row=0, column=1)
    itemname = Entry(ContactForm, textvariable=ITEMNAME, font=('arial', 14))
    itemname.grid(row=1, column=1)
    dop = Entry(ContactForm, textvariable=DATEOFPURCHASE,  font=('arial', 14))
    dop.grid(row=3, column=1)
    itemprice = Entry(ContactForm, textvariable=ITEMPRICE,  font=('arial', 14))
    itemprice.grid(row=3, column=1)


    #BUTTONS
    btn_updatecon = Button(ContactForm, text="Update", width=50, command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)


#fn1353p    
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("python.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    
def AddNewWindow():
    global NewWindow
    ITEMTYPE.set("")
    ITEMNAME.set("")
    DATEOFPURCHASE.set("")
    ITEMPRICE.set("")
    NewWindow = Toplevel()
    NewWindow.title("Expense List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    #FRAMES
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    
    #LABELS
    lbl_title = Label(FormTitle, text="Adding New Expenses", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="Item Type", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Item Name", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Date Of Purchase", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Item-Price", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    

    #ENTRY
    itemtype = Entry(ContactForm, textvariable=ITEMTYPE, font=('arial', 14))
    itemtype.grid(row=0, column=1)
    itemname = Entry(ContactForm, textvariable=ITEMNAME, font=('arial', 14))
    itemname.grid(row=1, column=1)
    dop = Entry(ContactForm, textvariable=DATEOFPURCHASE, font=('arial', 14))
    dop.grid(row=2, column=1)
    itemprice = Entry(ContactForm, textvariable=ITEMPRICE,  font=('arial', 14))
    itemprice.grid(row=3, column=1)
    

    #BUTTONS
    btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)

    
#FRAMES
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="yellow")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="yellow")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)

#LABELS
lbl_title = Label(Top, text="Expense Tracker System", font=('arial', 16), width=500)
lbl_title.pack(fill=X)

#ENTRY

#BUTTONS
btn_add = Button(MidLeft, text="ADD NEW EXPENSE", bg="orange", command=AddNewWindow)
btn_add.pack()
btn_delete = Button(MidRight, text="DELETE AN EXPENSE", bg="orange", command=DeleteData)
btn_delete.pack(side=RIGHT)

#TABLES
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "ITEMTYPE", "ITEMNAME", "DATEOFPURCHASE", "ITEMPRICE"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('ITEMTYPE', text="ITEMTYPE", anchor=W)
tree.heading('ITEMNAME', text="ITEMNAME", anchor=W)
tree.heading('DATEOFPURCHASE', text="DATEOFPURCHASE", anchor=W)
tree.heading('ITEMPRICE', text="ITEMPRICE", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

#INITIALIZATION
if __name__ == '__main__':
    Database()
    root.mainloop()
    

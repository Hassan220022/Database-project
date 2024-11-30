import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

import pypyodbc as odbc # pip install pypyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-BRK7TP3\SQLEXPRESS'
DATABASE_NAME = 'libManagement'
connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust_Connection=yes;
"""
staff_qry="Select * From Staff"
author_qry="Select * From Author"
member_qry="Select * From _Member"
book_qry="Select * From Book"
borrow_qry="Select * From Borrow"
book_insert=""
db = odbc.connect(connection_string)
print(db)
cursor = db.cursor()

cursor.execute(staff_qry)
staff_list=cursor.fetchall()

cursor.execute(member_qry)
member_list=cursor.fetchall()

cursor.execute(book_qry)
book_list=cursor.fetchall()
cursor.execute(borrow_qry)
borrow_list =cursor.fetchall()
books=[]
for book in book_list:
    for borrow in borrow_list:
        if book[0]== borrow[3]:
            continue
        if book[1]in books: 
            continue
        books.append(book[1])

cursor.execute(author_qry)
author_list=cursor.fetchall()
authors=[]
for author in author_list:
    authors.append(author[1])


    

app = customtkinter.CTk()
app.geometry("200x200")
app.title("Library System")
app.resizable(0,0)


label = customtkinter.CTkLabel(app, text="Login", fg_color="transparent")
label.pack(pady=20)
txt_usr = customtkinter.CTkEntry(app, placeholder_text="Username")
txt_usr.pack(pady=5,anchor="center")

txt_pswrd = customtkinter.CTkEntry(app, placeholder_text="Password")
txt_pswrd.pack(pady=5,anchor="center")
def add_book():
    athr=combobox.get()

    for author in author_list:
        if author[1]==athr:
            athr_id=author[0]
            print(athr_id)
    isbn=txt_isbn.get()
    title=txt_book.get()
    book_insert=f"""
insert into Book values('{isbn}','{title}','{athr_id}','{curr_staff}')
"""
    print(book_insert)
    cursor.execute(book_insert)
    db.commit()

def borrow_book():
    bk=combobox2.get()

    for book in book_list:
        if book[1]==bk:
            isbn=book[0]
            print(isbn)
    borrow_id=txt_borrow_id.get()
    duedate=txt_duedate.get()
    book_insert=f"""
insert into Borrow values('{borrow_id}','{duedate}','{curr_member}','{isbn}')
"""
    print(book_insert)
    cursor.execute(book_insert)
    db.commit()

def member_window():
    global txt_borrow_id
    global txt_duedate
    global combobox2
    m_app=customtkinter.CTkToplevel()
    m_app.geometry("200x250")
    m_app.resizable(0,0)
    label = customtkinter.CTkLabel(m_app, text="Borrow Books", fg_color="transparent")
    label.pack(pady=20)
    txt_borrow_id = customtkinter.CTkEntry(m_app, placeholder_text="BorrowID")
    txt_borrow_id.pack(pady=5,anchor="center")
    txt_duedate = customtkinter.CTkEntry(m_app, placeholder_text="Date:YYYY-MM-DD")
    txt_duedate.pack(pady=5,anchor="center")
    combobox2 = customtkinter.CTkComboBox(m_app, values=books,command=combobox_callback)
    combobox2.set("Book Title")
    combobox2.pack(pady=5)
    add_btn = customtkinter.CTkButton(m_app, text="Borrow Book", command=borrow_book)
    add_btn.pack(pady=5,anchor="center")
    m_app.focus()



def staff_window():
    global txt_isbn
    global txt_book
    global combobox
    s_app=customtkinter.CTkToplevel()
    s_app.geometry("200x250")
    s_app.resizable(0,0)
    label = customtkinter.CTkLabel(s_app, text="Add Books", fg_color="transparent")
    label.pack(pady=20)
    txt_book = customtkinter.CTkEntry(s_app, placeholder_text="Title")
    txt_book.pack(pady=5,anchor="center")
    txt_isbn = customtkinter.CTkEntry(s_app, placeholder_text="ISBN")
    txt_isbn.pack(pady=5,anchor="center")
    combobox = customtkinter.CTkComboBox(s_app, values=authors,command=combobox_callback)
    combobox.set("Author")
    combobox.pack(pady=5)
    add_btn = customtkinter.CTkButton(s_app, text="Add Book", command=add_book)
    add_btn.pack(pady=5,anchor="center")
    s_app.focus()



def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)


def login():
    global x
    x = 0
    global curr_staff
    global curr_member
    for staff in staff_list:

        print(staff[0]+str(x))
        x=x+1
        print(txt_pswrd.get())
        if staff[0]==txt_pswrd.get():
            if staff[1]==txt_usr.get():
                curr_staff=txt_pswrd.get()
                app.withdraw()
                staff_window()
                break
    x=0
    for member in member_list:

        print(member[0]+str(x))
        x=x+1
        print(txt_pswrd.get())
        if member[0]==txt_pswrd.get():
            if member[1]==txt_usr.get():
                curr_member=txt_pswrd.get()
                app.withdraw()
                member_window()
                break

    print("button pressed")

login_btn = customtkinter.CTkButton(app, text="Login", command=login)
login_btn.pack(pady=5,anchor="center")

app.mainloop()
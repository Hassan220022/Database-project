import os
import tkinter
import tkinter.messagebox
import customtkinter
import mysql.connector
from mysql.connector import Error  # pip install mysql-connector-python
import logging
import tkinter as tk  # Modify import for clarity
from tkinter import ttk  # Import ttk for Treeview
import bcrypt  # Add bcrypt for password hashing
import configparser

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Set appearance and theme
customtkinter.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue", "green", "dark-blue"

# Initialize ConfigParser
config = configparser.ConfigParser()

# Read config.ini
config.read('config.ini')

try:
    HOST = config['mysql']['host']
    USER = config['mysql']['user']
    PASSWORD = config['mysql']['password']
    DATABASE = config['mysql']['database']
except KeyError as e:
    logging.error(f"Missing configuration for {e}")
    print(f"Error: Missing configuration for {e}")
    exit(1)


# # Database credentials
# HOST = '196.221.151.195'
# USER = 'root'
# PASSWORD = 'FtAL6ljzqY5IC'
# DATABASE = 'libManagement'

try:
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    if db.is_connected():
        print("Connected to MySQL database")
        cursor = db.cursor()
except Error as e:
    print(f"Error: {e}")
    exit(1)

# Remove references to Staff and Author tables

# Update query to use Users table
member_qry = "SELECT * FROM Users"
cursor.execute(member_qry)
member_list = cursor.fetchall()

# Initialize the main window
app = customtkinter.CTk()
app.geometry("800x600")  # Adjusted size for login interface
app.title("Library Management System")

# Shared input fields for Username, Email, and Password
label_username = customtkinter.CTkLabel(app, text="Username")
label_username = customtkinter.CTkLabel(app, text="Username")
label_username.pack(pady=(50, 5))

entry_username = customtkinter.CTkEntry(app, placeholder_text="Enter Username")
entry_username.pack(pady=5)

label_email = customtkinter.CTkLabel(app, text="Email")
label_email.pack(pady=10)

entry_email = customtkinter.CTkEntry(app, placeholder_text="Enter Email")
entry_email.pack(pady=5)

label_password = customtkinter.CTkLabel(app, text="Password")
label_password.pack(pady=10)

entry_password = customtkinter.CTkEntry(app, placeholder_text="Enter Password", show="*")
entry_password.pack(pady=5)

# Frame for Sign In and Sign Up buttons
button_frame = customtkinter.CTkFrame(app)
button_frame.pack(pady=20)

# Modify the sign-up action to interact with the database with password hashing
def signup_action():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    if not username or not email or not password:
        tkinter.messagebox.showerror("Error", "Please fill all fields.")
        return
    try:
        # Check if the username or email already exists
        check_qry = "SELECT * FROM Users WHERE username = %s OR email = %s"
        cursor.execute(check_qry, (username, email))
        if cursor.fetchone():
            tkinter.messagebox.showerror("Error", "Username or email already exists.")
            return
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # Insert the new user into the database
        insert_qry = "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)"
        cursor.execute(insert_qry, (username, hashed_password.decode('utf-8'), email))
        db.commit()
        tkinter.messagebox.showinfo("Success", "Signup successful!")
    except Error as e:
        logging.error(f"Signup failed for user {username}: {e}")
        tkinter.messagebox.showerror("Error", f"Failed to signup: {e}")

# Modify the sign-in action to validate against the database and handle admin login with hashed passwords
def sign_in_action():
    username = entry_username.get()
    password = entry_password.get()
    if not username or not password:
        tkinter.messagebox.showerror("Error", "Please enter both username and password.")
        return
    try:
        # Fetch the user record
        validate_qry = "SELECT password, role FROM Users WHERE username = %s"
        cursor.execute(validate_qry, (username,))
        user = cursor.fetchone()
        if user:
            stored_password, role = user
            # Verify the hashed password
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                if role == 'admin':
                    app.withdraw()
                    open_admin_page()
                else:
                    app.withdraw()
                    open_library()
                return
        tkinter.messagebox.showerror("Error", "Invalid username or password")
    except Error as e:
        logging.error(f"Sign-in failed for user {username}: {e}")
        tkinter.messagebox.showerror("Error", f"Failed to sign in: {e}")

# Sign In and Sign Up buttons
sign_in_button = customtkinter.CTkButton(button_frame, text="Sign In", command=sign_in_action)
sign_in_button.pack(side="left", padx=10)

signup_button = customtkinter.CTkButton(button_frame, text="Sign Up", command=signup_action)
signup_button.pack(side="left", padx=10)

# Define function to open the library view
def open_library():
    library_window = customtkinter.CTkToplevel(app)
    library_window.geometry("800x600")
    library_window.title("Library")

    # Frame for search bar
    search_frame = customtkinter.CTkFrame(library_window)
    search_frame.pack(pady=10, padx=10, fill="x")

    label_search = customtkinter.CTkLabel(search_frame, text="Search:")
    label_search.pack(side="left", padx=(0, 10))

    entry_search = customtkinter.CTkEntry(search_frame, placeholder_text="Enter Title or ISBN")
    entry_search.pack(side="left", fill="x", expand=True, padx=(0, 10))

    def search_books():
        query = entry_search.get().strip()
        if not query:
            refresh_treeview()
            return
        search_qry = """
        SELECT isbn, title, author
        FROM Books
        WHERE isbn LIKE %s OR title LIKE %s OR author LIKE %s
        """
        like_query = f"%{query}%"
        cursor.execute(search_qry, (like_query, like_query, like_query))
        filtered_books = cursor.fetchall()
        update_treeview(filtered_books)

    search_button = customtkinter.CTkButton(search_frame, text="Search", command=search_books)
    search_button.pack(side="left")

    # Add Exit button
    exit_button = customtkinter.CTkButton(library_window, text="Exit", command=lambda: exit_library(library_window))
    exit_button.pack(pady=10)

    def exit_library(window):
        window.destroy()
        app.deiconify()

    # Fetch books
    library_qry = "SELECT isbn, title, author FROM Books"
    cursor.execute(library_qry)
    books = cursor.fetchall()

    # Display books in a Treeview for better presentation
    tree = ttk.Treeview(library_window, columns=("ISBN", "Title", "Author"), show="headings")
    tree.heading("ISBN", text="ISBN")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")

    # Set column widths
    tree.column("ISBN", width=100)
    tree.column("Title", width=300)
    tree.column("Author", width=200)

    # Vertical scrollbar for the treeview
    scrollbar = ttk.Scrollbar(library_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Function to insert books into the treeview
    def refresh_treeview():
        for item in tree.get_children():
            tree.delete(item)
        cursor.execute(library_qry)
        all_books = cursor.fetchall()
        for book in all_books:
            tree.insert("", tk.END, values=book)

    def update_treeview(book_list):
        for item in tree.get_children():
            tree.delete(item)
        for book in book_list:
            tree.insert("", tk.END, values=book)

    tree.pack(fill="both", expand=True, padx=20, pady=10)

    refresh_treeview()

# Define function to open the admin page
def open_admin_page():
    admin_window = customtkinter.CTkToplevel(app)
    admin_window.geometry("800x600")
    admin_window.title("Admin Page")

    # Frame for adding new books
    add_frame = customtkinter.CTkFrame(admin_window)
    add_frame.pack(pady=10, padx=10, fill="x")

    label_add = customtkinter.CTkLabel(add_frame, text="Add New Book")
    label_add.pack(pady=5)

    entry_add_isbn = customtkinter.CTkEntry(add_frame, placeholder_text="ISBN")
    entry_add_isbn.pack(pady=5)

    entry_add_title = customtkinter.CTkEntry(add_frame, placeholder_text="Title")
    entry_add_title.pack(pady=5)

    entry_add_author = customtkinter.CTkEntry(add_frame, placeholder_text="Author Name")
    entry_add_author.pack(pady=5)

    add_book_button = customtkinter.CTkButton(
        add_frame, 
        text="Add Book", 
        command=lambda: admin_add_book(
            entry_add_isbn.get(), 
            entry_add_title.get(), 
            entry_add_author.get(),
            entry_add_isbn,
            entry_add_title,
            entry_add_author
        )
    )
    add_book_button.pack(pady=5)

    # Frame for editing existing books
    edit_frame = customtkinter.CTkFrame(admin_window)
    edit_frame.pack(pady=10, padx=10, fill="x")

    label_edit = customtkinter.CTkLabel(edit_frame, text="Edit Existing Book")
    label_edit.pack(pady=5)

    entry_edit_isbn = customtkinter.CTkEntry(edit_frame, placeholder_text="ISBN of Book to Edit")
    entry_edit_isbn.pack(pady=5)

    entry_edit_title = customtkinter.CTkEntry(edit_frame, placeholder_text="New Title")
    entry_edit_title.pack(pady=5)

    entry_edit_author = customtkinter.CTkEntry(edit_frame, placeholder_text="New Author Name")
    entry_edit_author.pack(pady=5)

    edit_book_button = customtkinter.CTkButton(
        edit_frame, 
        text="Edit Book", 
        command=lambda: admin_edit_book(
            entry_edit_isbn.get(), 
            entry_edit_title.get(), 
            entry_edit_author.get(),
            admin_tree
        )
    )
    edit_book_button.pack(pady=5)

    # Add Exit button
    exit_admin_button = customtkinter.CTkButton(admin_window, text="Exit", command=lambda: exit_admin(admin_window))
    exit_admin_button.pack(pady=10)

    def exit_admin(window):
        window.destroy()
        app.deiconify()

    # Display books in a Treeview for admin
    library_qry = "SELECT isbn, title, author FROM Books"
    cursor.execute(library_qry)
    books = cursor.fetchall()

    global admin_tree  # Declare tree as global
    admin_tree = ttk.Treeview(admin_window, columns=("ISBN", "Title", "Author"), show="headings")
    admin_tree.heading("ISBN", text="ISBN")
    admin_tree.heading("Title", text="Title")
    admin_tree.heading("Author", text="Author")

    # Set column widths
    admin_tree.column("ISBN", width=100)
    admin_tree.column("Title", width=300)
    admin_tree.column("Author", width=200)

    # Vertical scrollbar for the treeview
    scrollbar = ttk.Scrollbar(admin_window, orient="vertical", command=admin_tree.yview)
    admin_tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Function to insert books into the treeview
    def refresh_admin_treeview():
        for item in admin_tree.get_children():
            admin_tree.delete(item)
        cursor.execute(library_qry)
        all_books = cursor.fetchall()
        for book in all_books:
            admin_tree.insert("", tk.END, values=book)

    admin_tree.pack(fill="both", expand=True, padx=20, pady=10)

    refresh_admin_treeview()

# Define admin add book functionality
def admin_add_book(isbn, title, author_name, entry_isbn, entry_title, entry_author):
    if not isbn or not title or not author_name:
        tkinter.messagebox.showerror("Error", "Please fill all fields to add a book.")
        return
    try:
        # Check if the book ISBN already exists
        check_qry = "SELECT * FROM Books WHERE isbn = %s"
        cursor.execute(check_qry, (isbn,))
        if cursor.fetchone():
            tkinter.messagebox.showerror("Error", "A book with this ISBN already exists.")
            return
        # Insert the new book
        insert_book_qry = "INSERT INTO Books (isbn, title, author) VALUES (%s, %s, %s)"
        cursor.execute(insert_book_qry, (isbn, title, author_name))
        db.commit()
        tkinter.messagebox.showinfo("Success", "Book added successfully!")
        
        # Insert the new book into the Treeview
        admin_tree.insert("", tk.END, values=(isbn, title, author_name))
        
        # Clear the input fields
        entry_isbn.delete(0, tk.END)
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
    except Error as e:
        logging.error(f"Failed to add book: {e}")
        tkinter.messagebox.showerror("Error", f"Failed to add book: {e}")

# Define admin edit book functionality
def admin_edit_book(isbn, new_title, new_author_name, admin_tree):
    if not isbn:
        tkinter.messagebox.showerror("Error", "Please enter the ISBN of the book to edit.")
        return
    try:
        # Check if the book exists
        check_qry = "SELECT * FROM Books WHERE isbn = %s"
        cursor.execute(check_qry, (isbn,))
        book = cursor.fetchone()
        if not book:
            tkinter.messagebox.showerror("Error", "Book not found.")
            return
        updates = []
        params = []
        
        # Update title if provided
        if new_title:
            updates.append("title = %s")
            params.append(new_title)
        
        # Update author if provided
        if new_author_name:
            updates.append("author = %s")
            params.append(new_author_name)
        
        if not updates:
            tkinter.messagebox.showwarning("Warning", "No fields to update.")
            return
        
        update_book_qry = f"UPDATE Books SET {', '.join(updates)} WHERE isbn = %s"
        params.append(isbn)
        
        cursor.execute(update_book_qry, tuple(params))
        db.commit()
        tkinter.messagebox.showinfo("Success", "Book updated successfully!")
        
        # Refresh the admin_tree to reflect changes
        refresh_admin_treeview(admin_tree)
    except Error as e:
        logging.error(f"Failed to edit book: {e}")
        tkinter.messagebox.showerror("Error", f"Failed to edit book: {e}")

# Function to refresh the Treeview
def refresh_admin_treeview(admin_tree):
    for item in admin_tree.get_children():
        admin_tree.delete(item)
    cursor.execute("SELECT isbn, title, author FROM Books")
    all_books = cursor.fetchall()
    for book in all_books:
        admin_tree.insert("", tk.END, values=book)

# Start the main loop
app.mainloop()

# Close the database connection when the application is closed
if db.is_connected():
    cursor.close()
    db.close()
    print("MySQL connection is closed")

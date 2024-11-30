# Library Management System

A comprehensive Library Management System designed to streamline the process of managing books, users, and their interactions within a library. This application features a user-friendly graphical interface built with Python's Tkinter library and leverages a MySQL database to securely handle data storage and retrieval.

## Table of Contents
- [Project Description](#project-description)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [How to Run the Project](#how-to-run-the-project)
- [Usage](#usage)
  - [Sign Up](#sign-up)
  - [Sign In](#sign-in)
  - [Library Interface](#library-interface)
  - [Admin Panel](#admin-panel)
- [Troubleshooting](#troubleshooting)
- [Security Considerations](#security-considerations)
- [Future Work and Contributions](#future-work-and-contributions)

## Project Description

The **Library Management System** is a robust application that facilitates the efficient management of library operations. It enables users to sign up, sign in, search for books, and manage their borrowing activities through an intuitive graphical user interface. Administrators have additional privileges to add or edit book records, ensuring the library's catalog remains up-to-date.

### Key Features
- **User Authentication:** Secure signup and signin functionalities with hashed password storage.
- **Book Management:** Allows administrators to add and edit book details.
- **Search Functionality:** Users can search for books by title or ISBN.
- **Responsive GUI:** Built with Tkinter for a seamless user experience across platforms.

## Prerequisites

Before setting up the project, ensure that your system meets the following requirements:

### Software Requirements
- **Python 3.7 or higher:** [Download Python](https://www.python.org/downloads/)
- **MySQL Server 5.7 or higher:** [Download MySQL](https://dev.mysql.com/downloads/)
- **pip:** Python package installer (comes bundled with Python)

### Python Libraries
Install the required Python libraries using `pip`:

```bash
pip install mysql-connector-python bcrypt customtkinter
```

### Operating Systems Supported
- **Windows 10 or higher**
- **macOS Catalina or higher**
- **Linux (Ubuntu, Fedora, etc.)**

## Setup Instructions

Follow these steps to set up the Library Management System on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Hassan220022/library-management-system.git
cd library-management-system
```

### 2. Set Up the MySQL Database

#### a. Launch MySQL

Ensure that your MySQL server is running. You can start it using the following command based on your OS:

- **macOS:**
  ```bash
  brew services start mysql
  ```
- **Linux:**
  ```bash
  sudo service mysql start
  ```
- **Windows:**
  Start the MySQL service from the Services panel.

#### b. Execute the Database Setup Script

Run the provided SQL script to create the necessary database and tables with dummy data.

```bash
mysql -u root -p < setup_database.sql
```

- **Note:** Replace `root` with your MySQL username if different.
- **Password Prompt:** Enter your MySQL password when prompted.

### 3. Configure Database Credentials

Open the **gui_lb.py**
file and update the database credentials to match your MySQL configuration.

```python
# Database credentials
HOST = 'localhost'       # Replace with your MySQL host if different
USER = 'root'            # Replace with your MySQL username
PASSWORD = 'your_password'  # Replace with your MySQL password
DATABASE = 'libManagement'
```

### 4. Install Required Python Libraries

Ensure all necessary Python libraries are installed. If not already done, execute:

```bash
pip install mysql-connector-python bcrypt customtkinter
```

## How to Run the Project

Launch the application using the Python script provided.

```bash
python gui_lb.py
```

### Expected Behavior
- **Login Interface:** Upon running, a login window appears where users can sign in or sign up.
- **Library Interface:** After signing in, users can search for books and view available titles.
- **Admin Panel:** Administrators have access to additional functionalities like adding or editing books.

## Usage

### Sign Up

1. **Navigate to the Sign-Up Section:**
   - Click on the "Sign Up" button in the main window.
2. **Enter User Details:**
   - **Username:** Choose a unique username.
   - **Email:** Provide a valid email address.
   - **Password:** Create a secure password.
   - **Role:** Select your role (user or `admin`).

3. **Submit:**
   - Click the "Submit" button to create a new account.

### Sign In

1. **Enter Credentials:**
   - Provide your username and password.
2. **Authenticate:**
   - Click the "Sign In" button to access the system.
3. **Access Granted:**
   - Upon successful authentication, you will be redirected to the library interface.

### Library Interface

- **Search for Books:**
  - Use the search bar to find books by title or ISBN.
- **View Book Details:**
  - Select a book from the list to view more information.

### Admin Panel

1. **Access Admin Features:**
   - Only users with the `admin` role can access the admin panel.
2. **Add New Books:**
   - Enter the ISBN, title, and author details to add a new book.
3. **Edit Existing Books:**
   - Modify the title or author of an existing book by providing its ISBN.

## Troubleshooting

### Common Issues

#### 1. **Database Connection Error**

- **Error Message:** `"Error: 1045 (28000): Access denied for user 'root'@'localhost'"`
- **Solution:**
  - Verify that the MySQL credentials in gui_lb.py are correct.
  - Ensure that the MySQL server is running.
  - Check user privileges for the MySQL user.

#### 2. **Missing Python Libraries**

- **Symptom:** Import errors when running gui_lb.py.
- **Solution:**
  - Install the required libraries using:
    ```bash
    pip install mysql-connector-python bcrypt customtkinter
    ```

#### 3. **Password Hashing Issues**

  - **Symptom:** Errors related to password hashing or authentication fails despite correct credentials.
  - **Solution:**
  - Ensure that the bcrypt library is installed.
  - Verify that passwords are being hashed and verified correctly in gui_lb.py.

#### 4. **SQL Syntax Errors**

- **Symptom:** Errors when executing SQL scripts.
- **Solution:**
  - Ensure that setup_database.sql is executed without modifications.
  - Check for typos or unintended changes in the SQL script.

### Additional Help

If you encounter issues not listed here, please refer to the application's log file app.log for detailed error messages or open an issue in the [GitHub repository](https://github.com/Hassan220022/library-management-system/issues).

## Security Considerations

- **Password Security:**
  - Passwords are hashed using bcrypt before being stored in the database to ensure they are not stored in plain text.
- **Database Credentials:**
  - Avoid hardcoding sensitive information like database passwords. Consider using environment variables or configuration files to manage credentials securely.
- **Input Validation:**
  - Implement input validation to prevent SQL injection and other malicious inputs.

## Future Work and Contributions

### Future Enhancements

- **Role-Based Access Control (RBAC):**
  - Implement more granular permissions for different user roles.
- **Book Borrowing System:**
  - Allow users to borrow and return books, tracking due dates and availability.
- **Reporting Features:**
  - Generate reports on book inventory, user activity, and borrowing statistics.
- **User Interface Improvements:**
  - Enhance the GUI for better user experience and responsiveness.

### Contributing

Contributions are welcome! To contribute to the Library Management System, follow these steps:

1. **Fork the Repository:**
   - Click the "Fork" button at the top of the repository page.

2. **Clone the Forked Repository:**
   ```bash
   git clone https://github.com/Hassan220022/library-management-system.git
   cd library-management-system
   ```

3. **Create a New Branch:**
   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Your Changes:**
   - Implement your feature or fix bugs.

5. **Commit Your Changes:**
   ```bash
   git commit -m "Add feature: YourFeatureName"
   ```

6. **Push to the Branch:**
   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Open a Pull Request:**
   - Navigate to the original repository and create a pull request from your forked repository.

### Guidelines

- **Code Quality:** Ensure your code follows best practices and is well-documented.
- **Testing:** Include tests for new features or bug fixes.
- **Documentation:** Update the README and other documentation as needed.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Developed with ❤️  Your Mikawi*

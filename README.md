# Library Management System

This project consists of a simple GUI application and a SQL script for a library management system. The GUI application is built with Python using the `tkinter`, `customtkinter`, and `pypyodbc` libraries. The SQL script sets up the database for the system.

## Features

- Login system for staff and members
- Staff can add books to the library
- Members can borrow books from the library
- SQL script to set up the database

## Dependencies

- tkinter
- customtkinter
- pypyodbc

You can install the dependencies with pip:

```bash
pip install tkinter customtkinter pypyodbc
```

## Database Setup

The SQL script `database.sql` creates a database named `libManagement` and sets up the necessary tables. It also inserts some initial data into the tables.

To run the script, you need to have SQL Server installed and running. You can use the included Docker command to run a SQL Server container:

```bash
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Has238$$" -e "MSSQL_PID=Evaluation" -p 1433:1433  --name sqlpreview --hostname sqlpreview -d mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04 
```

After running the SQL Server container, you can execute the SQL script to set up the database.

## GUI Application

The Python script `gui_lb.py` is the GUI application for the library management system. It connects to the `libManagement` database and allows staff and members to interact with the system.

To run the application, simply execute the script with a Python interpreter:

```bash
python gui_lb.py
```

The GUI will appear, and you can interact with the library management system.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
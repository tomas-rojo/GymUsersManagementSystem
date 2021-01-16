import sqlite3
from tkinter import messagebox


# Connection to DDBB for creating new table if not exists
def create_table():
    try:
        # Connect to Database
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # SQL Command for creating table
        sql = """CREATE TABLE IF NOT EXISTS usuarios( 
                dni INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(30) NOT NULL,
                last VARCHAR(30) NOT NULL,
                email VARCHAR(50),
                number VARCHAR(20),
                pase VARCHAR(20))
                """

        # Inserting and Executing Query
        cursor.execute(sql)
        conn.commit()
        print("Tabla cargada con éxito")

        # Closing connection
        conn.close()
    except:
        messagebox.showwarning("Error al conectar con BBDD")


# Connection to DDBB to register new user
def add_user(name, last, dni, email, number, pase):

    # Connect to Database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Inserting and Executing Query
    try:
        query = '''INSERT INTO USUARIOS(name, last, dni, email, number, pase) VALUES (?, ?, ?, ?, ?, ?)'''
        cursor.execute(query, (name.title(), last.title(), dni, email, number, pase))
        conn.commit()
    except:
        a = True
        return a

    # Closing Connection
    conn.close()


# Connection to DDBB to modify user
def modify_user(name, last, dni, email, number, pase):

    # Connect to Database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Inserting and Executing Query
    query = '''UPDATE USUARIOS SET name = ?, last = ?, email = ?, number = ?, pase = ? WHERE dni = ?'''
    cursor.execute(query, (name.title(), last.title(), email, number, pase, dni))
    conn.commit()

    # Closing Connection
    conn.close()


# Connection to DDBB to find user by ID
def find_user_by_id(dni):

    # Connect to Database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Inserting and Executing Query
    query = '''SELECT * FROM USUARIOS WHERE dni=?'''
    cursor.execute(query, (dni,))
    rows = cursor.fetchall()
    conn.commit()
    info = []
    for element in rows:
        info.append(element[0])
        info.append(element[1])
        info.append(element[2])
        info.append(element[3])
        info.append(element[4])
        info.append(element[5])
        return info

    # Closing Connection
    conn.close()


# Connection to DDBB to start by ID
def start_by_id(dni_entry):

    # Connect to Database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Inserting and Executing Query
    query = '''SELECT * FROM USUARIOS WHERE dni=?'''
    cursor.execute(query, (dni_entry,))
    rows = cursor.fetchall()
    conn.commit()
    info = []
    for element in rows:
        info.append(element[1])
        info.append(element[2])
        return info

    # Closing Connection
    conn.close()


# Connection to DDBB to delete user
def delete_user(dni_entry):

    # Connect to Database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Inserting and Executing Query
    query = '''DELETE FROM USUARIOS WHERE dni=?'''
    cursor.execute(query, (dni_entry,))
    conn.commit()

    # Closing Connection
    conn.close()

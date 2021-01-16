# Description: UTN Gym Users Management System

# Importing Modules
from tkinter import *
from new_user import Usuario
from search_user import Search
from start_app import Start
import connection


# Creating Main Window
class Main:

    def __init__(self, root):
        self.root = root
        self.root.title("GESTION USUARIOS * GYM")
        self.root.geometry('600x350+300+100')
        self.main_title = Label(root,
                                text="SELECCIONE UNA OPCIÓN ",
                                bg="blue2",
                                fg="white",
                                font=("calibri", 15, "bold")
                                )
        self.main_title.pack()
        connection.create_table()

        # Loading Image for Main Window
        self.label1 = Label(root)
        self.img1 = PhotoImage(file="gym_logo.png")
        self.label1.configure(image=self.img1)
        self.label1.pack(side=LEFT, padx=15)

        # Software Copyright
        self.copyrights = Label(root, text="© All Rights Reserved 2020 - Tomas Rojo", bg="Grey",
                                font=("calibri", 8, "italic"))
        self.copyrights.pack(side=BOTTOM)

        # User Options
        self.button_add = Button(root, text="Agregar Usuario", font=("calibri", 14), height=2, width=20, borderwidth=3,
                                 command=self.add_user)
        self.button_search = Button(root, text="Buscar Usuario", font=("calibri", 14), height=2, width=20,
                                    borderwidth=3, command=self.search_user)
        self.button_start = Button(root, text="COMENZAR", bg="tomato", fg="white", font=("calibri", 16, "bold"),
                                   height=2, width=20, borderwidth=3, command=self.start_app)
        self.button_add.pack(expand=True)
        self.button_search.pack(expand=True)
        self.button_start.pack(expand=True)

    # Add User Window
    @staticmethod
    def add_user():
        add_user_window = Toplevel()
        Usuario(add_user_window)
        add_user_window.grab_set()
        add_user_window.focus_set()
        add_user_window.wait_window()

    # Search User Window
    @staticmethod
    def search_user():
        search_window = Toplevel()
        Search(search_window)
        search_window.grab_set()
        search_window.focus_set()
        search_window.wait_window()

    # Start Application
    @staticmethod
    def start_app():
        start_window = Toplevel()
        Start(start_window)
        start_window.grab_set()
        start_window.focus_set()
        start_window.wait_window()


if __name__ == '__main__':
    root = Tk()
    application = Main(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import connection
from update_user import Modificar


class Search:

    # Creating Search User Window
    def __init__(self, search_user_window):
        self.window = search_user_window
        self.window.title("GESTION USUARIOS * GYM")
        self.window.geometry('1237x330+50+100')

        # Creating Frame
        frame = LabelFrame(self.window, text=" Buscar Usuario ", font=("calibri", 18))
        frame.grid(row=0, column=0, rowspan=5, pady=15, padx=10)

        # Search Buttons by ID or Last Name
        info_dni = StringVar()
        Label(frame, text="Ingrese DNI: ", font=("calibri", 18)).grid(row=1, column=0, sticky=W, padx=200)
        self.dni_entry = Entry(frame, width=35, font=("calibri", 15), textvariable=info_dni)
        self.dni_entry.grid(row=1, column=0, pady=15)
        self.dni_entry.focus_set()

        # Submit Button
        self.start_btn = Button(frame, text="OK", width=10, bg='blue', fg='white', font=("calibri", 15),
                                command=lambda: self.start_app(self.dni_entry.get()))
        self.start_btn.grid(row=2, column=0, sticky=W, padx=340, pady=10)

        # Treeview Usuario
        self.tree = ttk.Treeview(frame, height=2, columns=("#1", "#2", "#3", "#4", "#5"))
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Apellido', anchor=CENTER)
        self.tree.heading('#2', text='DNI', anchor=CENTER)
        self.tree.heading('#3', text='Email', anchor=CENTER)
        self.tree.heading('#4', text='Num. Telefono', anchor=CENTER)
        self.tree.heading('#5', text='Tipo de Pase', anchor=CENTER)
        self.tree.grid(row=4, column=0, columnspan=2, pady=5, padx=5)

        # Delete Button
        self.delete_btn = Button(frame, text="Eliminar Usuario", width=20, bg='tomato', fg='white',
                                 font=("calibri", 15), command=self.delete_user)
        self.delete_btn.grid(row=5, column=0, sticky=W, padx=330, pady=10)

        # Modify Button
        self.modify_btn = Button(frame, text="Modificar Usuario", width=20, bg='blue', fg='white', font=("calibri", 15),
                                 command=self.modify_user)
        self.modify_btn.grid(row=5, column=0, sticky=E, padx=150, pady=10)

    # Cleans the form
    def clean(self):
        self.dni_entry.delete(0, END)
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
            return Search

    def start_app(self, dni_entry):
        validar_dni = re.search(r'[a-zA-Z]+', dni_entry)
        if validar_dni is not None:
            messagebox.showerror("DNI", "Ingrese DNI válido")
            return Search
        elif dni_entry == "":
            messagebox.showwarning("DNI", "Campo DNI vacío")
            return Search
        else:
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            info = connection.find_user_by_id(dni_entry)
            if info is None:
                messagebox.showerror("DNI", "DNI no encontrado")
                return Search
            else:
                self.tree.insert('', 0, text=info[1], values=(info[2], info[0], info[3], info[4], info[5]))
                return Search

    # Deleting user
    def delete_user(self):
        dni = self.dni_entry.get()
        if dni == "":
            messagebox.showwarning("DNI", "Campo DNI vacío")
            return Search
        info = connection.find_user_by_id(dni)
        if info is None:
            messagebox.showerror("DNI", "Ingrese DNI válido")
            return Search
        validar_dni = re.fullmatch(r'([0-9])', dni)
        if validar_dni is not None:
            messagebox.showerror("DNI", "Ingrese DNI válido")
            return Search
        ask_question = messagebox.askquestion("Advertencia", "Está seguro de eliminar usuario?")
        if ask_question == "yes":
            connection.delete_user(dni)
            messagebox.showinfo("Éxito", "Usuario eliminado con éxito!")
            self.clean()
        else:
            return Search

    # Modifying user
    def modify_user(self):
        dni = self.dni_entry.get()
        if dni == "":
            messagebox.showwarning("DNI", "Campo DNI vacío")
            return Search
        info = connection.find_user_by_id(dni)
        if info is None:
            messagebox.showerror("DNI", "Ingrese DNI válido")
            return Search
        validar_dni = re.fullmatch(r'([0-9])', dni)
        if validar_dni is not None:
            messagebox.showerror("DNI", "Ingrese DNI válido")
            return Search
        info = connection.find_user_by_id(dni)
        update_user_window = Toplevel()
        Modificar(update_user_window, info)
        self.window.destroy()
        update_user_window.grab_set()
        update_user_window.focus_set()
        update_user_window.wait_window()


if __name__ == '__main__':
    search_user_window = Tk()
    application = Search(search_user_window)
    search_user_window.mainloop()

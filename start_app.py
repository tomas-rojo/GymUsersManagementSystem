from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connection
import re
import datetime as dt


class Start:

    # Creating Start App Window
    def __init__(self, start_window):
        self.window = start_window
        self.window.title("GESTION USUARIOS * GYM")
        self.window.geometry('432x275+300+100')

        # Creating Frame
        frame = LabelFrame(start_window, text=" Ingrese DNI para comenzar ", font=("calibri", 18))
        frame.grid(row=0, column=0, columnspan=3, rowspan=6, pady=15, padx=10)

        # DNI Entry
        info_dni = StringVar()
        self.dni_entry = Entry(frame, width=35, font=("calibri", 15), textvariable=info_dni)
        self.dni_entry.grid(row=1, column=1, padx=10, pady=15)
        self.dni_entry.focus_set()

        # Submit Button
        self.start_btn = Button(frame, text="OK", width=10, bg='blue', fg='white', font=("calibri", 15),
                                command=self.start_app)
        self.start_btn.grid(row=2, column=1, sticky=W+E, padx=150, pady=10)

        # Treeview Usuario
        self.tree = ttk.Treeview(frame, height=3, columns=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Apellido', anchor=CENTER)
        self.tree.grid(row=4, column=0, columnspan=2, pady=5)

    # Cleans the form
    def clean(self, info):
        self.dni_entry.delete(0, END)
        messagebox.showinfo("Bienvenido", "Bienvenido" + " " + info[0] + " " + info[1] + " - Ingresó " +
                            str(dt.datetime.now().strftime("%H:%M %p")))

    def start_app(self):
        dni = self.dni_entry.get()
        validar_dni = re.search(r'[a-zA-Z]+', dni)
        if validar_dni is not None:
            messagebox.showerror("DNI", "Ingrese DNI válido")
            return Start
        elif dni == "":
            messagebox.showwarning("DNI", "Campo DNI vacío")
            return Start
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        info = connection.start_by_id(dni)
        if info is None:
            messagebox.showerror("DNI", "DNI no encontrado")
            return Start
        else:
            self.tree.insert('', 0, text=info[0], values=info[1])
        self.clean(info)


if __name__ == '__main__':
    start_window = Tk()
    application = Start(start_window)
    start_window.mainloop()

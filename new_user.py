from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connection
import re


class Usuario:

    # Creating New User Window
    def __init__(self, add_user_window):
        self.window = add_user_window
        self.window.title("GESTION USUARIOS * GYM")
        self.window.geometry('515x415+300+100')

        # Creating Frame
        frame = LabelFrame(self.window, text=" Registrar Nuevo Usuario ", font=("calibri", 18))
        frame.grid(row=0, column=0, columnspan=3, rowspan=3, pady=10, padx=10)

        # Input Nombre
        Label(frame, text="Nombre:", font=("calibri", 15)).grid(row=1, column=0, pady=10)
        self.name = Entry(frame, width=35, font=("calibri", 15))
        self.name.grid(row=1, column=1, padx=10)
        self.name.focus_set()

        # Input Apellido
        Label(frame, text="Apellido:", font=("calibri", 15)).grid(row=2, column=0, pady=10)
        self.last = Entry(frame, width=35, font=("calibri", 15))
        self.last.grid(row=2, column=1, padx=10)

        # Input DNI
        Label(frame, text="DNI:", font=("calibri", 15)).grid(row=3, column=0, pady=10)
        self.dni = Entry(frame, width=35, font=("calibri", 15))
        self.dni.grid(row=3, column=1, padx=10)

        # Input Email
        Label(frame, text="Email:", font=("calibri", 15)).grid(row=4, column=0, pady=10)
        self.email = Entry(frame, width=35, font=("calibri", 15))
        self.email.grid(row=4, column=1, padx=10)

        # Input Telefono Celular
        Label(frame, text="Celular:", font=("calibri", 15)).grid(row=5, column=0, pady=10)
        self.number = Entry(frame, width=35, font=("calibri", 15))
        self.number.grid(row=5, column=1, padx=10)

        # Input Tipo de Pase
        Label(frame, text="Tipo de Pase:", font=("calibri", 15)).grid(row=6, column=0, pady=10)
        self.pase = ttk.Combobox(frame, values=['Selecciona un pase...', 'Crossfit', 'Funcional', 'Musculación',
                                                'Pase Full'], font=("calibri", 15))
        self.pase.grid(row=6, column=1, sticky=W+E, padx=10)
        self.pase.current(0)

        # Submit Button
        submit_btn = Button(frame, text="GUARDAR USUARIO", bg='blue', fg='white', font=("calibri", 15),
                            command=lambda: self.submit_info(
                                self.name.get(),
                                self.last.get(),
                                self.dni.get(),
                                self.email.get(),
                                self.number.get(),
                                self.pase.get(),
                            ))
        submit_btn.grid(row=7, column=1, sticky=W, padx=47, pady=10)

    # Cleans the form
    def clean_screen(self):
        self.name.delete(0, END)
        self.last.delete(0, END)
        self.dni.delete(0, END)
        self.email.delete(0, END)
        self.number.delete(0, END)
        self.pase.delete(0, END)
        self.name.focus_set()
        messagebox.showinfo("Éxito", "Usuario cargado con éxito!")

    # Submit info & validate it through Regex
    def submit_info(self, name, last, dni, email, number, pase):
        if name == "":
            messagebox.showwarning("Nombre", "Campo Nombre Vacío.")
            return Usuario
        validar_name = re.fullmatch(r'[A-Za-z_ÑñÁáÉéÍíÓóÚú ]+', name)
        if validar_name is None:
            messagebox.showerror("Nombre", "Ingrese Nombre Válido.")
            return Usuario
        if last == "":
            messagebox.showwarning("Apellido", "Campo Apellido Vacío.")
            return Usuario
        validar_apellido = re.fullmatch(r'[A-Za-z_ÑñÁáÉéÍíÓóÚú ]+', last)
        if validar_apellido is None:
            messagebox.showerror("Apellido", "Ingrese Apellido Válido.")
            return Usuario
        if dni == "":
            messagebox.showwarning("DNI", "Campo DNI Vacío.")
            return Usuario
        validar_dni = re.fullmatch(r'(\d{8,10})', dni)
        if validar_dni is None:
            messagebox.showerror("DNI", "Ingrese DNI válido. Sólo Números - Entre 8 y 10 Números.")
            return Usuario
        if email == "":
            messagebox.showwarning("Email", "Campo Email Vacío")
            return Usuario
        validar_email = re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email)
        if validar_email is None:
            messagebox.showerror("Email", "Ingrese Mail válido")
            return Usuario
        if number == "":
            messagebox.showwarning("Número", "Campo Número Vacío.")
            return Usuario
        validar_number = re.fullmatch(r'(\d{8,10})', number)
        if validar_number is None:
            messagebox.showerror("Número Celular", "Ingrese DNI válido. Sólo Números - Entre 8 y 10 Números.")
            return Usuario
        if pase == "Selecciona un pase...":
            messagebox.showwarning("Pase", "Campo Pase Vacío.")
            return Usuario
        check_user = connection.add_user(name, last, dni, email, number, pase)
        if check_user is True:
            messagebox.showerror("DNI", "El DNI ya Existe - Ingrese DNI Válido.")
            return Usuario
        else:
            self.clean_screen()


if __name__ == '__main__':
    add_user_window = Tk()
    application = Usuario(add_user_window)
    add_user_window.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connection
import re


class Modificar:

    # Creating Modify User Window
    def __init__(self, update_user_window, info):
        self.window = update_user_window
        self.window.title("GESTION USUARIOS * GYM")
        self.window.geometry('515x415+300+100')
        name_info = StringVar()
        last_info = StringVar()
        dni_info = StringVar()
        email_info = StringVar()
        number_info = StringVar()

        # Creating Frame
        frame = LabelFrame(self.window, text=" Modificar Usuario ", font=("calibri", 18))
        frame.grid(row=0, column=0, columnspan=3, rowspan=3, pady=10, padx=10)

        # Input Nombre
        Label(frame, text="Nombre:", font=("calibri", 15)).grid(row=1, column=0, pady=10)
        self.name = Entry(frame, textvariable=name_info, width=35, font=("calibri", 15))
        self.name.grid(row=1, column=1, padx=10)
        self.name.focus_set()
        name_info.set(info[1])

        # Input Apellido
        Label(frame, text="Apellido:", font=("calibri", 15)).grid(row=2, column=0, pady=10)
        self.last = Entry(frame, textvariable=last_info, width=35, font=("calibri", 15))
        self.last.grid(row=2, column=1, padx=10)
        last_info.set(info[2])

        # Input DNI
        Label(frame, text="DNI:", font=("calibri", 15)).grid(row=3, column=0, pady=10)
        self.dni = Entry(frame, state=DISABLED, textvariable=dni_info, width=35, font=("calibri", 15))
        self.dni.grid(row=3, column=1, padx=10)
        dni_info.set(info[0])

        # Input Email
        Label(frame, text="Email:", font=("calibri", 15)).grid(row=4, column=0, pady=10)
        self.email = Entry(frame, textvariable=email_info, width=35, font=("calibri", 15))
        self.email.grid(row=4, column=1, padx=10)
        email_info.set(info[3])

        # Input Telefono Celular
        Label(frame, text="Celular:", font=("calibri", 15)).grid(row=5, column=0, pady=10)
        self.number = Entry(frame, textvariable=number_info, width=35, font=("calibri", 15))
        self.number.grid(row=5, column=1, padx=10)
        number_info.set(info[4])

        # Input Tipo de Pase
        Label(frame, text="Tipo de Pase:", font=("calibri", 15)).grid(row=6, column=0, pady=10)
        self.pase = ttk.Combobox(frame, values=['Selecciona un pase...', 'Crossfit', 'Funcional', 'Musculación',
                                                'Pase Full'], font=("calibri", 15))
        self.pase.grid(row=6, column=1, sticky=W + E, padx=10)
        self.pase.current(0)

        # Submit Button
        submit_btn = Button(frame, text="Modificar Usuario", bg='blue', fg='white', font=("calibri", 15),
                            command=lambda: self.submit_info(
                                self.name.get(),
                                self.last.get(),
                                self.dni.get(),
                                self.email.get(),
                                self.number.get(),
                                self.pase.get(),
                            ))
        submit_btn.grid(row=7, column=1, sticky=W, padx=47, pady=10)

    # Submit info & validate it through Regex
    def submit_info(self, name, last, dni, email, number, pase):
        if name == "":
            messagebox.showwarning("Nombre", "Campo Nombre Vacío.")
            return Modificar
        validar_name = re.fullmatch(r'[A-Za-z_ÑñÁáÉéÍíÓóÚú ]+', name)
        if validar_name is None:
            messagebox.showerror("Nombre", "Ingrese Nombre Válido.")
            return Modificar
        if last == "":
            messagebox.showwarning("Apellido", "Campo Apellido Vacío.")
            return Modificar
        validar_apellido = re.fullmatch(r'[A-Za-z_ÑñÁáÉéÍíÓóÚú ]+', last)
        if validar_apellido is None:
            messagebox.showerror("Apellido", "Ingrese Apellido Válido.")
            return Modificar
        if email == "":
            messagebox.showwarning("Email", "Campo Email Vacío.")
            return Modificar
        validar_email = re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email)
        if validar_email is None:
            messagebox.showerror("Email", "Ingrese Mail válido.")
            return Modificar
        if number == "":
            messagebox.showwarning("Número", "Campo Número Vacío.")
            return Modificar
        validar_number = re.fullmatch(r'(\d{8,10})', number)
        if validar_number is None:
            messagebox.showerror("Número Celular", "Ingrese Celular Válido. Sólo Números - Entre 8 y 10 Números.")
            return Modificar
        if pase == "Selecciona un pase...":
            messagebox.showwarning("Pase", "Campo Pase Vacío.")
            return Modificar
        connection.modify_user(name, last, dni, email, number, pase)
        messagebox.showinfo("Éxito", "Usuario modificado con éxito!")
        self.window.destroy()


if __name__ == '__main__':
    update_user_window = Tk()
    application = Modificar(update_user_window)
    update_user_window.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        # Window
        self.geometry('300x130')
        self.title('Login')
        self.resizable(0,0)

        # Configuracion del Grid
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=2)
        self.rowconfigure(2,weight=4)

        self._crear_componentes()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        # usuario
        etiqueta_usuario = tk.Label(text='Usuario:')
        etiqueta_usuario.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.valor_usuario = tk.StringVar()
        input_usuario = ttk.Entry(self, width=20, textvariable=self.valor_usuario)
        input_usuario.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # password
        etiqueta_password = tk.Label(text='Password:')
        etiqueta_password.grid(row=1,column=0,sticky=tk.E, padx=5, pady= 5)
        self.valor_password = tk.StringVar()
        input_password = ttk.Entry(self, width=20, textvariable=self.valor_password, show='*')
        input_password.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # boton Login
        boton_login = ttk.Button(self, text='Login', command=self._iniciar_sesion)
        boton_login.grid(row=2, column=0, columnspan=2)


    # Handlers
    def _iniciar_sesion(self):
        messagebox.showinfo('Datos Login', f'Usuario: {self.valor_usuario.get()}, Password: {self.valor_password.get()}')

# Ejecutar la ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()

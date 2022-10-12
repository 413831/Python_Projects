import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
# ventana.iconbitmap('icono.ico')

# Eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    # boton2.config(text='Botón 2 presionado')
    pass

def evento3():
    # boton3.config(text='Botón 3 presionado')
    pass

def evento4():
    style = Style()
    style.configure('W.TButton', font=
    ('calibri', 10, 'bold', 'underline'),
                    foreground='red', relief='RAISED', background='yellow')
    #boton4.config(text='Boton 4 presionado', style = 'W.TButton')

# nota: los botones del paquete tk y ttk requieren diferentes configuraciones
# Definimos los botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE',padx=40, pady=30 ,ipady=20, ipadx=50, columnspan= 2, rowspan=2)

# N(arriba), E(derecha), S(abajo), W(izquierda)
#boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
#boton2.grid(row=1, column=0, sticky='NSWE')

# boton3 = ttk.Button(ventana, text='Boton 3', command=evento3)
# boton3.grid(row=0, column=1, sticky='NSWE')

#boton4 = ttk.Button(ventana, text='Boton 4', command=evento4)
#boton4.grid(row=1, column=1, sticky='NSWE')

# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

ventana.mainloop()

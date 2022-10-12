import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')

# show -> configura el caracter a mostrar por cada caracter
# state -> configura el estado del input
# width -> es la cantidad de caracteres que ocupa la caja de texto
# justify -> alinceación horizontal del texto

# Entry - Input
# Definimos una variable que podremos modificar posteriormente (set), leer (get)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana,width=30)
entrada1.grid(row=0,column=0)
# insert agrega un texto por defecto
# entrada1.insert(0, 'Introduce una cadena')
# entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')


# Label - Etiqueta
etiqueta1 = tk.Label(ventana, text='Aqui se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

# Handler del botón
def enviar():
    # Recuperamos la información a partir de la variable asociada con la caja de texto
    boton1.config(text=entrada1.get())

    # Modificación utilizamos la variable de texto y el método set
    entrada_var1.set('Ingrese un texto')

    # Modificamos el texto de label
    etiqueta1.config(text=entrada_var1.get())

    # Messagebox (cajas mensajes)
    mensaje1 = entrada1.get()
    messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')
    # messagebox.showerror('Mensaje Error', mensaje1 + ' Error')
    # messagebox.showwarning('Mensaje Alerta', mensaje1 + ' Alerta')

    # print(entrada1.get())
    # boton1.config(text=entrada1.get())
    # Eliminar el contenido
    # entrada1.delete(0, tk.END)
    # Seleccionar el texto de la caja
    # entrada1.select_range(0, tk.END)
    # Para hacer efectiva la selección del texto
    # entrada1.focus()

def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos...')
    sys.exit()


def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    # tearoff = False para evitar que se separe el menú de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=False)
    # Agregamos una nueva opción al menú de archivos
    submenu_archivo.add_command(label='Nuevo')
    # Agregar un separador
    submenu_archivo.add_separator()
    # Agregamos la opción de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    # Agregamos el submenu al menú principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    # Submenú ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=False)
    submenu_ayuda.add_command(label='Acerca de...')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    # Mostramos el menú en la ventana principal
    ventana.config(menu=menu_principal)

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0,column=1)
# Creamos el menu
crear_menu()

ventana.mainloop()
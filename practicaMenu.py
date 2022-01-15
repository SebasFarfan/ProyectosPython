from tkinter import *
from tkinter import messagebox

root=Tk()

def informacionAdicional():
    messagebox.showinfo('Procesador de Sebastián', 'Procesador de texto 2021')

def avisoLicencia():
    messagebox.showwarning('Licencia', 'Producto bajo licencia GPL')

def salirAplicacion():
    # valor=messagebox.askquestion('Salir', '¿Desea salir de la aplicación?')
    valor=messagebox.askokcancel('Salir', '¿Desea salir de la aplicación?')
    # if valor=='yes':
    #     root.destroy()
    if valor:
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel('Reintentar', 'No es posible cerrar documento bloqueado')
    if not valor:
        
        root.destroy()

menuBar=Menu(root)
root.config(menu=menuBar, width=300, height=300)

archivoMenu=Menu(menuBar, tearoff=0)
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar Como')
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar', command=cerrarDocumento)
archivoMenu.add_command(label='Salir', command=salirAplicacion)

edicionMenu=Menu(menuBar, tearoff=0)
edicionMenu.add_command(label='Copiar')
edicionMenu.add_command(label='Cortar')
edicionMenu.add_command(label='Pegar')
herramientaMenu=Menu(menuBar)
ayudaMenu=Menu(menuBar, tearoff=0)
ayudaMenu.add_command(label='Licencia', command=avisoLicencia)
ayudaMenu.add_command(label='Acerca de', command=informacionAdicional)

menuBar.add_cascade(label='Archivo', menu=archivoMenu)
menuBar.add_cascade(label='Edición', menu=edicionMenu)
menuBar.add_cascade(label='Herramientas', menu=herramientaMenu)
menuBar.add_cascade(label='Ayuda', menu=ayudaMenu)

root.mainloop()
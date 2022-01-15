from tkinter import *
from tkinter import filedialog

root=Tk()

def abrirFichero():
    fichero=filedialog.askopenfilename(title='Abrir', initialdir='C:', filetypes=(('Fichero de Excel', '*.xlsx'), ('Todos los archivos', '*.*')))
    print(fichero)

Button(root, text='Abrir Fichero', command=abrirFichero).pack()

root.mainloop()
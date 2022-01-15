from tkinter import *

raiz=Tk()
raiz.title('Ventana de Prueba')
# raiz.resizable(0,0) #(ancho, alto) para definir si se puede redimensionar la ventana
# raiz.iconbitmap('ruta del icono')
# raiz.geometry('540x400') #para darle una dimension a la ventana
raiz.config(bg='red') #cambiar de color el fondo de la ventana
# creo un frame
miFrame = Frame()
# situar el frame a la izquierda y arriba
# miFrame.pack(side='left', anchor='n')
# expandir el frame en forma vertical
# miFrame.pack(fill='y', expand=True)
# expanda para cualquier dimension el frame
miFrame.pack(fill='both', expand=True)

miFrame.config(bg='orange')
miFrame.config(width='650', height='400')
# caracteristicas de borde
miFrame.config(bd=35) # grosor de borde
miFrame.config(relief='groove') #tipo de borde
# miFrame.config(cursor='hand2') #la flecha del cursor cambia al pasar por el frame
miFrame.config(cursor='pirate')
raiz.mainloop()

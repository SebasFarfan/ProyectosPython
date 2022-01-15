from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()

# si uso una imagen tipo png o gif
# miImagen=PhotoImage(file='imagen.png') # siempre que la imagen esté en el mismo directorio del archivo 
# Label(miFrame, image=miImagen).place(x=10,y=20)

miLabel=Label(miFrame, text='Hola Python', fg='orange', font=(18))

miLabel.place(x=10, y=20)

root.mainloop()

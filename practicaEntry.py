from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miNombre=StringVar()


nombreTexto=Entry(miFrame, textvariable=miNombre) # este cuadro de texto esta asociado con la variable miNombre
nombreTexto.grid(row=0, column=1, padx=10, pady=10)
nombreTexto.config(fg='orange', justify='center')

passTexto=Entry(miFrame)
passTexto.grid(row=1, column=1, padx=10, pady=10)
passTexto.config(show='*')


apellidoTexto=Entry(miFrame)
apellidoTexto.grid(row=2, column=1, padx=10, pady=10)

direccionTexto=Entry(miFrame)
direccionTexto.grid(row=3, column=1, padx=10, pady=10)

comentarioTexto=Text(miFrame, width=23, height=5)
comentarioTexto.grid(row=4, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=comentarioTexto.yview)
scrollVert.grid(row=4, column=2, sticky='nsew')

comentarioTexto.config(yscrollcommand=scrollVert.set)

nombreLabel=Label(miFrame, text='Nombre:') 
nombreLabel.grid(row=0, column=0, sticky='e', padx=10,pady=10) # la letra "e" significa ESTE 

passLabel=Label(miFrame, text='Password')
passLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

apellidoLabel=Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=2, column=0, sticky='e', padx=10,pady=10)

direccionLabel=Label(miFrame, text='Dirección:')
direccionLabel.grid(row=3, column=0, sticky='e', padx=10,pady=10)

comentarioLabel=Label(miFrame, text='Comentario:')
comentarioLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

def codigoBoton():
    miNombre.set('Sebastián')

botonEnvio=Button(root, text='Enviar', command=codigoBoton)
botonEnvio.pack()

root.mainloop()



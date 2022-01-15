from tkinter import *


root=Tk()
root.title('Ejemplo')
playa=IntVar()
montania=IntVar()
turismoRural=IntVar()

foto=PhotoImage(file='avion.png')
Label(root, image=foto).pack()

def opcionViaje():
    opcionEscogida=''
    if playa.get()==1:
        opcionEscogida+=' Playa'
    if montania.get()==1:
        opcionEscogida+=' Montaña'
    if turismoRural.get()==1:
        opcionEscogida+=' TurismoRural'
    textoFinal.config(text=opcionEscogida)

frame=Frame(root)
frame.pack()
Label(frame, text='Elige destino')

Checkbutton(frame, text='Playa', variable=playa, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text='Montaña', variable=montania, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text='Turismo Rural', variable=turismoRural, onvalue=1, offvalue=0, command=opcionViaje).pack()
textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()
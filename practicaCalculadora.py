from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

operacion=''
resultado=0

# -------- pantalla---------------
numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg='black', fg='#41F3A2', justify='right')

# -------------- tecla pulsada-------------------
def numeroPulsado(num):
    global operacion
    if operacion !='':
        numeroPantalla.set(num)
        operacion=''
    else:
        numeroPantalla.set(numeroPantalla.get()+num)
    

# --------------- operación suma---------------------
def sumar(num):
    global operacion
    global resultado

    resultado+=int(num)
    operacion = 'suma'

    numeroPantalla.set(resultado)

#----------------- funcion el_resultado------------------
def elResultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado=0


#------------fila 1 ------------------------------
button7=Button(miFrame, text='7', width=3, command=lambda:numeroPulsado('7'))
button7.grid(row=2, column=1)
button8=Button(miFrame, text='8', width=3, command=lambda:numeroPulsado('8'))
button8.grid(row=2, column=2)
button9=Button(miFrame, text='9', width=3, command=lambda:numeroPulsado('9'))
button9.grid(row=2, column=3)
buttonDiv=Button(miFrame, text='/', width=3)
buttonDiv.grid(row=2, column=4)

#------------fila 2 ------------------------------
button4=Button(miFrame, text='4', width=3, command=lambda:numeroPulsado('4'))
button4.grid(row=3, column=1)
button5=Button(miFrame, text='5', width=3, command=lambda:numeroPulsado('5'))
button5.grid(row=3, column=2)
button6=Button(miFrame, text='6', width=3, command=lambda:numeroPulsado('6'))
button6.grid(row=3, column=3)
buttonMult=Button(miFrame, text='x', width=3)
buttonMult.grid(row=3, column=4)

#------------fila 3 ------------------------------
button1=Button(miFrame, text='1', width=3, command=lambda:numeroPulsado('1'))
button1.grid(row=4, column=1)
button2=Button(miFrame, text='2', width=3, command=lambda:numeroPulsado('2'))
button2.grid(row=4, column=2)
button3=Button(miFrame, text='3', width=3, command=lambda:numeroPulsado('3'))
button3.grid(row=4, column=3)
buttonRestar=Button(miFrame, text='-', width=3)
buttonRestar.grid(row=4, column=4)

#------------fila 4 ------------------------------
button0=Button(miFrame, text='0', width=3, command=lambda:numeroPulsado('0'))
button0.grid(row=5, column=1)
buttonPunto=Button(miFrame, text='.', width=3, command=lambda:numeroPulsado('.'))
buttonPunto.grid(row=5, column=2)
buttonIgual=Button(miFrame, text='=', width=3, command=lambda:elResultado())
buttonIgual.grid(row=5, column=3)
buttonSuma=Button(miFrame, text='+', width=3, command=lambda:sumar(numeroPantalla.get()))
buttonSuma.grid(row=5, column=4)


raiz.mainloop()
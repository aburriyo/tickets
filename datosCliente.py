import tkinter 
import os
from turtle import color

roots = tkinter.Tk()
roots.title('Registro Ticket')
roots.geometry('600x800')

titulo = tkinter.Label(roots, text='Registro de usuario', font=('Arial', 20)).place(x=170, y=0)
nombre = tkinter.Label(roots, text='Nombre:', font=('Arial', 15)).place(x=50, y=100)
nombreEntrada = tkinter.Entry(roots, width=50).place(x=200, y=100,width=300, height=25)
apellido = tkinter.Label(roots, text='Apellidos:', font=('Arial', 15)).place(x=50, y=150)
apellidoEntrada = tkinter.Entry(roots, width=50).place(x=200, y=150, width=300, height=25)
correo = tkinter.Label(roots, text='Correo:', font=('Arial', 15)).place(x=50, y=200)
correoEntrada = tkinter.Entry(roots, width=50).place(x=200, y=200 ,width=300, height=25)

ticket = tkinter.Label(roots, text='Ticket:', font=('Arial', 15)).place(x=50, y=300)
ticketEntrada = tkinter.Text(roots, width=50).place(x=200, y=300, width=350, height=300)

registrar = tkinter.Button(roots, text='Registrar', command=lambda: registrar()).place(x=100, y=700, width=100, height=50)
salir = tkinter.Button(roots, text='Salir', command=lambda: salir(),bg='red',fg='white').place(x=400, y=700, width=100, height=50)

menu = tkinter.Menu(roots)
menu_file = tkinter.Menu(menu, tearoff=0)
menu_file.add_command(label='Salir', 
                      accelerator='Ctrl+Q',
                      state='normal',)
menu_file.add_cascade(label='Ayuda')


roots.mainloop()
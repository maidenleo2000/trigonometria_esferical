import math as m
import tkinter as tk
from cgitb import text
from tkinter import ttk
from tkinter import messagebox

# Este es  el módulo que permite calcular cuanto debería esconderse el horizonte
# bajo la curvatura de la Tierra si esta fuera una bola
"""
L = input('Introduce la distancia (en Kms): ')
response = 6373-(6373*(m.cos(m.asin(float(L)/6373))))
response *= 1000
print (f'El horizonte se esconde  {str(response)} metros en una esfera')
"""


def apretarboton():
    dato=ingdatos.get()

    if dato == "":
        
        messagebox.showinfo(title="¡Advertencia!", message="No se ingresaron datos")
        label = ttk.Label(text="                                     ")        
        label.place(x=10, y=35)
        
    else:
        
        L = dato
        response = 6373-(6373*(m.cos(m.asin(float(L)/6373))))
        response *= 1000
        resultado = float("{0:.2f}".format(response))
        
        label = ttk.Label(text=f"El horizonte se esconde  {str(resultado)} metros en una esfera           ")
        label.place(x=25, y=100)
        
    

ventana = tk.Tk()
ventana.title("Calcular caída de curvatura")
ventana.config(width=350, height=230)

label = ttk.Label(text="Ingresa la distancia en KM")
label.place(x=100, y=7)

ingdatos = ttk.Entry()
ingdatos.place(x=109, y=30)
ingdatos.config(width=20, )

boton = ttk.Button(text="Calcular", command=apretarboton)
boton.place(x=109, y=60)

ventana.mainloop()
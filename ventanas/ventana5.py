import tkinter as tk
from tkinter import messagebox

#creación de las operaciones
def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado=num1+num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos")

#creación de la ventana 
ventana= tk.Tk() 
ventana.title("Calculadora de Suma") #nombre de la ventana
ventana.geometry("300x200") #tamaño de la ventana

#etiquetas y entradas
tk.Label(ventana, text="Primer número: ").pack(pady=5) #etiqueta
entrada1= tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Segundo número: ").pack(pady=5)
entrada2= tk.Entry(ventana)
entrada2.pack()

#boton para sumar
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=10)

#etiqueta para mostrar resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()

#ejecutar 
ventana.mainloop()
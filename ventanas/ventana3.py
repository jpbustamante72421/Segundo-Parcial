import tkinter as tk

#creamos la ventana principal
def saludo():
    label_resultado.config(text="Hola Alumnos de Python")

ventana = tk.Tk()
ventana.title("Ejemplo con Botones")
ventana.geometry("400x300")

#creamos el boton
boton=tk.Button(ventana, text="Saludar", command=saludo)
boton.pack(pady=20)

#creamos una etiqueta
label_resultado = tk.Label(ventana, text="Hola Mundo", font=("Arial",16,"bold"))
label_resultado.pack(pady=20)

#iniciamos la etiqueta en la ventana
ventana.mainloop()
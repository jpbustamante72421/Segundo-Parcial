import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
#diccionarios
colores = {
    "Negro": 0,
    "Café": 1,
    "Rojo": 2,
    "Naranja": 3,
    "Amarillo": 4,
    "Verde": 5,
    "Azul": 6,
    "Morado": 7,
    "Gris": 8,
    "Blanco": 9,
}

multiplica = {
    "Negro": 1,
    "Café": 10,
    "Rojo": 100,
    "Naranja": 1000,
    "Amarillo": 10000,
    "Verde": 100000,
    "Azul": 1000000,
    "Morado": 10000000,
    "Gris": 100000000,
    "Blanco": 1000000000,
}

def operaciones():

    color1 = banda1.get()
    color2 = banda2.get()
    color_m = banda_multiplicador.get()

    numero1 = colores[color1]
    numero2 = colores[color2]
    multiplicador = multiplica[color_m]

    valor_base = int(str(numero1) + str(numero2))
    valor_resistencia = valor_base * multiplicador

    if var_tolerancia.get() == 1:
        tolerancia = 0.05
    else:
        tolerancia = 0.10

    maximo = valor_resistencia + (valor_resistencia * tolerancia)
    minimo = valor_resistencia - (valor_resistencia * tolerancia)

    label_resultado.config(text="Valor: " + str(valor_resistencia))
    label_maximo.config(text="Máximo: " + str(maximo))
    label_minimo.config(text="Mínimo: " + str(minimo))


# ventana
ventana = tk.Tk()
ventana.title("Calculadora de Resistencias")
ventana.geometry("500x1000")
ventana.config(bg="#1E9433")

titulo = tk.Label(ventana, text="Calculadora de Resistencias", font=("Arial", 18, "bold"))
titulo.pack(pady=10)
titulo.config(bg="Blue")
#imagen
frame_imagen = tk.Frame(ventana)
frame_imagen.pack()
frame_imagen.config(bg="green")
imagen = Image.open("Resistencia.jpg")
imagen = imagen.resize((450,300))
fondo = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(frame_imagen, image=fondo)
label_imagen.pack()

# debajo de imagen
frame_principal = tk.Frame(ventana)
frame_principal.pack(pady=20)

# bandas
frame_izquierda = tk.Frame(frame_principal)
frame_izquierda.grid(row=0, column=0, padx=30)

tk.Label(frame_izquierda, text="Banda 1").pack()
banda1 = ttk.Combobox(frame_izquierda, values=list(colores.keys()))
banda1.pack()

tk.Label(frame_izquierda, text="Banda 2").pack()
banda2 = ttk.Combobox(frame_izquierda, values=list(colores.keys()))
banda2.pack()

tk.Label(frame_izquierda, text="Multiplicador").pack()
banda_multiplicador = ttk.Combobox(frame_izquierda, values=list(multiplica.keys()))
banda_multiplicador.pack()
# tolerancia y resultados
frame_derecha = tk.Frame(frame_principal)
frame_derecha.grid(row=0, column=1, padx=30)

tk.Label(frame_izquierda, text="Tolerancia").pack()

var_tolerancia = tk.IntVar()
tk.Radiobutton(frame_izquierda, text="Dorado = 5%", variable=var_tolerancia, value=1).pack()
tk.Radiobutton(frame_izquierda, text="Plata = 10%", variable=var_tolerancia, value=2).pack()
tk.Button(frame_derecha, text="Calcular", command=operaciones).pack(pady=10)

label_resultado = tk.Label(frame_derecha, text="Valor:")
label_resultado.pack()

label_maximo = tk.Label(frame_derecha, text="Máximo:")
label_maximo.pack()

label_minimo = tk.Label(frame_derecha, text="Mínimo:")
label_minimo.pack()

ventana.mainloop()
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def cinepolis():
    try:
        nombre = entry_nombre.get()
        personas = int(entry_personas.get())
        cantidad_boletos = int(entry_boleto.get())
        cineco = variable_cinec.get()

        precio = 12
        venta_max = personas * 7

        if nombre == "":
            messagebox.showerror("Error", "Ingresa el nombre de la persona.")
            return

        if personas <= 0:
            messagebox.showerror("Error", "Debe haber al menos una persona.")
            return

        if cantidad_boletos <= 0:
            messagebox.showerror("Error", "Debe comprar al menos un boleto.")
            return

        if cantidad_boletos > venta_max:
            messagebox.showerror("Error", f"Máximo permitido: {venta_max} boletos.")
            return

        total = cantidad_boletos * precio

        # Descuento por cantidad de boletos
        if cantidad_boletos > 5:
            descuento = total * 0.15
        elif cantidad_boletos >= 3:
            descuento = total * 0.10
        else:
            descuento = 0

        subtotal = total - descuento

        # Descuento CINECO
        if cineco == 1:
            descuento_cineco = subtotal * 0.10
        else:
            descuento_cineco = 0

        total_pagar = subtotal - descuento_cineco

        resultado = f"""
        Nombre: {nombre}
        Boletos comprados: {cantidad_boletos}
        Máximo permitido: {venta_max}
        Total sin descuento: ${total:.2f} 
        Total a pagar: ${total_pagar:.2f}
        """
        messagebox.showinfo("Resultado de Compra", resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")

def salir():
    if messagebox.askyesno("Salir", "¿Deseas cerrar el programa?"):
        ventana.destroy()

#creacion ventana
ventana = tk.Tk()
ventana.title("Cinépolis")
ventana.geometry("1000x600")
ventana.resizable(False, False)

# imagen fond
imagen = Image.open("CINEpol.png")
imagen = imagen.resize((1000, 600))
fondo = ImageTk.PhotoImage(imagen)

label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# izquierdo
frame_izquierda = tk.Frame(ventana, bg="#22478D", bd=0)
frame_izquierda.place(x=50, y=180, width=400, height=300)

tk.Label(frame_izquierda, text="Nombre de la persona:", bg="#22478D", fg="white").place(x=20, y=40)
entry_nombre = tk.Entry(frame_izquierda)
entry_nombre.place(x=200, y=40, width=160)

tk.Label(frame_izquierda, text="Número de personas:", bg="#22478D", fg="white").place(x=20, y=90)
entry_personas = tk.Entry(frame_izquierda)
entry_personas.place(x=200, y=90, width=160)

tk.Label(frame_izquierda, text="Cantidad de boletos:", bg="#22478D", fg="white").place(x=20, y=140)
entry_boleto = tk.Entry(frame_izquierda)
entry_boleto.place(x=200, y=140, width=160)

variable_cinec = tk.IntVar()
tk.Checkbutton(frame_izquierda,text="Descuento tarjeta CINECO",variable=variable_cinec,bg="#22478D",fg="white",selectcolor="#22478D").place(x=90, y=180)

#DERECHO
frame_derecha = tk.Frame(ventana, bg="#22478D", bd=5)
frame_derecha.place(x=600, y=220, width=250, height=150)

tk.Button(frame_derecha, text="Calcular Pago", command=cinepolis, width=15).place(x=45, y=30)
tk.Button(frame_derecha, text="Salir", command=salir, width=15).place(x=45, y=80)

ventana.mainloop()
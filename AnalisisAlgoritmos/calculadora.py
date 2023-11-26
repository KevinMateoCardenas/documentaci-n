import tkinter as tk
from tkinter import ttk

class Calculadora:

    def __init__(self, root):
        self.expresion = ""
        self.root = root
        self.interface()

    def agregar(self, valor):
        self.expresion += str(valor)
        self.actualizar_pantalla()

    def limpiar(self):
        self.expresion = ""
        self.actualizar_pantalla()

    def calcular(self):
        try:
            self.expresion = str(eval(self.expresion))
            self.actualizar_pantalla()
        except Exception as e:
            self.expresion = "Error"
            self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.var_pantalla.set(self.expresion)

    def interface(self):
        self.root.title("Calculadora")
        self.root.geometry("320x400")

        self.var_pantalla = tk.StringVar()

        # Pantalla de la calculadora
        pantalla = ttk.Entry(self.root, textvar=self.var_pantalla, font=('Arial', 20))
        pantalla.grid(row=0, column=0, columnspan=4, ipady=10, padx=10, pady=10, sticky="ew")

        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (texto, fila, columna) in botones:
            ttk.Button(self.root, text=texto, width=5, command=lambda v=texto: self.agregar(v) if v not in ['=', 'C'] else self.calcular() if v == '=' else self.limpiar()).grid(row=fila, column=columna, ipadx=10, ipady=10, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()
# Importação da biblioteca de Interface
import tkinter as tk

# Funções Matemáticas da Calculadora
def somar():
    resultado.set(float(numero1.get()) + float(numero2.get()))
def subtrair():
    resultado.set(float(numero1.get()) - float(numero2.get()))
def multiplicar():
    resultado.set(float(numero1.get()) * float(numero2.get()))
def dividir():
    resultado.set(float(numero1.get()) / float(numero2.get()))
    
janela = tk.Tk()
janela.title("Calculadora simples do Allisson")

frame1 = tk.Frame(janela)
frame1.pack(pady=5)

frame2 = tk.Frame(janela)
frame2.pack(pady=5)

resultado = tk.StringVar()

tk.Label(frame1, text="Primeiro número:").grid(row=0, column=0)
numero1 = tk.Entry(frame1)
numero1.grid(row=0, column=1)
tk.Label(frame1, text="Segundo número:").grid(row=1, column=0)
numero2 = tk.Entry(frame1)
numero2.grid(row=1, column=1)

tk.Button(frame2, text="Somar", width=15, height=10, command=somar).grid(row=0, column=0, pady=5, padx=5)
tk.Button(frame2, text="Subtrair", width=15, height=10, command=subtrair).grid(row=0, column=1, pady=5, padx=5)
tk.Button(frame2, text="Multiplicar", width=15, height=10, command=multiplicar).grid(row=1, column=0, pady=5, padx=5)
tk.Button(frame2, text="Dividir", width=15, height=10, command=dividir).grid(row=1, column=1, pady=5, padx=5)

frame3 = tk.Frame(janela)
frame3.pack(pady=5)
tk.Label(frame3, text="Resultado: ", font=("Arial", 12, "bold")).grid(row=0, column=0)
tk.Label(frame3, textvariable=resultado, font=("Arial", 18)).grid(row=0, column=1)

janela.mainloop()
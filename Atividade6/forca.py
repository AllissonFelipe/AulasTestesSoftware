import random
import tkinter as tk
import time
 
PALAVRAS = ["python", "computador", "programação", "teclado", "inteligência", "dados", "ciência", "Turma 146 é Top"]
 
class Forca:
    def __init__(self):
        self.palavra = random.choice(PALAVRAS)
        self.tentativas = 6
        self.letras_corretas = set()
    
    def jogo_acabou(self):
        return self.tentativas == 0 or "_" not in self.mostrar_palavra()
 
    def ganhou(self):
        return "_" not in self.mostrar_palavra()
    def tentar_letra(self, letra):
        if letra in self.palavra:
            self.letras_corretas.add(letra)
        else:
            self.tentativas -= 1
 
    def mostrar_palavra(self):
        return " ".join(letra if letra in self.letras_corretas else "_" for letra in self.palavra)
         
def iniciar_jogo():
    jogo = Forca()
 
    def atualizar_tela():
        lbl_palavra.config(text=jogo.mostrar_palavra())
        lbl_tentativas.config(text=f"Tentativas restantes: {jogo.tentativas}")
        if jogo.jogo_acabou():
            if jogo.ganhou():
                lbl_status.config(text="Você Ganhou! Reiniciando jogo...")
                lbl_status.update_idletasks()
                time.sleep(3)
                jogo.__init__()
                atualizar_tela()
            else:
                lbl_status.config(text=f"Game Over! A palavra era: {jogo.palavra}. Reiniciando jogo...")
                lbl_status.update_idletasks()
                time.sleep(3)
                lbl_status.config(text=f"")
                jogo.__init__()
                atualizar_tela()
                
    def fazer_tentativa():
        letra = entrada_letra.get()
        if letra and letra not in jogo.letras_corretas:
            jogo.tentar_letra(letra)
            entrada_letra.delete(0, tk.END)
            atualizar_tela()
    
    janela = tk.Tk()
    janela.title("Jogo da Forca")
    janela.geometry("400x300")
    tk.Button(janela, text="Tentar", command=fazer_tentativa).pack()
    
    lbl_tentativas = tk.Label(janela, text=f"Tentativas restantes: {jogo.tentativas}")
    lbl_tentativas.pack()

    lbl_palavra = tk.Label(janela, text=jogo.mostrar_palavra(), font=("Arial", 20))
    lbl_palavra.pack()

    entrada_letra = tk.Entry(janela)
    entrada_letra.pack()

    lbl_status = tk.Label(janela, text="")
    lbl_status.pack()

    janela.mainloop()
iniciar_jogo()
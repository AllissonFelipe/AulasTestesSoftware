import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.resizable(False, False)
        self.board = [""] * 16
        self.current_player = "X"
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(16):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//4, column=i%4)
            self.buttons.append(button)
        self.reset_button = tk.Button(self.root, text="Reiniciar", font=("Arial", 14), command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=4, sticky="nsew")

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner() and not self.check_velha():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
            elif self.check_velha():
                messagebox.showinfo("Fim de Jogo", "Deu Velha")
            elif "" not in self.board:
                messagebox.showinfo("Fim de Jogo", "Empate!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    def check_velha(self):
        for row in self.board:
            for element in row:
                print(element)
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],  # Linhas
            [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],  # Colunas
            [0, 5, 10, 15], [3, 6, 9, 12]              # Diagonais
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == self.board[combo[3]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 16
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = JogoDaVelha(root)
    root.mainloop()
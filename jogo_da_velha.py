import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        self.janela.configure(bg="#1E1E1E")
        self.janela.geometry("400x500")
        
        self.jogador_atual = "X"
        self.placar = {"X": 0, "O": 0}
        
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.criar_interface()
        
        self.janela.mainloop()
    
    def criar_interface(self):
        self.frame_tabuleiro = tk.Frame(self.janela, bg="#1E1E1E")
        self.frame_tabuleiro.pack(pady=20)
        
        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.frame_tabuleiro, text="", font=("Arial", 20, "bold"), width=5, height=2,
                                              bg="#2D89EF", fg="#FFFFFF", relief="flat", bd=5,
                                              activebackground="#1B5D9B", activeforeground="#FFFFFF",
                                              highlightbackground="#000000", highlightthickness=3,
                                              command=lambda i=i, j=j: self.fazer_jogada(i, j))
                self.botoes[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        self.label_placar = tk.Label(self.janela, text=f"Placar - X: {self.placar['X']} | O: {self.placar['O']}", 
                                     font=("Arial", 14, "bold"), bg="#1E1E1E", fg="#FFFFFF")
        self.label_placar.pack()
        
        self.botao_reset = tk.Button(self.janela, text="Resetar Placar", font=("Arial", 12, "bold"), bg="#2D89EF", fg="#FFFFFF",
                                     relief="flat", activebackground="#1B5D9B", activeforeground="#FFFFFF",
                                     highlightbackground="#000000", highlightthickness=3, bd=5,
                                     command=self.resetar_placar)
        self.botao_reset.pack(pady=10)
    
    def fazer_jogada(self, i, j):
        if self.botoes[i][j]["text"] == "":
            self.botoes[i][j]["text"] = self.jogador_atual
            if self.verificar_vitoria():
                self.placar[self.jogador_atual] += 1
                messagebox.showinfo("Fim de Jogo", f"{self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
            self.atualizar_placar()
    
    def verificar_vitoria(self):
        for i in range(3):
            if self.botoes[i][0]["text"] == self.botoes[i][1]["text"] == self.botoes[i][2]["text"] != "":
                return True
            if self.botoes[0][i]["text"] == self.botoes[1][i]["text"] == self.botoes[2][i]["text"] != "":
                return True
        if self.botoes[0][0]["text"] == self.botoes[1][1]["text"] == self.botoes[2][2]["text"] != "":
            return True
        if self.botoes[0][2]["text"] == self.botoes[1][1]["text"] == self.botoes[2][0]["text"] != "":
            return True
        return False
    
    def verificar_empate(self):
        for i in range(3):
            for j in range(3):
                if self.botoes[i][j]["text"] == "":
                    return False
        return True
    
    def reiniciar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j]["text"] = ""
        self.jogador_atual = "X"
    
    def atualizar_placar(self):
        self.label_placar.config(text=f"Placar - X: {self.placar['X']} | O: {self.placar['O']}")
    
    def resetar_placar(self):
        self.placar = {"X": 0, "O": 0}
        self.atualizar_placar()

if __name__ == "__main__":
    JogoDaVelha()
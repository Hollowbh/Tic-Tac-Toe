import tkinter as tk
from tkinter import messagebox
from .engine import TicTacToeEngine

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Pro")
        self.engine = TicTacToeEngine()
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=('Arial', 24), width=5, height=2,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def on_click(self, i):
        player = self.engine.current_player
        result = self.engine.make_move(i)
        
        if result != "INVALID":
            self.buttons[i].config(text=player)
            
            if result == "WIN":
                messagebox.showinfo("Game Over", f"Player {player} wins!")
                self.reset_ui()
            elif result == "TIE":
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_ui()

    def reset_ui(self):
        self.engine = TicTacToeEngine()
        for btn in self.buttons:
            btn.config(text="")

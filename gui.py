import tkinter as tk
from tkinter import messagebox
from .engine import TicTacToeEngine

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg='#0d1117')
        
        
        self.root.attributes('-alpha', 0.98)
        
        self.score_x = 0
        self.score_o = 0
        
        window_width = 340
        window_height = 540
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}+{int(screen_width/2 - 170)}+{int(screen_height/2 - 270)}')
        self.root.resizable(False, False)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        for i in range(3): self.root.grid_columnconfigure(i, weight=1)

        self.engine = TicTacToeEngine()
        self.buttons = []

        
        self.score_label = tk.Label(
            self.root,
            text=f"{self.score_x} — {self.score_o}",
            font=('Segoe UI', 36, 'bold'),
            bg='#0d1117',
            fg='#58a6ff'
        )
        self.score_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))

        
        grid_frame = tk.Frame(self.root, bg='#30363d', padx=1, pady=1)
        grid_frame.grid(row=1, column=0, columnspan=3, rowspan=3)

        for i in range(9):
            btn = tk.Button(
                grid_frame,
                text="",
                font=('Arial', 32, 'bold'),
                width=3,
                height=1,
                bg='#161b22',
                fg='#c9d1d9',
                activebackground='#21262d',
                activeforeground='#f0f6fc',
                borderwidth=0,
                cursor="hand2",
                command=lambda i=i: self.on_click(i)
            )
            btn.grid(row=i//3, column=i%3, padx=1, pady=1)
            
            
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#21262d'))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg='#161b22'))
            
            self.buttons.append(btn)

        self.restart_btn = tk.Button(
            self.root,
            text="RESTART",
            font=('Segoe UI', 12, 'bold'),
            bg='#238636',
            fg='#ffffff',
            activebackground='#2ea043',
            borderwidth=0,
            padx=40,
            pady=12,
            cursor="hand2",
            command=self.reset_game
        )
        self.restart_btn.grid(row=4, column=0, columnspan=3, pady=(30, 40))

    def update_score_display(self):
        self.score_label.config(text=f"{self.score_x} — {self.score_o}")

    def on_click(self, i):
        player = self.engine.current_player
        result = self.engine.make_move(i)
        
        if result != "INVALID":
            color = '#58a6ff' if player == "X" else '#ff79c6'
            self.buttons[i].config(text=player, fg=color)
            
            if result == "WIN":
                if player == "X": self.score_x += 1
                else: self.score_o += 1
                self.update_score_display()
                messagebox.showinfo("Match End", f"Player {player} Topped >:3 !")
                self.reset_game()
            elif result == "TIE":
                messagebox.showinfo("Game Over :(", "Stalemate... no one wins >:3c")
                self.reset_game()

    def reset_game(self):
        self.engine = TicTacToeEngine()
        for btn in self.buttons:
            btn.config(text="", bg='#161b22')

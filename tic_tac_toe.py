import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe vs AI")
        self.window.geometry("400x450")
        self.window.configure(bg="#f0f0f0")

        self.current_player = "X"
        self.board = [None] * 9

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(
            self.window, text="Tic Tac Toe", font=("Lucida Bright", 18, "bold"), bg="#f0f0f0"
        )
        self.title_label.pack(pady=10)

        # Board frame
        self.board_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.board_frame.pack()

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.board_frame,
                text="",
                font=("Helvetica", 20, "bold"),
                width=5,
                height=2,
                bg="#ffffff",
                command=lambda i=i: self.make_move(i),
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        # Control buttons
        self.control_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.control_frame.pack(pady=10)

        self.start_button = tk.Button(
            self.control_frame,
            text="Mulai Game",
            font=("Helvetica", 12, "bold"),
            bg="#4caf50",
            fg="white",
            command=self.start_game,
        )
        self.start_button.pack(side="left", padx=10)

        self.refresh_button = tk.Button(
            self.control_frame,
            text="Refresh Game",
            font=("Helvetica", 12, "bold"),
            bg="#2196f3",
            fg="white",
            command=self.refresh_game,
        )
        self.refresh_button.pack(side="left", padx=10)

    def start_game(self):
        self.refresh_game()
        self.title_label.config(text="Giliran: Pemain X")

    def refresh_game(self):
        self.current_player = "X"
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="", state="normal", bg="#ffffff")
        self.title_label.config(text="Tic Tac Toe")

    def make_move(self, index):
        if not self.board[index]:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state="disabled")

            if self.check_winner():
                self.end_game(f"Pemain {self.current_player} menang!")
            elif None not in self.board:
                self.end_game("Permainan seri!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.title_label.config(text="Giliran: AI berpikir...")
                    self.window.after(500, self.ai_move)
                else:
                    self.title_label.config(text=f"Giliran: Pemain {self.current_player}")

    def ai_move(self):
        index = self.get_ai_move()
        self.make_move(index)

    def get_ai_move(self):
        # Prioritaskan langkah yang menang
        for i in range(9):
            if not self.board[i]:
                self.board[i] = "O"
                if self.check_winner():
                    self.board[i] = None
                    return i
                self.board[i] = None

        # Blokir langkah lawan yang menang
        for i in range(9):
            if not self.board[i]:
                self.board[i] = "X"
                if self.check_winner():
                    self.board[i] = None
                    return i
                self.board[i] = None

        # Pilih langkah terbaik berikutnya
        available_moves = [i for i, x in enumerate(self.board) if x is None]
        return random.choice(available_moves)

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for combo in winning_combinations:
            if (
                self.board[combo[0]]
                == self.board[combo[1]]
                == self.board[combo[2]]
                == self.current_player
            ):
                for i in combo:
                    self.buttons[i].config(bg="#ffcc00")
                return True
        return False

    def end_game(self, message):
        self.title_label.config(text=message)
        for button in self.buttons:
            button.config(state="disabled")
        messagebox.showinfo("Permainan Selesai", message)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()

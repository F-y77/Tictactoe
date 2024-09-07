import tkinter as tk
from tkinter import messagebox
 
class TicTacToe:
    # 井字棋游戏类
    def __init__(self, root):
        # 初始化游戏界面和状态
        self.root = root
        self.root.title("井字棋游戏")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_board()
 
    def create_board(self):
        # 创建棋盘界面
        for i in range(9):
            button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
 
    def on_button_click(self, index):
        # 处理按钮点击事件
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("游戏结束", f"玩家 {self.current_player} 获胜！")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("游戏结束", "平局！")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
 
    def check_winner(self):
        # 检查是否有玩家获胜
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                return True
        return False
 
    def is_board_full(self):
        # 检查棋盘是否已满
        return all(cell != "" for cell in self.board)
 
    def reset_board(self):
        # 重置棋盘状态
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"
 
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

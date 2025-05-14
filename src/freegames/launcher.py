import tkinter as tk
import subprocess
import os

# 需要包含的 Python 脚本列表
scripts = [
    "ant.py", "avoid.py", "bagels.py", "bounce.py", "cannon.py", "connect.py", "crypto.py",
    "fidget.py", "flappy.py", "guess.py", "illusion.py", "life.py", "madlibs.py", "maze.py",
    "memory.py", "minesweeper.py", "pacman.py", "paint.py", "pong.py", "rps.py", "simonsays.py",
    "snake.py", "tetris.py", "tictactoe.py", "tiles.py", "tron.py", "typing.py", "utils.py"
]

# 初始化主窗口
root = tk.Tk()
root.title("Python 程序启动器")

# 设置窗口大小和背景色
root.geometry("900x600")  # 设置窗口大小
root.config(bg="#f0f0f0")  # 设置背景颜色

# 设置窗口图标（可选）
# root.iconbitmap('icon.ico')  # 如果有图标文件，可以取消注释并设置图标

# 启动 Python 脚本的函数
def run_script(script_name):
    subprocess.Popen(["python", script_name], cwd=os.getcwd())

# 创建一个滚动框架
canvas = tk.Canvas(root, bg="#f0f0f0")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas, bg="#f0f0f0")

# 添加滚动条
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# 设置每行按钮的数量
buttons_per_row = 4  # 每行最多3个按钮

# 将按钮添加到框架中
for i, script in enumerate(scripts):
    row = i // buttons_per_row  # 计算按钮所在的行
    col = i % buttons_per_row  # 计算按钮所在的列

    button = tk.Button(frame, text=script, width=20, height=2, font=("Arial", 12), fg="#fff", bg="#007BFF",
                       relief="flat", command=lambda s=script: run_script(s))
    button.grid(row=row, column=col, padx=10, pady=10)

# 将框架添加到画布中
canvas.create_window((0, 0), window=frame, anchor="nw")

# 更新框架大小以适应内容
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# 启动 Tkinter 事件循环
root.mainloop()

import os
import tkinter as tk
import random
import sys
import pkgutil
import runpy
import tkinter as tk
from tkinter import messagebox

# 确保能 import 到 src 下的 freegames 包
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

import freegames  # type: ignore

def get_games():
    """
    Discover available game modules in the freegames package,
    but skip the special __main__.py.
    """
    games = []
    for _, module_name, is_pkg in pkgutil.iter_modules(freegames.__path__):
        if not is_pkg and module_name != "__main__":
            games.append(module_name)
    return sorted(games)

def launch_game(game_name):
    """
    在当前进程里以脚本方式运行选中的游戏模块。
    """
    try:
        runpy.run_module(f"freegames.{game_name}", run_name="__main__")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch '{game_name}': {e}")

def main():
    root = tk.Tk()
    root.title("Free Python Games Launcher")
    root.geometry("300x400")

    games = get_games()
    if not games:
        messagebox.showinfo("No Games Found", "No games were found in the freegames package.")
        return

    # 用 Listbox 列出所有游戏
    list_var = tk.StringVar(value=games)
    listbox = tk.Listbox(root, listvariable=list_var, height=15, selectmode=tk.SINGLE)
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def on_launch():
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a game to launch.")
            return
        game = games[selection[0]]
        # 先关掉启动器，再运行游戏
        root.destroy()
        launch_game(game)

    launch_btn = tk.Button(root, text="Launch Game", command=on_launch)
    launch_btn.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()

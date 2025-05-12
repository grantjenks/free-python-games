import os
import sys
import pkgutil
import runpy
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import ttk

# 确保能 import 到 src 下的 freegames 包
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
import freegames  # type: ignore


def get_games():
    games = []
    for _, module_name, is_pkg in pkgutil.iter_modules(freegames.__path__):
        if not is_pkg and module_name != "__main__":
            games.append(module_name)
    return sorted(games)


def launch_game(game_name):
    try:
        runpy.run_module(f"freegames.{game_name}", run_name="__main__")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch '{game_name}':\n{e}")


class LauncherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Free Python Games Launcher")
        self.configure(bg="#2e2e2e")
        self.geometry("500x500")
        self.resizable(False, False)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#2e2e2e")
        style.configure("Header.TLabel", background="#2e2e2e", foreground="#ffffff", font=("Segoe UI", 18, "bold"))
        style.configure("Game.TButton", font=("Segoe UI", 12), padding=10, background="#3e3e3e", foreground="#ffffff")
        style.map("Game.TButton",
                  background=[("active", "#565656")],
                  foreground=[("active", "#ffffff")])

        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=11)

        self._build_ui()

    def _build_ui(self):
        container = ttk.Frame(self, style="TFrame")
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        header = ttk.Label(container, text="Choose a Game", style="Header.TLabel")
        header.pack(pady=(0, 10))

        # Canvas + Scrollbar 以支持滚动
        canvas = tk.Canvas(container, bg="#2e2e2e", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 在 Canvas 中放置一个 Frame，用于网格布局按钮
        btn_frame = ttk.Frame(canvas, style="TFrame")
        canvas.create_window((0, 0), window=btn_frame, anchor="nw")

        games = get_games()
        if not games:
            messagebox.showinfo("No Games Found", "No games were found in the freegames package.")
            self.destroy()
            return

        # 网格布局：两列
        cols = 2
        for idx, game in enumerate(games):
            btn = ttk.Button(btn_frame, text=game.replace("_", " ").title(),
                             style="Game.TButton",
                             command=lambda g=game: self._on_launch(g))
            r, c = divmod(idx, cols)
            btn.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

        # 让列等宽
        for c in range(cols):
            btn_frame.columnconfigure(c, weight=1)

        # 更新 scroll region
        btn_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        # 绑定鼠标滚轮
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

    def _on_launch(self, game):
        self.destroy()
        launch_game(game)


if __name__ == '__main__':
    LauncherApp().mainloop()

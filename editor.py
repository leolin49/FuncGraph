# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/13 15:25
# Author  : linyf49@qq.com
# File    : editor.py
import time
import tkinter as tk
import threading
from tkinter import filedialog, messagebox, font

import config as cfg
import util
from func_cpp import FuncCpp
from func_go import FuncGolang
from func_py import FuncPython


class Editor:
    def __init__(self, run_type: str):
        self.root = tk.Tk()
        self.root.title("FCAV Code Editor")
        # create text box
        self.text_box = tk.Text(self.root, wrap=tk.WORD)
        self.text_box.pack(expand=True, fill=tk.BOTH)
        self.build_menu()
        self.run_type = run_type
        self.context = ""

    def build_menu(self):
        # build menu
        menu_bar = tk.Menu(self.root)
        self.root.protocol("WM_DELETE_WINDOW", self.quit_file)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        # File
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        # file_menu.add_separator()
        menu_bar.add_cascade(label="File", menu=file_menu)
        # About
        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="About", command=self.show_about)
        about_menu.add_command(label="Version", command=self.show_version)
        menu_bar.add_cascade(label="Help", menu=about_menu)
        # Run
        menu_bar.add_cascade(label="Run", command=self.begin_with_file)
        self.root.config(menu=menu_bar)
        self.text_box.configure(
            font=("consolas", 14, "bold"),
            tabs=" " * 4,
            bg="white",
            fg="black",
            insertbackground="black",
            insertwidth=2,
        )

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            content = self.text_box.get("1.0", tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

    def begin(self):
        self.context = self.text_box.get("1.0", tk.END)
        lines = self.context.split("\n")
        f = None
        if self.run_type == "cpp" or self.run_type == "c++":
            f = FuncCpp(cfg.SUPPORT_MODE_EDIT, lines)
        elif self.run_type == "go" or self.run_type == "golang":
            f = FuncGolang(cfg.SUPPORT_MODE_EDIT, lines)
        elif self.run_type == "py" or self.run_type == "python":
            f = FuncPython(cfg.SUPPORT_MODE_EDIT, lines)
        t1 = threading.Thread(f.start())
        t1.start()

    def begin_with_file(self):
        file_path = "./tmp/{}.{}".format(
            int(time.time()), util.run_type2file_type(self.run_type)
        )
        content = self.text_box.get("1.0", tk.END)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        f = None
        if self.run_type == "cpp" or self.run_type == "c++":
            f = FuncCpp(cfg.SUPPORT_MODE_EDIT, file_path)
        elif self.run_type == "go" or self.run_type == "golang":
            f = FuncGolang(cfg.SUPPORT_MODE_EDIT, file_path)
        elif self.run_type == "py" or self.run_type == "python":
            f = FuncPython(cfg.SUPPORT_MODE_EDIT, file_path)
        t1 = threading.Thread(f.start())
        t1.start()

    def quit_file(self):
        self.root.destroy()
        exit(0)

    @staticmethod
    def show_about():
        messagebox.showinfo(
            "About",
            "Contact: linyf49@qq.com\n" "Github: https://github.com/leolin49/FuncGraph",
        )

    @staticmethod
    def show_version():
        messagebox.showinfo("Version about FCAV", "1.0")

    def run(self):
        self.root.mainloop()

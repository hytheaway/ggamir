# Window management operations, such as centering and resizing, etc.

import shared.globals

import gui.lookandfeel

import tkinter as tk

def centered_window(window,):  # https://www.geeksforgeeks.org/how-to-center-a-window-on-the-screen-in-tkinter/
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def create_new_window(root, window_title:str, width:int, height:int):
    window = tk.Toplevel(root)
    gui.lookandfeel.apply_theme_to_titlebar(window)
    window.iconphoto(False, shared.globals.icon_photo)
    window.minsize(width, height)
    window.title(window_title)
    return window

if __name__ == '__main__':
    pass
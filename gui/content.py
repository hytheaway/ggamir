# Puts content on the window

import tkinter as tk
from tkinter import (ttk,)
import gui.lookandfeel

def populateRoot(root):
    icon_frame = tk.Frame(root)
    icon_frame.grid(row=0, column=0)
    icon_label = tk.Label(icon_frame, image=gui.lookandfeel.icon_photo)
    icon_label.grid(row=0, column=0)
    
    title_label = tk.Label(root, text="Garrett's Great Analyzer of Mono Impulse Responses", justify='center', font=('TkDefaultFont', str(gui.lookandfeel.parse_font_dict["size"] + 2), "bold"))
    title_label.grid(row=1, column=0, columnspan=3)
    
    selectImpulseResponseButton = ttk.Button(root, text="Select IR (.wav)...", style="my.TButton", command=lambda:print('hello'))
    selectImpulseResponseButton.grid(row=2, column=0, columnspan=3)
    
    selectedIRLabel = tk.Label(root, text='IR file:\n', justify='center', wraplength=120)
    selectedIRLabel.grid(row=3, column=0, columnspan=3)
    return

if __name__ == '__main__':
    pass
# Application start up

import os
import tkinter as tk

# env vars
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = (
    "hide"  # <- gets rid of pygame welcome message, which clutters up cli
)

def startUp():
    root = tk.Tk()
    root.minsize(600,400)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.option_add('*tearOff', False)
    root_menubar = tk.Menu(root)
    root['menu'] = root_menubar
    
    return root

if __name__ == '__main__':
    pass
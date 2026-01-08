# Application start up.
# Make sure to avoid circular imports! They'll happen here.

import os
import tkinter as tk

# env vars
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = (
    "hide"  # <- gets rid of pygame welcome message, which clutters up cli
)

def start_up():
    root = tk.Tk()
    root.minsize(600,500)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.option_add('*tearOff', False)
    root_menubar = tk.Menu(root)
    root['menu'] = root_menubar
    
    return root

if __name__ == '__main__':
    pass
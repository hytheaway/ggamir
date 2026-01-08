# Puts content on the window

import shared.globals

import gui.lookandfeel
import gui.dyncontent

import func.app
import func.audio
import func.graphs

import tkinter as tk
from tkinter import (ttk,)

def populate_root(root):
    display_frame = tk.Frame(root)
    display_frame.grid(row=0, column=0, columnspan=3)
    icon_label = tk.Label(display_frame, image=gui.lookandfeel.icon_photo)
    icon_label.grid(row=0, column=1)
    
    title_label = tk.Label(display_frame, text="Garrett's Great Analyzer of Mono Impulse Responses\n", justify='center', font=('TkDefaultFont', str(gui.lookandfeel.parse_font_dict["size"] + 2), "bold"))
    title_label.grid(row=1, column=1)
    
    select_impulse_response_button = ttk.Button(display_frame, text="Select IR (.wav)...", style="my.TButton", command=lambda:func.audio.pick_ir(selected_ir_label))
    select_impulse_response_button.grid(row=2, column=1)
    
    selected_ir_label = tk.Label(display_frame, text='IR file:\n', justify='center', wraplength=120)
    selected_ir_label.grid(row=3, column=1)
    
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=0, columnspan=3)
    
    shared.globals.file_data_button = ttk.Button(button_frame, text="File data", style="my.TButton", command=lambda:gui.dyncontent.create_file_data_window(root, shared.globals.audio_file_path), state=shared.globals.graph_buttons_state)
    shared.globals.file_data_button.grid(row=0, column=0)
    
    shared.globals.td_vis_button = ttk.Button(button_frame, text="Time Domain Graph", style="my.TButton", command=lambda:func.graphs.time_domain_graph(shared.globals.audio_file_path, shared.globals.IR), state=shared.globals.graph_buttons_state)
    shared.globals.td_vis_button.grid(row=0, column=1)
    
    shared.globals.fd_vis_button = ttk.Button(button_frame, text="Frequency Domain Graph", style="my.TButton", command=lambda:func.graphs.freq_domain_graph(shared.globals.audio_file_path, shared.globals.IR, shared.globals.fs), state=shared.globals.graph_buttons_state)
    shared.globals.fd_vis_button.grid(row=0, column=2)
    
    nav_spacer = tk.Label(root, text=' ')
    nav_spacer.grid(row=2, column=1)
    
    contact_button = ttk.Button(root, text='Contact', style='my.TButton', command=lambda:gui.dyncontent.create_contact_window())
    contact_button.grid(row=3, column=0, sticky='w', padx=15)
    
    quit_button = ttk.Button(root, text='Quit', style='my.TButton', command=lambda:func.app.quit_function())
    quit_button.grid(row=3, column=2, sticky='e', padx=15)
    
    spacer_bottom = tk.Label(root, text=' ')
    spacer_bottom.grid(row=4, column=1)
    
    return

if __name__ == '__main__':
    pass
# Dynamic content management

import shared.globals

import gui.tooltips
import gui.soundio
import gui.windowmanagement
import func.stringops

import tkinter as tk
from tkinter import (ttk,)
import os
import webbrowser

def manipulate_tk_with_func(function, tkObject, tkAttribute, func_params=None, return_value=None, tooltip_return_value=None):
    try:
        if return_value == None:
            if func_params == None:
                new_value = function()
            elif func_params != None:
                new_value = function(func_params)
        elif return_value != None:
            if func_params == None:
                return_values = function()
            elif func_params != None:
                return_values = function(func_params)
            new_value = return_values[return_value]
            if tooltip_return_value != None:
                gui.tooltips.create_tooltip(tkObject, text=str(return_values[tooltip_return_value]))
    except Exception as e:
        return -1
    
    match tkAttribute:
        case 'text':
            if len(new_value) > 30:
                new_value = func.stringops.shorten_file_name(new_value, 30)
            new_value += "\n"
            tkObject.config(text=new_value)
        case 'state':
            tkObject.config(state=new_value)
    return

def create_file_data_window(root, full_path):
    file_data_window = gui.windowmanagement.create_new_window(root, "File data", 300, 210)
    gui.windowmanagement.centered_window(file_data_window)
    
    window_title_label = ttk.Label(file_data_window, text="\n" + os.path.basename(full_path) + "\n", justify="center",)
    window_title_label.pack()
    gui.tooltips.create_tooltip(window_title_label, full_path)
    
    sr_label = ttk.Label(
        file_data_window,
        text="Sample rate: " + str(shared.globals.fs),
        justify="center"
    )
    sr_label.pack()
    data_dim_label = ttk.Label(
        file_data_window,
        text="Data dimensions: " + str(shared.globals.IR.shape) + "\n",
        justify="center",
    )
    data_dim_label.pack()
    play_button = ttk.Button(
        file_data_window,
        text="Play",
        style="my.TButton",
        command=lambda: gui.soundio.play_audio(shared.globals.audio_file_path),
    )
    play_button.pack()
    pause_button = ttk.Button(
        file_data_window,
        text="Pause",
        style="my.TButton",
        command=lambda: gui.soundio.pause_audio(),
    )
    pause_button.pack()
    close_button = ttk.Button(
        file_data_window,
        text="Close",
        style="my.TButton",
        command=lambda: gui.soundio.stop_audio_and_close_window(file_data_window),
    )
    close_button.pack()
    
    shared.globals.file_data_window = file_data_window
    
    return

def callback_url(url:str):
    webbrowser.open_new(url)

def create_contact_window():
    contact_window = gui.windowmanagement.create_new_window(shared.globals.root, 'Contact')
    contact_window.grid_columnconfigure(0, weight=1)
    contact_window.grid_rowconfigure(0, weight=1)
    contact_window.grid_rowconfigure(1, weight=1)
    
    gui.windowmanagement.centered_window(contact_window)
    
    title_frame = tk.Frame(contact_window)
    title_frame.grid(row=0, column=0)
    contact_title = tk.Label(
        title_frame,
        text="Contact/Feedback",
        font=("TkDefaultFont", str(shared.globals.parse_font_dict["size"] + 2), "bold"),
    )
    contact_title.grid(row=0, column=0)
    
    links_frame = tk.Frame(contact_window)
    links_frame.grid(row=1, column=0)
    contact_url1 = tk.Label(
        links_frame,
        text="https://hytheaway.github.io/contact.html",
        fg=shared.globals.light_or_dark_blue,
        cursor="hand2",
    )
    contact_url1.grid(row=0, column=0)
    contact_url1.bind(
        "<Button-1>", lambda e: callback_url("https://hytheaway.github.io/contact.html")
    )
    contact_url2 = tk.Label(
        links_frame,
        text="https://github.com/hytheaway",
        fg=shared.globals.light_or_dark_blue,
        cursor="hand2",
    )
    contact_url2.grid(row=1, column=0)
    contact_url2.bind(
        "<Button-1>", lambda e: callback_url("https://github.com/hytheaway")
    )
    contact_url3 = tk.Label(
        links_frame,
        text="hytheaway@gmail.com",
        fg=shared.globals.light_or_dark_blue,
        cursor="hand2",
    )
    contact_url3.grid(row=2, column=0)
    contact_url3.bind(
        "<Button-1>", lambda e: callback_url("mailto:hytheaway@gmail.com")
    )
    
    return
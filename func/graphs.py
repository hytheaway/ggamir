# Abstract functions related to creating graphs

import shared.globals

import gui.windowmanagement

import tkinter as tk
from tkinter import (ttk,)
import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

def time_domain_graph(file_path, IR):
    graph_window = gui.windowmanagement.create_new_window(shared.globals.root, f"Time Domain for {os.path.basename(file_path)}")
    fig = Figure(figsize=(5,4), dpi=100)
    ax = fig.add_subplot()
    data = ax.plot(IR)
    ax.set_xlabel('Time (samples)')
    ax.set_ylabel('Amplitude')
    ax.set_title(f"IR: {os.path.basename(file_path)}")
    
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    
    toolbar = NavigationToolbar2Tk(canvas, graph_window, pack_toolbar=False)
    toolbar.update()
    
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    fig.tight_layout()
    
    return

def freq_domain_graph(file_path, IR, fs):
    nfft = len(IR) * 8
    IR = np.fft.fft(IR, n=nfft, axis=0)
    IR_mag = (2/nfft) * np.abs(IR[0 : int(len(IR) / 2) + 1])
    IR_mag_dB = 20 * np.log10(IR_mag)
    f_axis = np.linspace(0, fs / 2, len(IR_mag_dB))
    
    graph_window = gui.windowmanagement.create_new_window(shared.globals.root, f"Frequency Domain for {os.path.basename(file_path)}")
    fig = Figure(figsize=(5,4), dpi=100)
    ax = fig.add_subplot()
    data = ax.semilogx(f_axis, IR_mag_dB)
    ax.grid(which='minor', color='0.9')
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude (dB)")
    ax.set_title(f"IR: {os.path.basename(file_path)}")
    
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    
    toolbar = NavigationToolbar2Tk(canvas, graph_window, pack_toolbar=False)
    toolbar.update()
    
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    fig.tight_layout()
    
    return

if __name__ == '__main__':
    pass
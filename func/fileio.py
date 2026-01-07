# File I/O Operations

import shared.globals

import gui.alerts

import func.app
import func.stringops

root = shared.globals.root

import os
from tkinter import filedialog

def select_audio_file():
    audio_file_path = filedialog.askopenfilename(filetypes=[(".wav files", ".wav")])
    func.app.force_root_focus(root)
    try:
        if audio_file_path == "":
            return
        audio_file_path_print = audio_file_path.split("/")
        audio_file_path_short = func.stringops.shorten_file_name(os.path.basename(audio_file_path), 13)
        shared.globals.audio_file_path = audio_file_path
        shared.globals.audio_file_path_print = audio_file_path_print
        shared.globals.audio_file_path_short = audio_file_path_short
        return audio_file_path, audio_file_path_print, audio_file_path_short
    except Exception as e:
        gui.alerts.error_window(
            error_message=f"\nError: {e}\n",
            title="Error",
            width=300,
            height=220
        )
        return

if __name__ == '__main__':
    pass
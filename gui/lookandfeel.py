# Look and feel of the GUI

import sys

import tkinter as tk
from tkinter import (ttk,)
from tkinter import filedialog
from tkinter import font
import sv_ttk
import darkdetect
from base64 import b64decode

import func.app

# variables
default_font = font.nametofont("TkDefaultFont")
parse_font_dict = default_font.actual()

with open("gui/icon_photo_b64", 'rb') as icon_photo_file:
    icon_photo_data = icon_photo_file.read()
    icon_photo = tk.PhotoImage(data=b64decode(icon_photo_data))

# start up behaviour that relates to aesthetics and therefore, i feel, fits better here than in gui/startup.py

if sys.platform == "win32":
    import pywinstyles # <- aesthetics on dark mode for windows only
    try:
        import matplotlib
        import pyi_splash # <- windows-only splash screen (needed for pyinstaller, bc pyinstaller wipes the matplotlib cache everytime the application closes, and cx_freeze doesn't build to windows with python 3.13)
        pyi_splash.close()
        matplotlib.use('TkAgg')
    except:
        pass
if sys.platform == "darwin":
    pass
if sys.platform == "linux":
    pass

if sys.platform != 'win32':
    ttkStyles = ttk.Style()
    ttkStyles.configure("my.TButton", font=(default_font, 12))

sv_ttk.set_theme(darkdetect.theme())

if sys.platform == 'win32':
    ttkStyles = ttk.Style()
    ttkStyles.configure("my.TButton", font=("SunValleyBodyFont", 9))

# functions
def apply_theme_to_titlebar(
    root,
):  # https://github.com/rdbende/Sun-Valley-ttk-theme/tree/main
    if sys.platform == 'win32':
        version = sys.getwindowsversion()

        if version.major == 10 and version.build >= 22000:
            # Set the title bar color to the background color on Windows 11 for better appearance
            pywinstyles.change_header_color(
                root, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa"
            )
        elif version.major == 10:
            pywinstyles.change_header_color(
                root, "dark" if sv_ttk.get_theme() == "dark" else "normal"
            )
            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            root.wm_attributes("-alpha", 0.99)
            root.wm_attributes("-alpha", 1)
    else:
        return

if __name__ == '__main__':
    pass
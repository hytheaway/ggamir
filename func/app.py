# Application handling

import gui.lookandfeel

import sys
import pygame

def root_management(root):
    root.iconphoto(False, gui.lookandfeel.icon_photo)
    if sys.platform == 'win32':
        gui.lookandfeel.apply_theme_to_titlebar(root)
    root.focus_force()
    root.title("GGAMIR")
    root.protocol('WM_DELETE_WINDOW', lambda: sys.exit())

def force_root_focus(root):
    root.focus_force()
    return

def refresh_tkobject(tkObject, state_var):
    tkObject.config(state=state_var)
    return


def quit_function():
    """
    Quit function that properly closes out of pygame and the python script, which prevents a segfault when this project is compiled by nuitka.
    """    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    pass